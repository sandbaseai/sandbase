# Douyin Hot Topic Detail Analysis API: pricing, parameters and code examples

`douyin/index/hot-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comprehensive trend analysis metrics for a specified Douyin hot topic. Requires a topic name sourced from the hot topic list.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/hot-detail", "topic_name": "请三休十三的人现在都到哪里了"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/hot-detail', {'topic_name': '请三休十三的人现在都到哪里了'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/hot-detail", {
  "topic_name": "请三休十三的人现在都到哪里了"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/hot-detail", sandbase.Params{
	"topic_name": "请三休十三的人现在都到哪里了",
})
```

Same call via the path form: `POST /v1/api/douyin/index/hot-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `topic_name` | string | yes | Hot topic name, obtained from fetch_current_hot_topic results  |

## Details

Access in-depth index analysis for a trending Douyin subject by passing `topic_name`. It delivers detailed engagement and trend metrics for performance tracking.

### Use cases

- Inspect detailed index metrics for a specific Douyin trending topic.
- Analyze performance trends for subjects surfaced on hot topic lists.
- Evaluate audience interest around popular topics for content planning.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/hot-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"topic_name": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `topic_name` | string | Yes | Hot topic name, obtained from fetch_current_hot_topic results |

### Notes

- Provide `topic_name` obtained from the current hot topic list results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/hot-detail.json`](../../../../catalog/models/douyin/index/hot-detail.json) · Store page: https://www.sandbase.ai/model/douyin/index/hot-detail
