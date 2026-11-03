# Bilibili Web Video Details API: pricing, parameters and code examples

`bilibili/web/video-detail` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata, season sections, and episode listings for a specific Bilibili video using its unique video identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/video-detail", "aid": "114902186396822"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/video-detail', {'aid': '114902186396822'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/video-detail", {
  "aid": "114902186396822"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/video-detail", sandbase.Params{
	"aid": "114902186396822",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aid` | string | yes | Video id  |

## Details

Access detailed metadata and episode sections for a Bilibili video by providing the target `aid`.

### Use cases

- Retrieve full video information including episode lists and season metadata.
- Extract release timestamps and duration metrics for specific video items.
- Inspect UGC season structure and chapter breakdowns for long-form content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aid": "114902186396822"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aid` | string | Yes | Video id |

### Notes

- Requires `aid`, representing the numeric Bilibili video identifier.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/video-detail.json`](../../../../catalog/models/bilibili/web/video-detail.json) · Store page: https://www.sandbase.ai/model/bilibili/web/video-detail
