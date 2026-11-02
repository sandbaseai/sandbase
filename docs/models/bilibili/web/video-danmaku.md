# Bilibili Video Danmaku API: pricing, parameters and code examples

`bilibili/web/video-danmaku` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns timed on-screen danmaku comments for a specified Bilibili video in XML format using the video content identifier (cid).

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/video-danmaku", "cid": "1639235405"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/video-danmaku', {'cid': '1639235405'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/video-danmaku", {
  "cid": "1639235405"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/video-danmaku", sandbase.Params{
	"cid": "1639235405",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/video-danmaku` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cid` | string | yes | Video cid  |

## Details

Look up timed danmaku (bullet comments) for any Bilibili video part by providing its `cid`.

### Use cases

- Analyze audience sentiment and real-time reactions across specific video timestamps.
- Archive bullet comments alongside video content for offline playback or research.
- Detect high-engagement video moments where danmaku density peaks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/video-danmaku" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cid": "1639235405"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cid` | string | Yes | Video cid |

### Notes

- Requires the video `cid` (content ID), which represents a specific video part or episode.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/video-danmaku.json`](../../../../catalog/models/bilibili/web/video-danmaku.json) · Store page: https://www.sandbase.ai/model/bilibili/web/video-danmaku
