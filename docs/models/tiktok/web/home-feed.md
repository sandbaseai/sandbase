# TikTok Web Home Feed API: pricing, parameters and code examples

`tiktok/web/home-feed` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns recommended video items and metadata from the TikTok web home feed. Supports filtering by target region code and page item count.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/home-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/home-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/home-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/home-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/home-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page default `15` |
| `region` | string |  | Region code, optional parameter, affects the region of recommended content, e.g. US/GB/JP/KR/SG, default US. default `"US"` |

## Details

Call this endpoint to retrieve recommended feed posts from TikTok web using optional `region` and `count` parameters.

### Use cases

- Inspect trending and recommended video posts across specific regions.
- Track engagement metrics such as play, digg, and share counts for top feed videos.
- Analyze author statistics and associated background audio details.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/home-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number per page |
| `region` | string | No | Region code, optional parameter, affects the region of recommended content, e.g. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "itemList": [
    {
      "CategoryType": 111,
      "createTime": 1790911701,
      "desc": "Cooking stir fried crab and eat recipe",
      "id": "7691907160216734994",
      "itemCommentStatus": 0,
      "textLanguage": "en",
      "textTranslatable": true,
      "author": {
        "id": "7607710948674159632",
        "nickname": "<user>",
        "privateAccount": false,
        "verified": false
      },
      "authorStats": {
        "diggCount": 0,
        "followerCount": 101900,
        "followingCount": 0,
        "friendCount": 0,
        "heartCount": 2000000,
        "videoCount": 76
      },
      "authorStatsV2": {
        "diggCount": "0",
        "followerCount": "101900",
        "followingCount": "0",
        "friendCount": "0",
        "heartCount": "2000000",
        "videoCount": "76"
      },
      "contentContext": {
        "status_tag": "{\"traffic_structure_info\":\"{\\\"slate_group_type\\\":\\\"0\\\"}\"}"
      },
      "music": {
        "authorName": "Cooking Vibe",
        "duration": 400,
        "id": "7691907345098853141",
        "shoot_duration": 400,
        "title": "original sound - Cooking Vibe"
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
        "collectCount": 73100,
        "commentCount": 14200,
        "diggCount": 1400000,
        "playCount": 28600000,
        "shareCount": 95700
      }
    }
  ]
}
```

### Notes

- The `region` parameter accepts country codes such as US, GB, JP, KR, or SG, defaulting to US.
- The `count` parameter specifies the number of items returned per page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/home-feed.json`](../../../../catalog/models/tiktok/web/home-feed.json) · Store page: https://www.sandbase.ai/model/tiktok/web/home-feed
