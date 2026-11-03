# DataForSEO Labs Historical SERPs API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/historical_serps/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00024 per call · **Modes:** sync

Past Google search results for a keyword within a date range.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00024**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/historical_serps/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/historical_serps/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/historical_serps/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/historical_serps/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/historical_serps/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date_to` | string |  | Optional end date.  |
| `keyword` | string |  | Keyword.  |
| `date_from` | string |  | Optional start date, "yyyy-mm-dd".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns saved snapshots of the Google search results page for one keyword, in one location and language. Each snapshot has a date and the result items that ranked at that time. Send `keyword`, `location_code` and `language_code`, and optionally `date_from` and `date_to`.

### Use cases

- Track how the top organic results for a keyword changed between two dates.
- Check when a SERP feature such as `people_also_ask` or `local_pack` first appeared for a keyword.
- Compare the estimated traffic value of ranking domains across snapshots.
- Review the backlink profile of pages that held a ranking at a past date.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/historical_serps/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "coffee", "location_code": 2840, "language_code": "en", "date_from": "2026-06-01"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date_from` | string | No | Optional start date, "yyyy-mm-dd". |
| `date_to` | string | No | Optional end date. |
| `keyword` | string | No | Keyword. |
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
        "api": "dataforseo_labs",
        "date_from": "2026-06-01",
        "function": "historical_serps",
        "keyword": "coffee",
        "language_code": "en",
        "location_code": 2840,
        "se_type": "google"
      },
      "id": "11030828-2190-0408-0000-f2c2f49c435f",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "check_url": "https://www.google.com/search?q=coffee&hl=en&gl=US&ie=UTF-8&uule=w+CAIQIFISCQs2M…",
              "datetime": "2026-06-17 02:01:42 +00:00",
              "item_types": [
                "organic"
              ],
              "items": [
                {
                  "about_this_result": null,
                  "amp_version": false,
                  "backlinks_info": {
                    "backlinks": 30045,
                    "dofollow": 25839,
                    "referring_domains": 3735,
                    "referring_main_domains": 3247,
                    "referring_pages": 27700,
                    "time_update": "2026-06-11 06:43:29 +00:00"
                  },
                  "breadcrumb": "https://en.wikipedia.org › wiki › Coffee",
                  "checks": [
                    "is_image"
                  ],
                  "clickstream_etv": null,
                  "description": "Coffee is a beverage brewed from roasted, ground coffee beans. Darkly colored, b…",
                  "domain": "en.wikipedia.org"
                }
              ],
              "items_count": 42,
              "keyword": "coffee",
              "language_code": "en",
              "location_code": 2840
            }
          ],
          "items_count": 3,
          "keyword": "coffee",
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google",
          "total_count": 3
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.1083 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.1142 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[]` | One SERP snapshot per entry. Each snapshot holds the results seen on that date. |
| `tasks[].result[].items[].datetime` | Date and time of the snapshot, for example `2026-06-17 02:01:42 +00:00`. |
| `tasks[].result[].items[].item_types` | List of result types on that snapshot, such as `organic`, `people_also_ask` or `local_pack`. |
| `tasks[].result[].items[].check_url` | Google search URL that matches the keyword, language and location of the snapshot. |
| `tasks[].result[].items[].items[].type` | Type of the result element, for example `people_also_ask`. |
| `tasks[].result[].items[].items[].rank_absolute / rank_group` | Position of the element on the page (`rank_absolute`) and within its type group (`rank_group`). |
| `tasks[].result[].items[].items[].domain / main_domain` | Domain of the result, and its main domain. Both can be `null` for items without a site, such as some local results. |
| `tasks[].result[].items[].items[].backlinks_info.backlinks / referring_domains / referring_pages` | Backlink counts for the ranking page. `backlinks_info.time_update` shows when these counts were taken. The whole object can be `null`. |
| `tasks[].result[].items[].items[].etv / estimated_paid_traffic_cost` | `etv` is the estimated traffic value of the item. `estimated_paid_traffic_cost` is the estimated cost of buying that traffic with ads. |
| `tasks[].result[].items[].items[].items[].title` | Question text for each `people_also_ask_element`. The `expanded_element` list holds the answer source with its `url` and `domain`. |

### Notes

- The response is nested: `tasks[].result[].items[]` lists snapshots, and each snapshot has its own `items[]` list of results.
- Each snapshot has `items_count`, and the outer result has `total_count` for the number of snapshots returned.
- Use `location_code` 2840 for the United States and `language_code` `en` for English. Dates use the `yyyy-mm-dd` format.

### Pricing

Billed at the actual cost of each call, about $0.00024 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/historical_serps/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/historical_serps/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/historical_serps/live
