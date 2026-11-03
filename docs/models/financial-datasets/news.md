# Financial Datasets Get Company News API: pricing, parameters and code examples

`financial-datasets/news` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

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

Returns a list of recent news articles, each with a headline, source name, publish date and link. Pass a `ticker` to get news for one company, or leave it out to get general market news.

### Use cases

- Show a feed of recent headlines next to a stock quote for a given ticker.
- Scan broad market headlines each morning to see what moved global markets.
- Collect article links for a company to feed a sentiment or summarization pipeline.
- Track which news outlets cover a ticker by grouping results on the `source` field.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/news" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or modify  |
| `limit` | string | No | The maximum number of news articles to return (default: 5, max: 10). This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. Provider reference (supplier schema): |
| `ticker` | string | No | The ticker symbol of the company. Omit for broad market news. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "news": [
    {
      "date": "2026-11-03T01:03:00+00:00",
      "source": "The Economic Times",
      "ticker": "MARKET",
      "title": "Global Market Today: Asian stocks slide as US chip selloff deepens - The Economi…",
      "url": "https://m.economictimes.com/markets/us-stocks/news/global-market-today-asian-sto…"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `news[]` | List of news articles. Each item is one article. |
| `news[].title` | Headline of the article. It ends with the publisher name after a dash in the examples. |
| `news[].source` | Name of the outlet that published the article, such as `The Economic Times`. |
| `news[].date` | Publish time of the article as an ISO 8601 timestamp with a UTC offset, such as `2026-11-03T01:03:00+00:00`. |
| `news[].ticker` | Ticker the article is tied to. Market-wide news returns the value `MARKET`. |
| `news[].url` | Link to the full article on the publisher's site. |

### Notes

- The request with no `ticker` returns market news, and each item has `ticker` set to `MARKET`.
- `limit` is the total number of articles across all pages. The default is 5 and the maximum is 10.
- To get the next page, send the `cursor` value taken from `next_page_url` in a previous response. When you send `cursor`, all other parameters are ignored.
- Use [Financial Datasets Get Company Facts](/apis/financial-datasets/company-facts) to check company details for a ticker, or [Financial Datasets Get Stock Price Snapshot](/apis/financial-datasets/prices-snapshot) to see its current price.

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/news.json`](../../../catalog/models/financial-datasets/news.json) · Store page: https://www.sandbase.ai/model/financial-datasets/news
