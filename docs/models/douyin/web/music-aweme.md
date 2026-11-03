# Douyin Web Music Videos API: pricing, parameters and code examples

`douyin/web/music-aweme` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves music videos from Douyin Web based on pagination settings. Returns a list of video items using the specified count and refresh index parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/music-aweme", "count": 1, "refresh_index": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/music-aweme', {'count': 1, 'refresh_index': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/music-aweme", {
  "count": 1,
  "refresh_index": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/music-aweme", sandbase.Params{
	"count": 1,
	"refresh_index": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/web/music-aweme` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer | yes | Number per page, default is 16  |
| `refresh_index` | integer |  | Paging index, default is 1  |

## Details

Returns a page of music-related videos from Douyin Web as a list of video items in `aweme_list`. It needs only `count`, the number of items per page. You can add `refresh_index` to move through pages.

### Use cases

- Build a feed of long-form music videos on Douyin, such as artist profiles and concert retrospectives.
- Track which hashtags and captions appear on music videos by reading `caption` and `desc`.
- Collect `aweme_id` values and author IDs to feed into video detail or user lookups.
- Compare video lengths across a music feed using `duration`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/music-aweme" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"count": 16, "refresh_index": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | Yes | Number per page, default is 16 |
| `refresh_index` | integer | No | Paging index, default is 1 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [
    {
      "ad_candidates": null,
      "ai_follow_images": null,
      "anchors": null,
      "authentication_token": "MS4wLjAA…",
      "author": {
        "avatar_thumb": {
          "height": 720,
          "uri": "100x100/aweme-avatar/tos-cn-i-0813_41ceaf508ceb46e0a555bec09f119930",
          "url_list": [
            "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813_41ceaf508ce…"
          ],
          "width": 720
        },
        "cha_list": null,
        "common_interest": null,
        "cover_url": [
          {
            "height": 720,
            "uri": "c8510002be9a3a61aad2",
            "url_list": [
              "https://p3-pc-sign.douyinpic.com/obj/c8510002be9a3a61aad2?lk3s=138a59ce&x-expire…"
            ],
            "width": 720
          }
        ],
        "custom_verify": "",
        "enterprise_verify_reason": "",
        "follow_status": 0,
        "follower_status": 0
      },
      "author_user_id": 102008689680,
      "aweme_control": {
        "can_comment": true,
        "can_forward": true,
        "can_share": true,
        "can_show_comment": true
      },
      "aweme_id": "7673013362283891977",
      "aweme_listen_struct": {
        "trace_info": "{\"copyright_not_speech\":\"false\",\"copyright_reason\":\"has_listen_cp_new\",\"copyrigh…"
      },
      "aweme_type": 0,
      "can_cache_to_local": true,
      "caption": "#地下八英里 结束了，是时候从头到尾好好说一下这场比赛的历史了#说唱 #说场比赛 #抖音创作者大会 #贝贝李京泽"
    }
  ],
  "chime_video_list": null,
  "filter_infos": null,
  "log_pb": {
    "impr_id": "202611031532328B5907C61486A95FC51D"
  },
  "status_code": 0,
  "video_cover_image_list": null,
  "video_cover_url_list": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[]` | The list of video items on this page. |
| `aweme_list[].aweme_id` | The ID of the video, as a string. Use it to look up the video in other APIs. |
| `aweme_list[].desc / aweme_list[].caption` | The video text, including hashtags. `desc` can be longer than `caption`. |
| `aweme_list[].create_time` | When the video was created, as a Unix timestamp in seconds. |
| `aweme_list[].duration` | The video length. The values look like milliseconds, for example `535175` for a video of about nine minutes. |
| `aweme_list[].author_user_id` | The numeric user ID of the video author. |
| `aweme_list[].author.avatar_thumb.url_list[]` | URLs of the author's avatar thumbnail image. |
| `aweme_list[].chapter_list[]` | Chapters for videos that have them. Each has a `desc` title, a `detail` summary, a `timestamp` and a `url` for an image. `timestamp` values look like milliseconds. |
| `aweme_list[].chapter_abstract` | A text summary of the video content, present only on some videos. |
| `aweme_list[].aweme_control.can_comment / aweme_list[].aweme_control.can_share` | Flags that show whether commenting and sharing are allowed on the video. |

### Notes

- `count` is required. `refresh_index` is the paging index and starts at `1`.
- Many fields are `null` on some items, and `chapter_list` is `null` for videos without chapters. Check for `null` before reading nested values.
- To get full details for a video, pass its `aweme_id` to [Douyin Single Video Details (V1)](/apis/douyin/web/one-video).
- To read comments on a video, use [Douyin Video Comments (Web)](/apis/douyin/web/video-comments).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/music-aweme.json`](../../../../catalog/models/douyin/web/music-aweme.json) · Store page: https://www.sandbase.ai/model/douyin/web/music-aweme
