# Zhihu Article Search API: pricing, parameters and code examples

`zhihu/web/article-search-v3` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offset pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/article-search-v3", "keyword": "教育", "limit": "5", "offset": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/article-search-v3', {'keyword': '教育', 'limit': '5', 'offset': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/article-search-v3", {
  "keyword": "教育",
  "limit": "5",
  "offset": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/article-search-v3", sandbase.Params{
	"keyword": "教育",
	"limit": "5",
	"offset": "0",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/article-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Empty comprehensive sorting default `""` |
| `limit` | string |  | Number of articles per page default `"20"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |
| `vertical` | string |  | Empty unlimited type default `""` |
| `search_source` | string |  | Search Source default `"Normal"` |
| `time_interval` | string |  | Time interval default `""` |
| `vertical_info` | string |  | Vertical information default `""` |
| `search_hash_id` | string |  | Search Hash ID, used to filter duplicate search results default `""` |
| `show_all_topics` | integer |  | Show all topics default `0` |

## Details

Searches Zhihu for a keyword and returns matching questions, answers and articles. Each result includes highlighted title and excerpt text, the author, and vote, answer and comment counts. The only required input is `keyword`.

### Use cases

- Track how a company or product such as OpenAI is discussed on Zhihu by pulling the top matching answers and questions.
- Find high-engagement answers on a topic by comparing `comment_count` and `answer_count` across results.
- Collect result text and author details on a topic for content analysis.
- Spot recent discussion threads on a keyword through the `hot_timing` result block.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/article-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `limit` | string | No | Number of articles per page |
| `offset` | string | No | Offset |
| `search_hash_id` | string | No | Search Hash ID, used to filter duplicate search results |
| `search_source` | string | No | Search Source |
| `show_all_topics` | integer | No | Show all topics |
| `sort` | string | No | Empty comprehensive sorting |
| `time_interval` | string | No | Time interval |
| `vertical` | string | No | Empty unlimited type |
| `vertical_info` | string | No | Vertical information |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ab_params": "sb_eduzhi=1;dm_pu_sug=0;dm_ai_corner1=0;dm_ai_hot_more=0;dm_a1_suppress=1;sb_new…",
  "data": [
    {
      "highlight": null,
      "hit_labels": null,
      "index": 0,
      "object": {
        "attached_info_bytes": "OsYBEiA1MDJlNTkxZGJmYzdkMjhjZjRjZjZmOGQxNmVhMmE2OBhxKhJPcGVuQUnkvLDlgLznvKnmsLRK…",
        "background_color": "",
        "campaign_type": "normal",
        "content_items": [
          {
            "index": 1,
            "object": {
              "answer_count": 0,
              "attached_info_bytes": "OoICCgtwbGFjZWhvbGRlchIgNTAyZTU5MWRiZmM3ZDI4Y2Y0Y2Y2ZjhkMTZlYTJhNjgYAyIJMTIxODQw…",
              "comment_count": 0,
              "description": "#OpenAI估值缩水1500亿美元# 【#每经热评#丨OpenAI砍估值砍融资，美国AI产业的“供给侧”叙事步入拐点】#美国AI产业的供给侧叙事步入拐点#10…",
              "follower_count": 0,
              "id": "2100618848953227176",
              "is_anonymous": false,
              "relationship": {
                "is_following": false
              }
            },
            "type": "question"
          }
        ],
        "description": {
          "index": 0,
          "object": {
            "answer_count": 0,
            "attached_info_bytes": "OvwBCgtwbGFjZWhvbGRlchIgNTAyZTU5MWRiZmM3ZDI4Y2Y0Y2Y2ZjhkMTZlYTJhNjgYAyIJMTIxODQw…",
            "comment_count": 0,
            "description": "#OpenAI估值缩水1500亿美元# 【#每经热评#丨OpenAI砍估值砍融资，美国AI产业的“供给侧”叙事步入拐点】#美国AI产业的供给侧叙事步入拐点#10…",
            "follower_count": 0,
            "id": "2100618848953227176",
            "is_anonymous": false,
            "relationship": {
              "is_following": false
            }
          },
          "type": "question"
        },
        "expert": "",
        "has_more": false,
        "icon_title": "最新讨论"
      },
      "type": "hot_timing"
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
    "next": "https://api.zhihu.com/search_v3?advert_count=0&correction=1&filter_fields=&gk_ve…"
  },
  "pendant": null,
  "related_search_result": [],
  "search_action_info": {
    "attached_info_bytes": "OqQBEiA1MDJlNTkxZGJmYzdkMjhjZjRjZjZmOGQxNmVhMmE2OEoGb3BlbmFpUABYAWABagZPcGVuQUlw…",
    "isfeed": false,
    "lc_idx": 20,
    "search_hash_id": "502e591dbfc7d28cf4cf6f8d16ea2a68"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].type` | Kind of result block. The sample shows `search_result` for normal hits and `hot_timing` for a block of recent discussion. |
| `data[].object.answer_count` | Number of answers on a matching question. |
| `data[].object.comment_count` | Number of comments on the matched item. |
| `data[].object.author.follower_count / data[].object.author.headline` | Follower count and profile headline of the author. |
| `data[].object.content` | Body of the answer or article as an HTML string. The sample value is cut off. |
| `data[].object.created_time` | Creation time of the item as a Unix timestamp in seconds. |
| `data[].highlight.title / data[].highlight.description` | Matched title and excerpt text. Search terms are wrapped in `<em>` tags. |
| `data[].object.content_items[].object.description` | Text of the question shown in a `hot_timing` block, with its `id` and `answer_count`. |
| `paging.is_end / paging.next` | `is_end` shows whether more results exist. `next` holds the URL of the following page. |
| `search_action_info.search_hash_id` | Hash ID for this search. Pass it as `search_hash_id` on later pages to filter duplicate results. |

### Notes

- Page through results with `offset` and `limit`. The `next` URL in `paging` shows `limit=20` and `offset=20` for the second page.
- Copy `search_action_info.search_hash_id` into `search_hash_id` when you request later pages.
- Result blocks differ by `type`, so check `data[].type` before you read fields. `hot_timing` blocks have no `highlight` text and no `author`.
- To read a full question, call [Zhihu Question Detail](/apis/zhihu/web/question-detail). For one answer, call [Zhihu Answer Details](/apis/zhihu/web/answer-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu Hot List](/apis/zhihu/web/hot-list): Get the Zhihu hot list: trending questions with title, excerpt, heat, answer and follower counts, and links.
- [Get Zhihu AI Search (v2)](/apis/zhihu/web/ai-search-stream): Get Zhihu AI Search results (new endpoint).
- [Get Zhihu Answer Detail](/apis/zhihu/web/answer-detail): Get a single Zhihu answer's detail (content / stats / author / question, etc.).

---
Machine-readable: [`catalog/models/zhihu/web/article-search-v3.json`](../../../../catalog/models/zhihu/web/article-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/article-search-v3
