# WeChat Channels Account Videos API: pricing, parameters and code examples

`wechat-channels/account-videos` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.071429 per call · **Modes:** sync

Get a paginated WeChat Channels account feed by v2Name with continuation-buffer support. Use it to browse videos and other feed entries published by a known creator account.

## Pricing

- **$0.071429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/account-videos", "v2Name": "v2_060000231003b20faec8c7e48d1dc6d5c802e83db0770775bb566d2b495e6aae711d6d56bd04@finder"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/account-videos', {'v2Name': 'v2_060000231003b20faec8c7e48d1dc6d5c802e83db0770775bb566d2b495e6aae711d6d56bd04@finder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/account-videos", {
  "v2Name": "v2_060000231003b20faec8c7e48d1dc6d5c802e83db0770775bb566d2b495e6aae711d6d56bd04@finder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/account-videos", sandbase.Params{
	"v2Name": "v2_060000231003b20faec8c7e48d1dc6d5c802e83db0770775bb566d2b495e6aae711d6d56bd04@finder",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/account-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `v2Name` | string | yes | WeChat Channels account unique id, usually ending with @finder.  |
| `last_buffer` | string |  | Pagination buffer returned by the previous WeChat Channels account videos response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.  |

## Details

Returns one page of a WeChat Channels account feed, plus the account profile. It needs the account's `v2Name` and, for later pages, the `last_buffer` value from the previous response.

### Use cases

- Pull the latest videos from a known creator account and track their like, comment and forward counts.
- Build a list of an account's video titles and publish dates for content research.
- Collect `object_id` and `export_id` values to feed into video detail, comment or download lookups.
- Read an account's nickname, signature and region to check who runs a feed.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/account-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"v2Name": "v2_060000231003b20faec8c7e48d1dc6d5c802e83db0770775bb566d2b495e6aae711d6d56bd04@finder"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `v2Name` | string | Yes | WeChat Channels account unique id, usually ending with @finder. |
| `last_buffer` | string | No | Pagination buffer returned by the previous WeChat Channels account videos response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "anchor_stat": {
    "recent_live_count": 0,
    "total_live_count": 0
  },
  "contact": {
    "additional_flag": "1",
    "bind_info": [],
    "cover_img_url": "http://mmsns.qpic.cn/mmsns/aXUpZVUYfjzXyNIQ6sVE3W3YFkDoWicHoyoticEJ2x1Ny5I0v5gjY…",
    "ext_flag": 2097152,
    "follow_flag": 0,
    "head_url": "https://wx.qlogo.cn/finderhead/ver_1/cYjfLLvyawMia46XlTZvhpGlrG51EzMk4Atg5MZY1St…",
    "live_cover_img_url": "",
    "live_info": {
      "anchor_status_flag": "2048",
      "ktv_live_cover_imgs": [],
      "live_cover_imgs": [],
      "lottery_setting": {},
      "mic_setting": {
        "setting_flag": 0,
        "setting_switch_flag": 4
      },
      "replay_setting": {
        "can_use_intelligently_gen_replay_highlight": true
      },
      "source_type": 0,
      "switch_flag": 4607,
      "voice_live_cover_imgs": []
    },
    "live_status": 2,
    "menu": [],
    "nickname": "人工智能",
    "original_entrance_flag": 1
  },
  "continue_flag": 1,
  "feeds_count": 80,
  "ip_region_info": {
    "region_text": "湖北"
  },
  "last_buffer": "EAEYADAAOM/MhJCn65cDQIDog+SHiPoCSOKRzPz9qZKSyAFI5pDw1aSsod3HAUjHkfze4rCjiMcBSLSx…",
  "live_duration_hours": 0,
  "mcn_info": {},
  "object": [
    {
      "comment_count": 5,
      "cover_url": "https://finder.video.qq.com/251/20304/stodownload?encfilekey=oibeqyX228riaCwo9ST…",
      "decode_key": "926853272",
      "download_url": "https://finder.video.qq.com/251/20302/stodownload?encfilekey=Cvvj5Ix3eez3Y79Sxtv…",
      "export_id": "export/UzFfAgtgekIEAQAAAAAAwp0tv-W0sgAAAAstQy6ubaLX4KHWvLEZgBPEtqI8Qm1FSPeLzNPgM…",
      "fav_count": 20,
      "file_size": 25854106,
      "forward_count": 25,
      "like_count": 15,
      "live_info": {},
      "media_type": "视频",
      "object_id": "14421732514149370082"
    }
  ],
  "original_count": 3,
  "req_p": "192.168.130.85:2020, 192.168.1.122:8090"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `object[]` | The feed entries on this page. Each item is one video. |
| `object[].title` | Caption text of the video, including hashtags. |
| `object[].publish_time` | Publish time of the video as a `YYYY-MM-DD HH:MM:SS` string. |
| `object[].like_count / comment_count / fav_count / forward_count` | Engagement counts for the video. |
| `object[].video_play_len` | Length of the video. The response does not state the unit. |
| `object[].object_id / export_id / object_nonce_id` | Identifiers for the video. Use them with other video lookups. |
| `object[].cover_url / thumb_url / download_url / openurl` | Links to the cover image, thumbnail, media file and the preview page of the video. |
| `contact.nickname / contact.signature / contact.head_url` | Account display name, bio text and avatar link. |
| `continue_flag` | `1` in this response, which shows more pages are available. Use it with `last_buffer` to decide whether to keep paging. |
| `feeds_count / original_count` | Counts reported for the account. `feeds_count` was `80` and `original_count` was `3` in this response. |

### Notes

- Send the `last_buffer` value from the response as the `last_buffer` parameter to get the next page. Leave it empty for the first page.
- The `last_buffer` parameter goes in an `application/x-www-form-urlencoded` form body for this POST endpoint.
- `v2Name` usually ends with `@finder`. It is also returned as `contact.username`.
- Call [WeChat Channels Video Detail](/apis/wechat-channels/v2/video-detail) or [WeChat Channels Video Comments](/apis/wechat-channels/v2/video-comments) to go deeper on a single video.

### Pricing

$0.071429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/account-videos.json`](../../../catalog/models/wechat-channels/account-videos.json) · Store page: https://www.sandbase.ai/model/wechat-channels/account-videos
