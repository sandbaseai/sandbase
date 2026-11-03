# Xigua User Profile Details API: pricing, parameters and code examples

`xigua/app-v2/user-info` · data API · Xigua · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns profile and personal information for a specified Xigua account. Queries details using the target user identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xigua/app-v2/user-info", "user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xigua/app-v2/user-info', {'user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xigua/app-v2/user-info", {
  "user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xigua/app-v2/user-info", sandbase.Params{
	"user_id": "example",
})
```

Same call via the path form: `POST /v1/api/xigua/app-v2/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User id  |

## Details

Returns the public profile of a Xigua account, including name, bio, verification status, follower counts and video totals. It needs one input, the numeric `user_id` of the account.

### Use cases

- Show a creator's name, avatar and bio on a profile card.
- Compare follower counts across several Xigua creators before picking partners.
- Check whether an account is verified and read its verification label.
- Track a creator's `video_total_count` and follower totals over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xigua/app-v2/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "52712347586"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "bottom_tab_list": [],
  "data": [],
  "debug_info": "",
  "has_more": false,
  "has_more_to_refresh": true,
  "live_data": null,
  "live_datas": null,
  "message": "success",
  "room_id_str": "",
  "shop_tab_url": "",
  "status": 0,
  "tab": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user_info.name` | Display name of the account. |
| `user_info.description / user_info.author_desc` | Profile bio text and the author description shown on the account. |
| `user_info.user_id / user_info.media_id` | Numeric account ID and numeric media ID of the account. |
| `user_info.followers_count / user_info.followers_count_str` | Follower total as a number and as a short display string such as `2488万`. |
| `user_info.followers_count_detail.toutiao_followers_count / user_info.followers_count_detail.xigua_followers_count` | Follower counts split into the Toutiao and Xigua parts. |
| `user_info.following_count` | Number of accounts this user follows. |
| `user_info.user_verified / user_info.verified_content` | Whether the account is verified, and the verification label text. |
| `user_info.video_total_count / user_info.author_info.video_total_share_count` | Total number of videos posted and total share count across them. |
| `user_info.user_digg_count.article_digg_count / user_info.user_digg_count.comment_digg_count` | Like counts the user received on articles and on comments. |
| `user_info.avatar_url / user_info.large_avatar_url` | Image URLs for the avatar, in a small and a large size. |
| `user_info.share_url` | Link to the user's public page on Xigua. |
| `user_info.ip_info.address` | Location label shown on the profile. |

### Notes

- `user_id` is a numeric string, for example `52712347586`. It also appears in `user_info.share_url`.
- The top-level `data`, `tab_list` and `total_number` fields carry no profile data in this response. Read profile details from `user_info`.
- To list the videos this account posted, call [Xigua User Post List](/apis/xigua/app-v2/user-post-list).
- To fetch one video from a user's list, call [Xigua Single Video Information](/apis/xigua/app-v2/one-video).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xigua Single Video Information](/apis/xigua/app-v2/one-video): Returns lightweight single video data and associated related video information from Xigua for a specific post by its unique item ID.
- [Xigua Video Play URL](/apis/xigua/app-v2/one-video-play-url): Returns the direct playback URL for a specific Xigua video using its unique item identifier.
- [Xigua Video Search](/apis/xigua/app-v2/search-video): Search Xigua Video (ByteDance long-form video) by keyword: titles, creators, duration, publish time and comment counts, with sort and duration filters.

---
Machine-readable: [`catalog/models/xigua/app-v2/user-info.json`](../../../../catalog/models/xigua/app-v2/user-info.json) · Store page: https://www.sandbase.ai/model/xigua/app-v2/user-info
