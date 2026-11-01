# Douyin Short Link Generator

`douyin/app-v3/generate-short-url` · api · Douyin

Converts a standard Douyin web link into a shortened Douyin URL. Returns the shortened link string and operation status for the provided URL.

## Pricing

- **$0.0015 per call** (USD)
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

Convert full Douyin links into compact short URLs by supplying the target link via `url`.

### Use cases

- Shorten full Douyin video URLs for compact sharing.
- Convert standard Douyin web links into mobile-friendly URLs.
- Process Douyin links to embed shorter paths in external platforms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/generate-short-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.douyin.com/video/7691553968815623478"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Douyin link |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "short_url": "https://v.douyin.com/jAO8y1A55-Y/",
      "status": "success"
    }
  ]
}
```

### Notes

- Requires a valid Douyin link passed in `url`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Video Share QR Code](/model/douyin/app-v3/generate-video-share-qrcode): Returns a Douyin share QR code for a designated target.

---
Machine-readable: [`catalog/models/douyin/app-v3/generate-short-url.json`](../../../../catalog/models/douyin/app-v3/generate-short-url.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/generate-short-url
