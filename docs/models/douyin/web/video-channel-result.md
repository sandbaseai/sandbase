# Douyin Video Channel Feed API: pricing, parameters and code examples

`douyin/web/video-channel-result` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns video listings from a specific Douyin channel page. Requires a channel tag ID and supports pagination through count and refresh index parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/video-channel-result", "tag_id": 2027}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/video-channel-result', {'tag_id': 2027})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/video-channel-result", {
  "tag_id": 2027
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/video-channel-result", sandbase.Params{
	"tag_id": 2027,
})
```

Same call via the path form: `POST /v1/api/douyin/web/video-channel-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number  |
| `tag_id` | integer | yes | Tag id, get from the URL  |
| `refresh_index` | integer |  | Refresh index  |

## Details

Returns a list of videos shown on a Douyin channel page. You pass the numeric channel `tag_id`, and each item in `aweme_list` carries the video ID, caption, author and timing data.

### Use cases

- Pull the latest videos from a single Douyin channel to see what creators post there.
- Collect video IDs and captions from a channel, then fetch full details for the ones you want.
- Track which hashtags and topics appear in a channel's feed over repeated calls.
- Find authors who post in a channel by reading `author_user_id` across the results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/video-channel-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tag_id": 2027}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag_id` | integer | Yes | Tag id, get from the URL |
| `count` | integer | No | Number |
| `refresh_index` | integer | No | Refresh index |

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
          "uri": "100x100/aweme-avatar/tos-cn-i-c9aec8xkvj_3ca9fb3749af4d07a262465e7c671a67",
          "url_list": [
            "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-c9aec8xkvj_3ca9f…"
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
      "author_user_id": 3732215835919732,
      "aweme_control": {
        "can_comment": true,
        "can_forward": true,
        "can_share": true,
        "can_show_comment": true
      },
      "aweme_id": "7702765014096088339",
      "aweme_listen_struct": {
        "trace_info": "{\"copyright_not_speech\":\"false\",\"copyright_reason\":\"not_intercept\",\"copyright_ta…"
      },
      "aweme_type": 0,
      "can_cache_to_local": true,
      "caption": "为什么只有他对我不心动？\n杀手系列正在制作第三集，下周就发，绝对不断更；\n谢谢各位小伙伴们对我的支持；\n故事才刚刚开始，我也一直在细细打磨，希望大家能够喜欢。全…"
    }
  ],
  "chime_video_list": null,
  "filter_infos": null,
  "log_pb": {
    "impr_id": "202611031532356C37C8CDD6062EFC2308"
  },
  "status_code": 0,
  "video_cover_image_list": null,
  "video_cover_url_list": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list` | List of videos returned for the channel. Each entry is one video. |
| `aweme_list[].aweme_id` | String ID of the video. Use it to look up the video in other APIs. |
| `aweme_list[].desc / aweme_list[].caption` | Text of the video post, including hashtags and @mentions. `caption` is the shorter version of the text. |
| `aweme_list[].create_time` | Publish time of the video as a Unix timestamp in seconds. |
| `aweme_list[].duration` | Length of the video. The values look like milliseconds (for example `609409`). |
| `aweme_list[].author_user_id` | Numeric ID of the account that posted the video. |
| `aweme_list[].author.avatar_thumb.url_list[]` | URLs of the author's small avatar image. |
| `aweme_list[].danmaku_control.danmaku_cnt` | Number of danmaku (on-screen comments) on the video. |
| `aweme_list[].chapter_list[]` | Chapters for videos that have them. Each has a `desc` title, a `detail` summary and a `timestamp` offset. |
| `aweme_list[].chapter_abstract` | Short text summary of the video content. It appears only on some videos. |

### Notes

- Take `tag_id` from the channel page URL on Douyin. The example uses `2027`.
- Use `count` to set how many videos to request and `refresh_index` to page through the channel feed.
- Not every video has every field. For example, `chapter_list` is `null` on some items and `chapter_abstract` is missing.
- To get full details for a video, pass its `aweme_id` to [Douyin Single Video Details (V1)](/apis/douyin/web/one-video).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/video-channel-result.json`](../../../../catalog/models/douyin/web/video-channel-result.json) · Store page: https://www.sandbase.ai/model/douyin/web/video-channel-result
