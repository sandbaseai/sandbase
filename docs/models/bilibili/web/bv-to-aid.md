# Bilibili BV to AID Converter API: pricing, parameters and code examples

`bilibili/web/bv-to-aid` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Converts a Bilibili BV identifier to its corresponding numeric AID value. Input the target video BV string to return the legacy video identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/bv-to-aid", "bv_id": "BV1M1421t7hT"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/bv-to-aid', {'bv_id': 'BV1M1421t7hT'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/bv-to-aid", {
  "bv_id": "BV1M1421t7hT"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/bv-to-aid", sandbase.Params{
	"bv_id": "BV1M1421t7hT",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/bv-to-aid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bv_id` | string | yes | Video id  |

## Details

Convert a Bilibili video BV identifier to its corresponding numeric AID using `bv_id`. This enables mapping between alphanumeric and numeric video identifiers.

### Use cases

- Look up the numeric AID for legacy Bilibili endpoints requiring numeric identifiers.
- Convert modern BV alphanumeric strings into corresponding AID integers.
- Bridge data pipelines that index Bilibili videos by numeric AID instead of BV format.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/bv-to-aid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bv_id": "BV1M1421t7hT"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bv_id` | string | Yes | Video id |

### Notes

- Supply a valid video string via `bv_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.
- [Bilibili Comprehensive Popular Videos](/apis/bilibili/web/com-popular): Returns a comprehensive list of trending videos on Bilibili, including video metadata, author details, and engagement statistics across pages.

---
Machine-readable: [`catalog/models/bilibili/web/bv-to-aid.json`](../../../../catalog/models/bilibili/web/bv-to-aid.json) · Store page: https://www.sandbase.ai/model/bilibili/web/bv-to-aid
