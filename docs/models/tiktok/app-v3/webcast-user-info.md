# TikTok Webcast User Information API: pricing, parameters and code examples

`tiktok/app-v3/webcast-user-info` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves profile information for a specified TikTok Webcast user. Queries data using either a numeric user ID or a secure user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/webcast-user-info", "user_id": "7016736142473561094"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/webcast-user-info', {'user_id': '7016736142473561094'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/webcast-user-info", {
  "user_id": "7016736142473561094"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/webcast-user-info", sandbase.Params{
	"user_id": "7016736142473561094",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/webcast-user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User uid, optional parameter, pure number, if used, please keep sec_user_id and unique_id empty. default `""` |
| `sec_user_id` | string |  | User sec_user_id default `""` |

## Details

Returns Webcast profile data for one TikTok user: bio, avatar images, verification details, privacy and live-interaction settings, and aggregate video stats. Send either `sec_user_id` or a numeric `user_id`.

### Use cases

- Show a broadcaster's bio and avatar in a live-stream monitoring dashboard.
- Check whether an account carries a verification badge and read its verification reason.
- Read the account's live-interaction settings, such as linkmic and stranger comments, before planning outreach.
- Pull a creator's total favorite count to compare accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/webcast-user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | No | User sec_user_id |
| `user_id` | string | No | User uid, optional parameter, pure number, if used, please keep sec_user_id and unique_id empty. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "allow_find_by_contacts": false,
    "allow_others_download_video": false,
    "allow_others_download_when_sharing_video": false,
    "allow_share_show_profile": false,
    "allow_show_in_gossip": false,
    "allow_show_my_action": false,
    "allow_strange_comment": false,
    "allow_unfollower_comment": false,
    "allow_use_linkmic": false,
    "authentication_info": {
      "authentication_badge": {
        "avg_color": "",
        "height": 0,
        "image_type": 0,
        "is_animated": false,
        "open_web_url": "",
        "uri": "webcast-va/authentication_icon.png",
        "url_list": [
          "https://p16-webcast.tiktokcdn.com/webcast-va/authentication_icon.png~tplv-obj.im…"
        ],
        "width": 0
      },
      "custom_verify": "",
      "enterprise_verify_reason": "verified account",
      "has_cert": true
    },
    "author_stats": {
      "variety_show_play_count": 0,
      "video_total_count": 0,
      "video_total_favorite_count": 466687469,
      "video_total_play_count": 0,
      "video_total_series_count": 0,
      "video_total_share_count": 0
    },
    "avatar_large": {
      "avg_color": "",
      "height": 0,
      "image_type": 0,
      "is_animated": false,
      "open_web_url": "",
      "uri": "1080x1080/tos-useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a",
      "url_list": [
        "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691…"
      ],
      "width": 0
    }
  },
  "extra": {
    "anonymous_is_silence": false,
    "mirror_profile_card_decoration": false,
    "now": 1793691843072,
    "preload_empty_reason": ""
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.bio_description` | Profile bio text of the user. |
| `data.authentication_info.has_cert` | Whether the account holds a verification certificate. In this response it is `true`. |
| `data.authentication_info.enterprise_verify_reason` | Text explaining the verification, such as `verified account`. |
| `data.authentication_info.authentication_badge.url_list[]` | Image URLs for the verification badge icon. |
| `data.author_stats.video_total_favorite_count` | Total favorites (likes) counted across the user's videos. |
| `data.author_stats.video_total_count / video_total_play_count / video_total_share_count` | Aggregate video count, play count and share count. They return `0` in this response, so do not rely on them for this account. |
| `data.avatar_large.url_list[] / avatar_medium.url_list[] / avatar_thumb.url_list[]` | Avatar image URLs in 1080x1080, 720x720 and 100x100 sizes. Each list holds several CDN links in webp and jpeg formats. |
| `data.allow_use_linkmic / allow_strange_comment / allow_unfollower_comment` | Privacy flags for live co-hosting (linkmic), comments from strangers, and comments from non-followers. |
| `data.allow_others_download_video / allow_share_show_profile` | Flags for whether others may download the user's videos and whether sharing shows the profile. |
| `extra.now` | Server timestamp of the response, as a number in the form `1793691843072`. |

### Notes

- Use either `sec_user_id` or `user_id`. If you send `user_id`, leave `sec_user_id` and `unique_id` empty.
- `user_id` is a purely numeric string. `sec_user_id` is a longer string that starts with `MS4wLjABAAAA`.
- If you only have a username, call [TikTok User ID by Username](/apis/tiktok/app-v3/user-id-and-sec-user-id-by-username) to get the IDs first.
- Fields named `deprecated*` and several empty lists such as `badge_list` carry no data in this response.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/webcast-user-info.json`](../../../../catalog/models/tiktok/app-v3/webcast-user-info.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/webcast-user-info
