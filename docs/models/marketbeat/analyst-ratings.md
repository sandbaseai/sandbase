# MarketBeat Analyst Ratings

`marketbeat/analyst-ratings` · api · MarketBeat

Get historical monthly analyst rating counts and breakdown. Returns time series data with buy, hold, sell, strong buy counts and total ratings per month, typically covering 3 years of history.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "marketbeat/analyst-ratings", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('marketbeat/analyst-ratings', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("marketbeat/analyst-ratings", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "marketbeat/analyst-ratings", sandbase.Params{
	"ticker": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/marketbeat/analyst-ratings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string | yes | Stock ticker symbol (e.g. 'AAPL').  |
| `exchange` | string |  | Stock exchange (e.g. 'NYSE', '').  |

## Details

Get historical monthly analyst rating counts and breakdown. Returns time series data with buy, hold, sell, strong buy counts and total ratings per month, typically covering 3 years of history.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/marketbeat/analyst-ratings" \
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
Machine-readable: [`catalog/models/marketbeat/analyst-ratings.json`](../../../catalog/models/marketbeat/analyst-ratings.json) · Store page: https://www.sandbase.ai/model/marketbeat/analyst-ratings
