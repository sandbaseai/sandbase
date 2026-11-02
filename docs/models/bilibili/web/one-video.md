# Bilibili Video Details API: pricing, parameters and code examples

`bilibili/web/one-video` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata and honor tags for a single Bilibili video based on its unique BV identifier, including recommendation status.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/one-video", "bv_id": "BV1dVbC6WE6p"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/one-video', {'bv_id': 'BV1dVbC6WE6p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/one-video", {
  "bv_id": "BV1dVbC6WE6p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/one-video", sandbase.Params{
	"bv_id": "BV1dVbC6WE6p",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/one-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bv_id` | string | yes | Video id  |

## Details

Access metadata and honor highlights for a specific Bilibili video by providing its `bv_id`.

### Use cases

- Look up honor badges and weekly recommendation highlights for a specific video.
- Monitor video recognition and tag status across Bilibili.
- Display video details within external reporting and analytics dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/one-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bv_id": "BV1M1421t7hT"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bv_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "honor_reply": {
      "honor": [
        {
          "desc": "热门",
          "type": 4,
          "weekly_recommend_num": 0
        }
      ]
    }
  }
}
```

### Notes

- Provide the video BV identifier in `bv_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/one-video.json`](../../../../catalog/models/bilibili/web/one-video.json) · Store page: https://www.sandbase.ai/model/bilibili/web/one-video
