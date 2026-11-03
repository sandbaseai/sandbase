# TikTok Web Explore Posts API: pricing, parameters and code examples

`tiktok/web/explore-post` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns explore feed posts from TikTok Web, filtered by video category and page count, along with author metrics and audio details.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/explore-post", "categoryType": "120", "count": 16}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/explore-post', {'categoryType': '120', 'count': 16})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/explore-post", {
  "categoryType": "120",
  "count": 16
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/explore-post", sandbase.Params{
	"categoryType": "120",
	"count": 16,
})
```

Same call via the path form: `POST /v1/api/tiktok/web/explore-post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page default `16` |
| `categoryType` | string |  | Video category default `"120"` |

## Details

Access explore feed videos from TikTok Web by specifying optional parameters such as `categoryType` and `count`.

### Use cases

- Discover trending videos within specific content categories.
- Analyze engagement metrics such as play, digg, and share counts.
- Look up author stats and background audio details for explore posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/explore-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number per page |
| `categoryType` | string | No | Video category |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "itemList": [
    {
      "CategoryType": 120,
      "createTime": 1789793820,
      "desc": "ប្រទេស​នីមួយៗ​មានចំណុចល្អនិងមិនល្អ​រៀងខ្លួន​",
      "id": "7687105888674385160",
      "itemCommentStatus": 0,
      "textLanguage": "km",
      "textTranslatable": true,
      "author": {
        "id": "6964213552958473217",
        "nickname": "<user>",
        "privateAccount": false,
        "verified": false
      },
      "authorStats": {
        "diggCount": 1407,
        "followerCount": 51800,
        "followingCount": 629,
        "friendCount": 0,
        "heartCount": 731700,
        "videoCount": 122
      },
      "authorStatsV2": {
        "diggCount": "1407",
        "followerCount": "51800",
        "followingCount": "629",
        "friendCount": "0",
        "heartCount": "731700",
        "videoCount": "122"
      },
      "music": {
        "authorName": "English by Solida",
        "duration": 130,
        "id": "7687105936380414728",
        "shoot_duration": 130,
        "title": "original sound - English by Solida"
      },
      "penaltyContext": {
        "arb_content_safety_status": 102,
        "display_penalty_type": 0,
        "display_ui_type": 0,
        "status": 102,
        "tns_status": 102,
        "video_status": 10
      },
      "stats": {
        "collectCount": 340,
        "commentCount": 97,
        "diggCount": 9454,
        "playCount": 102200,
        "shareCount": 393
      },
      "statsV2": {
        "collectCount": "340",
        "commentCount": "97",
        "diggCount": "9454",
        "playCount": "102200",
        "repostCount": "0",
        "shareCount": "393"
      }
    }
  ]
}
```

### Notes

- Specify `categoryType` to filter explore posts by a particular category.
- Use `count` to control the number of posts returned per page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/explore-post.json`](../../../../catalog/models/tiktok/web/explore-post.json) · Store page: https://www.sandbase.ai/model/tiktok/web/explore-post
