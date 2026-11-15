# Eastmoney Real Time Hot Queries API: pricing, parameters and code examples

`eastmoney/real-time-hot-queries` · data API · Eastmoney · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get real-time hot search query recommendations from the platform. Recommendations are popular screening queries users can try. Also returns stock heat ranking data (empty object when market is closed).

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "eastmoney/real-time-hot-queries"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('eastmoney/real-time-hot-queries', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("eastmoney/real-time-hot-queries", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "eastmoney/real-time-hot-queries", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/eastmoney/real-time-hot-queries` with the body above minus `model`.

## Details

Get real-time hot search query recommendations from the platform. Recommendations are popular screening queries users can try. Also returns stock heat ranking data (empty object when market is closed).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "eastmoney/real-time-hot-queries"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/eastmoney/real-time-hot-queries.json`](../../../catalog/models/eastmoney/real-time-hot-queries.json) · Store page: https://www.sandbase.ai/model/eastmoney/real-time-hot-queries
