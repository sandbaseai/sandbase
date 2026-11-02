# Douyin Single Video by Share URL API: pricing, parameters and code examples

`douyin/app-v3/one-video-by-share-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns detailed video metadata and playback stream specifications for a specific Douyin post using its public share link.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/one-video-by-share-url", "share_url": "https://static.sandbase.ai/examples/a4f6780e-576a-4cd7-b3b0-ef3f793529c1/input/a037f59a-0a2e-4214-8938-b5c11d2ac95a.bin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/one-video-by-share-url', {'share_url': 'https://static.sandbase.ai/examples/a4f6780e-576a-4cd7-b3b0-ef3f793529c1/input/a037f59a-0a2e-4214-8938-b5c11d2ac95a.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/one-video-by-share-url", {
  "share_url": "https://static.sandbase.ai/examples/a4f6780e-576a-4cd7-b3b0-ef3f793529c1/input/a037f59a-0a2e-4214-8938-b5c11d2ac95a.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/one-video-by-share-url", sandbase.Params{
	"share_url": "https://static.sandbase.ai/examples/a4f6780e-576a-4cd7-b3b0-ef3f793529c1/input/a037f59a-0a2e-4214-8938-b5c11d2ac95a.bin",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/one-video-by-share-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `share_url` | string | yes | Share link  |

## Details

Retrieve video metadata and stream specs from Douyin by providing a post link in `share_url`.

### Use cases

- Extract video stream qualities from a Douyin post link.
- Look up Douyin video details from shared mobile URLs.
- Parse media bitrates and playback specifications for a clip.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/one-video-by-share-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_url": "https://www.douyin.com/video/7512756548356492544"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_url` | string | Yes | Share link |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_detail": {
    "video": {
      "bit_rate": [
        {
          "bit_rate": 582425,
          "gear_name": "540_2_2",
          "quality_type": 23
        }
      ]
    }
  }
}
```

### Notes

- Pass the full post URL in `share_url` to retrieve video details.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/one-video-by-share-url.json`](../../../../catalog/models/douyin/app-v3/one-video-by-share-url.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/one-video-by-share-url
