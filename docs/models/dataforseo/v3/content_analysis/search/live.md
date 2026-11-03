# DataForSEO Content Analysis Search API: pricing, parameters and code examples

`dataforseo/v3/content_analysis/search/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02418 per call · **Modes:** sync

Returns web content analysis results matching specified search topics. Useful for evaluating online content, monitoring discussions, and performing natural language processing workflows across web sources.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02418**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/content_analysis/search/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/content_analysis/search/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/content_analysis/search/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/content_analysis/search/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/content_analysis/search/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `keyword` | string |  | Search query.  |

## Details

Returns web pages that mention a keyword, with sentiment scores, a content quality score and domain details for each page. It needs a `keyword` and an optional `limit` for the number of results.

### Use cases

- Pull pages that mention a brand such as `nike` and compare their positive and negative sentiment scores.
- Find high-ranking domains that write about a topic, using `domain_rank` to sort outreach targets.
- Filter mentions by `language` or `country` to see how a topic appears in different markets.
- Feed page-level sentiment and quality scores into a content monitoring or NLP pipeline.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/content_analysis/search/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "nike", "limit": 5}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query. |
| `limit` | integer | No | Maximum number of results (up to 100). |

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
        "function": "search",
        "keyword": "nike",
        "limit": 5
      },
      "id": "11030828-2190-0463-0000-97b94d154e5f",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "content_info": {
                "author": null,
                "connotation_types": {
                  "negative": 0.14120648801326752,
                  "neutral": 0.19344741106033325,
                  "positive": 0.6653761863708496
                },
                "content_quality_score": 94,
                "content_type": "page_content",
                "date_published": null,
                "group_date": "2019-01-16 04:49:50 +00:00",
                "highlighted_text": null,
                "language": "en"
              },
              "country": "CA",
              "domain": "www.ssense.com",
              "domain_rank": 456,
              "fetch_time": "2026-07-21 12:08:42 +00:00",
              "language": "en",
              "main_domain": "ssense.com",
              "page_category": [
                10014
              ]
            }
          ],
          "items_count": 5,
          "offset_token": "eyJDdXJy…",
          "total_count": 146180252
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "34.6436 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "34.6552 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Total number of pages that match the keyword. Only the first `limit` pages come back in `items`. |
| `tasks[].result[].items_count` | Number of items returned in this response. |
| `tasks[].result[].items[].domain / main_domain` | Host name of the page and its root domain, for example `about.nike.com` and `nike.com`. |
| `tasks[].result[].items[].domain_rank` | Rank value for the domain. A higher value means a stronger domain in the response. |
| `tasks[].result[].items[].content_info.connotation_types.positive / negative / neutral` | Sentiment scores between 0 and 1 for the page content. The three values add up to about 1. |
| `tasks[].result[].items[].content_info.content_quality_score` | Quality score for the page content. The sample values run from 93 to 100. |
| `tasks[].result[].items[].content_info.language / country` | Language code of the content, and the country code of the page (`country` sits on the item itself). |
| `tasks[].result[].items[].fetch_time` | Date and time the page was fetched, in the format `2026-10-03 14:31:40 +00:00`. |
| `tasks[].result[].items[].content_info.group_date` | Date tied to the content, in the same timestamp format. `date_published` is often `null`. |
| `tasks[].result[].offset_token` | Token that marks where this result page ended. It encodes the current offset and the original request. |

### Notes

- Set `limit` to control how many items you get. The parameter accepts up to 100.
- `offset_token` in the response points to the next page of results for the same search.
- Several fields such as `author`, `date_published` and `highlighted_text` can be `null`, so check for them before use.
- `page_category` holds a list of numeric category codes for each page.

### Pricing

Billed at the actual cost of each call, about $0.02418 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/content_analysis/search/live.json`](../../../../../../catalog/models/dataforseo/v3/content_analysis/search/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/content_analysis/search/live
