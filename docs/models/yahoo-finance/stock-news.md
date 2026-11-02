# Yahoo Finance Stock News API: pricing, parameters and code examples

`yahoo-finance/stock-news` · data API · Yahoo Finance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** async

Gather the latest financial news articles related to a specified stock ticker. Returns headlines, publishers, links, publish timestamps, and related tickers for each article.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo-finance/stock-news", "symbol": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo-finance/stock-news', {'symbol': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo-finance/stock-news", {
  "symbol": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo-finance/stock-news", sandbase.Params{
	"symbol": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/yahoo-finance/stock-news` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number of news items to retrieve. range -9007199254740991–9007199254740991 |
| `symbol` | string | yes | Stock ticker symbol (e.g., AAPL).  |

## Details

Gather the latest financial news articles related to a specified stock ticker. Returns headlines, publishers, links, publish timestamps, and related tickers for each article.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yahoo-finance/stock-news" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "AAPL"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | Yes | Stock ticker symbol (e.g., AAPL). |
| `count` | integer | No | Number of news items to retrieve. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo-finance/stock-news.json`](../../../catalog/models/yahoo-finance/stock-news.json) · Store page: https://www.sandbase.ai/model/yahoo-finance/stock-news
