# Zhihu Ebook Search API: pricing, parameters and code examples

`zhihu/web/ebook-search-v3` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches Zhihu for ebooks matching a query term. Returns publication details including commodity IDs, SKU IDs, and direct product links.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/ebook-search-v3", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/ebook-search-v3', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/ebook-search-v3", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/ebook-search-v3", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/ebook-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of ebooks per page default `"20"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |
| `search_hash_id` | string |  | Search Hash ID default `""` |

## Details

Searches Zhihu for ebooks that match a keyword. Each result gives the title, authors, description, cover image, publish time and the `commodity_id` of the ebook. It needs one input, `keyword`.

### Use cases

- Build a list of Zhihu ebooks on a topic such as OpenAI, with titles, authors and cover images.
- Collect `commodity_id` values to index ebooks in a catalog.
- Track publication dates of ebooks about a subject over time.
- Page through all matches for a keyword to compare how many ebooks cover it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/ebook-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `limit` | string | No | Number of ebooks per page |
| `offset` | string | No | Offset |
| `search_hash_id` | string | No | Search Hash ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ab_params": "dm_a1_abc=0;sb_nvip_ecpm=1;sb_zhiedu=1;sb_vip_tag=1;dm_ai_search_safe=1;dm_AI_ho…",
  "data": [
    {
      "highlight": {},
      "hit_labels": null,
      "id": 674492,
      "index": 0,
      "object": {
        "ab_id_list": [
          "dm_a1_abc=0"
        ],
        "attached_info_bytes": "OrwECgtwbGFjZWhvbGRlchIgMDEzMWY4YmEzYjM5MGQyNGQxNGQzMDhhZGZlZGEzZTcYDyIGNjc0NDky…",
        "body": {
          "authors": [
            {
              "bio": "",
              "icon": "",
              "name": "雷韦春",
              "url_token": ""
            }
          ],
          "description": "<em>OpenAI</em> API 是一个为开发者、企业和研究者打造的平台。通过这个 API，用户可以轻松地融合和应用最前沿的 AI 技术",
          "images": [
            "https://picx.zhimg.com/v2-f22e1778a7fab84b1a2b9278761879ef.jpg?source=31184dd1"
          ],
          "play_icon": "",
          "publish_at": 1727417136,
          "show_author": "",
          "show_image": "",
          "title": "<em>OpenAI</em> API 接口应用实战"
        },
        "card_type": "",
        "card_version": "1",
        "commodity_id": "120480981",
        "commodity_type": "publication",
        "footer": ""
      },
      "type": "knowledge_ad"
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
    "attached_info_bytes": "OqQBEiAwMTMxZjhiYTNiMzkwZDI0ZDE0ZDMwOGFkZmVkYTNlN0oGb3BlbmFpUABYB2ABagZPcGVuQUlw…",
    "isfeed": false,
    "lc_idx": 9,
    "search_hash_id": "0131f8ba3b390d24d14d308adfeda3e7"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].object.commodity_id` | ID of the ebook as a string. Use it to identify the ebook across calls. |
| `data[].object.commodity_type` | Kind of item. Here the value is `publication`. |
| `data[].object.body.title` | Ebook title. Matched search terms are wrapped in `<em>` tags. |
| `data[].object.body.authors[].name` | Name of each author. Books with several authors return several rows. |
| `data[].object.body.description` | Short description of the ebook. It is cut off for long texts and may contain `<em>` tags around matched terms. |
| `data[].object.body.images[]` | Cover image URLs for the ebook. |
| `data[].object.body.publish_at` | Publish time as a Unix timestamp in seconds. |
| `data[].index / data[].id` | Position of the result in the list, and a numeric ID for the result row. |
| `paging.is_end / paging.next` | `is_end` is `false` when more results exist. `next` holds the URL for the next page. |
| `search_action_info.search_hash_id` | Hash ID for this search. Send it back as `search_hash_id` on later pages. |

### Notes

- Use `limit` for page size and `offset` to move through results. Both are sent as strings.
- Pass the `search_hash_id` from `search_action_info` in follow-up page requests for the same keyword.
- Strip the `<em>` tags from `title` and `description` before showing them as plain text.
- To find other Zhihu content on the same keyword, try [Zhihu Article Search](/apis/zhihu/web/article-search-v3) or [Zhihu Video Search (V3)](/apis/zhihu/web/video-search-v3).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/ebook-search-v3.json`](../../../../catalog/models/zhihu/web/ebook-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/ebook-search-v3
