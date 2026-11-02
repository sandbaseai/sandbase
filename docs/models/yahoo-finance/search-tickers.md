# Yahoo Finance Search Tickers API: pricing, parameters and code examples

`yahoo-finance/search-tickers` · data API · Yahoo Finance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** async

Search for stock tickers and companies by name or keyword. Returns matching equities, ETFs, and other instruments across global exchanges with symbol, name, exchange, quote type, sector, and industry.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo-finance/search-tickers", "query": "apple"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo-finance/search-tickers', {'query': 'apple'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo-finance/search-tickers", {
  "query": "apple"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo-finance/search-tickers", sandbase.Params{
	"query": "apple",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/yahoo-finance/search-tickers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query string (e.g., Apple, Tesla, MSFT).  |

## Details

Search for stock tickers and companies by name or keyword. Returns matching equities, ETFs, and other instruments across global exchanges with symbol, name, exchange, quote type, sector, and industry.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yahoo-finance/search-tickers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "apple"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query string (e.g., Apple, Tesla, MSFT). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo-finance/search-tickers.json`](../../../catalog/models/yahoo-finance/search-tickers.json) · Store page: https://www.sandbase.ai/model/yahoo-finance/search-tickers
