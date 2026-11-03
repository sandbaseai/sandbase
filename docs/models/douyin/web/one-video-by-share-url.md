# Douyin Video Details by Share URL API: pricing, parameters and code examples

`douyin/web/one-video-by-share-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed video information and available stream bitrate qualities for a single Douyin video using its web sharing link.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/one-video-by-share-url", "share_url": "https://static.sandbase.ai/examples/359eb7d4-4fa9-4d07-8f2c-1848998bd134/input/ff5ce252-e396-407c-b39c-b43cbd50b1d7.bin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/one-video-by-share-url', {'share_url': 'https://static.sandbase.ai/examples/359eb7d4-4fa9-4d07-8f2c-1848998bd134/input/ff5ce252-e396-407c-b39c-b43cbd50b1d7.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/one-video-by-share-url", {
  "share_url": "https://static.sandbase.ai/examples/359eb7d4-4fa9-4d07-8f2c-1848998bd134/input/ff5ce252-e396-407c-b39c-b43cbd50b1d7.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/one-video-by-share-url", sandbase.Params{
	"share_url": "https://static.sandbase.ai/examples/359eb7d4-4fa9-4d07-8f2c-1848998bd134/input/ff5ce252-e396-407c-b39c-b43cbd50b1d7.bin",
})
```

Same call via the path form: `POST /v1/api/douyin/web/one-video-by-share-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `share_url` | string | yes | Share link  |

## Details

Returns the details of one Douyin video, including the caption, author profile, creation time and duration. It needs one input, a Douyin web share link passed as `share_url`.

### Use cases

- Look up the caption, author and posting time of a Douyin video from its web link.
- Check the follower count of a video's author at the time of the lookup.
- Read the comment permission and danmaku settings of a single video.
- Get the `aweme_id` and `sec_uid` for a video to use in other Douyin calls.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/one-video-by-share-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_url": "https://www.douyin.com/video/7512756548356492544"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_url` | string | Yes | Share link |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_detail": {
    "activity_video_type": 0,
    "anchors": null,
    "authentication_token": "MS4wLjAA…",
    "author": {
      "account_cert_info": "{}",
      "avatar_thumb": {
        "height": 720,
        "uri": "100x100/aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c745843",
        "url_list": [
          "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_9186d2f6f…"
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
      "endorsement_info_list": null
    },
    "author_mask_tag": 0,
    "author_user_id": 3635433641882579,
    "aweme_control": {
      "can_comment": true,
      "can_forward": true,
      "can_share": true,
      "can_show_comment": true
    },
    "aweme_id": "7512756548356492544",
    "aweme_listen_struct": {
      "trace_info": "{\"copyright_not_speech\":\"false\",\"copyright_reason\":\"not_intercept\",\"copyright_ta…"
    },
    "aweme_type": 0,
    "aweme_type_tags": "",
    "boost_status": 0
  },
  "log_pb": {
    "impr_id": "202611031532295F7C784015B58FD80C2B"
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_detail.aweme_id` | ID of the video. It matches the number at the end of the share link. |
| `aweme_detail.desc / aweme_detail.caption` | Text of the video post. In this example both hold the hashtag `#neo浪漫蓝调`. |
| `aweme_detail.create_time` | Creation time of the video as a Unix timestamp in seconds. |
| `aweme_detail.duration` | Length of the video. The example value is `12634`. |
| `aweme_detail.author.nickname` | Display name of the author. |
| `aweme_detail.author.sec_uid` | Secure user ID of the author. Use it to look up the author's profile or posts. |
| `aweme_detail.author.follower_count` | Number of followers the author has. |
| `aweme_detail.author.signature` | Bio text of the author. |
| `aweme_detail.aweme_control.can_comment / aweme_detail.aweme_control.can_share` | Booleans that show whether commenting and sharing are allowed on the video. |
| `aweme_detail.danmaku_control.danmaku_cnt` | Number of danmaku (on-screen comments) on the video. It is `enable_danmaku` that shows whether danmaku are turned on. |

### Notes

- Pass a full video link such as `https://www.douyin.com/video/7512756548356492544` in `share_url`.
- Fetch the video's danmaku with [Douyin Video Danmaku](/apis/douyin/web/one-video-danmaku).
- Fetch the author's profile with [Douyin User Profile (Web)](/apis/douyin/web/user-profile), using the value in `aweme_detail.author.sec_uid`.
- Image URLs in the response, such as `aweme_detail.author.cover_url[].url_list`, are signed and carry an `x-expires` value.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/one-video-by-share-url.json`](../../../../catalog/models/douyin/web/one-video-by-share-url.json) · Store page: https://www.sandbase.ai/model/douyin/web/one-video-by-share-url
