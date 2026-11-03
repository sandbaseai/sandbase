# WeChat Channels Video Download URL API: pricing, parameters and code examples

`wechat-channels/video-download-url` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.042857 per call · **Modes:** sync

Get a downloadable media URL for a WeChat Channels video by object ID and optional nonce ID. Use it to download or play media from a known Channels video.

## Pricing

- **$0.042857 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/video-download-url", "objectId": "14941130915890399732"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/video-download-url', {'objectId': '14941130915890399732'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/video-download-url", {
  "objectId": "14941130915890399732"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/video-download-url", sandbase.Params{
	"objectId": "14941130915890399732",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/video-download-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `objectId` | string | yes | WeChat Channels video object id used to fetch downloadable media links.  |
| `objectNonceId` | string |  | Optional WeChat Channels object nonce id. Supplying it can improve media lookup accuracy.  |

## Details

Returns a download URL for a WeChat Channels video, plus cover and thumbnail URLs and basic post details such as title, author name, and engagement counts. It needs the video `objectId`, and accepts an optional `objectNonceId`.

### Use cases

- Download a known Channels video file for archiving or offline review.
- Play a Channels video in your own tool using the returned `download_url`.
- Save the cover image and title of a video next to the media file.
- Record the like, comment, and forward counts of a video at the time of download.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/video-download-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"objectId": "14941130915890399732"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `objectId` | string | Yes | WeChat Channels video object id used to fetch downloadable media links. |
| `objectNonceId` | string | No | Optional WeChat Channels object nonce id. Supplying it can improve media lookup accuracy. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comment_count": 97,
  "cover_url": "https://finder.video.qq.com/251/20304/stodownload?encfilekey=KGDRibp2wkicK7MMrxH…",
  "download_url": "http://47.117.133.51:30015/media/weixin-channels/download/bddf15ad0c5646a99ff86e…",
  "fav_count": 13502,
  "file_size": 2018860,
  "forward_count": 614382,
  "like_count": 9158,
  "media_type": 4,
  "nickname": "人民日报",
  "object_id": "14941130915890399732",
  "object_nonce_id": "13119916…",
  "publish_time": "2026-06-11 04:00:01"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `download_url` | Link to the video media file. The URL carries a `signature` query parameter. |
| `cover_url / thumb_url` | Image links for the video cover and its thumbnail. |
| `title` | Caption text of the video, including any hashtags. |
| `nickname` | Display name of the account that posted the video. |
| `publish_time` | Publish time as a `YYYY-MM-DD HH:MM:SS` string. |
| `like_count / fav_count / forward_count / comment_count` | Engagement counts for the video: likes, favorites, forwards, and comments. |
| `file_size` | Size of the media file. The response does not state the unit. |
| `video_play_len` | Play length of the video. The value `15` is the only hint, and the response does not state the unit. |
| `object_id / object_nonce_id` | The video's object ID and nonce ID. You can reuse them in other Channels calls. |
| `media_type` | Numeric media type code. The response shows `4` for this video and does not explain the code. |

### Notes

- `objectId` is the only required input. Add `objectNonceId` when you have it, since it can improve media lookup.
- The response returns `object_nonce_id` (for example `13119916371223643581_0_146_0_0`), which you can pass as `objectNonceId` in later calls.
- To find an `objectId` first, call [WeChat Channels Video Search](/apis/wechat-channels/search-video) or [WeChat Channels Account Videos](/apis/wechat-channels/account-videos).
- For fuller post details on the same video, call [WeChat Channels Video Detail](/apis/wechat-channels/v2/video-detail).

### Pricing

$0.042857 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/video-download-url.json`](../../../catalog/models/wechat-channels/video-download-url.json) · Store page: https://www.sandbase.ai/model/wechat-channels/video-download-url
