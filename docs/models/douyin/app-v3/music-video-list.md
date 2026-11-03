# Douyin Music Video List API: pricing, parameters and code examples

`douyin/app-v3/music-video-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a paginated list of Douyin videos that feature a specified audio track, identified by its music ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/music-video-list", "music_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/music-video-list', {'music_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/music-video-list", {
  "music_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/music-video-list", sandbase.Params{
	"music_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/music-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number Please keep the default, otherwise there will be BUG.  |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.  |
| `music_id` | string | yes | Music id  |

## Details

Returns a paginated list of Douyin videos that use a given audio track. You send the track's `music_id` and get back video entries with caption, author, hashtags and creation time.

### Use cases

- Collect the videos that use one Douyin sound to see how creators use it.
- Find the accounts that post with a track, using each video's author fields.
- Build a list of captions and hashtags that go with a track.
- Page through all videos for a track and store their `aweme_id` values for later lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/music-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"music_id": "7348905216869174025"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `music_id` | string | Yes | Music id |
| `count` | integer | No | Number Please keep the default, otherwise there will be BUG. |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [
    {
      "activity_video_type": 0,
      "ai_follow_images": null,
      "anchors": null,
      "authentication_token": "MS4wLjAA…",
      "author": {
        "account_cert_info": "{}",
        "ad_cover_url": null,
        "allow_story_normal_like": true,
        "authority_status": 0,
        "avatar_168x168": {
          "height": 720,
          "uri": "168x168/aweme-avatar/tos-cn-avt-0015_08c81910adcc8424b0095ff35df40625",
          "url_list": [
            "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_08c81910adcc8424b0095f…"
          ],
          "width": 720
        },
        "avatar_300x300": {
          "height": 720,
          "uri": "300x300/aweme-avatar/tos-cn-avt-0015_08c81910adcc8424b0095ff35df40625",
          "url_list": [
            "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_08c81910adcc8424b0095f…"
          ],
          "width": 720
        },
        "avatar_larger": {
          "height": 720,
          "uri": "1080x1080/aweme-avatar/tos-cn-avt-0015_08c81910adcc8424b0095ff35df40625",
          "url_list": [
            "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_08c81910ad…"
          ],
          "width": 720
        },
        "avatar_medium": {
          "height": 720,
          "uri": "720x720/aweme-avatar/tos-cn-avt-0015_08c81910adcc8424b0095ff35df40625",
          "url_list": [
            "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_08c81910adcc…"
          ],
          "width": 720
        }
      },
      "author_mask_tag": 0,
      "author_user_id": 4055412235572862,
      "aweme_control": {
        "can_comment": true,
        "can_forward": true,
        "can_share": true,
        "can_show_comment": true
      },
      "aweme_id": "7357708701425224997",
      "aweme_listen_struct": {
        "listen_diversion": {
          "extra": [
            {
              "key": "new_guide_prefix",
              "val": "下载汽水"
            }
          ],
          "popup_scene": 4,
          "side_desc": "听更多精彩内容",
          "sub_title_type": "relation"
        },
        "trace_info": "{\"copyright_not_speech\":\"true\",\"copyright_reason\":\"not_intercept\",\"copyright_tag…"
      },
      "aweme_type": 68,
      "aweme_type_tags": ""
    }
  ],
  "cursor": 10,
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153136BE9467C4608A615EE8A7",
    "now": 1793691097000
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "20261103153136BE9467C4608A615EE8A7"
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list` | List of videos that use the requested audio track. |
| `aweme_list[].aweme_id` | ID of the video, as a string. Use it to look up that video in other APIs. |
| `aweme_list[].caption / aweme_list[].desc` | Text the creator wrote for the video, including any `#` hashtags. |
| `aweme_list[].create_time` | Time the video was created, as a Unix timestamp in seconds. |
| `aweme_list[].author_user_id` | Numeric ID of the account that posted the video. |
| `aweme_list[].author.avatar_larger.url_list` | Image URLs for the author's avatar. Smaller sizes are in `avatar_168x168`, `avatar_300x300`, `avatar_medium` and `avatar_thumb`. |
| `aweme_list[].cha_list[].cha_name` | Name of a hashtag (challenge) attached to the video. |
| `aweme_list[].cha_list[].cid` | ID of that hashtag, as a string. |
| `aweme_list[].city` | City code for the video. Values such as `130400` and `440100` appear in the response. |
| `aweme_list[].commerce_info.is_ad` | Shows whether the video is an ad. |

### Notes

- Pass the `music_id` as a string. The example uses `7348905216869174025`.
- For paging, send `cursor` as `0` for the first page. For the next page, send the cursor value returned in the previous response.
- Keep the default `count`. The parameter description warns that changing it can cause bugs.
- To get details about the track itself, call [Douyin Music Details](/apis/douyin/app-v3/music-detail). For one video from the list, use [Douyin Single Video Details](/apis/douyin/app-v3/one-video) with its `aweme_id`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/music-video-list.json`](../../../../catalog/models/douyin/app-v3/music-video-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/music-video-list
