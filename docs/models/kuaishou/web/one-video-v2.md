# Kuaishou Single Video Details (V2) API: pricing, parameters and code examples

`kuaishou/web/one-video-v2` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Retrieves video streaming manifests and media details for a specific Kuaishou video using its unique identifier.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/one-video-v2", "photo_id": "5193494945927590140"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/one-video-v2', {'photo_id': '5193494945927590140'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/one-video-v2", {
  "photo_id": "5193494945927590140"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/one-video-v2", sandbase.Params{
	"photo_id": "5193494945927590140",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/one-video-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `photo_id` | string | yes | 作品ID/Photo ID  |

## Details

Use this endpoint to retrieve video stream URLs, resolution tiers, and frame rate metadata by supplying a `photo_id`.

### Use cases

- Extract direct video stream links and format specifications for a Kuaishou post.
- Inspect available resolution tiers and encoding qualities for individual videos.
- Integrate Kuaishou video playback data into external media tools.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/one-video-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"photo_id": "5193494945927590140"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `photo_id` | string | Yes | — |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "photo": {
    "manifest": {
      "adaptationSet": [
        {
          "representation": [
            {
              "frameRate": 60,
              "hdrType": 0,
              "id": 1,
              "qualityLabel": "高清",
              "qualityType": "720p",
              "url": "https://v1.kwaicdn.com/upic/2024/12/29/22/BMjAyNDEyMjkyMjE1NDJfMzc5NTIxNDQxMV8xN…",
              "kvqScore": {
                "nnvcScore": -1
              }
            }
          ]
        }
      ]
    }
  }
}
```

### Notes

- Requires a valid `photo_id` to look up video manifest information.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Web Share Short URL](/model/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/model/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/model/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/one-video-v2.json`](../../../../catalog/models/kuaishou/web/one-video-v2.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/one-video-v2
