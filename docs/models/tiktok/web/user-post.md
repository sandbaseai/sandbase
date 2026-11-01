# TikTok User Posts

`tiktok/web/user-post` · api · TikTok

Returns a list of posts from a specific TikTok user using their `secUid`, including video details, author metrics, and interaction statistics.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/user-post", "count": 3, "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/user-post', {'count': 3, 'secUid': 'MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/user-post", {
  "count": 3,
  "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/user-post", sandbase.Params{
	"count": 3,
	"secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/user-post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page, default is 20, cannot be changed. default `20` |
| `cursor` | integer |  | Page cursor default `0` |
| `secUid` | string | yes | User secUid  |
| `coverFormat` | integer |  | Cover format, default is 2, optional values are 1 or 2. default `2` |
| `post_item_list_request_type` | integer |  | Sort type default `0` |

## Details

Fetch post lists for any TikTok user using their `secUid`. Supports cursor pagination via `cursor` and custom sorting with `post_item_list_request_type`.

### Use cases

- Retrieve recent video posts from a target TikTok user profile.
- Track post metrics including play, digg, comment, and share counts.
- Inspect background music details and author statistics across user posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | Yes | User secUid |
| `count` | integer | No | Number per page, default is 20, cannot be changed. |
| `cursor` | integer | No | Page cursor |
| `coverFormat` | integer | No | Cover format, default is 2, optional values are 1 or 2. |
| `post_item_list_request_type` | integer | No | Sort type |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "itemList": [
    {
      "CategoryType": 120,
      "createTime": 1791209149,
      "desc": "Real conversations happen on TikTok, and protecting the integrity of elections is a top p…",
      "id": "7693184538704416031",
      "itemCommentStatus": 0,
      "textLanguage": "en",
      "textTranslatable": true,
      "author": {
        "id": "107955",
        "nickname": "<user>",
        "privateAccount": false,
        "verified": true
      },
      "authorStats": {
        "diggCount": 4361,
        "followerCount": 96100000,
        "followingCount": 1,
        "friendCount": 0,
        "heartCount": 465100000,
        "videoCount": 1510
      },
      "authorStatsV2": {
        "diggCount": "4361",
        "followerCount": "96100000",
        "followingCount": "1",
        "friendCount": "0",
        "heartCount": "465100000",
        "videoCount": "1510"
      },
      "music": {
        "authorName": "TikTok",
        "duration": 68,
        "id": "7693184700604599071",
        "shoot_duration": 68,
        "title": "original sound"
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
        "collectCount": 377,
        "commentCount": 759,
        "diggCount": 4234,
        "playCount": 91000,
        "shareCount": 375
      },
      "statsV2": {
        "collectCount": "377",
        "commentCount": "759",
        "diggCount": "4234",
        "playCount": "91000",
        "repostCount": "0",
        "shareCount": "375"
      }
    }
  ]
}
```

### Notes

- `secUid` is required to identify the TikTok user account.
- `count` defaults to 20 and cannot be changed.
- `coverFormat` accepts 1 or 2, defaulting to 2.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-post.json`](../../../../catalog/models/tiktok/web/user-post.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-post
