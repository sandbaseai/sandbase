# Xiaohongshu (RED) User Search API: pricing, parameters and code examples

`xiaohongshu/app-v2/search-users` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns Xiaohongshu user profiles matching a specified query term. Includes user identifiers, verification details, and follower count metrics.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/search-users", "keyword": "技术爬爬虾", "page": 1, "source": "explore_feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/search-users', {'keyword': '技术爬爬虾', 'page': 1, 'source': 'explore_feed'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/search-users", {
  "keyword": "技术爬爬虾",
  "page": 1,
  "source": "explore_feed"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/search-users", sandbase.Params{
	"keyword": "技术爬爬虾",
	"page": 1,
	"source": "explore_feed",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/search-users` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, start from 1 default `1` |
| `source` | string |  | Source, default "explore_feed" default `"explore_feed"` |
| `keyword` | string | yes | Search keyword  |
| `search_id` | string |  | Search ID, pass value from first search response for pagination default `""` |

## Details

Returns a page of Xiaohongshu (RED) user accounts that match a search term. Each result has the user ID, display name, RED ID, verification flags, and a follower label. The only required input is `keyword`.

### Use cases

- Find creator and brand accounts on Xiaohongshu that match a niche or brand name.
- Collect user IDs and RED IDs to look up full profiles or posted notes later.
- Check which accounts carry an official verification flag before shortlisting them.
- Compare follower sizes across search results with the `sub_title` label.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/search-users" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "小红书"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `page` | integer | No | Page number, start from 1 |
| `search_id` | string | No | Search ID, pass value from first search response for pagination |
| `source` | string | No | Source, default "explore_feed" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "filters": [
      {
        "filter_tags": [
          {
            "icon_tail_url": "",
            "icon_tail_url_night": "",
            "icon_url": "",
            "icon_url_night": "",
            "id": "all",
            "name": "All",
            "need_location_info": false,
            "origin_text": ""
          }
        ],
        "group_show_type": 0,
        "id": "fans_count",
        "invisible": true,
        "name": "Followers",
        "type": "single",
        "word_request_id": "71db60eedf9fe0be6ff5538195b2f1f1"
      }
    ],
    "users": [
      {
        "desc": "官方账号",
        "followed": false,
        "id": "59f985684eacab1ce3cc5409",
        "image": "https://sns-avatar-qc.xhscdn.com/avatar/600e72c904b7c90001c6e3bf.jpg?imageView2/…",
        "link": "xhsdiscover://1/user/user.59f985684eacab1ce3cc5409",
        "name": "小红书REDesign",
        "reason": "",
        "red_id": "63044481856",
        "red_official_verified": true,
        "red_official_verify_type": 0,
        "self": false,
        "show_red_official_verify_icon": false
      }
    ]
  },
  "debug_id": "88ccd612",
  "debug_info": "gAAAAABq6ZFs1ibV7bP6A-JK73XWLOTYM3KJaXbSgyAbPq8pvyOCx7gNSP7HregcC4Xa3-EQL8VNxM7e…",
  "next_page": 2,
  "page": 1,
  "search_id": "20f427c7a6d3496b",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.users[].id` | The user ID of the account. Use it as the user identifier in other Xiaohongshu user calls. |
| `data.users[].red_id` | The public RED ID of the account, shown as a numeric string. |
| `data.users[].name` | The display name of the account. |
| `data.users[].desc` | Short profile label for the account. Official accounts show `官方账号` here. |
| `data.users[].sub_title` | Follower count as display text, for example `Fans 581.2k`. It is a rounded label, not a number. |
| `data.users[].red_official_verified / data.users[].red_official_verify_type` | Whether the account has official verification, and a numeric code for the verification type. The meaning of each code is not described in the response. |
| `data.users[].show_red_official_verify_icon` | Whether the app shows the verification icon next to the account. |
| `data.users[].image` | URL of the account avatar image. |
| `data.users[].link` | App deep link that opens the user profile in the Xiaohongshu app. |
| `search_id` | ID of this search. Send it back in `search_id` when you request the next page. |

### Notes

- `next_page` in the response gives the page number to request next, and `page` shows the current page. Set `page` to that value to continue.
- Pass the `search_id` from the first response on every later page request.
- `data.filters` lists filter groups such as `fans_count` and `user_type`, each with tag IDs like `0-100` and `personal_verification`. The request schema has no parameter for them.
- To get full profile details for a result, call [Xiaohongshu (RED) User Information](/apis/xiaohongshu/app-v2/user-info) with the user ID. To see their posts, call [Xiaohongshu (RED) User Posted Notes](/apis/xiaohongshu/app-v2/user-posted-notes).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/search-users.json`](../../../../catalog/models/xiaohongshu/app-v2/search-users.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/search-users
