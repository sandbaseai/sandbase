# Zhihu User Search API: pricing, parameters and code examples

`zhihu/web/user-search-v3` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search for Zhihu user profiles by query terms. Returns matching accounts along with follower numbers, article counts, and answer statistics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/user-search-v3", "keyword": "deepseek"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/user-search-v3', {'keyword': 'deepseek'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/user-search-v3", {
  "keyword": "deepseek"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/user-search-v3", sandbase.Params{
	"keyword": "deepseek",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/user-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of users per page default `"25"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |

## Details

This API searches Zhihu for user accounts that match a `keyword`. Each result includes the account's answer count, article count, total creation count, avatar and verification badges.

### Use cases

- Find official brand or organization accounts on Zhihu by searching a product or company name.
- Compare how many answers and articles each matching creator has published.
- Build a list of verified accounts on a topic such as `deepseek` for outreach research.
- Collect user IDs from search results to feed into other Zhihu user lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/user-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "deepseek"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `limit` | string | No | Number of users per page |
| `offset` | string | No | Offset |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ab_params": "sb_kvip_xz=1;dm_ai_hot_ui=0;dm_rum_v5=1;dm_tag_t5gemma=1;dm_aicard_mutex=1;dm_v_…",
  "data": [
    {
      "highlight": {
        "description": "",
        "title": "<em>DeepSeek</em>"
      },
      "hit_labels": null,
      "id": 4029889030,
      "index": 0,
      "object": {
        "answer_count": 0,
        "articles_count": 4,
        "attached_info_bytes": "OpgCCgtwbGFjZWhvbGRlchIgOTRmOWY3ZTcyMjM5ODM2OGQ0N2Y3MGFlZGE0OGMxMjIYASIKMTU1OTI2…",
        "avatar_url": "https://picx.zhimg.com/50/v2-dabcd3ba1cbbf8e188aac13ad1a25106_l.jpg?source=4e949…",
        "badge": [
          {
            "description": "已认证账号",
            "topics": [],
            "type": "identity"
          }
        ],
        "badge_v2": {
          "detail_badges": [
            {
              "description": "已认证机构号",
              "detail_type": "identity_org",
              "icon": "https://picx.zhimg.com/v2-2ddc5cc683982648f6f123616fb4ec09_l.png?source=32738c0c",
              "night_icon": "https://pic1.zhimg.com/v2-2ddc5cc683982648f6f123616fb4ec09_l.png?source=32738c0c",
              "sources": [],
              "title": "已认证机构号",
              "type": "identity",
              "url": "https://www.zhihu.com/term/institution-settle"
            }
          ],
          "icon": "https://picx.zhimg.com/v2-2ddc5cc683982648f6f123616fb4ec09_l.png?source=32738c0c",
          "merged_badges": [
            {
              "description": "已认证机构号",
              "detail_type": "identity_org",
              "icon": "",
              "night_icon": "",
              "sources": [],
              "title": "认证",
              "type": "identity",
              "url": "https://www.zhihu.com/term/institution-settle"
            }
          ],
          "night_icon": "https://picx.zhimg.com/v2-2ddc5cc683982648f6f123616fb4ec09_l.png?source=32738c0c",
          "title": "已认证机构号"
        },
        "badge_v2_string": "{\"title\":\"已认证机构号\",\"merged_badges\":[{\"type\":\"identity\",\"detail_type\":\"identity_or…",
        "creation_count": 4
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
    "next": "https://api.zhihu.com/search_v3?advert_count=0&correction=1&filter_fields=&gk_ve…"
  },
  "pendant": null,
  "related_search_result": [],
  "search_action_info": {
    "attached_info_bytes": "OqgBEiA5NGY5ZjdlNzIyMzk4MzY4ZDQ3ZjcwYWVkYTQ4YzEyMkoIZGVlcHNlZWtQAFgCYAFqCGRlZXBz…",
    "isfeed": false,
    "lc_idx": 20,
    "search_hash_id": "94f9f7e722398368d47f70aeda48c122"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].id` | Numeric ID of the search hit. It is a number, not the same as the user token in other Zhihu APIs. |
| `data[].index` | Position of the result in the list, starting at `0`. |
| `data[].highlight.title / data[].highlight.description` | The user's name and bio text with the matched keyword wrapped in `<em>` tags. `description` can be an empty string. |
| `data[].object.answer_count / data[].object.articles_count / data[].object.creation_count` | Counts of answers, articles and total creations for the account. For example, one result shows `1147` answers, `32` articles and `5788` creations. |
| `data[].object.avatar_url` | Link to the account's avatar image. |
| `data[].object.badge[].description` | Plain text of each verification badge, such as a certified account or a certified organization. The list is empty for accounts without badges. |
| `data[].object.badge_v2.title` | Short title of the account's main badge. It is an empty string when the account has none. |
| `paging.is_end` | `false` when more results are available. `true` means no more pages. |
| `paging.next` | Full URL for the next page of results. |
| `search_action_info.search_hash_id` | Identifier for this search session, which also appears inside `paging.next`. |

### Notes

- Only `keyword` is required. Set `limit` and `offset` as strings to page through results, for example `offset` of `20` for the next page.
- Check `paging.is_end` to know when to stop paging.
- In the sample response, `paging.next` uses `limit=20` and `offset=20`, so the next page starts after the first 20 results.
- To search other Zhihu content by the same keyword, use [Zhihu Article Search](/apis/zhihu/web/article-search-v3).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/user-search-v3.json`](../../../../catalog/models/zhihu/web/user-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/user-search-v3
