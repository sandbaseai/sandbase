# DataForSEO Google Finance Explore API: pricing, parameters and code examples

`dataforseo/v3/serp/google/finance_explore/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Fetch Google Finance's explore page: market movers, indexes, and news. Google Finance explore data for a location.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/finance_explore/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/finance_explore/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/finance_explore/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/finance_explore/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/finance_explore/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns the Google Finance explore page for a location and language. The response holds major stock index values grouped by region, an earnings calendar, and a list of news stories. It needs `location_code` and `language_code`.

### Use cases

- Show a dashboard of the Dow Jones, S&P 500, Nasdaq, DAX, FTSE 100, and Nikkei 225 with their daily change.
- List companies that report earnings today and link each one to its Google Finance quote page.
- Collect current market news headlines with source names and timestamps for a finance news feed.
- Compare what Google Finance shows in different countries by changing `location_code` and `language_code`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/finance_explore/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "serp",
        "device": "desktop",
        "function": "live",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "google",
        "se_type": "finance_explore"
      },
      "id": "11030829-1614-0139-0000-501a544e31e7",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://www.google.com/finance/beta?hl=en&gl=us",
          "datetime": "2026-11-03 08:29:24 +00:00",
          "item_types": [
            "google_finance_hero_groups"
          ],
          "items": [
            {
              "markets": [
                {
                  "items": [
                    {
                      "displayed_name": "Dow Jones Industrial Average",
                      "identifier": ".DJI:INDEXDJX",
                      "index_value": 51983.98,
                      "index_value_delta": 213.67188,
                      "location": "America/New_York",
                      "market_identifier": "INDEXDJX",
                      "percentage_delta": 0.41273054,
                      "ticker": ".DJI"
                    }
                  ],
                  "market": "US"
                }
              ],
              "rank_absolute": 1,
              "rank_group": 1,
              "type": "google_finance_hero_groups"
            }
          ],
          "items_count": 4,
          "keyword": null,
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "2.1080 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "2.2048 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].type` | Block type. The response shows `google_finance_hero_groups`, `google_finance_earnings_calendar`, and `google_finance_news`. |
| `tasks[].result[].items[].markets[].market` | Region name for a group of indexes, such as `US`, `Europe`, or `Asia`. |
| `tasks[].result[].items[].markets[].items[].displayed_name / ticker / identifier` | Index name, ticker symbol, and the full identifier that joins ticker and exchange, such as `.INX:INDEXSP`. |
| `tasks[].result[].items[].markets[].items[].index_value` | Current value of the index. |
| `tasks[].result[].items[].markets[].items[].index_value_delta / percentage_delta` | Change in the index value, as a point amount and as a percentage. Negative values mean the index is down. |
| `tasks[].result[].items[].markets[].items[].location` | Time zone of the index's market, such as `America/New_York`. |
| `tasks[].result[].items[].items[].title / url` | In the earnings calendar block, the event title and the Google Finance quote link for the company. In the news block, the headline and the article link. |
| `tasks[].result[].items[].items[].timestamp` | Event date for calendar entries, or publish time for news entries. Format is `YYYY-MM-DD HH:MM:SS +00:00`. |
| `tasks[].result[].items[].items[].source` | Name of the news source for each news story. |

### Notes

- Set `location_code` (for example `2840` for the United States) and `language_code` (for example `en`) in the request body.
- The result is in `tasks[].result[]`. The `item_types` array lists which blocks the page contains.
- Each block has `rank_absolute` and `rank_group`, which give its order on the page.
- Earnings calendar `url` values contain the ticker and exchange, such as `SHOP:NASDAQ`.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/finance_explore/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/finance_explore/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/finance_explore/live/advanced
