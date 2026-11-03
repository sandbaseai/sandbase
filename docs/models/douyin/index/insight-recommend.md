# Douyin Recommended Insight Reports API: pricing, parameters and code examples

`douyin/index/insight-recommend` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended trend insight reports featured on the Douyin index home page. Useful for tracking high-level platform trends and discovering top reports without specifying filters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/insight-recommend"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/insight-recommend', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/insight-recommend", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/insight-recommend", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/insight-recommend` with the body above minus `model`.

## Details

Access recommended Douyin trend insight reports from the home page. This endpoint requires no query parameters to retrieve current platform recommendations.

### Use cases

- Discover trending industry insights and research topics on Douyin.
- Monitor featured analytical reports highlighted on the platform home page.
- Automate regular retrieval of platform-curated trend highlights.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/insight-recommend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/insight-recommend.json`](../../../../catalog/models/douyin/index/insight-recommend.json) · Store page: https://www.sandbase.ai/model/douyin/index/insight-recommend
