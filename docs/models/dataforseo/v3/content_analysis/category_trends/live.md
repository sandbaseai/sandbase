# DataForSEO Content Analysis Category Trends API: pricing, parameters and code examples

`dataforseo/v3/content_analysis/category_trends/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024324 per call · **Modes:** sync

Citation counts, sentiment and top domains over time for a content category.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024324**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/content_analysis/category_trends/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/content_analysis/category_trends/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/content_analysis/category_trends/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/content_analysis/category_trends/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/content_analysis/category_trends/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date_to` | string |  | Optional end date.  |
| `date_from` | string |  | Start date, "yyyy-mm-dd".  |
| `date_group` | string |  | "day", "week" or "month".  |
| `category_code` | integer |  | Content category code, e.g. 10994.  |

## Details

Returns time-bucketed content statistics for one content category. You send a `category_code` and a `date_from`, and you can group results by `day`, `week` or `month` with `date_group`. Each bucket shows counts by sentiment, country, language, page type and sub-category.

### Use cases

- Track whether positive or negative mentions in a content category are rising week over week.
- Compare how many pages in a category are blogs, news, ecommerce or message boards over time.
- Find which countries and languages produce the most content for a category in a given period.
- Spot shifts in emotions such as `happiness` or `anger` across a category before planning content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/content_analysis/category_trends/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_code": 10994, "date_from": "2026-09-01", "date_group": "week"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_code` | integer | No | Content category code, e.g. 10994. |
| `date_from` | string | No | Start date, "yyyy-mm-dd". |
| `date_group` | string | No | "day", "week" or "month". |
| `date_to` | string | No | Optional end date. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "content_analysis",
        "category_code": 10994,
        "date_from": "2026-09-01",
        "date_group": "week",
        "function": "category_trends"
      },
      "id": "11030828-2190-0468-0000-a26395f7a23d",
      "path": [
        "v3"
      ],
      "result": [
        {
          "connotation_types": {
            "negative": 84064,
            "neutral": 216464,
            "positive": 169808
          },
          "countries": {
            "AU": 8664,
            "BR": 4088,
            "CL": 2928,
            "DE": 19472,
            "ES": 6280,
            "FR": 15304,
            "GB": 26512,
            "US": 79008
          },
          "date": "2026-08-31",
          "languages": {
            "de": 36256,
            "en": 332264,
            "es": 15512,
            "fr": 58200,
            "it": 1088,
            "ja": 3880,
            "pt": 5104,
            "ro": 4176
          },
          "page_categories": [
            {
              "category": null,
              "count": 21168
            }
          ],
          "page_types": {
            "blogs": 36368,
            "ecommerce": 254736,
            "message-boards": 160,
            "news": 3000,
            "organization": 124616
          },
          "rank": 480,
          "sentiment_connotations": {
            "anger": 248,
            "fun": 840,
            "happiness": 65608,
            "love": 2624,
            "sadness": 304,
            "share": 7920
          }
        }
      ],
      "result_count": 10,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "24.8884 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "24.9285 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].date` | Start date of the time bucket, in `yyyy-mm-dd` format. With `date_group` set to `week`, the sample dates are a week apart. |
| `tasks[].result[].rank` | A rank number for the category in that bucket. The response does not state the scale, so treat it as a relative value. |
| `tasks[].result[].connotation_types.negative / neutral / positive` | Counts of content in the bucket grouped by overall tone. |
| `tasks[].result[].sentiment_connotations.anger / fun / happiness / love / sadness / share` | Counts of content in the bucket tagged with each emotion. |
| `tasks[].result[].countries` | Counts of content by two-letter country code, such as `US` or `GB`. Only a handful of countries appear per bucket. |
| `tasks[].result[].languages` | Counts of content by language code, such as `en` or `de`. |
| `tasks[].result[].page_types.blogs / ecommerce / news / organization / message-boards` | Counts of content by type of page. |
| `tasks[].result[].page_categories[].category` | List of category codes for a sub-category group, or `null` when no category applies. Use it together with `count`. |
| `tasks[].result[].page_categories[].count` | Number of items in that category group for the bucket. |

### Notes

- The `date` in each result is the start of its bucket and may fall before your `date_from`. The first sample bucket is `2026-08-31` for a `date_from` of `2026-09-01`.
- Set `date_to` to limit the range. Set `date_group` to `day`, `week` or `month` to change the bucket size.
- Read the data from `tasks[].result[]`. Check `tasks[].status_code` for `20000` to confirm the task succeeded.
- Each `page_categories[].category` value is an array of numeric category codes, and you can reuse such codes as `category_code` in a new call.

### Pricing

Billed at the actual cost of each call, about $0.024324 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/content_analysis/category_trends/live.json`](../../../../../../catalog/models/dataforseo/v3/content_analysis/category_trends/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/content_analysis/category_trends/live
