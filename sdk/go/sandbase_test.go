package sandbase

import (
	"context"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"sync/atomic"
	"testing"
	"time"
)

func TestRunWaitsForAsyncCapability(t *testing.T) {
	var polls int32
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.Header.Get("Authorization") != "Bearer sk-test" {
			w.WriteHeader(http.StatusUnauthorized)
			return
		}
		switch {
		case r.Method == http.MethodPost && r.URL.Path == "/v1/run":
			var body map[string]any
			_ = json.NewDecoder(r.Body).Decode(&body)
			if body["model"] != "app-store/search" || body["term"] != "notes" {
				t.Errorf("unexpected body %v", body)
			}
			_, _ = w.Write([]byte(`{"id":"r1","model":"app-store/search","status":"pending"}`))
		case r.Method == http.MethodGet && r.URL.Path == "/v1/run/r1":
			if atomic.AddInt32(&polls, 1) < 2 {
				_, _ = w.Write([]byte(`{"id":"r1","status":"processing"}`))
				return
			}
			_, _ = w.Write([]byte(`{"id":"r1","status":"completed","outputs":[{"data":{"ok":true}}]}`))
		default:
			w.WriteHeader(http.StatusNotFound)
		}
	}))
	defer srv.Close()

	c := &Client{APIKey: "sk-test", BaseURL: srv.URL, HTTPClient: srv.Client()}
	ctx, cancel := context.WithTimeout(context.Background(), 20*time.Second)
	defer cancel()
	run, err := c.Run(ctx, "app-store/search", Params{"term": "notes"})
	if err != nil {
		t.Fatal(err)
	}
	if run.Status != "completed" || run.Outputs[0]["data"].(map[string]any)["ok"] != true {
		t.Fatalf("unexpected run %+v", run)
	}
}

func TestRunReturnsErrorForFailedRunAndHTTPError(t *testing.T) {
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == "/v1/run" {
			var body map[string]any
			_ = json.NewDecoder(r.Body).Decode(&body)
			if body["model"] == "bad" {
				w.WriteHeader(http.StatusBadRequest)
				_, _ = w.Write([]byte(`{"error":"parameter validation failed"}`))
				return
			}
			_, _ = w.Write([]byte(`{"id":"r2","status":"failed","error":{"type":"upstream_error","message":"x"}}`))
		}
	}))
	defer srv.Close()
	c := &Client{APIKey: "k", BaseURL: srv.URL, HTTPClient: srv.Client()}

	if _, err := c.Run(context.Background(), "m", nil); err == nil {
		t.Fatal("expected failed-run error")
	} else if e, ok := err.(*Error); !ok || e.Run == nil || e.Run.ID != "r2" {
		t.Fatalf("unexpected error %#v", err)
	}
	if _, err := c.Run(context.Background(), "bad", nil); err == nil {
		t.Fatal("expected HTTP error")
	} else if e, ok := err.(*Error); !ok || e.StatusCode != http.StatusBadRequest {
		t.Fatalf("unexpected error %#v", err)
	}
}
