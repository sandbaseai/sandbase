# sandbase (Go)

No dependencies beyond the standard library. Go 1.21+.

```bash
go get github.com/sandbaseai/sandbase/sdk/go
export SANDBASE_API_KEY=sk-...
```

```go
import sandbase "github.com/sandbaseai/sandbase/sdk/go"

c, err := sandbase.NewClient("") // reads SANDBASE_API_KEY
ctx, cancel := context.WithTimeout(context.Background(), 15*time.Minute)
defer cancel()

// Any capability, sync or async: Run returns the finished result
run, err := c.Run(ctx, "exa/search", sandbase.Params{"query": "AI agents", "numResults": 3})
fmt.Println(run.Status, run.Outputs[0]["data"])

// Async without blocking
job, _ := c.Submit(ctx, "app-store/search", sandbase.Params{"term": "notes"}, nil)
done, _ := c.Wait(ctx, job.ID)
cost, _ := c.Cost(ctx, done.ID)

// LLM (OpenAI-compatible)
resp, _ := c.Chat(ctx, "openai/gpt-6.1-sol", []map[string]any{{"role": "user", "content": "Hi"}}, nil)
```

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
