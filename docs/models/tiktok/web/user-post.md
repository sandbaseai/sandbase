# TikTok User Posts API: pricing, parameters and code examples

`tiktok/web/user-post` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of posts from a specific TikTok user using their `secUid`, including video details, author metrics, and interaction statistics.

## Pricing

- **$0.001 per call** (USD)
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

List the videos a TikTok account has posted, newest first, with each video's caption, cover, play URL, music, hashtags and play, like, comment and share counts. Identify the account by its `secUid`.

### Use cases

- Monitor a creator's new uploads and engagement.
- Collect a creator's recent videos for content or brand-deal analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | Yes | User secUid |
| `count` | integer | No | Number per page, default is 20, cannot be changed. |
| `coverFormat` | integer | No | Cover format, default is 2, optional values are 1 or 2. |
| `cursor` | integer | No | Page cursor |
| `post_item_list_request_type` | integer | No | Sort type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "itemList": [
    {
      "id": "7702947070604332319",
      "createTime": 1793482137,
      "desc": "already planning next halloween? 👀🎃  take notes from @Mason Smith. find more DIY",
      "stats": {
        "collectCount": 352,
        "commentCount": 1159,
        "diggCount": 4093,
        "playCount": 287200,
        "shareCount": 328
      },
      "author": {
        "uniqueId": "tiktok",
        "nickname": "TikTok"
      }
    }
  ],
  "cursor": "1788468783000",
  "hasMore": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `itemList[]` | Videos on this page (about 15). |
| `itemList[].id` | Video ID (aweme_id). |
| `itemList[].desc` | Caption. |
| `itemList[].createTime` | Upload time, Unix seconds. |
| `itemList[].stats` | `playCount`, `diggCount` (likes), `commentCount`, `shareCount`, `collectCount`. |
| `itemList[].author / authorStats` | Author profile and follower, like and video counts. |
| `cursor / hasMore` | Pass `cursor` back to get the next page while `hasMore` is true. |

### Notes

- `secUid` is the long ID starting with `MS4wLjABAAAA`. Get it from a profile with [TikTok User Profile](/apis/tiktok/web/user-profile).
- Video and cover URLs are signed and expire; download them soon after the call.

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-post.json`](../../../../catalog/models/tiktok/web/user-post.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-post
