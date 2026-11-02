# Douyin Hot Challenge Billboard API: pricing, parameters and code examples

`douyin/creator/creator-hot-challenge-billboard` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending challenge billboard rankings directly from Douyin. Discover active community challenges and monitor popular campaign topics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-hot-challenge-billboard"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-hot-challenge-billboard', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-hot-challenge-billboard", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-hot-challenge-billboard", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-hot-challenge-billboard` with the body above minus `model`.

## Details

Retrieves the latest hot challenge billboard rankings from Douyin without requiring additional query parameters.

### Use cases

- Track trending Douyin challenges to guide video content strategy.
- Analyze rising hashtag themes across the Douyin ecosystem.
- Identify viral community challenges for influencer collaboration opportunities.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-hot-challenge-billboard" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Creator Activity Details](/model/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/model/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/model/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-hot-challenge-billboard.json`](../../../../catalog/models/douyin/creator/creator-hot-challenge-billboard.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-hot-challenge-billboard
