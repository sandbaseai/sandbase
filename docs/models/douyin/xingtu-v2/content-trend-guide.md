# Douyin Xingtu Content Trend Guide

`douyin/xingtu-v2/content-trend-guide` · api · Douyin

Returns content trend guide data from Douyin Xingtu via static CDN JSON. Provides insights into trending content directions without requiring session cookies.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/content-trend-guide"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/content-trend-guide', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/content-trend-guide", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/content-trend-guide", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/content-trend-guide` with the body above minus `model`.

## Details

Access static content trend guide data directly from Douyin Xingtu. This endpoint requires no input parameters or session cookies.

### Use cases

- Analyze trending content directions on Douyin Xingtu.
- Guide creative video production using official trend data.
- Monitor shifting content topics without maintaining session cookies.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/content-trend-guide" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Notes

- Delivered as static JSON from a CDN with no cookie requirement.
- No query parameters are required.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/content-trend-guide.json`](../../../../catalog/models/douyin/xingtu-v2/content-trend-guide.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/content-trend-guide
