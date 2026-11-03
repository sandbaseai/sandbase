# DataForSEO Content Analysis Rating Distribution API: pricing, parameters and code examples

`dataforseo/v3/content_analysis/rating_distribution/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024 per call · **Modes:** sync

Returns the distribution of ratings across analyzed web content and media sources. Helps evaluate audience sentiment and review scores across aggregated citations.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/content_analysis/rating_distribution/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/content_analysis/rating_distribution/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/content_analysis/rating_distribution/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/content_analysis/rating_distribution/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/content_analysis/rating_distribution/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |

## Details

Returns a list of rating buckets for web content that mentions a keyword. Each bucket covers a score range from `min` to `max` and holds counts of sentiment, countries, languages, page types and categories. The request needs one `keyword`.

### Use cases

- Compare how many citations of a brand fall into each rating range.
- Check whether low-rated mentions of a brand come from stores, blogs or message boards.
- Find which countries and languages produce the most content in a given rating range.
- Track emotion counts such as `anger` and `happiness` for a brand in each rating bucket.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/content_analysis/rating_distribution/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "nike"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query. |

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
        "function": "rating_distribution",
        "keyword": "nike"
      },
      "id": "11030828-2190-0466-0000-0426958cc45a",
      "path": [
        "v3"
      ],
      "result": [
        {
          "max": 0.1,
          "metrics": {
            "connotation_types": {
              "negative": 0,
              "neutral": 0,
              "positive": 0
            },
            "countries": null,
            "languages": null,
            "page_categories": null,
            "page_types": null,
            "rank": 0,
            "sentiment_connotations": {
              "anger": 0,
              "fun": 0,
              "happiness": 0,
              "love": 0,
              "sadness": 0,
              "share": 0
            },
            "text_categories": null
          },
          "min": 0,
          "type": "content_analysis_rating_distribution"
        }
      ],
      "result_count": 10,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "14.8977 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "14.9059 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].min / max` | Lower and upper bound of the rating range for this bucket. In the example, the buckets run in steps of 0.1, such as 0 to 0.1 and 0.1 to 0.2. |
| `tasks[].result[].metrics.connotation_types` | Counts of `negative`, `neutral` and `positive` citations in the bucket. |
| `tasks[].result[].metrics.sentiment_connotations` | Counts of citations by emotion: `anger`, `fun`, `happiness`, `love`, `sadness` and `share`. |
| `tasks[].result[].metrics.countries` | Citation counts keyed by country code, such as `DE` or `CH`. The value is `null` when the bucket has no data. |
| `tasks[].result[].metrics.languages` | Citation counts keyed by language code, such as `en` or `de`. |
| `tasks[].result[].metrics.page_types` | Citation counts by page type, such as `ecommerce`, `blogs`, `news`, `message-boards` and `organization`. |
| `tasks[].result[].metrics.page_categories[] / text_categories[]` | Lists of category ID arrays with a `count` for each. A `category` of `null` means no category was assigned. |
| `tasks[].result[].metrics.rank` | Rank value for the bucket. It is `0` in empty buckets and `454` in the 0.1 to 0.2 bucket. |
| `tasks[].result_count` | Number of result buckets in the task. |

### Notes

- Pass the brand, product or topic you want to analyze as `keyword`.
- Buckets with no matching content return `0` counts or `null` for the breakdown fields, so check for `null` before reading them.
- Category values are numeric IDs, not names.

### Pricing

Billed at the actual cost of each call, about $0.024 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/content_analysis/rating_distribution/live.json`](../../../../../../catalog/models/dataforseo/v3/content_analysis/rating_distribution/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/content_analysis/rating_distribution/live
