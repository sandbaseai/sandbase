# Xiaohongshu (RED) User Search

`xiaohongshu/app-v2/search-users` · api · Xiaohongshu

Returns Xiaohongshu user profiles matching a specified query term. Includes user identifiers, verification details, and follower count metrics.

## Pricing

- **$0.015 per call** (USD)
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

Search for Xiaohongshu accounts by providing a search term in `keyword`. Supports pagination via `page` and `search_id`.

### Use cases

- Find relevant creators on Xiaohongshu by niche or brand name.
- Retrieve profile identifiers and official verification status for influencer research.
- Track creator fan scale metrics through search results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/search-users" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "小红书"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `page` | integer | No | Page number, start from 1 |
| `source` | string | No | Source, default "explore_feed" |
| `search_id` | string | No | Search ID, pass value from first search response for pagination |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "users": [
      {
        "desc": "官方账号",
        "id": "59f985684eacab1ce3cc5409",
        "link": "xhsdiscover://1/user/user.59f985684eacab1ce3cc5409",
        "name": "小红书REDesign",
        "red_id": "63044481856",
        "red_official_verified": true,
        "red_official_verify_type": 0,
        "sub_title": "Fans 576.1k"
      }
    ]
  }
}
```

### Notes

- `page` starts from 1 for paginating through search results.
- Pass `search_id` returned from the initial search response when requesting subsequent pages.
- `source` defaults to "explore_feed" if not specified.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/model/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/model/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/model/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/search-users.json`](../../../../catalog/models/xiaohongshu/app-v2/search-users.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/search-users
