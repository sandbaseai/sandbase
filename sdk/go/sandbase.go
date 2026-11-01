// Package sandbase is a small client for the SandBase API: one key for every
// model and API capability, with the same call for sync and async runs.
//
//	c, _ := sandbase.NewClient("")                       // reads SANDBASE_API_KEY
//	run, err := c.Run(ctx, "exa/search", sandbase.Params{"query": "AI agents"})
package sandbase

import (
	"bytes"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
	"time"
)

const (
	DefaultBaseURL = "https://api.sandbase.ai"
	Version        = "0.1.0"
)

// Params are the capability-specific request fields (see catalog/models/<name>.json).
type Params map[string]any

// RunResult is the response of POST /v1/run and GET /v1/run/{id}.
type RunResult struct {
	ID      string           `json:"id"`
	Model   string           `json:"model"`
	Status  string           `json:"status"`
	Output  json.RawMessage  `json:"output,omitempty"`
	Outputs []map[string]any `json:"outputs,omitempty"`
	Error   json.RawMessage  `json:"error,omitempty"`
}

// Done reports whether the run reached a terminal status.
func (r *RunResult) Done() bool {
	switch r.Status {
	case "completed", "succeeded", "failed", "cancelled", "canceled":
		return true
	}
	return false
}

// Error is returned for non-2xx responses and failed runs.
type Error struct {
	StatusCode int
	Body       string
	Run        *RunResult
}

func (e *Error) Error() string {
	if e.Run != nil {
		return fmt.Sprintf("sandbase: run %s %s: %s", e.Run.ID, e.Run.Status, string(e.Run.Error))
	}
	return fmt.Sprintf("sandbase: HTTP %d: %s", e.StatusCode, e.Body)
}

// Client calls the SandBase API.
type Client struct {
	APIKey     string
	BaseURL    string
	HTTPClient *http.Client
}

// NewClient returns a client. An empty apiKey falls back to SANDBASE_API_KEY.
func NewClient(apiKey string) (*Client, error) {
	if apiKey == "" {
		apiKey = os.Getenv("SANDBASE_API_KEY")
	}
	if apiKey == "" {
		return nil, errors.New("sandbase: missing API key (pass one or set SANDBASE_API_KEY)")
	}
	base := os.Getenv("SANDBASE_BASE_URL")
	if base == "" {
		base = DefaultBaseURL
	}
	return &Client{APIKey: apiKey, BaseURL: strings.TrimRight(base, "/"), HTTPClient: &http.Client{Timeout: 5 * time.Minute}}, nil
}

// Do calls any endpoint and decodes the JSON response into out (which may be nil).
func (c *Client) Do(ctx context.Context, method, path string, body, out any) error {
	return c.DoWithHeaders(ctx, method, path, nil, body, out)
}

// DoWithHeaders is Do with extra request headers (for example Idempotency-Key).
func (c *Client) DoWithHeaders(ctx context.Context, method, path string, headers map[string]string, body, out any) error {
	var reader io.Reader
	if body != nil {
		buf, err := json.Marshal(body)
		if err != nil {
			return err
		}
		reader = bytes.NewReader(buf)
	}
	req, err := http.NewRequestWithContext(ctx, method, c.BaseURL+path, reader)
	if err != nil {
		return err
	}
	req.Header.Set("Authorization", "Bearer "+c.APIKey)
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("User-Agent", "sandbase-go/"+Version)
	for k, v := range headers {
		req.Header.Set(k, v)
	}
	resp, err := c.HTTPClient.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	raw, err := io.ReadAll(resp.Body)
	if err != nil {
		return err
	}
	if resp.StatusCode >= 300 {
		return &Error{StatusCode: resp.StatusCode, Body: string(raw)}
	}
	if out == nil || len(raw) == 0 {
		return nil
	}
	return json.Unmarshal(raw, out)
}

// SubmitOptions are optional controls for Submit.
type SubmitOptions struct {
	Mode       string // "sync" | "async"; only values listed in the model's catalog record
	WebhookURL string // async image/video/audio only
}

// Submit sends POST /v1/run. Sync capabilities return a finished run; async
// ones return {id, status: "pending"} to pass to Wait.
func (c *Client) Submit(ctx context.Context, model string, params Params, opts *SubmitOptions) (*RunResult, error) {
	body := map[string]any{"model": model}
	for k, v := range params {
		body[k] = v
	}
	if opts != nil {
		if opts.Mode != "" {
			body["mode"] = opts.Mode
		}
		if opts.WebhookURL != "" {
			body["webhook_url"] = opts.WebhookURL
		}
	}
	var out RunResult
	if err := c.Do(ctx, http.MethodPost, "/v1/run", body, &out); err != nil {
		return nil, err
	}
	return &out, nil
}

// Get returns GET /v1/run/{id}.
func (c *Client) Get(ctx context.Context, id string) (*RunResult, error) {
	var out RunResult
	if err := c.Do(ctx, http.MethodGet, "/v1/run/"+id, nil, &out); err != nil {
		return nil, err
	}
	return &out, nil
}

// Wait polls with backoff until the run is terminal or ctx is done.
func (c *Client) Wait(ctx context.Context, id string) (*RunResult, error) {
	interval := 2 * time.Second
	for {
		run, err := c.Get(ctx, id)
		if err != nil {
			return nil, err
		}
		if run.Done() {
			return run, nil
		}
		select {
		case <-ctx.Done():
			return run, ctx.Err()
		case <-time.After(interval):
		}
		if interval < 15*time.Second {
			interval = interval * 3 / 2
		}
	}
}

// Run submits and, for async capabilities, waits. A failed run returns *Error.
// Bound the total time with ctx (e.g. context.WithTimeout).
func (c *Client) Run(ctx context.Context, model string, params Params) (*RunResult, error) {
	run, err := c.Submit(ctx, model, params, nil)
	if err != nil {
		return nil, err
	}
	if !run.Done() {
		if run, err = c.Wait(ctx, run.ID); err != nil {
			return run, err
		}
	}
	if run.Status == "failed" {
		return run, &Error{Run: run}
	}
	return run, nil
}

// Cost returns GET /v1/tasks/{id}/cost (billed amount of a run).
func (c *Client) Cost(ctx context.Context, id string) (map[string]any, error) {
	var out map[string]any
	err := c.Do(ctx, http.MethodGet, "/v1/tasks/"+id+"/cost", nil, &out)
	return out, err
}

// Chat calls the OpenAI-compatible /v1/chat/completions and returns the raw response.
func (c *Client) Chat(ctx context.Context, model string, messages []map[string]any, extra Params) (map[string]any, error) {
	body := map[string]any{"model": model, "messages": messages}
	for k, v := range extra {
		body[k] = v
	}
	var out map[string]any
	err := c.Do(ctx, http.MethodPost, "/v1/chat/completions", body, &out)
	return out, err
}
