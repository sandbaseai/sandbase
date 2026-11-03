# DataForSEO Content Analysis Summary API: pricing, parameters and code examples

`dataforseo/v3/content_analysis/summary/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024036 per call · **Modes:** sync

Returns aggregated content metrics and high-level citation statistics for content analysis workflows. Evaluates summary indicators across analyzed online content.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024036**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/content_analysis/summary/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/content_analysis/summary/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/content_analysis/summary/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/content_analysis/summary/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/content_analysis/summary/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |

## Details

Returns aggregated statistics about online content that mentions a keyword. The response covers sentiment counts, page types, countries, languages and content categories. It needs one input: `keyword`.

### Use cases

- Compare how positive, neutral and negative the online content about a brand is.
- Check which page types, such as news, blogs or ecommerce, mention a keyword most often.
- See which countries and languages produce the most content about a topic.
- Find the content categories that a brand or topic appears in.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/content_analysis/summary/live" \
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
        "function": "summary",
        "keyword": "nike"
      },
      "id": "11030828-2190-0464-0000-6d1e54caa56c",
      "path": [
        "v3"
      ],
      "result": [
        {
          "connotation_types": {
            "negative": 1513464,
            "neutral": 494208,
            "positive": 1745224
          },
          "countries": {
            "BR": 96008,
            "DE": 106128,
            "FR": 89168,
            "GB": 118000,
            "IN": 83352,
            "IR": 51672,
            "NL": 60472,
            "US": 148608
          },
          "languages": {
            "af": 28224,
            "br": 11728,
            "de": 50664,
            "en": 2590960,
            "es": 38952,
            "fr": 32616,
            "it": 13096,
            "ja": 1189688
          },
          "page_categories": [
            {
              "category": null,
              "count": 381568
            }
          ],
          "page_types": {
            "blogs": 233416,
            "ecommerce": 2845640,
            "message-boards": 66912,
            "news": 922688,
            "organization": 299064
          },
          "rank": 520,
          "sentiment_connotations": {
            "anger": 48,
            "fun": 6592,
            "happiness": 435160,
            "love": 180360,
            "sadness": 376,
            "share": 14840
          },
          "text_categories": [
            {
              "category": null,
              "count": 241760
            }
          ]
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "2.8243 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "2.8336 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].connotation_types` | Counts of mentions by tone. The keys are `negative`, `neutral` and `positive`. |
| `tasks[].result[].sentiment_connotations` | Counts of mentions by emotion type, such as `anger`, `happiness`, `love`, `fun`, `sadness` and `share`. |
| `tasks[].result[].page_types` | Counts of mentions by type of page, such as `news`, `blogs`, `ecommerce`, `message-boards` and `organization`. |
| `tasks[].result[].countries` | Counts of mentions by country. Keys are two-letter country codes such as `US` and `GB`. |
| `tasks[].result[].languages` | Counts of mentions by language. Keys are language codes such as `en`, `ja` and `de`. |
| `tasks[].result[].page_categories[].category / tasks[].result[].text_categories[].category` | A list of numeric category codes, or `null` when no category applies. The code list is not part of this response. |
| `tasks[].result[].page_categories[].count / tasks[].result[].text_categories[].count` | Number of mentions that fall into the matching category. |
| `tasks[].result[].rank` | A numeric rank value for the keyword's content. The response does not state its scale. |
| `tasks[].result_count` | Number of result objects in the task. A summary call returns one. |

### Notes

- Pass the search term in the `keyword` parameter, for example `nike`.
- Category values are numeric code lists such as `[10014, 13605, 13609]`. A `null` category groups content with no category.
- The result object is nested under `tasks[].result[]`. Read the first item of each list.

### Pricing

Billed at the actual cost of each call, about $0.024036 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/content_analysis/summary/live.json`](../../../../../../catalog/models/dataforseo/v3/content_analysis/summary/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/content_analysis/summary/live
