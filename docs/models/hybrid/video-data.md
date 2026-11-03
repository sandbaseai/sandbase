# Universal Video Link Parser API: pricing, parameters and code examples

`hybrid/video-data` · data API · Hybrid · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Parse a shared video link from Douyin, TikTok and other supported platforms and get the video details, author and no-watermark media URLs.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hybrid/video-data", "url": "https://v.douyin.com/L4FJNR3/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hybrid/video-data', {'url': 'https://v.douyin.com/L4FJNR3/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hybrid/video-data", {
  "url": "https://v.douyin.com/L4FJNR3/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hybrid/video-data", sandbase.Params{
	"url": "https://v.douyin.com/L4FJNR3/",
})
```

Same call via the path form: `POST /v1/api/hybrid/video-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | url  |
| `minimal` | boolean |  | Whether to return minimal data default `false` |
| `base64_url` | boolean |  | Base64 encoding URL default `false` |

## Details

This API takes a shared video link from Douyin, TikTok or another supported platform and returns the video details, the author profile and media URLs. The only required input is `url`. The example response is for a Douyin video.

### Use cases

- Resolve a short Douyin share link such as `https://v.douyin.com/L4FJNR3/` to its full video ID in `aweme_id`.
- Collect the caption in `desc`, the hashtags in `cha_list` and the post time in `create_time` for a shared video.
- Read the author's avatar images and video count to build a creator card from a pasted link.
- Use the `minimal` parameter to request a smaller response when you only need the main video fields.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/hybrid/video-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://v.douyin.com/L4FJNR3/", "minimal": false, "base64_url": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | url |
| `base64_url` | boolean | No | Base64 encoding URL |
| `minimal` | boolean | No | Whether to return minimal data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "activity_video_type": 0,
  "admire_auth": {
    "admire_button": 1,
    "author_can_admire": 0,
    "exit_admire_in_aweme_post": 0,
    "is_admire": 0,
    "is_click_admire_icon_recently": 0,
    "is_fifty_admire_author_stable_fans": 0,
    "is_iron_fans_in_aweme_post": 0,
    "is_show_admire_button": 0,
    "is_show_admire_tab": 0
  },
  "anchors": null,
  "authentication_token": "MS4wLjAA…",
  "author": {
    "accept_private_policy": false,
    "account_cert_info": "{}",
    "account_region": "",
    "ad_cover_url": null,
    "allow_story_normal_like": true,
    "apple_account": 0,
    "authority_status": 0,
    "avatar_168x168": {
      "height": 720,
      "uri": "168x168/aweme-avatar/tos-cn-avt-0015_7582e9bc5e5c154ae24a5edff9989f80",
      "url_list": [
        "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_7582e9bc5e5c154ae24a5e…"
      ],
      "width": 720
    },
    "avatar_300x300": {
      "height": 720,
      "uri": "300x300/aweme-avatar/tos-cn-avt-0015_7582e9bc5e5c154ae24a5edff9989f80",
      "url_list": [
        "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_7582e9bc5e5c154ae24a5e…"
      ],
      "width": 720
    },
    "avatar_larger": {
      "height": 720,
      "uri": "1080x1080/aweme-avatar/tos-cn-avt-0015_7582e9bc5e5c154ae24a5edff9989f80",
      "url_list": [
        "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_7582e9bc5e…"
      ],
      "width": 720
    },
    "avatar_medium": {
      "height": 720,
      "uri": "720x720/aweme-avatar/tos-cn-avt-0015_7582e9bc5e5c154ae24a5edff9989f80",
      "url_list": [
        "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_7582e9bc5e5c…"
      ],
      "width": 720
    },
    "avatar_thumb": {
      "height": 720,
      "uri": "100x100/aweme-avatar/tos-cn-avt-0015_7582e9bc5e5c154ae24a5edff9989f80",
      "url_list": [
        "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_7582e9bc5e5c…"
      ],
      "width": 720
    }
  },
  "author_mask_tag": 0,
  "author_user_id": 59840491348,
  "aweme_control": {
    "can_comment": true,
    "can_forward": true,
    "can_share": true,
    "can_show_comment": true
  },
  "aweme_id": "6918273131559881997",
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
    "trace_info": "{\"copyright_not_speech\":\"true\",\"copyright_reason\":\"label_risk_music_or_speech\",\"…"
  },
  "aweme_type": 0,
  "aweme_type_tags": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_id` | ID of the video. It is a numeric string. |
| `desc` | Caption text of the video, including hashtags written as `#tag`. |
| `create_time` | Time the video was posted. The value `1610786002` looks like a Unix timestamp in seconds. |
| `author_user_id` | Numeric ID of the account that posted the video. |
| `author.aweme_count` | Number of videos on the author's account. |
| `author.avatar_168x168 / author.avatar_300x300 / author.avatar_medium / author.avatar_larger / author.avatar_thumb` | Author avatar images in several sizes. Each object has `uri`, `width`, `height` and a `url_list` of image links. |
| `cha_list[].cha_name` | Name of a hashtag challenge attached to the video. |
| `cha_list[].cid` | ID of the hashtag challenge. |
| `cha_list[].desc` | Description text of the hashtag challenge. |
| `city` | City code for the video. The example value is `330100`. |

### Notes

- Send a share link in `url`. The example uses a short `v.douyin.com` link.
- Set `base64_url` to `true` to send the `url` value Base64 encoded.
- The response holds many nested and null fields. Set `minimal` to `true` to get less data.
- The result is returned in `outputs[0].data`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/hybrid/video-data.json`](../../../catalog/models/hybrid/video-data.json) · Store page: https://www.sandbase.ai/model/hybrid/video-data
