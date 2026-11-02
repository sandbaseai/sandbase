# Douyin Content Categories API: pricing, parameters and code examples

`douyin/creator/creator-content-category` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the list of content categories available on Douyin. Authors and applications can review official topic classifications without requiring input parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-content-category"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-content-category', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-content-category", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-content-category", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-content-category` with the body above minus `model`.

## Details

Retrieve the list of Douyin video categories for account tagging. This endpoint requires no query parameters to fetch the classification directory.

### Use cases

- Classify video topics according to official Douyin taxonomy.
- Populate category selection menus inside analytics dashboards.
- Map Douyin classification tags across external media platforms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-content-category" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Creator Activity Details](/model/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/model/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Creator Content Courses](/model/douyin/creator/creator-content-course): Returns content development courses from the Douyin creator platform for a specified category.

---
Machine-readable: [`catalog/models/douyin/creator/creator-content-category.json`](../../../../catalog/models/douyin/creator/creator-content-category.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-content-category
