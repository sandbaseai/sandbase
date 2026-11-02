# Bilibili Video Details (V2) API: pricing, parameters and code examples

`bilibili/web/one-video-v2` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Returns detailed metadata and playback information for a specific Bilibili video using its unique video and CID identifiers.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/one-video-v2", "a_id": "114006081739452", "c_id": "28400484458"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/one-video-v2', {'a_id': '114006081739452', 'c_id': '28400484458'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/one-video-v2", {
  "a_id": "114006081739452",
  "c_id": "28400484458"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/one-video-v2", sandbase.Params{
	"a_id": "114006081739452",
	"c_id": "28400484458",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/one-video-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `a_id` | string | yes | Video id  |
| `c_id` | string | yes | Video cid  |

## Details

Retrieve detailed information for a Bilibili video by providing the target `a_id` and `c_id`.

### Use cases

- Retrieve video metadata and stream identifiers for player integration
- Monitor performance metrics of a specific Bilibili video
- Inspect individual video components using video and CID identifiers

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/one-video-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"a_id": "<a_id>", "c_id": "<c_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `a_id` | string | Yes | Video id |
| `c_id` | string | Yes | Video cid |

### Notes

- Requires both the video ID `a_id` and the video component identifier `c_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/one-video-v2.json`](../../../../catalog/models/bilibili/web/one-video-v2.json) · Store page: https://www.sandbase.ai/model/bilibili/web/one-video-v2
