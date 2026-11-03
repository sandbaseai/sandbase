# TikTok Video Download API: pricing, parameters and code examples

`tiktok/video-download` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

Get the playable media files behind a TikTok video URL: the clean no-watermark MP4, the watermarked one TikTok's own save button produces, and the cover image, with duration and pixel dimensions. Photo-mode posts carry no video file - use tiktok.photos for those.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/video-download", "url": "https://www.tiktok.com/@mrbeast/video/7654638524729216287"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/video-download', {'url': 'https://www.tiktok.com/@mrbeast/video/7654638524729216287'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/video-download", {
  "url": "https://www.tiktok.com/@mrbeast/video/7654638524729216287"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/video-download", sandbase.Params{
	"url": "https://www.tiktok.com/@mrbeast/video/7654638524729216287",
})
```

Same call via the path form: `POST /v1/api/tiktok/video-download` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full TikTok video URL. Share links and tracking query params are fine.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `height` or `width`, and it is served only by a source that returns…  |

## Details

This API returns the downloadable media links for one TikTok video: the clean MP4, the watermarked MP4 and the cover image. It also returns the author, caption, sound and duration. It needs the full TikTok video URL as `url`.

### Use cases

- Save the clean MP4 of a TikTok video to your own storage for archiving or review.
- Fetch the cover image and caption to build a preview card for a TikTok link.
- Check the `durationSeconds` of a video before you queue it for transcoding or editing.
- Collect the sound title and clip ID used in a video to track which audio creators reuse.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/video-download" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@mrbeast/video/7654638524729216287"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full TikTok video URL. Share links and tracking query params are fine. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `height` or `width`, and it is served only by a source that returns ev |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "authorFollowers": null,
    "authorHandle": "mrbeast",
    "authorImage": "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/1e2348ca19d3940…",
    "authorName": "MrBeast",
    "authorUserId": "6614519312189947909",
    "authorVerified": null,
    "caption": "I raced Usain Bolt 😅",
    "createdUtc": 1782234434,
    "durationSeconds": 24,
    "hashtags": [],
    "id": "7654638524729216287",
    "image": "https://p19-common-sign.tiktokcdn-us.com/tos-useast8-p-0068-tx2/owAeXLqoAomjAGOl…"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.videoUrl` | Link to the MP4 file without a watermark. |
| `data.watermarkedUrl` | Link to the MP4 with the TikTok watermark, like the one the save button produces. |
| `data.sdVideoUrl` | Link to a second video file for the same post. The key name suggests a standard-definition version. |
| `data.image` | Link to the cover image of the video. |
| `data.durationSeconds` | Length of the video in seconds. |
| `data.id / data.url` | The video ID and the canonical TikTok URL of the post. |
| `data.caption` | Caption text of the post. |
| `data.createdUtc` | Creation time of the post as a Unix timestamp in seconds, UTC. |
| `data.authorHandle / data.authorName / data.authorUserId` | Handle, display name and numeric user ID of the creator. |
| `data.soundTitle / data.soundAuthor / data.soundClipId` | Title, author and clip ID of the sound used in the video. |

### Notes

- Pass the full video URL in `url`. Share links and URLs with tracking query params work.
- `data.authorFollowers`, `data.authorVerified`, `height` and `width` can come back as `null` or be absent. List them in `requireFields` to get a source that returns them. This can change the price.
- Photo-mode posts have no video file. Use tiktok.photos for those.
- For views, likes and other post details, call [TikTok Video Details](/apis/tiktok/app-v3/one-video).

### Pricing

Billed at the actual cost of each call, about $0.0008 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/video-download.json`](../../../catalog/models/tiktok/video-download.json) · Store page: https://www.sandbase.ai/model/tiktok/video-download
