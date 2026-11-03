# TikTok User Profile API: pricing, parameters and code examples

`tiktok/web/user-profile` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns public profile information for a specified TikTok user. Look up accounts by providing either the unique handle or secure user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/user-profile", "uniqueId": "srlechuza2.0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/user-profile', {'uniqueId': 'srlechuza2.0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/user-profile", {
  "uniqueId": "srlechuza2.0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/user-profile", sandbase.Params{
	"uniqueId": "srlechuza2.0",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `secUid` | string |  | User secUid default `""` |
| `uniqueId` | string |  | User uniqueId default `""` |

## Details

Returns the public profile of a TikTok account, including its bio, verification status, avatar URLs and follower, like and video counts. Send either `uniqueId` (the handle) or `secUid` (the secure user ID).

### Use cases

- Check follower, like and video counts for a creator before outreach.
- Confirm that a handle exists and is verified.
- Convert a handle to its `secUid` so you can call other user endpoints.
- Save a creator's nickname, bio and avatar for a dashboard or CRM.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uniqueId": "tiktok"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | No | User secUid |
| `uniqueId` | string | No | User uniqueId |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "needFix": false,
  "shareMeta": {
    "desc": "@tiktok 96.5m Followers, 1 Following, 466.7m Likes - Watch awesome short videos …",
    "title": "TikTok on TikTok"
  },
  "statusCode": 0,
  "statusMsg": "",
  "userInfo": {
    "itemList": [],
    "stats": {
      "diggCount": 0,
      "followerCount": 96500000,
      "followingCount": 1,
      "friendCount": 1,
      "heart": 466700000,
      "heartCount": 466700000,
      "videoCount": 1514
    },
    "statsV2": {
      "diggCount": "0",
      "followerCount": "96532208",
      "followingCount": "1",
      "friendCount": "1",
      "heart": "466687514",
      "heartCount": "466687514",
      "videoCount": "1514"
    },
    "user": {
      "UserStoryStatus": 0,
      "avatarLarger": "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691…",
      "avatarMedium": "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691…",
      "avatarThumb": "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691…",
      "bioLink": {
        "link": "tiktok.com/discovermore",
        "risk": 0
      },
      "canExpPlaylist": true,
      "commentSetting": 0,
      "commerceUserInfo": {
        "category": "Others",
        "categoryButton": false,
        "commerceUser": true,
        "downLoadLink": {
          "android": "",
          "ios": ""
        }
      },
      "createTime": 1425144149,
      "downloadSetting": 0,
      "duetSetting": 0,
      "eventList": []
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `userInfo.user.uniqueId / userInfo.user.nickname` | The account handle and the display name. |
| `userInfo.user.secUid` | Secure user ID of the account. Use it as input to other user endpoints. |
| `userInfo.user.id` | Numeric user ID of the account, returned as a string. |
| `userInfo.user.signature` | The bio text on the profile. |
| `userInfo.user.verified` | `true` when the account is verified. |
| `userInfo.user.privateAccount` | `true` when the account is private. |
| `userInfo.user.createTime` | Account creation time as a Unix timestamp in seconds. |
| `userInfo.user.avatarLarger / userInfo.user.avatarMedium / userInfo.user.avatarThumb` | Avatar image URLs in large, medium and thumbnail sizes. |
| `userInfo.stats.followerCount / userInfo.stats.followingCount / userInfo.stats.videoCount` | Number of followers, number of accounts followed, and number of videos. The follower count is rounded in this block. |
| `userInfo.statsV2.followerCount / userInfo.statsV2.heartCount / userInfo.statsV2.videoCount` | Exact counts for followers, total likes received and videos. Values are strings, so convert them to numbers before you do math. |

### Notes

- Send either `uniqueId` or `secUid`. The request example uses `uniqueId` only.
- Use `userInfo.statsV2` when you need exact counts. `userInfo.stats` shows rounded values such as `96500000` for followers.
- To get a user's videos, call [TikTok User Posts](/apis/tiktok/web/user-post) with the `secUid` from this response.
- If you only have a profile link, use [TikTok Profile Sec User ID](/apis/tiktok/web/sec-user-id) to get the `secUid` first.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-profile.json`](../../../../catalog/models/tiktok/web/user-profile.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-profile
