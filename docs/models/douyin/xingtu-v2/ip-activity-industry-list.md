# Douyin Xingtu IP Activity Industry List API: pricing, parameters and code examples

`douyin/xingtu-v2/ip-activity-industry-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the list of supported industries for the Xingtu IP calendar on Douyin. Use this reference data to filter and categorize upcoming IP activities.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/ip-activity-industry-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/ip-activity-industry-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/ip-activity-industry-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/ip-activity-industry-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/ip-activity-industry-list` with the body above minus `model`.

## Details

Retrieves the industry taxonomy for the Xingtu IP calendar. This endpoint requires no input parameters and returns the complete industry reference list.

### Use cases

- Retrieve available industry options to populate search filters.
- Categorize IP activities on the Xingtu calendar by industry.
- Map internal industry classifications to Douyin Xingtu categories.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/ip-activity-industry-list" \
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
Machine-readable: [`catalog/models/douyin/xingtu-v2/ip-activity-industry-list.json`](../../../../catalog/models/douyin/xingtu-v2/ip-activity-industry-list.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/ip-activity-industry-list
