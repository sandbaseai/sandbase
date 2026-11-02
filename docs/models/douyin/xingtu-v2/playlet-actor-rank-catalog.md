# Douyin Xingtu Playlet Actor Rank Catalog API: pricing, parameters and code examples

`douyin/xingtu-v2/playlet-actor-rank-catalog` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the ranking catalog options for Douyin Xingtu playlet actors. Use this endpoint to inspect available categories and ranking classifications.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/playlet-actor-rank-catalog"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/playlet-actor-rank-catalog', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/playlet-actor-rank-catalog", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/playlet-actor-rank-catalog", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/playlet-actor-rank-catalog` with the body above minus `model`.

## Details

Access the available ranking catalog and classification categories for Douyin Xingtu playlet actors. This endpoint requires no request parameters.

### Use cases

- Discover available ranking categories for playlet actors on Xingtu.
- Map catalog identifiers prior to querying specific actor leaderboards.
- Keep local category definitions synchronized with Douyin Xingtu taxonomies.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/playlet-actor-rank-catalog" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/playlet-actor-rank-catalog.json`](../../../../catalog/models/douyin/xingtu-v2/playlet-actor-rank-catalog.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/playlet-actor-rank-catalog
