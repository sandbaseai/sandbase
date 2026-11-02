# Kuaishou Video Details (V1) API: pricing, parameters and code examples

`kuaishou/app/one-video` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns detailed video metadata for a single Kuaishou video post using its photo identifier. Query by video ID to inspect post attributes.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/one-video", "photo_id": "5193494945927590140"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/one-video', {'photo_id': '5193494945927590140'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/one-video", {
  "photo_id": "5193494945927590140"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/one-video", sandbase.Params{
	"photo_id": "5193494945927590140",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/one-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `photo_id` | string | yes | 作品ID/Photo ID  |

## Details

Retrieve detailed information for a single Kuaishou video post by supplying its `photo_id`.

### Use cases

- Look up metadata for an individual Kuaishou video.
- Inspect comment priority and display settings for a post.
- Retrieve post details using a photo identifier.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/one-video" \
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
  "photos": [
    {
      "commentTopBarPriority": [
        {
          "bizType": "PLC",
          "subBizType": "51"
        }
      ]
    }
  ]
}
```

### Notes

- Requires a valid `photo_id` to look up the video.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/one-video.json`](../../../../catalog/models/kuaishou/app/one-video.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/one-video
