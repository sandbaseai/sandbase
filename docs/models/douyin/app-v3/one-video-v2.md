# Douyin Single Video Data (App V3) API: pricing, parameters and code examples

`douyin/app-v3/one-video-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata for a single Douyin item, including video and photo posts, using the specific video identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/one-video-v2", "aweme_id": "7675551740036612985"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/one-video-v2', {'aweme_id': '7675551740036612985'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/one-video-v2", {
  "aweme_id": "7675551740036612985"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/one-video-v2", sandbase.Params{
	"aweme_id": "7675551740036612985",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/one-video-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Video id  |

## Details

Retrieve detailed metadata for a Douyin post by supplying the item identifier in `aweme_id`.

### Use cases

- Inspect video quality levels and bitrate options for a specific post.
- Retrieve Douyin photo and video post details using a known item ID.
- Verify media playback parameters for content archiving workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/one-video-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7448118827402972455"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_detail": {
    "video": {
      "bit_rate": [
        {
          "bit_rate": 122767,
          "gear_name": "additional_adapt_lowest_1080_1",
          "quality_type": 2
        }
      ]
    }
  }
}
```

### Notes

- Provide the unique post identifier in `aweme_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/one-video-v2.json`](../../../../catalog/models/douyin/app-v3/one-video-v2.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/one-video-v2
