# DataForSEO Google Finance Ticker Search API: pricing, parameters and code examples

`dataforseo/v3/serp/google/finance_ticker_search/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Resolve a company or instrument name to Google Finance tickers. Google Finance search for a company or instrument name.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/finance_ticker_search/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/finance_ticker_search/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/finance_ticker_search/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/finance_ticker_search/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/finance_ticker_search/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns Google Finance ticker matches for a company or instrument name. Send a `keyword` such as `apple`, plus an optional `location_code` and `language_code`, and get a ranked list of instruments with their current price and daily change.

### Use cases

- Convert a company name typed by a user into a Google Finance identifier such as `AAPL:NASDAQ`.
- Build a ticker autocomplete box for a portfolio or watchlist tool.
- Check the latest quoted price and daily move for each match of a brand name.
- Find related listed companies that Google Finance returns for a broad search term.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/finance_ticker_search/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "apple", "location_code": 2840, "language_code": "en"}'
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
        "keyword": "apple",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "google"
      },
      "id": "11030829-1614-0139-0000-2b797d78d405",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": null,
          "datetime": "2026-11-03 08:29:28 +00:00",
          "item_types": [
            "google_finance_market_instrument"
          ],
          "items": [
            {
              "displayed_name": "Apple Inc",
              "identifier": "AAPL:NASDAQ",
              "location": "America/New_York",
              "percentage_delta": -1.8309484,
              "price": 338.32,
              "price_currency": "USD",
              "price_delta": -6.3099976,
              "rank_absolute": 1
            }
          ],
          "items_count": 5,
          "keyword": "apple",
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "2.8961 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "3.0161 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].displayed_name` | Company or instrument name as Google Finance shows it, for example `Apple Inc`. |
| `tasks[].result[].items[].identifier` | Ticker and exchange joined by a colon, for example `AAPL:NASDAQ`. Use it to identify the instrument in later lookups. |
| `tasks[].result[].items[].price / price_currency` | Quoted price of the instrument and the currency code it is quoted in, such as `USD`. |
| `tasks[].result[].items[].price_delta / percentage_delta` | Change in price and change in percent. Negative values mean the price fell. |
| `tasks[].result[].items[].location` | Time zone name tied to the instrument, for example `America/New_York`. |
| `tasks[].result[].items[].rank_absolute` | Position of the match in the result list, starting at 1. |
| `tasks[].result[].items_count` | Number of matches returned for the keyword. |
| `tasks[].result[].datetime` | Time the result was collected, in `YYYY-MM-DD HH:MM:SS +00:00` format. |
| `tasks[].status_code / tasks[].status_message` | Task status. `20000` with `Ok.` means the task succeeded. |

### Notes

- Read matches from `tasks[].result[].items[]`. The `keyword` you send is echoed in `tasks[].data.keyword`.
- Matches are not limited to the searched name. A search for `apple` also returned `Microsoft Corp`.
- `location_code` `2840` is the United States and `language_code` `en` is English.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/finance_ticker_search/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/finance_ticker_search/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/finance_ticker_search/live/advanced
