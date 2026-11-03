# DataForSEO Content Analysis Phrase Trends API: pricing, parameters and code examples

`dataforseo/v3/content_analysis/phrase_trends/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024324 per call · **Modes:** sync

Citation counts, sentiment and top domains over time for a keyword across web content.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024324**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/content_analysis/phrase_trends/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/content_analysis/phrase_trends/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/content_analysis/phrase_trends/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/content_analysis/phrase_trends/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/content_analysis/phrase_trends/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date_to` | string |  | Optional end date.  |
| `keyword` | string |  | Keyword or phrase.  |
| `date_from` | string |  | Start date, "yyyy-mm-dd".  |
| `date_group` | string |  | "day", "week" or "month".  |

## Details

Returns time-bucketed mentions data for a keyword across web content. Each bucket has sentiment counts, country and language splits, page types and page categories. It needs a `keyword` and a `date_from` date, and you can group results by `day`, `week` or `month`.

### Use cases

- Track how many positive, neutral and negative web mentions a product name gets each week.
- Compare mentions by country or language to see where a brand is discussed most.
- Check whether a keyword is covered mostly by blogs, news, ecommerce or organization sites over time.
- Plot emotion counts such as `happiness` and `share` to spot shifts in tone around a launch.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/content_analysis/phrase_trends/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "iphone", "date_from": "2026-09-01", "date_group": "week"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date_from` | string | No | Start date, "yyyy-mm-dd". |
| `date_group` | string | No | "day", "week" or "month". |
| `date_to` | string | No | Optional end date. |
| `keyword` | string | No | Keyword or phrase. |

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
        "date_from": "2026-09-01",
        "date_group": "week",
        "function": "phrase_trends",
        "keyword": "iphone"
      },
      "id": "11030828-2190-0467-0000-4a26efffea9e",
      "path": [
        "v3"
      ],
      "result": [
        {
          "connotation_types": {
            "negative": 88128,
            "neutral": 64160,
            "positive": 109544
          },
          "countries": {
            "BR": 6256,
            "DE": 12744,
            "ES": 8432,
            "GB": 3424,
            "IN": 6168,
            "IT": 8312,
            "NL": 7152,
            "PL": 6848
          },
          "date": "2026-08-31",
          "languages": {
            "de": 22776,
            "en": 114144,
            "es": 27144,
            "fr": 6416,
            "it": 17832,
            "ja": 60712,
            "nl": 6704,
            "pl": 4640
          },
          "page_categories": [
            {
              "category": [
                10019
              ],
              "count": 76192
            }
          ],
          "page_types": {
            "blogs": 110840,
            "ecommerce": 93424,
            "message-boards": 96,
            "news": 11448,
            "organization": 114104
          },
          "rank": 396,
          "sentiment_connotations": {
            "anger": 0,
            "fun": 760,
            "happiness": 6816,
            "love": 1232,
            "sadness": 24,
            "share": 5768
          }
        }
      ],
      "result_count": 10,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "9.8149 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "9.8224 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].date` | Start date of the time bucket, in `yyyy-mm-dd` format. With `date_group` set to `week`, each row is one week. |
| `tasks[].result[].connotation_types.negative / neutral / positive` | Number of mentions in the bucket with each overall sentiment. |
| `tasks[].result[].sentiment_connotations.anger / fun / happiness / love / sadness / share` | Number of mentions in the bucket tagged with each emotion. |
| `tasks[].result[].countries` | Mention counts per country code, such as `DE` or `GB`. |
| `tasks[].result[].languages` | Mention counts per language code, such as `en` or `ja`. |
| `tasks[].result[].page_types.blogs / ecommerce / news / organization / message-boards` | Mention counts by type of page that carries the keyword. |
| `tasks[].result[].page_categories[].category` | List of numeric category IDs for the page group. |
| `tasks[].result[].page_categories[].count` | Number of mentions in that category for the bucket. |
| `tasks[].result[].rank` | Rank value for the keyword in that bucket. The response does not state how it is scored. |
| `tasks[].result_count` | Number of buckets in the result. The sample shows only a few rows. |

### Notes

- The `date` of the first row (`2026-08-31`) comes before the requested `date_from` (`2026-09-01`), so weekly buckets can start on an earlier day.
- Only some countries and languages appear in each bucket, and the set can change from one bucket to the next.
- Category values are numeric IDs, and the response does not include their names.
- Use `date_to` to set an end date for the range.

### Pricing

Billed at the actual cost of each call, about $0.024324 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/content_analysis/phrase_trends/live.json`](../../../../../../catalog/models/dataforseo/v3/content_analysis/phrase_trends/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/content_analysis/phrase_trends/live
