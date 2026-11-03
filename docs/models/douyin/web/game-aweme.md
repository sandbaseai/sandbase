# Douyin Game Videos API: pricing, parameters and code examples

`douyin/web/game-aweme` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a paginated list of game-related videos from Douyin web. Callers specify the number of items per page and a refresh index to navigate through video feeds.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/game-aweme", "count": 1, "refresh_index": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/game-aweme', {'count': 1, 'refresh_index': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/game-aweme", {
  "count": 1,
  "refresh_index": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/game-aweme", sandbase.Params{
	"count": 1,
	"refresh_index": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/web/game-aweme` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer | yes | Number per page, default is 16  |
| `refresh_index` | integer |  | Paging index, default is 1  |

## Details

Returns a page of game-related videos from the Douyin web feed. Send `count` for the page size and an optional `refresh_index` to move through the feed. No video ID or user ID is needed.

### Use cases

- Build a feed of current Douyin game videos for a gaming content dashboard.
- Collect captions and hashtags to see which games and topics creators post about.
- Find game video creators by reading the `author_user_id` of each item.
- Read AI chapter summaries to skim long game videos without watching them.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/game-aweme" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"count": 16}'
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
          "uri": "100x100/aweme-avatar/tos-cn-avt-0015_44fcbdc791e4a9ada24548dd15bed9b1",
          "url_list": [
            "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_44fcbdc79…"
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
      "author_user_id": 96892863306,
      "aweme_control": {
        "can_comment": true,
        "can_forward": true,
        "can_share": true,
        "can_show_comment": true
      },
      "aweme_id": "7680789415634963722",
      "aweme_listen_struct": {
        "trace_info": "{\"copyright_not_speech\":\"false\",\"copyright_reason\":\"not_intercept\",\"copyright_ta…"
      },
      "aweme_type": 0,
      "can_cache_to_local": true,
      "caption": "《这把打完，蒙多的瘾更重了》#游戏日常#抖音游戏趣讲作者团"
    }
  ],
  "chime_video_list": null,
  "filter_infos": null,
  "log_pb": {
    "impr_id": "202611031532292CEF27670B1BB1F97A55"
  },
  "status_code": 0,
  "video_cover_image_list": null,
  "video_cover_url_list": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[]` | The list of game videos on this page. Each item is one video. |
| `aweme_list[].aweme_id` | The ID of the video, as a string. |
| `aweme_list[].desc / aweme_list[].caption` | The video text, including hashtags and @mentions. `caption` is often the shorter version of `desc`. |
| `aweme_list[].create_time` | When the video was posted, as a Unix timestamp in seconds. |
| `aweme_list[].duration` | The video length. Values like `690901` suggest milliseconds, but the response does not state the unit. |
| `aweme_list[].author_user_id` | The numeric ID of the creator who posted the video. |
| `aweme_list[].author.avatar_thumb.url_list[]` | URLs for the creator's small avatar image. |
| `aweme_list[].chapter_abstract` | A text summary of the video. It appears only on some videos. |
| `aweme_list[].chapter_list[]` | Chapter markers for a video. Each has a title in `desc`, a longer `detail` text, a `timestamp` and a preview image `url`. |
| `aweme_list[].aweme_control` | Flags that show whether commenting, forwarding and sharing are allowed for the video. |
| `log_pb.impr_id` | An ID for this feed request. |

### Notes

- `count` is the only required parameter. The page size defaults to 16.
- Use `refresh_index` to request further pages. It defaults to 1.
- Fields such as `chapter_abstract` and `chapter_list` can be missing or `null` for some videos.
- To get full details for one video, pass its `aweme_id` to [Douyin Single Video Details (V1)](/apis/douyin/web/one-video).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/game-aweme.json`](../../../../catalog/models/douyin/web/game-aweme.json) · Store page: https://www.sandbase.ai/model/douyin/web/game-aweme
