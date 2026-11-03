# Douyin Video Detail App Link API: pricing, parameters and code examples

`douyin/app-v3/open-app-to-video-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a Douyin share URL for a given video ID. The resulting link opens the Douyin mobile application directly to the specified video detail screen.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/open-app-to-video-detail", "aweme_id": "7197598285882789120"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/open-app-to-video-detail', {'aweme_id': '7197598285882789120'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/open-app-to-video-detail", {
  "aweme_id": "7197598285882789120"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/open-app-to-video-detail", sandbase.Params{
	"aweme_id": "7197598285882789120",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/open-app-to-video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Video id  |

## Details

Returns a Douyin short share URL for a video. The link opens the Douyin mobile app on that video's detail screen. You send the video ID as `aweme_id`.

### Use cases

- Send mobile users straight to one Douyin video inside the app from a web page or message.
- Build a short share link for a specific Douyin video to put in a campaign or post.
- Store a tap-to-open link next to each video ID in your own database.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/open-app-to-video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7197598285882789120"}'
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
  "aweme_id": "7197598285882789120",
  "short_url": "https://v.douyin.com/leMEOXh1Mec/",
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_id` | The video ID you sent. It echoes the input so you can match the result to your request. |
| `short_url` | The short Douyin share link for the video. It has the form `https://v.douyin.com/<code>/`. |
| `status` | Result of the call. The value is `success` when the link was created. |

### Notes

- `aweme_id` is the numeric Douyin video ID, for example `7197598285882789120`. Pass it as a string.
- The same `aweme_id` can return a different `short_url` code on different calls.
- To get video details such as description or stats, call [Douyin Single Video Details](/apis/douyin/app-v3/one-video) or [Douyin Video Statistics](/apis/douyin/app-v3/video-statistics).
- To get a QR code for sharing a video, use [Douyin Video Share QR Code](/apis/douyin/app-v3/generate-video-share-qrcode).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/open-app-to-video-detail.json`](../../../../catalog/models/douyin/app-v3/open-app-to-video-detail.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/open-app-to-video-detail
