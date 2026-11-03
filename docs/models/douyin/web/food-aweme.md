# Douyin Food Videos API: pricing, parameters and code examples

`douyin/web/food-aweme` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a feed of food-related videos from Douyin Web. Results can be paginated using count and refresh index parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/food-aweme", "count": 1, "refresh_index": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/food-aweme', {'count': 1, 'refresh_index': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/food-aweme", {
  "count": 1,
  "refresh_index": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/food-aweme", sandbase.Params{
	"count": 1,
	"refresh_index": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/web/food-aweme` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer | yes | Number per page, default is 16  |
| `refresh_index` | integer |  | Paging index, default is 1  |

## Details

Returns a feed of food-related videos from Douyin Web. Each item in `aweme_list` has the video ID, caption, author ID, creation time and duration. The only input is `count`, with an optional `refresh_index` for paging.

### Use cases

- Pull a batch of current food videos to see which dishes and hashtags appear in the feed.
- Collect captions and hashtags from food posts for text analysis of recipe and restaurant topics.
- Build a list of food creator IDs from `author_user_id` to review further.
- Read the chapter summaries of cooking videos to see the steps without watching the video.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/food-aweme" \
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
          "uri": "100x100/aweme-avatar/tos-cn-avt-0015_8b0ae19bedfdef9006f590a3fd2f35a9",
          "url_list": [
            "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_8b0ae19be…"
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
      "author_user_id": 91657343363,
      "aweme_control": {
        "can_comment": true,
        "can_forward": true,
        "can_share": true,
        "can_show_comment": true
      },
      "aweme_id": "7695804504796564774",
      "aweme_listen_struct": {
        "trace_info": "{\"copyright_not_speech\":\"false\",\"copyright_reason\":\"not_intercept\",\"copyright_ta…"
      },
      "aweme_type": 0,
      "can_cache_to_local": true,
      "caption": "孜然羊肉，豆酱焗黄脚立，咸蛋黄焗丝瓜，炖羊肉汤。#vlog美食记#家常菜#晚饭吃什么#吴师傅vlog"
    }
  ],
  "chime_video_list": null,
  "filter_infos": null,
  "log_pb": {
    "impr_id": "20261103153230C564E68FDE9A6AEFE5EA"
  },
  "status_code": 0,
  "video_cover_image_list": null,
  "video_cover_url_list": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[]` | List of food videos in the feed. Each entry is one video. |
| `aweme_list[].aweme_id` | ID of the video, as a string of digits. |
| `aweme_list[].desc / aweme_list[].caption` | Video text. `desc` is the full description and `caption` is a short version. Both can include hashtags such as `#家常菜`. |
| `aweme_list[].create_time` | Creation time of the video. The values look like Unix timestamps in seconds. |
| `aweme_list[].duration` | Length of the video. Values such as `469600` suggest milliseconds, so that video would run about 7.8 minutes. |
| `aweme_list[].author_user_id` | Numeric ID of the account that posted the video. |
| `aweme_list[].author.avatar_thumb.url_list[]` | URLs of the author's small avatar image. |
| `aweme_list[].chapter_abstract` | Short text summary of the video content. Only some videos have it. |
| `aweme_list[].chapter_list[]` | Chapters of the video. Each has `desc` (title), `detail` (text), `timestamp` (position in the video) and `url` (image link). |
| `log_pb.impr_id` | ID of this feed request, as logged by Douyin. |

### Notes

- `count` is required. It sets how many videos come back per page. `refresh_index` is the paging index and starts at `1`.
- Many fields are `null` on some videos, for example `chapter_list` and `chapter_abstract`. Check for `null` before you read them.
- To get full details for a video, pass its `aweme_id` to [Douyin Single Video Details (V1)](/apis/douyin/web/one-video).
- To read the comments on a video, use [Douyin Video Comments (Web)](/apis/douyin/web/video-comments).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/food-aweme.json`](../../../../catalog/models/douyin/web/food-aweme.json) · Store page: https://www.sandbase.ai/model/douyin/web/food-aweme
