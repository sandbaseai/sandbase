# TikTok User Mix Video List API: pricing, parameters and code examples

`tiktok/web/user-mix` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns videos compiled inside a specific TikTok user mix or playlist. Supports pagination through cursor and count parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/user-mix", "mixId": "7101538765474106158"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/user-mix', {'mixId': '7101538765474106158'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/user-mix", {
  "mixId": "7101538765474106158"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/user-mix", sandbase.Params{
	"mixId": "7101538765474106158",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/user-mix` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page default `30` |
| `mixId` | string | yes | Mix id  |
| `cursor` | integer |  | Page cursor default `0` |

## Details

Access all videos compiled under a user mix by specifying `mixId`. Manage result pagination using optional `cursor` and `count` parameters.

### Use cases

- Retrieve videos organized within a specific TikTok user playlist.
- Track engagement and play statistics across items in a curated mix.
- Page through sequential multi-part video collections for analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-mix" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mixId": "7101538765474106158"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `mixId` | string | Yes | Mix id |
| `count` | integer | No | Number per page |
| `cursor` | integer | No | Page cursor |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "itemList": [
    {
      "CategoryType": 110,
      "createTime": 1669790506,
      "desc": "Pit in my stomach when I think ab going to the bathroom lol #fyp #pathologicaldemandavoid…",
      "id": "7171695560922058030",
      "itemCommentStatus": 0,
      "textLanguage": "en",
      "textTranslatable": true,
      "author": {
        "id": "6762702053111383045",
        "nickname": "<user>",
        "privateAccount": false,
        "verified": true
      },
      "authorStats": {
        "diggCount": 8322,
        "followerCount": 457200,
        "followingCount": 359,
        "friendCount": 0,
        "heartCount": 7700000,
        "videoCount": 942
      },
      "authorStatsV2": {
        "diggCount": "8322",
        "followerCount": "457200",
        "followingCount": "359",
        "friendCount": "0",
        "heartCount": "7700000",
        "videoCount": "942"
      },
      "music": {
        "id": "7114291002097142570",
        "shoot_duration": 0
      },
      "penaltyContext": {
        "display_penalty_type": 0,
        "display_ui_type": 0,
        "status": 102,
        "tns_status": 102,
        "video_status": 10
      },
      "stats": {
        "collectCount": 33,
        "commentCount": 10,
        "diggCount": 377,
        "playCount": 38200,
        "shareCount": 20
      },
      "statsV2": {
        "collectCount": "33",
        "commentCount": "10",
        "diggCount": "377",
        "playCount": "38200",
        "repostCount": "0",
        "shareCount": "20"
      }
    }
  ]
}
```

### Notes

- The `mixId` parameter is required to identify the mix collection.
- Pagination is handled via `cursor` and `count`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-mix.json`](../../../../catalog/models/tiktok/web/user-mix.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-mix
