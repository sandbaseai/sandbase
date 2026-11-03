# Douyin Short Link Generator API: pricing, parameters and code examples

`douyin/app-v3/generate-short-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Converts a standard Douyin web link into a shortened Douyin URL. Returns the shortened link string and operation status for the provided URL.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/generate-short-url", "url": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/generate-short-url', {'url': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/generate-short-url", {
  "url": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/generate-short-url", sandbase.Params{
	"url": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/generate-short-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Douyin link  |

## Details

Converts a standard Douyin web link into a short `v.douyin.com` URL. It needs one input, `url`, which is the full Douyin link to shorten. The response returns the short link, the original target and an operation status.

### Use cases

- Shorten a long Douyin video URL before pasting it into a message, post or spreadsheet.
- Generate short links in bulk for a list of Douyin videos in a campaign report.
- Confirm that a Douyin link resolves to the expected `target` by reading it back from the response.
- Store compact Douyin links in a database or QR code workflow where length matters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/generate-short-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.douyin.com/video/7691553968815623478"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Douyin link |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": [
    {
      "short_url": "https://v.douyin.com/cuksjs-5j5k/",
      "status": "success",
      "target": "https://www.douyin.com/video/7691553968815623478"
    }
  ],
  "message": "success",
  "now": 1793691092
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].short_url` | The shortened Douyin link. It uses the `https://v.douyin.com/` domain. |
| `data[].target` | The full Douyin link the short URL points to. It matches the `url` you sent. |
| `data[].status` | Result of the shortening step for this link. The value is `success` when a short link was created. |
| `code / message` | Overall request result. `code` is `0` and `message` is `success` when the call worked. |
| `now` | A numeric timestamp returned with the response. It looks like a Unix time in seconds. |

### Notes

- Pass the full Douyin web link in `url`, for example a `https://www.douyin.com/video/<id>` link.
- The result sits in a list under `data`. Read the first item for the short link.
- To turn a video link into a scannable code, call [Douyin Video Share QR Code](/apis/douyin/app-v3/generate-video-share-qrcode).
- To get video details from a share link, call [Douyin Single Video by Share URL](/apis/douyin/app-v3/one-video-by-share-url).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Video Share QR Code](/apis/douyin/app-v3/generate-video-share-qrcode): Returns a Douyin share QR code for a designated target.

---
Machine-readable: [`catalog/models/douyin/app-v3/generate-short-url.json`](../../../../catalog/models/douyin/app-v3/generate-short-url.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/generate-short-url
