# sandbase (Go)

No dependencies beyond the standard library. Go 1.21+.

```bash
# In a new project, first run: go mod init example.com/my-sandbase-app
go get github.com/sandbaseai/sandbase/sdk/go
export SANDBASE_API_KEY=sk-...
```

Save as `main.go` in a Go module, then run `go run .`:

```go
package main

import (
    "context"
    "encoding/json"
    "log"
    "os"
    "time"

    sandbase "github.com/sandbaseai/sandbase/sdk/go"
)

func main() {
    client, err := sandbase.NewClient("") // reads SANDBASE_API_KEY
    if err != nil {
        log.Fatal(err)
    }
    ctx, cancel := context.WithTimeout(context.Background(), 15*time.Minute)
    defer cancel()

    run, err := client.Run(ctx, "exa/search", sandbase.Params{"query": "AI agents", "numResults": 3})
    if err != nil {
        log.Fatal(err)
    }
    // Print the complete result; output shapes differ between capabilities.
    if err := json.NewEncoder(os.Stdout).Encode(run); err != nil {
        log.Fatal(err)
    }
}
```

`Run` waits for async work as well as returning sync results. For manual polling, use `Submit`, save `job.ID`, then call `Wait(ctx, job.ID)` or `Get(ctx, job.ID)`. Handle each returned error before accessing the result. A context timeout does not cancel the server-side job; resume its ID instead of submitting it again.

Run the example: `cd sdk/go && go run ./examples/run exa/search '{"query":"AI agents"}'`.

## Agents

```go
a, _ := c.CreateAgent(ctx, sandbase.Params{"model": "deepseek/deepseek-v4-flash", "instructions": "Answer briefly."})
res, _ := c.RunAgent(ctx, a.ID, "What is 2+2?")    // res.SessionID, res.Output
next, _ := c.Send(ctx, res.SessionID, "And times 10?")
run, _ := c.InvokeService(ctx, "svc_...", "What is 7+7?") // run.Output
```

Example: `AGENT_ID=agt_... go run ./examples/agent "your task"` (omit `AGENT_ID` to create a small Agent).

Sandboxes: there is no official E2B Go SDK. Use the E2B Python or JavaScript SDK, or call the control API at `https://sandbox.sandbase.ai` with header `X-API-Key`.

For website, API and AI-tool setup, see [Quick Start](https://www.sandbase.ai/docs/getting-started/quickstart). Calls may use your balance; inspect current inputs and prices before executing examples. `SANDBASE_BASE_URL` is the origin `https://api.sandbase.ai`, without `/v1`; the SDK adds the version prefix.
