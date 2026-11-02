# Douyin Video Search Filter Options API: pricing, parameters and code examples

`douyin/index/item-filter-options` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns all supported filter options and permissible values for Douyin video search queries. Use these criteria to construct structured search requests.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/item-filter-options"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/item-filter-options', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/item-filter-options", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/item-filter-options", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/item-filter-options` with the body above minus `model`.

## Details

Look up supported filter options for Douyin video search queries. This endpoint requires no parameters and returns valid criteria compatible with `fetch_item_query`.

### Use cases

- Retrieve valid filter criteria for Douyin video searches.
- Populate filter dropdowns and selections in video search interfaces.
- Validate video search arguments against accepted platform values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/item-filter-options" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Notes

- Provides filter criteria designed for use with the `fetch_item_query` video search endpoint.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/item-filter-options.json`](../../../../catalog/models/douyin/index/item-filter-options.json) · Store page: https://www.sandbase.ai/model/douyin/index/item-filter-options
