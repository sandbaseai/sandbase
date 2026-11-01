# Nasdaq Search Symbols

`nasdaq/search-symbols` · api · Nasdaq

Full-text search across stocks, ETFs, funds, and indices by symbol or company name. Returns scored results with metadata (exchange, asset type, market cap) and real-time market data (last sale, change, percent change).

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/search-symbols", "query": "apple"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/search-symbols', {'query': 'apple'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/search-symbols", {
  "query": "apple"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/search-symbols", sandbase.Params{
	"query": "apple",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/search-symbols` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Max results to return. range -9007199254740991–9007199254740991 |
| `query` | string | yes | Search keyword (symbol or company name).  |

## Details

Full-text search across stocks, ETFs, funds, and indices by symbol or company name. Returns scored results with metadata (exchange, asset type, market cap) and real-time market data (last sale, change, percent change).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/search-symbols" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "apple"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (symbol or company name). |
| `limit` | integer | No | Max results to return. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/nasdaq/search-symbols.json`](../../../catalog/models/nasdaq/search-symbols.json) · Store page: https://www.sandbase.ai/model/nasdaq/search-symbols
