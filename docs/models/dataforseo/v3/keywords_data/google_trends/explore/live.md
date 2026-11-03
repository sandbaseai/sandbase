# DataForSEO Google Trends API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/google_trends/explore/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.011 per call · **Modes:** sync

Get Google Trends interest over time for up to 5 keywords by location, language and time range, with weekly values on a 0–100 scale.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/google_trends/explore/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/google_trends/explore/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/google_trends/explore/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/google_trends/explore/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/google_trends/explore/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  | Up to 5 keywords to compare.  |
| `time_range` | string |  | Preset range, e.g. past_hour, past_day, past_7_days, past_30_days, past_90_days, past_12_months, past_5_years.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | DataForSEO location code, e.g. 2840 for the United States.  |

## Details

Returns Google Trends interest over time for up to 5 keywords. You send `keywords`, `location_code` and `language_code`, and optionally a `time_range`. The response lists weekly values on a 0 to 100 scale for each keyword.

### Use cases

- Compare weekly search interest in several product names in the United States.
- Spot seasonal peaks for a keyword such as `running shoes` before planning a content calendar.
- Check whether interest in a brand is rising or falling over the past year.
- Open the `check_url` link to see the same chart on trends.google.com.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/google_trends/explore/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No | Up to 5 keywords to compare. |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | DataForSEO location code, e.g. 2840 for the United States. |
| `time_range` | string | No | Preset range, e.g. past_hour, past_day, past_7_days, past_30_days, past_90_days, past_12_months, past_5_years. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "keywords_data",
        "function": "explore",
        "keywords": [
          "running shoes"
        ],
        "language_code": "en",
        "location_code": 2840,
        "se": "google_trends"
      },
      "id": "11030829-1614-0173-0000-6ef58a74867e",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://trends.google.com/trends/explore?hl=en&geo=US&date=2025-11-03%202026-11-…",
          "datetime": "2026-11-03 08:29:26 +00:00",
          "items": [
            {
              "averages": [],
              "data": [
                {
                  "date_from": "2025-11-02",
                  "date_to": "2025-11-08",
                  "missing_data": false,
                  "timestamp": 1762041600,
                  "values": [
                    17
                  ]
                }
              ],
              "keywords": [
                "running shoes"
              ],
              "position": 1,
              "title": null,
              "type": "google_trends_graph"
            }
          ],
          "items_count": 1,
          "keywords": [
            "running shoes"
          ],
          "language_code": "en",
          "location_code": 2840,
          "type": "trends"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "5.1526 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "5.1698 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].data[].values` | Interest values for that week. The list holds one number per keyword, in the same order as the request `keywords`. |
| `tasks[].result[].items[].data[].date_from / date_to` | First and last day of the weekly period, in `YYYY-MM-DD` format. |
| `tasks[].result[].items[].data[].timestamp` | Unix timestamp for the start of the period. |
| `tasks[].result[].items[].data[].missing_data` | `true` when Google Trends has no value for that period. |
| `tasks[].result[].items[].keywords` | Keywords that the graph item covers. |
| `tasks[].result[].items[].type` | Type of the item. The value `google_trends_graph` marks the interest-over-time chart. |
| `tasks[].result[].check_url` | Link to the same query on trends.google.com. |
| `tasks[].result[].datetime` | Date and time when the result was produced, in UTC. |
| `tasks[].result[].items_count` | Number of items in the result. |

### Notes

- Pass `time_range` with a preset such as `past_12_months` or `past_5_years` to change the window. The sample request left it out.
- `location_code` takes a numeric code, for example `2840` for the United States. `language_code` takes a code such as `en`.
- Check `tasks[].status_code` and `tasks[].status_message` for the status of each task. `20000` with `Ok.` means success.

### Pricing

Billed at the actual cost of each call, about $0.011 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Google Ads Keyword Search Volume](/apis/dataforseo/v3/keywords_data/google_ads/search_volume/live): Get Google Ads search volume, CPC, competition and 12-month trend for up to 1,000 keywords per request, by location and language.
- [DataForSEO Website Screenshot](/apis/dataforseo/v3/on_page/page_screenshot): Capture a full-page or viewport screenshot of any URL in desktop, mobile or tablet view.
- [DataForSEO Google SERP (Advanced)](/apis/dataforseo/v3/serp/google/organic/live/advanced): Get live Google organic search results for any keyword, location and language, including AI Overviews, featured snippets, People Also Ask and other SERP featur…

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/google_trends/explore/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/google_trends/explore/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/google_trends/explore/live
