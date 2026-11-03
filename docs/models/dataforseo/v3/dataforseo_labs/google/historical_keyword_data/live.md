# DataForSEO Google Historical Keyword Data API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/historical_keyword_data/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01212 per call · **Modes:** sync

Get month-by-month history of search volume, CPC and competition for up to 100 Google keywords, going back to 2019.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01212**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/historical_keyword_data/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/historical_keyword_data/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/historical_keyword_data/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/historical_keyword_data/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/historical_keyword_data/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

Returns month-by-month history of search volume, CPC, competition and top-of-page bids for Google keywords. It needs a `keywords` list, a `location_code` and a `language_code`.

### Use cases

- Chart how search demand for a keyword like `openai api` changed over several months.
- Compare past CPC and top-of-page bid ranges to plan a Google Ads budget.
- Spot seasonal patterns in search volume before scheduling content.
- Track how competition levels moved for a set of keywords in one country.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/historical_keyword_data/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["openai api"], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No |  |
| `language_code` | string | No |  |
| `location_code` | integer | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "dataforseo_labs",
        "function": "historical_keyword_data",
        "keywords": [
          "openai api"
        ],
        "language_code": "en",
        "location_code": 2840,
        "se_type": "google"
      },
      "id": "11030828-2190-0608-0000-1541d344a01a",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "history": [
                {
                  "keyword_info": {
                    "categories": [
                      10019
                    ],
                    "competition": 0.12,
                    "competition_level": "LOW",
                    "cpc": 7.57,
                    "high_top_of_page_bid": 18.55,
                    "last_updated_time": "2026-10-20 05:57:07 +00:00",
                    "low_top_of_page_bid": 3.71,
                    "monthly_searches": [
                      {
                        "month": 9,
                        "search_volume": 49500,
                        "year": 2026
                      }
                    ]
                  },
                  "month": 9,
                  "year": 2026
                }
              ],
              "keyword": "openai api",
              "language_code": "en",
              "location_code": 2840,
              "se_type": "google"
            }
          ],
          "items_count": 1,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.2996 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.3064 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keyword` | The keyword that the history belongs to. |
| `tasks[].result[].items[].history[].year / tasks[].result[].items[].history[].month` | The calendar year and month of this history snapshot. |
| `tasks[].result[].items[].history[].keyword_info.cpc` | Cost per click for the keyword in that month. |
| `tasks[].result[].items[].history[].keyword_info.competition / tasks[].result[].items[].history[].keyword_info.competition_level` | Competition as a number and as a label such as `LOW`. |
| `tasks[].result[].items[].history[].keyword_info.low_top_of_page_bid / tasks[].result[].items[].history[].keyword_info.high_top_of_page_bid` | Low and high bid values for an ad at the top of the page in that month. |
| `tasks[].result[].items[].history[].keyword_info.monthly_searches[].search_volume` | Search volume for the month given in the sibling `year` and `month` fields. Each snapshot lists several recent months. |
| `tasks[].result[].items[].history[].keyword_info.categories` | List of numeric category IDs for the keyword. |
| `tasks[].result[].items[].history[].keyword_info.last_updated_time` | Timestamp of the last update for that snapshot, for example `2026-10-20 05:57:07 +00:00`. |

### Notes

- Send up to 100 keywords in the `keywords` array. Each keyword gets its own entry in `items`.
- `location_code` `2840` and `language_code` `en` were used in the example request.
- The `history` list holds one entry per month, with the newest month first.

### Pricing

Billed at the actual cost of each call, about $0.01212 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/historical_keyword_data/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/historical_keyword_data/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/historical_keyword_data/live
