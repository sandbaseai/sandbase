# Bilibili Video Subtitle Details API: pricing, parameters and code examples

`bilibili/web/video-subtitle` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns subtitle data for a specified Bilibili video based on its video ID and CID. Helps retrieve available caption tracks and related metadata.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/video-subtitle", "a_id": "114006081739452", "c_id": "28400484458"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/video-subtitle', {'a_id': '114006081739452', 'c_id': '28400484458'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/video-subtitle", {
  "a_id": "114006081739452",
  "c_id": "28400484458"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/video-subtitle", sandbase.Params{
	"a_id": "114006081739452",
	"c_id": "28400484458",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/video-subtitle` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `a_id` | string | yes | Video id  |
| `c_id` | string | yes | Video cid  |

## Details

Retrieve subtitle information for a Bilibili video by providing the video ID in `a_id` and the specific part CID in `c_id`.

### Use cases

- Extract caption tracks for video transcription and translation workflows.
- Display synchronized subtitles in custom video players.
- Inspect available subtitle languages and formats for a given video clip.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/video-subtitle" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"a_id": "114006081739452", "c_id": "28400484458"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `a_id` | string | Yes | Video id |
| `c_id` | string | Yes | Video cid |

### Notes

- Both `a_id` and `c_id` are required to pinpoint the exact video part.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/video-subtitle.json`](../../../../catalog/models/bilibili/web/video-subtitle.json) · Store page: https://www.sandbase.ai/model/bilibili/web/video-subtitle
