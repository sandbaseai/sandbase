# Douyin Content Guide Valid Dates API: pricing, parameters and code examples

`douyin/index/content-valid-date` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the valid date ranges supported by the Douyin content guide index. Helps clients determine allowable date intervals before requesting trend and guide statistics.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/content-valid-date"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/content-valid-date', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/content-valid-date", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/content-valid-date", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/content-valid-date` with the body above minus `model`.

## Details

Returns valid date ranges for Douyin content index records without requiring query parameters.

### Use cases

- Check allowable date intervals before querying content index metrics.
- Configure date pickers for Douyin content guide dashboards.
- Verify active historical time spans supported by the content guide.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-valid-date" \
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
Machine-readable: [`catalog/models/douyin/index/content-valid-date.json`](../../../../catalog/models/douyin/index/content-valid-date.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-valid-date
