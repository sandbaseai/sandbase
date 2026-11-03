# Douyin Single Video Data (Web) API: pricing, parameters and code examples

`douyin/web/one-video-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata for a single Douyin video using its video identifier. The endpoint provides video properties such as bit rate and stream quality tiers.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/one-video-v2", "aweme_id": "7372484719365098803"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/one-video-v2', {'aweme_id': '7372484719365098803'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/one-video-v2", {
  "aweme_id": "7372484719365098803"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/one-video-v2", sandbase.Params{
	"aweme_id": "7372484719365098803",
})
```

Same call via the path form: `POST /v1/api/douyin/web/one-video-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Video id  |

## Details

Returns metadata for one Douyin video, including the caption, author profile, posting time, duration, comment and danmaku settings. It needs the video's `aweme_id`.

### Use cases

- Read the caption, author nickname and follower count for a Douyin video you already have the ID for.
- Check whether comments, sharing and forwarding are enabled on a video before building a workflow around it.
- Convert `create_time` into a posting date to sort or filter a list of Douyin videos.
- Count danmaku (on-screen comments) on a video and see when the first and last ones appear.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/one-video-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7372484719365098803"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_detail": {
    "activity_video_type": 0,
    "anchors": null,
    "authentication_token": "MS4wLjAA…",
    "author": {
      "avatar_thumb": {
        "height": 720,
        "uri": "100x100/aweme-avatar/tos-cn-avt-0015_f96ccdf24e53e435a85a1976f2c7fe0b",
        "url_list": [
          "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_f96ccdf24…"
        ],
        "width": 720
      },
      "awemehts_greet_info": "",
      "cf_list": null,
      "close_friend_type": 0,
      "contacts_status": 2,
      "contrail_list": null,
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
      "create_time": 0,
      "custom_verify": "",
      "data_label_list": null,
      "endorsement_info_list": null,
      "enterprise_verify_reason": ""
    },
    "author_mask_tag": 0,
    "author_user_id": 95823111667,
    "aweme_control": {
      "can_comment": true,
      "can_forward": true,
      "can_share": true,
      "can_show_comment": true
    },
    "aweme_id": "7372484719365098803",
    "aweme_listen_struct": {
      "trace_info": "{\"copyright_not_speech\":\"true\",\"copyright_reason\":\"not_intercept\",\"copyright_tag…"
    },
    "aweme_type": 0,
    "aweme_type_tags": "",
    "boost_status": 0
  },
  "log_pb": {
    "impr_id": "202611031532283EA01F15D8322E3D0328"
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_detail.aweme_id` | The ID of the video. It matches the `aweme_id` you sent. |
| `aweme_detail.desc / aweme_detail.caption` | The video text, including hashtags such as `#双子座`. |
| `aweme_detail.create_time` | Posting time of the video. The value `1716540374` looks like a Unix timestamp in seconds. |
| `aweme_detail.duration` | Length of the video. The value `8010` is likely in milliseconds, so about 8 seconds. |
| `aweme_detail.author.nickname / aweme_detail.author.sec_uid` | The display name of the author and their `sec_uid`, the ID used to look up the author's profile and posts. |
| `aweme_detail.author.follower_count` | Number of followers the author has. |
| `aweme_detail.author.signature` | The author's profile bio text. |
| `aweme_detail.aweme_control.can_comment / can_forward / can_share` | Flags that show whether commenting, forwarding and sharing are allowed on the video. |
| `aweme_detail.danmaku_control.danmaku_cnt` | Number of danmaku (on-screen comments) on the video. `enable_danmaku` shows whether danmaku is turned on. |
| `aweme_detail.author.avatar_thumb.url_list[]` | URLs of the author's small avatar image. |

### Notes

- Send the video ID in `aweme_id`. The example value is `7372484719365098803`.
- The response includes `status_code`, where `0` is shown for a successful call, and `log_pb.impr_id` as a request identifier.
- To get the author's profile, pass `aweme_detail.author.sec_uid` to [Douyin User Profile (Web)](/apis/douyin/web/user-profile).
- To read the video's comments, use [Douyin Video Comments (Web)](/apis/douyin/web/video-comments).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/one-video-v2.json`](../../../../catalog/models/douyin/web/one-video-v2.json) · Store page: https://www.sandbase.ai/model/douyin/web/one-video-v2
