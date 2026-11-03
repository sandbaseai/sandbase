# MarketBeat Marketrank API: pricing, parameters and code examples

`marketbeat/marketrank` · data API · MarketBeat · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Get MarketRank scores and component details for a stock. Includes overall percentile score and individual category scores for Analyst Opinion, Earnings and Valuation, Short Interest, Dividend, News/Social Media, and.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "marketbeat/marketrank", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('marketbeat/marketrank', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("marketbeat/marketrank", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "marketbeat/marketrank", sandbase.Params{
	"ticker": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/marketbeat/marketrank` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string | yes | Stock ticker symbol (e.g. 'AAPL').  |
| `exchange` | string |  | Stock exchange (e.g. 'NYSE', '').  |

## Details

Returns the MarketBeat MarketRank for one stock. It gives an overall percentile and a score out of 5 for each of six categories, with a short detail line for each. The only required input is a `ticker`.

### Use cases

- Screen a watchlist by sorting tickers on their overall MarketRank percentile.
- Find which category pulls a stock's rank down, such as a low earnings and valuation score.
- Show a MarketRank badge with category scores on a stock page in a portfolio app.
- Compare the dividend and short interest scores of two stocks before adding a position.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/marketbeat/marketrank" \
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
    "components": {
      "Analyst's Opinion": {
        "detail": "Analyst RatingModerate Buy",
        "score": "2.3 / 5"
      },
      "Company Ownership": {
        "detail": "Insider TradingSelling Shares",
        "score": "1.4 / 5"
      },
      "Dividend": {
        "detail": "Dividend StrengthStrong",
        "score": "3.3 / 5"
      },
      "Earnings and Valuation": {
        "detail": "Proj. Earnings Growth9.37%",
        "score": "1.9 / 5"
      },
      "News and Social Media": {
        "detail": "News Sentiment0.64",
        "score": "3.5 / 5"
      },
      "Short Interest": {
        "detail": "Short Interest LevelHealthy",
        "score": "3.0 / 5"
      }
    },
    "overall_score": "76th Percentile Overall Score",
    "percentile": "76th Percentile"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.percentile` | The stock's overall percentile as a string, for example `76th Percentile`. |
| `data.overall_score` | The same percentile as a longer label, for example `76th Percentile Overall Score`. |
| `data.components` | An object with one entry per category: Analyst's Opinion, Company Ownership, Dividend, Earnings and Valuation, News and Social Media, and Short Interest. Each entry holds a `score` and a `detail`. |
| `score` | Inside each category entry. Score out of 5, returned as text like `2.3 / 5`. |
| `detail` | Inside each category entry. A short label joined to its value, for example `Dividend StrengthStrong` or `Proj. Earnings Growth9.37%`. |
| `status` | Shows `success` when the call worked. |

### Notes

- Scores and percentiles are strings, not numbers. Parse the value before the `/` to sort or filter.
- The `detail` strings join the label and the value with no separator, such as `Dividend StrengthStrong`. Split on the known label to get the value.
- Category keys contain spaces, and one contains an apostrophe. Read them with bracket notation.
- For the data behind each category, call [MarketBeat Analyst Ratings](/apis/marketbeat/analyst-ratings), [MarketBeat Short Interest](/apis/marketbeat/short-interest) or [MarketBeat Insider Trades](/apis/marketbeat/insider-trades).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/marketbeat/marketrank.json`](../../../catalog/models/marketbeat/marketrank.json) · Store page: https://www.sandbase.ai/model/marketbeat/marketrank
