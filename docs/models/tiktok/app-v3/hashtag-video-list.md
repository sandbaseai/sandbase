# TikTok Hashtag Video List API: pricing, parameters and code examples

`tiktok/app-v3/hashtag-video-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of videos associated with a specific hashtag on TikTok. Filter results by region and paginate through records using cursor controls.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/hashtag-video-list", "ch_id": "7551"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/hashtag-video-list', {'ch_id': '7551'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/hashtag-video-list", {
  "ch_id": "7551"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/hashtag-video-list", sandbase.Params{
	"ch_id": "7551",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/hashtag-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ch_id` | string | yes | Hashtag id  |
| `count` | integer |  | Number default `10` |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. default `0` |
| `region` | string |  | Region, supports US, GB, FR, JP, VN, SG, default US default `"US"` |

## Details

Returns a list of TikTok videos tagged with a given hashtag. You pass the hashtag id as `ch_id`. Each item in `aweme_list` holds the video id, caption, author id, hashtags and sound info.

### Use cases

- Pull recent videos under a hashtag such as `cat` to review what content it attracts.
- Collect video ids and captions for a hashtag to feed a topic analysis.
- Find co-occurring hashtags by reading the tags listed on each video.
- Compare which videos show up for one hashtag in different regions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/hashtag-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ch_id": "7551"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ch_id` | string | Yes | Hashtag id |
| `count` | integer | No | Number |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |
| `region` | string | No | Region, supports US, GB, FR, JP, VN, SG, default US |

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
        "audition_duration": 64,
        "author": "cats.funny.wanted",
        "author_deleted": false,
        "author_position": null,
        "avatar_medium": {
          "data_size": 0,
          "height": 720,
          "uri": "tos-no1a-avt-0068c001-no/b3794e807afc1dde47f0ef1c979967e3",
          "url_list": [
            "https://p16-common-sign.tiktokcdn-eu.com/tos-no1a-avt-0068c001-no/b3794e807afc1d…"
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
      "allow_gift": true,
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
      "author_user_id": 7551884044088067094,
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
        "share_action_list": [
          {
            "action_id": "create_sticker",
            "code": 1,
            "extra": "216",
            "show_type": 1,
            "toast_msg": "Create sticker isn’t available for this video"
          }
        ],
        "share_general": {
          "code": 0,
          "mute": false,
          "show_type": 2,
          "transcode": 3
        },
        "share_list_status": 0
      },
      "aweme_id": "7700274205635480854",
      "aweme_type": 0
    }
  ],
  "cursor": 10,
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103074353FA76BD247EA57F3F78DC",
    "now": 1793691834000
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "20261103074353FA76BD247EA57F3F78DC"
  },
  "status_code": 0,
  "status_msg": "",
  "version": "v2"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[].aweme_id` | Id of the video, returned as a string. |
| `aweme_list[].desc` | Caption text of the video, including its hashtags. |
| `aweme_list[].desc_language` | Language code of the caption, for example `en`. |
| `aweme_list[].create_time` | Time the video was posted. The values look like Unix timestamps in seconds. |
| `aweme_list[].author_user_id` | Numeric id of the user who posted the video. |
| `aweme_list[].cha_list[].cha_name / aweme_list[].cha_list[].cid` | Name and id of a hashtag attached to the video. `cid` matches the `ch_id` input for that hashtag. |
| `aweme_list[].content_desc_extra[].hashtag_name / aweme_list[].content_desc_extra[].hashtag_id` | Hashtag name and id found in the caption. `start` and `end` give its position in the text. |
| `aweme_list[].added_sound_music_info.author` | Name of the author of the sound used in the video. |
| `aweme_list[].aigc_info.created_by_ai` | Flag that shows whether the video is marked as AI generated. |

### Notes

- Use `cursor` 0 for the first page. For the next page, pass the cursor value from the previous response.
- `count` sets how many videos to return per page. The default is 10.
- `region` accepts `US`, `GB`, `FR`, `JP`, `VN` and `SG`. The default is `US`.
- To find a hashtag id from a name, call [TikTok Hashtag Search Results](/apis/tiktok/app-v3/hashtag-search-result). For hashtag-level details, use [TikTok Hashtag Detail](/apis/tiktok/app-v3/hashtag-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/hashtag-video-list.json`](../../../../catalog/models/tiktok/app-v3/hashtag-video-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/hashtag-video-list
