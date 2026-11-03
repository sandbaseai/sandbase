# Zhihu Keyword Search API: pricing, parameters and code examples

`zhihu/search` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Search Zhihu by keyword with optional result-type, sort, time-interval, topic-display, and offset controls. Use it to find relevant answers, articles, or videos.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/search", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/search', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/search", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/search", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/zhihu/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sorting criteria. one of: `upvoted_count`, `created_time` |
| `offset` | integer |  | Start offset, begins with 0. default `0` |
| `keyword` | string | yes | Search keywords.  |
| `vertical` | string |  | Result type filter. one of: `answer`, `article`, `zvideo` |
| `timeInterval` | string |  | Publish time interval filter. one of: `a_day`, `a_week`, `a_month`, `three_months`, `half_a_year`, `a_year` |
| `showAllTopics` | string |  | Whether to show all topics. one of: `FALSE`, `TRUE`; default `"FALSE"` |

## Details

Returns Zhihu search results for a keyword. Each result in `data` can be a major or topic card with nested discussion items such as questions and answers. The only required input is `keyword`.

### Use cases

- Find popular Zhihu discussions about a topic such as `人工智能` for content research.
- Collect question titles and answer text on a subject to study what people ask about it.
- Track how a topic is discussed over time by filtering with `timeInterval` and sorting by `created_time`.
- Pull answer counts and comment counts to rank which questions draw the most engagement.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keywords. |
| `offset` | integer | No | Start offset, begins with 0. |
| `showAllTopics` | string | No | Whether to show all topics. |
| `sort` | string | No | Sorting criteria. |
| `timeInterval` | string | No | Publish time interval filter. |
| `vertical` | string | No | Result type filter. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ab_params": "dm_a1_suppress=0;dm_hot_pin=1;d_new_search_h2=0;sb_slot_time=2;sb_sku_rel=1;dm_a…",
  "data": [
    {
      "highlight": {},
      "hit_labels": null,
      "id": "0ea2cc3a-3048-402e-a710-5ab9e5fae076",
      "index": 0,
      "object": {
        "attached_info_bytes": "Os0BEiBjOGEzZWNhYjIzNmE4Mjc2ZGJmZGE0MmVmMTczODFiNxh6Sgzkurrlt6Xmmbrog71QAFgBYAFq…",
        "major_info": {
          "avg_salary": 0,
          "classification": "工学",
          "degree": [
            "工学学士"
          ],
          "discussions": {
            "contents": [
              {
                "has_more": false,
                "id": "experience",
                "items": [
                  {
                    "highlight": {
                      "description": "985及以上可以去，这是一个赢者通吃很看能力的专业。985以下慎重，一堆线性代数都教不清楚的学校，开设了一堆名叫“<em>人工智能</em>”的专业罢了。",
                      "title": "<em>人工智能</em>专业前景怎么样？"
                    },
                    "hit_labels": null,
                    "object": {
                      "answer_count": 43,
                      "answer_type": "normal",
                      "attached_info_bytes": "OpkCCgtwbGFjZWhvbGRlchIgYzhhM2VjYWIyMzZhODI3NmRiZmRhNDJlZjE3MzgxYjcYBCIJNzY0MzUz…",
                      "author": {
                        "authority_info": null,
                        "avatar_url": "https://pica.zhimg.com/50/v2-687e9d0a8ef814155e9c326283d50b68_l.jpg?source=4e949…",
                        "badge": [],
                        "badge_v2": {
                          "detail_badges": [],
                          "icon": "",
                          "merged_badges": [],
                          "night_icon": "",
                          "title": ""
                        },
                        "badge_v2_string": "{\"title\":\"\",\"merged_badges\":[],\"detail_badges\":null,\"icon\":\"\",\"night_icon\":\"\"}",
                        "follower_count": 5,
                        "gender": 1,
                        "headline": "万物有灵。"
                      },
                      "biz_encoded_params": "sw%3D%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD",
                      "comment_count": 4,
                      "content": "<p data-pid=\"12yf8I3e\">985及以上可以去，这是一个赢者通吃很看能力的专业。985以下慎重，一堆线性代数都教不清楚的学校，开设了一堆名叫“…",
                      "created_time": 1767749630
                    },
                    "type": "search_result"
                  }
                ],
                "name": "就读体验"
              }
            ],
            "default_tab_id": "experience"
          },
          "genre": [
            "本科"
          ],
          "id": "0ea2cc3a-3048-402e-a710-5ab9e5fae076",
          "name": "<em>人工智能</em>",
          "top_area": ""
        },
        "type": "major"
      },
      "type": "gaokao"
    }
  ],
  "domain_info": {
    "first_category": "科技"
  },
  "filter_items": null,
  "hit_labels": null,
  "is_brand_word": false,
  "is_koc_words": false,
  "item_in_view": [
    {
      "index": 5,
      "token": "f789e8e4…",
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
    "attached_info_bytes": "OrABEiBjOGEzZWNhYjIzNmE4Mjc2ZGJmZGE0MmVmMTczODFiN0oM5Lq65bel5pm66IO9UABYAWABagzk…",
    "isfeed": false,
    "lc_idx": 20,
    "search_hash_id": "c8a3ecab236a8276dbfda42ef17381b7"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].id` | Unique ID of the search result entry. |
| `data[].index` | Position of the entry in the result list, starting at 0. |
| `data[].object.major_info.classification / data[].object.major_info.degree[]` | Subject category and degree name of a university major card, for example `工学` and `工学学士`. |
| `data[].object.major_info.discussions.contents[].name` | Name of a discussion group inside a major card, such as `就读体验` or `就业前景`. The `id` key in the same object holds a short label like `experience`, `future` or `hot`. |
| `data[].object.major_info.discussions.contents[].items[].highlight.title` | Question title with the matched keyword wrapped in `<em>` tags. |
| `data[].object.major_info.discussions.contents[].items[].highlight.description` | Text snippet from the answer or question with matched keywords wrapped in `<em>` tags. |
| `data[].object.major_info.discussions.contents[].items[].object.answer_count / data[].object.major_info.discussions.contents[].items[].object.comment_count` | Number of answers and number of comments on the item. |
| `data[].object.major_info.discussions.contents[].items[].object.content` | Answer body as an HTML string. Some responses cut it short. |
| `data[].object.major_info.discussions.contents[].items[].object.created_time` | Creation time as a Unix timestamp in seconds. |
| `data[].object.major_info.discussions.contents[].items[].object.author.follower_count / data[].object.major_info.discussions.contents[].items[].object.author.headline` | Follower count and profile headline of the author. |

### Notes

- Use `offset` to page through results. It starts at 0.
- Set `vertical` to `answer`, `article` or `zvideo` to limit the result type. Set `sort` to `upvoted_count` or `created_time` to change the order.
- Results can differ in shape, so check `type` and the keys inside `object` before you read fields. The sample response shows a major card with grouped discussions.
- To read a full answer, call [Zhihu Answer Details](/apis/zhihu/web/answer-detail). To search only articles, use [Zhihu Article Search](/apis/zhihu/web/article-search-v3).

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/zhihu/search.json`](../../../catalog/models/zhihu/search.json) · Store page: https://www.sandbase.ai/model/zhihu/search
