# Bilibili Streaming Areas API: pricing, parameters and code examples

`bilibili/web/all-live-areas` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the complete list of streaming broadcast areas and categories on Bilibili. This endpoint provides category identifiers and partition structures without requiring any parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/all-live-areas"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/all-live-areas', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/all-live-areas", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/all-live-areas", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/bilibili/web/all-live-areas` with the body above minus `model`.

## Details

Retrieve the complete directory of streaming partitions and categories across Bilibili. This request takes no query parameters and returns the platform's current broadcast hierarchy.

### Use cases

- Explore available streaming partitions and categories across Bilibili.
- Map streaming area identifiers to their corresponding category labels.
- Populate category filters and navigation menus for streaming discovery.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/all-live-areas" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.
- [Bilibili Comprehensive Popular Videos](/model/bilibili/web/com-popular): Returns a comprehensive list of trending videos on Bilibili, including video metadata, author details, and engagement statistics across pages.

---
Machine-readable: [`catalog/models/bilibili/web/all-live-areas.json`](../../../../catalog/models/bilibili/web/all-live-areas.json) · Store page: https://www.sandbase.ai/model/bilibili/web/all-live-areas
