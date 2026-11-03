# DataForSEO Google Finance Markets API: pricing, parameters and code examples

`dataforseo/v3/serp/google/finance_markets/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Fetch Google Finance market summaries by region or asset class. Google Finance markets page for a market_type (indexes by region, most active, gainers, losers, climate leaders, crypto, currencies).

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/finance_markets/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/finance_markets/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/finance_markets/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/finance_markets/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/finance_markets/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `market_type` | string |  | Market type, e.g. "indexes".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns the Google Finance markets page as structured data for a given `market_type`, `location_code` and `language_code`. With `market_type` set to `indexes`, the response lists major stock indexes grouped by region, plus lists of top gainers, losers and most active stocks.

### Use cases

- Show a live dashboard of the Dow Jones, S&P 500, Nikkei 225 and other major indexes grouped by region.
- Build a daily list of the biggest stock gainers and losers on US exchanges.
- Track which tickers appear on the most active list and how far their prices moved.
- Store index values with a timestamp to chart how regional markets move across a day.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/finance_markets/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"market_type": "indexes", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |
| `market_type` | string | No | Market type, e.g. "indexes". |

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
        "market_type": "indexes",
        "os": "windows",
        "se": "google"
      },
      "id": "11030829-1614-0139-0000-6b557d971f5d",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://www.google.com/finance/beta?hl=en&gl=us",
          "datetime": "2026-11-03 08:29:36 +00:00",
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
          "items_count": 2,
          "keyword": null,
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "3.6343 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "3.7698 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].type` | Block type. This response has `google_finance_hero_groups` (indexes by region) and `google_finance_market_trends` (gainers, losers, most active). |
| `tasks[].result[].datetime` | Date and time of the result, for example `2026-11-03 08:29:36 +00:00`. |
| `tasks[].result[].items[].markets[].market` | Region name for a group of indexes, such as `US`, `Europe` or `Asia`. |
| `tasks[].result[].items[].markets[].items[].displayed_name / ticker / identifier` | Index name, short ticker (for example `.INX`) and full identifier with the market code (for example `.INX:INDEXSP`). |
| `tasks[].result[].items[].markets[].items[].index_value` | Current value of the index. |
| `tasks[].result[].items[].markets[].items[].index_value_delta / percentage_delta` | Change in the index value, and the same change as a percentage. Negative numbers mean the index fell. |
| `tasks[].result[].items[].markets[].items[].location` | Time zone name for the index's home market, such as `America/New_York`. |
| `tasks[].result[].items[].items.gainers[].quote / losers[].quote / most_active[].quote` | Stock quote for each list. Each quote holds `displayed_name`, `ticker`, `identifier`, `price`, `price_currency`, `price_delta` and `percentage_delta`. |
| `tasks[].result[].items[].items.gainers[].news` | News attached to the stock. It is `null` in this response. |

### Notes

- Set `market_type` to choose the page. The example uses `indexes`. The API description also lists most active, gainers, losers, climate leaders, crypto and currencies.
- `location_code` `2840` is the United States and `language_code` `en` is English.
- Check `tasks[].result[].item_types` to see which blocks the response holds before you read `items`.
- An `identifier` combines the ticker and the exchange or market code, separated by a colon, for example `NU:NYSE`.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/finance_markets/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/finance_markets/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/finance_markets/live/advanced
