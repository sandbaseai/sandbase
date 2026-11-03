# Zhihu Scholar Paper Search API: pricing, parameters and code examples

`zhihu/web/scholar-search-v3` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search Zhihu Scholar papers matching specified keywords and filters. Returns paper details including IDs, titles, highlight snippets, and Zhihu paper URLs.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/scholar-search-v3", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/scholar-search-v3', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/scholar-search-v3", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/scholar-search-v3", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/scholar-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of papers per page default `"25"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |
| `indexed_by` | string |  |  default `""` |
| `classification` | string |  |  default `""` |
| `advanced_filter` | string |  |  default `"keywords,title,authors,abstract"` |

## Details

Searches Zhihu Scholar for academic papers that match a keyword. It needs one input, `keyword`, and returns a page of papers with titles, authors, journal, keywords, and highlighted snippets.

### Use cases

- Build a reading list of papers that mention a company or topic, such as `OpenAI`.
- Collect author names and journal names to see who publishes on a subject.
- Scan the `<em>` highlight snippets to check how a keyword appears in each title and abstract.
- Page through results to build a paper dataset for a keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/scholar-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `advanced_filter` | string | No |  |
| `classification` | string | No |  |
| `indexed_by` | string | No |  |
| `limit` | string | No | Number of papers per page |
| `offset` | string | No | Offset |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ab_params": "sb_vip_xunzhi=1;sb_sku_ui=1;sb_slot_domain=2;dm_search_pregen=1;dm_ai_corner1=0;…",
  "data": [
    {
      "highlight": {
        "excerpt": "intelligence(AI)tool was developed using the <em>OpenAI</em>—Application Program…",
        "title": "Automation of Software Development Stages with the <em>OpenAI</em> API"
      },
      "hit_labels": null,
      "id": "2014571995023581630",
      "index": 0,
      "object": {
        "attached_info_bytes": "Ov8BCgtwbGFjZWhvbGRlchIgNWVkYzhhNWU2MjZjNTU4YmUwM2ZmZjhlYmNmN2E4MDkYhQEiEzIwMTQ1…",
        "authors": [
          "Verónica C.Tapia"
        ],
        "excerpt": "In recent years,automation has become a key focus in software development as org…",
        "id": "2014571995023581630",
        "journal": "Computer Systems Science & Engineering",
        "journal_volume": "49",
        "keywords": [
          "Artificial intelligence tools"
        ],
        "period": "1"
      },
      "type": "search_result"
    }
  ],
  "domain_info": {
    "first_category": ""
  },
  "filter_items": null,
  "hit_labels": null,
  "is_brand_word": false,
  "is_koc_words": false,
  "item_in_view": [
    {
      "index": 5,
      "token": "b62a7302…",
      "type": "user_survey"
    }
  ],
  "paging": {
    "is_end": false,
    "next": "https://api.zhihu.com/search_v3?advert_count=0&correction=1&filter_fields=%7B%27…"
  },
  "pendant": null,
  "related_search_result": [],
  "search_action_info": {
    "attached_info_bytes": "OqQBEiA1ZWRjOGE1ZTYyNmM1NThiZTAzZmZmOGViY2Y3YTgwOUoGb3BlbmFpUABYGWABagZPcGVuQUlw…",
    "isfeed": false,
    "lc_idx": 10,
    "search_hash_id": "5edc8a5e626c558be03fff8ebcf7a809"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].id` | ID of the search result. It matches the paper ID in `data[].object.id`. |
| `data[].highlight.title` | Paper title with each keyword match wrapped in `<em>` tags. |
| `data[].highlight.excerpt` | Snippet of the abstract around the match, with `<em>` tags on the keyword. |
| `data[].object.authors[]` | List of author names for the paper. |
| `data[].object.journal / data[].object.journal_volume / data[].object.period` | Journal name, volume, and issue number (`period`) of the paper. `journal_volume` is missing on some items. |
| `data[].object.keywords[]` | Keywords the paper lists for itself. |
| `data[].object.excerpt` | Plain-text abstract excerpt with no highlight tags. It is cut short. |
| `data[].object.title` | Plain title without highlight tags. It appears on some items only. |
| `paging.is_end` | `false` when more results are available. Use it to decide whether to request another page. |
| `paging.next` | URL for the next page of results. |

### Notes

- Set `keyword` to the search term. `limit` sets the page size and `offset` sets where the page starts. Both are strings.
- Keep reading pages until `paging.is_end` is `true`.
- Paper IDs are long numeric strings. Treat them as strings, not numbers.
- To search other Zhihu content, try [Zhihu Article Search](/apis/zhihu/web/article-search-v3) or [Zhihu Ebook Search](/apis/zhihu/web/ebook-search-v3).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/scholar-search-v3.json`](../../../../catalog/models/zhihu/web/scholar-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/scholar-search-v3
