# DataForSEO Google Finance Quote API: pricing, parameters and code examples

`dataforseo/v3/serp/google/finance_quote/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Fetch a Google Finance quote page for a stock, index, or currency pair. Google Finance quote for a ticker such as 'AAPL:NASDAQ' or 'EUR-USD'.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/finance_quote/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/finance_quote/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/finance_quote/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/finance_quote/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/finance_quote/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns the Google Finance quote page for one ticker, such as `AAPL:NASDAQ` or `EUR-USD`. It gives the current price and change, a minute-by-minute price series, a list of related tickers, and a snapshot of major world indexes. The input is a ticker in `keyword`, plus `location_code` and `language_code`.

### Use cases

- Pull the latest price and daily change for a stock to show in a dashboard.
- Chart intraday price and trading volume for a ticker from the minute-level series.
- Find related tickers that Google Finance lists next to a stock for peer comparison.
- Capture a snapshot of US, European and Asian index levels alongside a quote.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/finance_quote/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "AAPL:NASDAQ", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query. |
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
        "keyword": "AAPL:NASDAQ",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "google"
      },
      "id": "11030829-1614-0139-0000-7e12d7558f1e",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://www.google.com/finance/beta/quote/AAPL:NASDAQ?hl=en&gl=us&window=1d",
          "datetime": "2026-11-03 08:29:26 +00:00",
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
          "items_count": 7,
          "keyword": "AAPL:NASDAQ",
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "2.6208 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "2.7823 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].quote.displayed_name / ticker / identifier` | Company or instrument name, short ticker, and full identifier (for example `AAPL:NASDAQ`) of the quoted asset. This sits in the item with `type` set to `google_finance_quote`. |
| `tasks[].result[].items[].quote.price / price_currency` | Current quoted price and the currency code of that price. |
| `tasks[].result[].items[].quote.price_delta / percentage_delta` | Price change as an amount and as a percentage. A negative value means the price is down. |
| `tasks[].result[].items[].graph_items[].timestamp` | Time of each price point in the series, in `YYYY-MM-DD HH:MM:SS +00:00` format. Points in the sample are one minute apart. |
| `tasks[].result[].items[].graph_items[].value / volume` | Price and traded volume at that timestamp. |
| `tasks[].result[].items[].items[].displayed_name / identifier / price / percentage_delta` | In the `google_finance_compare_to` item, each row is a related ticker with its name, identifier, price and percentage change. |
| `tasks[].result[].items[].markets[].market` | Region name for a group of indexes, such as `US`, `Europe` or `Asia`. This sits in the `google_finance_hero_groups` item. |
| `tasks[].result[].items[].markets[].items[].displayed_name / index_value / index_value_delta / percentage_delta` | Name, current level, point change and percentage change of each market index. |
| `tasks[].result[].item_types` | List of the block types found on the page. Use it to see which blocks the response holds. |

### Notes

- Pass the ticker as `keyword` in the form `TICKER:EXCHANGE`, for example `AAPL:NASDAQ`. A currency pair uses the form `EUR-USD`.
- Blocks in `items` are identified by `type`: `google_finance_hero_groups`, `google_finance_quote` and `google_finance_compare_to`. Look up the quote block by `type` instead of by position.
- `tasks[].result[].check_url` holds the Google Finance page URL that was fetched.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/finance_quote/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/finance_quote/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/finance_quote/live/advanced
