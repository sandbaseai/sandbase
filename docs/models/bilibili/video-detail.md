# Bilibili Video Details API: pricing, parameters and code examples

`bilibili/video-detail` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get details for a Bilibili video identified by its BVID. Use it to look up a known video for content review, cataloging, or subsequent engagement analysis.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/video-detail", "bvid": "BV1GJ411x7h7"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/video-detail', {'bvid': 'BV1GJ411x7h7'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/video-detail", {
  "bvid": "BV1GJ411x7h7"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/video-detail", sandbase.Params{
	"bvid": "BV1GJ411x7h7",
})
```

Same call via the path form: `POST /v1/api/bilibili/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bvid` | string | yes | Bilibili Video ID (BVID).  |

## Details

Get details for a Bilibili video identified by its BVID. Use it to look up a known video for content review, cataloging, or subsequent engagement analysis.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bvid": "BV1GJ411x7h7"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bvid` | string | Yes | Bilibili Video ID (BVID). |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/bilibili/video-detail.json`](../../../catalog/models/bilibili/video-detail.json) · Store page: https://www.sandbase.ai/model/bilibili/video-detail
