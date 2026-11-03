# Xigua Video Play URL API: pricing, parameters and code examples

`xigua/app-v2/one-video-play-url` · data API · Xigua · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the direct playback URL for a specific Xigua video using its unique item identifier. Developers supply the target video ID to retrieve playable media links.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xigua/app-v2/one-video-play-url", "item_id": "7354954305222377999"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xigua/app-v2/one-video-play-url', {'item_id': '7354954305222377999'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xigua/app-v2/one-video-play-url", {
  "item_id": "7354954305222377999"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xigua/app-v2/one-video-play-url", sandbase.Params{
	"item_id": "7354954305222377999",
})
```

Same call via the path form: `POST /v1/api/xigua/app-v2/one-video-play-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video id  |

## Details

Returns the playback data for one Xigua video: a list of stream variants at different resolutions, a poster image, sprite thumbnails and loudness data. It needs the video's `item_id`.

### Use cases

- Pick a 360p, 480p or 720p stream from `video_list` and load it in an external video player.
- Compare `bitrate` and `size` across variants to choose a stream for a given bandwidth or storage budget.
- Build a seek preview bar from the `big_thumbs` sprite sheet data.
- Check `url_expire` on each stream to decide when to request fresh links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xigua/app-v2/one-video-play-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7354954305222377999"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "account_name": "xigua",
  "auto_definition": "360p",
  "big_thumbs": [
    {
      "duration": 189.566667,
      "fext": "jpg",
      "img_num": 190,
      "img_url": "https://p6-xg-sprite-sign.bdxiguaimg.com/tos-cn-p-0026/0b52ae3a5b00446689d50d82e…",
      "img_urls": [
        "https://p6-xg-sprite-sign.bdxiguaimg.com/tos-cn-p-0026/0b52ae3a5b00446689d50d82e…"
      ],
      "img_x_len": 10,
      "img_x_size": 136,
      "img_y_len": 19,
      "img_y_size": 182,
      "interval": 1,
      "uri": "tos-cn-p-0026/0b52ae3a5b00446689d50d82ecc812de_1712458757"
    }
  ],
  "enable_adaptive": true,
  "enable_ssl": true,
  "media_type": "video",
  "message": "success",
  "original_play_url": {
    "backup_url": "https://video-cn-public.bytedance.net/storage/v1/tos-cn-v-0026/oYAhhCz7EQDAhXCAj…",
    "main_url": "https://video-cn-public.bytedance.net/storage/v1/tos-cn-v-0026/oYAhhCz7EQDAhXCAj…"
  },
  "poster_meta_info": "",
  "poster_url": "https://p9-xg-cover-sign.bdxiguaimg.com/tos-cn-p-0026/o8eueGqmEAlnAG6FDGJg4pFBCS…",
  "status": 10,
  "validate": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `video_list.video_1 / video_list.video_2 / video_list.video_3` | One entry per stream variant. Each entry holds its own URLs, resolution, codec and file size. |
| `video_list.video_1.main_url / video_list.video_1.backup_url_1` | Primary and fallback URLs for that stream. The same pair exists for every `video_N` entry. |
| `video_list.video_1.definition / video_list.video_1.vwidth / video_list.video_1.vheight` | Quality label (for example `360p`) with the pixel width and height of the stream. |
| `video_list.video_1.bitrate / video_list.video_1.size` | Bitrate and file size of the stream. Use them to compare variants. |
| `video_list.video_1.vtype / video_list.video_1.codec_type` | Container format (`mp4`) and video codec (`h264`). |
| `video_list.video_1.url_expire` | Unix timestamp that appears to mark when the stream links expire. |
| `video_duration` | Length of the video, with decimals. The value 189.569 matches the `duration` in `big_thumbs`, so it is in seconds. |
| `poster_url` | Link to the cover image of the video. |
| `original_play_url.main_url / original_play_url.backup_url` | Primary and fallback links to the original file. |
| `big_thumbs[].img_urls / big_thumbs[].img_num` | Sprite sheet image links and the number of preview frames. `img_x_len` and `img_y_len` give the grid layout, and `interval` the spacing between frames. |

### Notes

- Send the video ID as `item_id`, for example `7354954305222377999`.
- The response has no title or author. Call [Xigua Single Video Information](/apis/xigua/app-v2/one-video) for video details.
- Use [Xigua Video Search](/apis/xigua/app-v2/search-video) or [Xigua User Post List](/apis/xigua/app-v2/user-post-list) to find video IDs.
- Stream variants are named `video_1`, `video_2` and so on. Read `definition` in each entry to see its resolution.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xigua Single Video Information](/apis/xigua/app-v2/one-video): Returns lightweight single video data and associated related video information from Xigua for a specific post by its unique item ID.
- [Xigua Video Search](/apis/xigua/app-v2/search-video): Search Xigua Video (ByteDance long-form video) by keyword: titles, creators, duration, publish time and comment counts, with sort and duration filters.
- [Xigua User Profile Details](/apis/xigua/app-v2/user-info): Returns profile and personal information for a specified Xigua account.

---
Machine-readable: [`catalog/models/xigua/app-v2/one-video-play-url.json`](../../../../catalog/models/xigua/app-v2/one-video-play-url.json) · Store page: https://www.sandbase.ai/model/xigua/app-v2/one-video-play-url
