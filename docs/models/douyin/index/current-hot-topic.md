# Douyin Current Hot Topics Leaderboard

`douyin/index/current-hot-topic` · api · Douyin

Returns Douyin real-time hot topics and the trending topics leaderboard. Use this endpoint to observe currently viral subjects and platform-wide discussions.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/current-hot-topic"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/current-hot-topic', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/current-hot-topic", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/current-hot-topic", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/current-hot-topic` with the body above minus `model`.

## Details

Retrieves the real-time leaderboard of trending topics on Douyin without requiring any input parameters.

### Use cases

- Track viral Douyin trends and real-time hot topics.
- Analyze platform-wide audience interests and trending themes.
- Monitor emerging discussions across Douyin leaderboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/current-hot-topic" \
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
Machine-readable: [`catalog/models/douyin/index/current-hot-topic.json`](../../../../catalog/models/douyin/index/current-hot-topic.json) · Store page: https://www.sandbase.ai/model/douyin/index/current-hot-topic
