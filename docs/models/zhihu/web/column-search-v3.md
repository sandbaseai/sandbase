# Zhihu Column Search API: pricing, parameters and code examples

`zhihu/web/column-search-v3` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches Zhihu columns matching a specified query term. Returns matching column profiles, follower counts, article totals, and snippet highlights with pagination support.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/column-search-v3", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/column-search-v3', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/column-search-v3", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/column-search-v3", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/column-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of columns per page default `"20"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |
| `search_hash_id` | string |  | Search Hash ID default `""` |

## Details

Searches Zhihu columns by keyword and returns a page of matching columns. Each result has the column ID, title with highlighted matches, follower count, article count and author details. The only required input is `keyword`.

### Use cases

- Find Zhihu columns that cover a topic such as OpenAI.
- Compare candidate columns by `followers` and `articles_count` before picking which to follow.
- Collect column IDs and descriptions for a topic to build a reading list or research set.
- Page through all matching columns for a keyword with `offset` and `limit`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/column-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `limit` | string | No | Number of columns per page |
| `offset` | string | No | Offset |
| `search_hash_id` | string | No | Search Hash ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ab_params": "dm_ai_search_safe=1;sb_caowei_4in10=1;sb_xg_search=1;dm_isocial=6;dm_ai_hot_ui=0…",
  "data": [
    {
      "highlight": {
        "content": "",
        "description": "",
        "title": "深入理解<em>OpenAI</em> 722篇数学论文"
      },
      "hit_labels": null,
      "id": "c_2091671086924670464",
      "index": 0,
      "object": {
        "articles_count": 20,
        "attached_info_bytes": "Ov8BCgtwbGFjZWhvbGRlchIgMGVmMzhhMjcwZmE5ZTg1MDQ2ZWU4YmMwOTQzZGE3NzQYBSIIMTM5NDAx…",
        "author": {
          "authority_info": [],
          "avatar_url": "https://picx.zhimg.com/50/v2-29f7a5d616b2689161e97fa9c3819784_l.jpg?source=4e949…",
          "badge": [],
          "badge_v2": {
            "detail_badges": [],
            "icon": "",
            "merged_badges": [],
            "night_icon": "",
            "title": ""
          },
          "badge_v2_string": "{\"title\":\"\",\"merged_badges\":[],\"detail_badges\":null,\"icon\":\"\",\"night_icon\":\"\"}",
          "follower_count": 0,
          "gender": 1,
          "headline": ""
        },
        "avatar_url": "https://picx.zhimg.com/v2-f111d7ee1c41944859e975a712c0883b_r.jpg?source=4e949a73",
        "column_type": "normal",
        "description": "",
        "flag": {
          "flag_text": "",
          "flag_type": ""
        },
        "followers": 54
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
    "attached_info_bytes": "OqQBEiAwZWYzOGEyNzBmYTllODUwNDZlZThiYzA5NDNkYTc3NEoGb3BlbmFpUABYBGABagZPcGVuQUlw…",
    "isfeed": false,
    "lc_idx": 20,
    "search_hash_id": "0ef38a270fa9e85046ee8bc0943da774"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].id` | Column ID, for example `c_2091671086924670464`. |
| `data[].highlight.title` | Column title. Matched search terms are wrapped in `<em>` tags. |
| `data[].highlight.description / data[].highlight.content` | Matching text from the column description, with matched terms wrapped in `<em>`. Both can be empty. |
| `data[].object.articles_count` | Number of articles in the column. |
| `data[].object.followers` | Number of followers of the column. |
| `data[].object.description` | Column description text. It can be empty. |
| `data[].object.column_type` | Type of the column, such as `normal`. |
| `data[].object.author.headline` | Short headline text from the column author's profile. |
| `paging.is_end` | `false` when more results exist, `true` on the last page. |
| `search_action_info.search_hash_id` | Hash ID of this search. It matches the `search_hash_id` request parameter. |

### Notes

- Set `limit` for page size and `offset` to move through results. Check `paging.is_end` to know when to stop.
- Pass `search_hash_id` from `search_action_info.search_hash_id` when requesting later pages of the same search.
- Use the [Zhihu Column Articles](/apis/zhihu/web/column-articles) API to read the articles in a column, and [Zhihu Similar Column Recommendations](/apis/zhihu/web/column-recommend) to find related columns.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/column-search-v3.json`](../../../../catalog/models/zhihu/web/column-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/column-search-v3
