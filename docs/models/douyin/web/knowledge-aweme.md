# Douyin Web Knowledge Videos API: pricing, parameters and code examples

`douyin/web/knowledge-aweme` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves a feed of knowledge-focused videos from Douyin Web. Supports pagination controls using item count and refresh index parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/knowledge-aweme", "count": 16}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/knowledge-aweme', {'count': 16})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/knowledge-aweme", {
  "count": 16
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/knowledge-aweme", sandbase.Params{
	"count": 16,
})
```

Same call via the path form: `POST /v1/api/douyin/web/knowledge-aweme` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer | yes | Number per page, default is 16  |
| `refresh_index` | integer |  | Paging index, default is 1  |

## Details

Returns a feed of knowledge-focused videos from Douyin Web. The request needs `count` (items per page) and can take `refresh_index` (paging index). Each item in `aweme_list` holds the video ID, caption, author, and publish time.

### Use cases

- Build a list of recent knowledge and education videos on Douyin for content research.
- Pull chapter summaries from videos to index long explainer clips by topic.
- Collect `aweme_id` values from the feed, then fetch full details for the videos you want to track.
- Check which authors appear in the knowledge feed by reading `author_user_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/knowledge-aweme" \
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
          "uri": "100x100/aweme-avatar/tos-cn-avt-0015_dd4b05b4fccb80527688626b4733df15",
          "url_list": [
            "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_dd4b05b4f…"
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
      "author_user_id": 1561572678432,
      "aweme_control": {
        "can_comment": true,
        "can_forward": true,
        "can_share": true,
        "can_show_comment": true
      },
      "aweme_id": "7679043412167776442",
      "aweme_listen_struct": {
        "trace_info": "{\"copyright_not_speech\":\"false\",\"copyright_reason\":\"not_intercept\",\"copyright_ta…"
      },
      "aweme_type": 0,
      "can_cache_to_local": true,
      "caption": "猜猜我们这幅花卉浮雕值多少钱？\n#狼尾兄弟浮雕壁画 #抖音青年艺术家计划 #青年创作者扶持计划 #抖音青年艺术家 #vlog十亿流量扶持计划"
    }
  ],
  "chime_video_list": null,
  "filter_infos": null,
  "log_pb": {
    "impr_id": "20261103153229F7FA9BD2BA0539DE78F4"
  },
  "status_code": 0,
  "video_cover_image_list": null,
  "video_cover_url_list": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[]` | List of videos in this page of the feed. |
| `aweme_list[].aweme_id / aweme_list[].group_id` | ID of the video. Both fields show the same value in the sample. |
| `aweme_list[].desc` | Full video description, including hashtags. |
| `aweme_list[].caption` | Shorter caption text of the video. It may be cut off compared with `desc`. |
| `aweme_list[].create_time` | Publish time of the video as a Unix timestamp in seconds. |
| `aweme_list[].duration` | Length of the video. The values (for example `469934`) look like milliseconds. |
| `aweme_list[].author_user_id` | Numeric ID of the account that posted the video. |
| `aweme_list[].author.avatar_thumb.url_list[]` | URLs of the author's small avatar image. |
| `aweme_list[].chapter_abstract` | Short text summary of the video. Only some videos have it. |
| `aweme_list[].chapter_list[].desc / aweme_list[].chapter_list[].detail / aweme_list[].chapter_list[].timestamp` | Chapter title, chapter description, and chapter start position. The `timestamp` values (for example `18000`) look like milliseconds. Only some videos have chapters. |

### Notes

- `count` is required. `refresh_index` is the paging index and starts at `1`.
- Many fields in each item are `null` when the video does not use them, so check for `null` before reading `chapter_list` or `chapter_abstract`.
- To get more detail on a video, pass its `aweme_id` to [Douyin Single Video Details (V1)](/apis/douyin/web/one-video) or [Douyin Batch Video Information (Web)](/apis/douyin/web/multi-video).
- For other topic feeds, see [Douyin Food Videos](/apis/douyin/web/food-aweme) and [Douyin Game Videos](/apis/douyin/web/game-aweme).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/knowledge-aweme.json`](../../../../catalog/models/douyin/web/knowledge-aweme.json) · Store page: https://www.sandbase.ai/model/douyin/web/knowledge-aweme
