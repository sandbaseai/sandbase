# TikTok User Repost Videos API: pricing, parameters and code examples

`tiktok/app-v3/user-repost-videos` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of videos reposted by a specific TikTok user based on their user ID. Supports result pagination through count and offset parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-repost-videos", "user_id": 107955}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-repost-videos', {'user_id': 107955})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-repost-videos", {
  "user_id": 107955
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-repost-videos", sandbase.Params{
	"user_id": 107955,
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-repost-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `21` |
| `offset` | integer |  | Offset default `0` |
| `user_id` | integer | yes | User id, which can be obtained through the handler_user_profile endpoint, with the keyword uid in the response.  |

## Details

Returns the list of videos a TikTok user has reposted, as `aweme_list`. The input is the numeric `user_id` of the reposting account. Use `count` and `offset` to page through results.

### Use cases

- List the videos a creator has reposted to see which content they amplify.
- Collect the original authors of reposted videos to find accounts a creator tends to endorse.
- Extract hashtags from reposted videos to see which topics a creator shares.
- Save the description and sound details of reposted videos for content research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-repost-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": 107955}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | integer | Yes | User id, which can be obtained through the handler_user_profile endpoint, with the keyword uid in the response. |
| `count` | integer | No | Number |
| `offset` | integer | No | Offset |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [
    {
      "added_sound_music_info": {
        "album": "",
        "allow_offline_music_to_detail_page": false,
        "artists": [],
        "audition_duration": 75,
        "author": "Christopher Sbrocco",
        "author_deleted": false,
        "author_position": null,
        "avatar_medium": {
          "height": 720,
          "uri": "tos-maliva-avt-0068/7330740761455820805",
          "url_list": [
            "https://p16-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/7330740761455820805…"
          ],
          "url_prefix": null,
          "width": 720
        }
      },
      "ai_remix_info": {
        "has_entrance": false
      },
      "aigc_info": {
        "aigc_label_type": 0,
        "created_by_ai": false
      },
      "anchors": null,
      "anchors_extras": "",
      "animated_image_info": {
        "effect": 0,
        "type": 0
      },
      "author": {
        "accept_private_policy": false,
        "account_labels": null,
        "account_region": "",
        "ad_cover_url": null,
        "advance_feature_item_order": null,
        "advanced_feature_info": null,
        "apple_account": 0,
        "authority_status": 0
      },
      "author_user_id": 6653919748492099589,
      "aweme_acl": {
        "download_general": {
          "code": 0,
          "mute": false,
          "show_type": 2,
          "transcode": 3
        },
        "download_mask_panel": {
          "code": 0,
          "mute": false,
          "show_type": 2,
          "transcode": 3
        },
        "platform_list": null,
        "press_action_list": null,
        "share_action_list": null,
        "share_general": {
          "code": 0,
          "mute": false,
          "show_type": 2,
          "transcode": 3
        },
        "share_list_status": 0
      },
      "aweme_id": "7696682138988514590",
      "aweme_type": 0,
      "banners": null
    }
  ],
  "biz_extra": {
    "7636195229141355789": 107955,
    "7636204885452672269": 107955,
    "7636211301831724301": 107955,
    "7636223701947665678": 107955,
    "7637007189244218638": 107955,
    "7641632110284901646": 107955,
    "7642600295100353805": 107955,
    "7646813308644936982": 107955,
    "7647625121582025998": 107955,
    "7655016712990952726": 107955,
    "7655392211147820319": 107955,
    "7656783830187117838": 107955
  },
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103074402E833C1BE34075E01C365",
    "now": 1793691842000
  },
  "has_more": true,
  "log_pb": {
    "impr_id": "20261103074402E833C1BE34075E01C365"
  },
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[].aweme_id` | ID of the reposted video, as a string. |
| `aweme_list[].author_user_id` | Numeric user ID of the account that originally posted the video. |
| `aweme_list[].desc / aweme_list[].content_desc` | Caption text of the video. `content_desc` holds the caption lines as a JSON-encoded list in a string. |
| `aweme_list[].create_time` | Unix timestamp in seconds for the video's creation time. |
| `aweme_list[].content_type` | Type of the item, for example `video`. |
| `aweme_list[].cha_list[].cha_name` | Name of a hashtag attached to the video. `cid` holds the hashtag ID. |
| `aweme_list[].content_desc_extra[]` | Marks the mentions and hashtags in the caption. `start` and `end` give the position of each one. Mentions carry `user_id` and `sec_uid`, and hashtags carry `hashtag_id` and `hashtag_name`. |
| `aweme_list[].added_sound_music_info.author` | Name of the author of the sound used in the video. |
| `aweme_list[].aigc_info.created_by_ai` | Whether the video is flagged as created by AI. |

### Notes

- Get `user_id` from the `uid` field of the user profile response. [TikTok User Profile Details](/apis/tiktok/app-v3/user-profile) returns the profile, and [TikTok User ID by Username](/apis/tiktok/app-v3/user-id-and-sec-user-id-by-username) looks up IDs from a username.
- Page through results with `count` (default `21`) and `offset` (default `0`).
- To see the videos the user posted themselves, call [TikTok User Videos (App V3)](/apis/tiktok/app-v3/user-post-videos).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-repost-videos.json`](../../../../catalog/models/tiktok/app-v3/user-repost-videos.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-repost-videos
