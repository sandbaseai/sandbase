package sandbase

import (
	"context"
	"crypto/rand"
	"encoding/hex"
	"fmt"
	"net/http"
	"strings"
	"time"
)

// Agent is a saved Agent (agt_ prefix).
type Agent struct {
	ID               string `json:"id"`
	Name             string `json:"name,omitempty"`
	Description      string `json:"description,omitempty"`
	Model            string `json:"model,omitempty"`
	Version          int    `json:"version,omitempty"`
	ProjectionStatus string `json:"projection_status,omitempty"`
}

// AgentTurnResult is the outcome of RunAgent / Send.
type AgentTurnResult struct {
	SessionID string         `json:"session_id"`
	Status    string         `json:"status"`
	Output    string         `json:"output"` // assistant text produced by this turn
	Turn      map[string]any `json:"turn"`
}

// ServiceRun is a Service invocation (run_ prefix).
type ServiceRun struct {
	ID        string `json:"id"`
	Status    string `json:"status"`
	SessionID string `json:"session_id,omitempty"`
	Output    string `json:"output,omitempty"` // filled by InvokeService after the Run finishes
}

type turn struct {
	ID     string `json:"id"`
	Status string `json:"status"`
}

type sessionItem struct {
	Type    string `json:"type"`
	Role    string `json:"role"`
	Content []struct {
		Type string `json:"type"`
		Text string `json:"text"`
	} `json:"content"`
}

func newKey() string {
	b := make([]byte, 16)
	_, _ = rand.Read(b)
	return "sdk-" + hex.EncodeToString(b)
}

func idem() map[string]string { return map[string]string{"Idempotency-Key": newKey()} }

// CreateAgent creates an Agent (fields: model, instructions, name, skills, mcp_connections, …)
// and waits until it can start Sessions.
func (c *Client) CreateAgent(ctx context.Context, fields Params) (*Agent, error) {
	var a Agent
	if err := c.DoWithHeaders(ctx, http.MethodPost, "/v1/agents", idem(), fields, &a); err != nil {
		return nil, err
	}
	return c.waitAgentReady(ctx, &a)
}

// RunAgent starts a Session with input and waits for the turn to finish.
func (c *Client) RunAgent(ctx context.Context, agentID, input string) (*AgentTurnResult, error) {
	var s struct {
		ID string `json:"id"`
	}
	if err := c.DoWithHeaders(ctx, http.MethodPost, "/v1/agents/sessions", idem(), Params{"agent_id": agentID, "input": input}, &s); err != nil {
		return nil, err
	}
	return c.finishTurn(ctx, s.ID, 0)
}

// Send posts a follow-up message to a Session and waits for its turn.
func (c *Client) Send(ctx context.Context, sessionID, input string) (*AgentTurnResult, error) {
	turns, err := c.turns(ctx, sessionID)
	if err != nil {
		return nil, err
	}
	if err := c.DoWithHeaders(ctx, http.MethodPost, "/v1/agents/sessions/"+sessionID+"/events", idem(), Params{"input": input}, nil); err != nil {
		return nil, err
	}
	return c.finishTurn(ctx, sessionID, len(turns))
}

// InvokeService starts a Service Run (empty input uses the saved input), waits for it and
// fills Output with the Session's final assistant text.
func (c *Client) InvokeService(ctx context.Context, serviceID, input string) (*ServiceRun, error) {
	body := Params{}
	if input != "" {
		body["input"] = input
	}
	var run ServiceRun
	if err := c.DoWithHeaders(ctx, http.MethodPost, "/v1/services/"+serviceID+"/invoke", idem(), body, &run); err != nil {
		return nil, err
	}
	interval := 2 * time.Second
	for run.Status != "succeeded" && run.Status != "failed" && run.Status != "cancelled" && run.Status != "canceled" {
		if err := sleepCtx(ctx, interval); err != nil {
			return &run, err
		}
		if interval < 15*time.Second {
			interval = interval * 3 / 2
		}
		if err := c.Do(ctx, http.MethodGet, "/v1/services/"+serviceID+"/runs/"+run.ID, nil, &run); err != nil {
			return nil, err
		}
	}
	if run.SessionID != "" {
		out, err := c.latestOutput(ctx, run.SessionID)
		if err != nil {
			return &run, err
		}
		run.Output = out
	}
	return &run, nil
}

func (c *Client) waitAgentReady(ctx context.Context, a *Agent) (*Agent, error) {
	for a.ProjectionStatus != "" && a.ProjectionStatus != "ready" {
		if a.ProjectionStatus == "failed" {
			return a, fmt.Errorf("sandbase: agent %s projection failed", a.ID)
		}
		if err := sleepCtx(ctx, 2*time.Second); err != nil {
			return a, err
		}
		if err := c.Do(ctx, http.MethodGet, "/v1/agents/"+a.ID, nil, a); err != nil {
			return nil, err
		}
	}
	return a, nil
}

func (c *Client) turns(ctx context.Context, sessionID string) ([]turn, error) {
	var out struct {
		Data []turn `json:"data"` // newest first
	}
	err := c.Do(ctx, http.MethodGet, "/v1/agents/sessions/"+sessionID+"/turns", nil, &out)
	return out.Data, err
}

func (c *Client) finishTurn(ctx context.Context, sessionID string, previous int) (*AgentTurnResult, error) {
	interval := 2 * time.Second
	for {
		turns, err := c.turns(ctx, sessionID)
		if err != nil {
			return nil, err
		}
		if len(turns) > previous {
			switch t := turns[0]; t.Status {
			case "completed":
				out, err := c.latestOutput(ctx, sessionID)
				if err != nil {
					return nil, err
				}
				return &AgentTurnResult{SessionID: sessionID, Status: t.Status, Output: out, Turn: map[string]any{"id": t.ID, "status": t.Status}}, nil
			case "failed", "cancelled", "canceled", "incomplete", "expired":
				return nil, fmt.Errorf("sandbase: turn %s %s", t.ID, t.Status)
			}
		}
		var s struct {
			Status  string `json:"status"`
			Failure any    `json:"failure"`
		}
		if err := c.Do(ctx, http.MethodGet, "/v1/agents/sessions/"+sessionID, nil, &s); err != nil {
			return nil, err
		}
		if s.Status == "failed" {
			return nil, fmt.Errorf("sandbase: session %s failed: %v", sessionID, s.Failure)
		}
		if err := sleepCtx(ctx, interval); err != nil {
			return nil, err
		}
		if interval < 10*time.Second {
			interval = interval * 3 / 2
		}
	}
}

func (c *Client) latestOutput(ctx context.Context, sessionID string) (string, error) {
	var out struct {
		Data []sessionItem `json:"data"`
	}
	if err := c.Do(ctx, http.MethodGet, "/v1/agents/sessions/"+sessionID+"/items?order=desc&limit=50", nil, &out); err != nil {
		return "", err
	}
	var texts []string
	for _, it := range out.Data {
		if it.Type == "message" && it.Role == "user" {
			break
		}
		if it.Type == "message" && it.Role == "assistant" {
			for i := len(it.Content) - 1; i >= 0; i-- {
				if it.Content[i].Type == "output_text" {
					texts = append([]string{it.Content[i].Text}, texts...)
				}
			}
		}
	}
	return strings.Join(texts, "\n"), nil
}

func sleepCtx(ctx context.Context, d time.Duration) error {
	select {
	case <-ctx.Done():
		return ctx.Err()
	case <-time.After(d):
		return nil
	}
}
