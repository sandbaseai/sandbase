# Financial Datasets Get Company News

`financial-datasets/news` · api · Financial Datasets

Get recent news articles for a specific company or the broad market. Pass a ticker for company-specific news, or omit the ticker for general market news.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/news"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/news', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/news", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/news", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/news` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | The maximum number of news articles to return (default: 5, max: 10). This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. Provider reference (supplier…  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `ticker` | string |  | The ticker symbol of the company. Omit for broad market news.  |

## Details

Get recent news articles for a specific company or the broad market. Pass a ticker for company-specific news, or omit the ticker for general market news.

The response is the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/news" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original reques |
| `limit` | string | No | The maximum number of news articles to return (default: 5, max: 10). This is the total across all pages, not a page size: each page holds up to 10 records, link |
| `ticker` | string | No | The ticker symbol of the company. Omit for broad market news. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/news.json`](../../../catalog/models/financial-datasets/news.json) · Store page: https://www.sandbase.ai/model/financial-datasets/news
