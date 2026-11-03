# Zhihu Salt Content Search API: pricing, parameters and code examples

`zhihu/web/salt-search-v3` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Zhihu Salt column and chapter search results matching a specified keyword. Supports pagination with offset and limit parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/salt-search-v3", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/salt-search-v3', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/salt-search-v3", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/salt-search-v3", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/salt-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of contents per page default `"20"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |
| `search_hash_id` | string |  | Search Hash ID default `""` |

## Details

Returns Zhihu Salt search results for a keyword. Each result is a paid column chapter with a title, description, author label and cover image. The only required input is `keyword`.

### Use cases

- Find paid Salt column chapters that mention a topic such as `OpenAI`.
- Build a list of chapter titles, descriptions and cover images for a content catalog.
- Track which Salt stories appear for a keyword by comparing `publish_at` dates.
- Page through all Salt results for a keyword with `offset` and `limit`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/salt-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `limit` | string | No | Number of contents per page |
| `offset` | string | No | Offset |
| `search_hash_id` | string | No | Search Hash ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ab_params": "dm_ai_rerank=3;sb_caowei_4in10=1;sb_pe=0;sb_kvip_xz=1;sb_nvip_ecpm=1;dm_related_…",
  "data": [
    {
      "highlight": {},
      "hit_labels": null,
      "id": 2016492680432075307,
      "index": 0,
      "object": {
        "ab_id_list": [
          "dm_ai_rerank=3"
        ],
        "attached_info_bytes": "OpYFCgtwbGFjZWhvbGRlchIgNDEyNzk4MGZlOGFhYzQyNjBkYjhhNzc1OTlmYmIwNDQYUyITMjAxODQw…",
        "body": {
          "authors": [
            {
              "name": "来自「 OpenClaw教我杀死了老公」",
              "url_token": ""
            }
          ],
          "description": "老公是 AI 工程师，他送了我一个 AI 助手「小虾」。他说小虾能通过大数据分析和行为干预，提高我们的夫妻感情。设置它时，我开玩笑说：「把我老公设定成永远不会背…",
          "images": [
            "https://pic1.zhimg.com/v2-afd40787055893006fed9aeafba7c405.jpg?source=31184dd1"
          ],
          "play_icon": "",
          "publish_at": 1774006859,
          "show_author": "",
          "show_image": "",
          "title": "OpenClaw教我杀死了老公"
        },
        "card_type": "",
        "card_version": "1",
        "commodity_id": "2016492680432075307",
        "commodity_type": "paid_column_chapter",
        "finish_label": {
          "text": "已完结"
        }
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
    "attached_info_bytes": "OqQBEiA0MTI3OTgwZmU4YWFjNDI2MGRiOGE3NzU5OWZiYjA0NEoGb3BlbmFpUABYFWABagZPcGVuQUlw…",
    "isfeed": false,
    "lc_idx": 2,
    "search_hash_id": "4127980fe8aac4260db8a77599fbb044"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].id / data[].object.commodity_id` | Identifier of the chapter. The top-level `id` is a number and `commodity_id` is the same value as a string. |
| `data[].object.commodity_type` | Kind of item. In this response the value is `paid_column_chapter`. |
| `data[].object.body.title` | Title of the chapter. |
| `data[].object.body.description` | Text excerpt from the chapter. It is cut off with an ellipsis. |
| `data[].object.body.authors[].name` | Author label for the chapter. It reads like a column name, such as `来自「…」`. `url_token` was empty in this response. |
| `data[].object.body.images[]` | Cover image URLs for the chapter. |
| `data[].object.body.publish_at` | Publish time as a Unix timestamp in seconds. |
| `data[].object.finish_label.text` | Completion label of the story, for example `已完结`. |
| `paging.is_end / paging.next` | `is_end` is `false` when more results exist. `next` is the URL of the next page. |
| `search_action_info.search_hash_id` | Hash ID of this search session. You can send it back as `search_hash_id`. |

### Notes

- Set `keyword` to the search term. `limit` defaults to `20` and `offset` defaults to `0`. Both are strings.
- To get the next page, raise `offset` by the number of items you received. Stop when `paging.is_end` is `true`.
- Pass the value of `search_action_info.search_hash_id` as `search_hash_id` on later page requests to stay in the same search session.
- To search other Zhihu content, try [Zhihu Column Search](/apis/zhihu/web/column-search-v3) or [Zhihu Ebook Search](/apis/zhihu/web/ebook-search-v3).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/salt-search-v3.json`](../../../../catalog/models/zhihu/web/salt-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/salt-search-v3
