# Douyin Brand Hot Videos Time Scope API: pricing, parameters and code examples

`douyin/index/brand-hot-videos-time-scope` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the queryable time scope for Douyin brand hot videos. Allows systems to check valid date ranges before querying related brand analytics endpoints.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/brand-hot-videos-time-scope"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/brand-hot-videos-time-scope', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/brand-hot-videos-time-scope", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/brand-hot-videos-time-scope", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/brand-hot-videos-time-scope` with the body above minus `model`.

## Details

Retrieves the allowed date boundaries for the brand hot videos feature. This endpoint takes no input parameters and establishes valid time windows for subsequent brand queries.

### Use cases

- Check supported date boundaries before querying brand hot video metrics.
- Synchronize analytical calendar controls with valid platform data windows.
- Prevent date out-of-range errors in automated reporting workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/brand-hot-videos-time-scope" \
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
Machine-readable: [`catalog/models/douyin/index/brand-hot-videos-time-scope.json`](../../../../catalog/models/douyin/index/brand-hot-videos-time-scope.json) · Store page: https://www.sandbase.ai/model/douyin/index/brand-hot-videos-time-scope
