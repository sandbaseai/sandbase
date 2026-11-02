# Douyin Relation Analysis Valid Dates API: pricing, parameters and code examples

`douyin/index/valid-date-for-relation` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the valid date range available for relation analysis on Douyin. Use this endpoint to discover supported timeframes before requesting relationship metrics.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/valid-date-for-relation"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/valid-date-for-relation', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/valid-date-for-relation", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/valid-date-for-relation", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/valid-date-for-relation` with the body above minus `model`.

## Details

This endpoint returns the available date range for Douyin relation analysis. Call it to verify supported date boundaries before querying relation index metrics.

### Use cases

- Check supported date windows before requesting relation metrics.
- Validate user-selected date ranges in relation analytics dashboards.
- Keep automated data pipelines aligned with platform data availability boundaries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/valid-date-for-relation" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/valid-date-for-relation.json`](../../../../catalog/models/douyin/index/valid-date-for-relation.json) · Store page: https://www.sandbase.ai/model/douyin/index/valid-date-for-relation
