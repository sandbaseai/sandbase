# MarketBeat Stock Headlines API: pricing, parameters and code examples

`marketbeat/stock-headlines` · data API · MarketBeat · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Get recent news headlines for a stock from various sources. Each headline includes the title, URL, relative date, and source domain.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "marketbeat/stock-headlines", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('marketbeat/stock-headlines', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("marketbeat/stock-headlines", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "marketbeat/stock-headlines", sandbase.Params{
	"ticker": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/marketbeat/stock-headlines` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string | yes | Stock ticker symbol (e.g. 'AAPL').  |
| `exchange` | string |  | Stock exchange (e.g. 'NYSE', '').  |

## Details

Returns a list of recent news headlines for one stock. Each item has a title, link, source domain, and a relative date. The call needs a stock `ticker` and accepts an optional `exchange`.

### Use cases

- Show a live news feed on a page for a single ticker such as `AAPL`.
- Scan headline titles for a watchlist to spot stories that need a closer look.
- Count which news domains cover a stock most often.
- Send a link to the newest story in an alert when a stock is in the news.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/marketbeat/stock-headlines" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | Yes | Stock ticker symbol (e.g. 'AAPL'). |
| `exchange` | string | No | Stock exchange (e.g. 'NYSE', ''). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "date": "3 minutes ago",
        "source": "benzinga.com",
        "title": "Pfizer, Apple And 3 Stocks To Watch Heading Into Tuesday",
        "url": "https://www.benzinga.com/trading-ideas/long-ideas/26/11/62806430/pfizer-apple-an…"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[]` | List of recent headlines for the requested stock. |
| `data.items[].title` | Headline text of the news story. |
| `data.items[].url` | Link to the full story on the source site. The same story can appear more than once with different tracking parameters in the URL. |
| `data.items[].source` | Domain of the site that published the story, for example `benzinga.com`. |
| `data.items[].date` | Relative age of the story, such as `3 minutes ago`. It is plain text, not a timestamp. |
| `status` | Shows `success` when the call worked. |

### Notes

- Pass the stock symbol in `ticker`. Use [MarketBeat Search Stocks](/apis/marketbeat/search-stocks) to find a ticker from a company name.
- `exchange` is optional. Leave it out or send an empty string if you do not need it.
- The same headline can appear twice with different `url` values (for example one with `?utm_source=snapi`). Remove duplicates by `title` if you need a clean list.
- For more on the stock, call [MarketBeat Stock Overview](/apis/marketbeat/stock-overview) or [MarketBeat Analyst Ratings](/apis/marketbeat/analyst-ratings).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/marketbeat/stock-headlines.json`](../../../catalog/models/marketbeat/stock-headlines.json) · Store page: https://www.sandbase.ai/model/marketbeat/stock-headlines
