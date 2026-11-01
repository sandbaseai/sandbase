# MarketBeat Institutional Ownership

`marketbeat/institutional-ownership` · api · MarketBeat

Get institutional ownership data including top institutional holders, their share positions, market value, portfolio percentage, quarterly change in shares, and ownership percentage in company.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "marketbeat/institutional-ownership", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('marketbeat/institutional-ownership', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("marketbeat/institutional-ownership", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "marketbeat/institutional-ownership", sandbase.Params{
	"ticker": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/marketbeat/institutional-ownership` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string | yes | Stock ticker symbol (e.g. 'AAPL').  |
| `exchange` | string |  | Stock exchange (e.g. 'NYSE', '').  |

## Details

Get institutional ownership data including top institutional holders, their share positions, market value, portfolio percentage, quarterly change in shares, and ownership percentage in company.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/marketbeat/institutional-ownership" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | Yes | Stock ticker symbol (e.g. 'AAPL'). |
| `exchange` | string | No | Stock exchange (e.g. 'NYSE', ''). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/marketbeat/institutional-ownership.json`](../../../catalog/models/marketbeat/institutional-ownership.json) · Store page: https://www.sandbase.ai/model/marketbeat/institutional-ownership
