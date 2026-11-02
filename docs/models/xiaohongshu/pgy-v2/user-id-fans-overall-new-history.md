# Xiaohongshu Pugongying Follower Growth History API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/user-id-fans-overall-new-history` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.020833 per call · **Modes:** sync

Get Xiaohongshu Pugongying follower history for a creator over the selected 30- or 90-day period. Use it to track total followers or new-follower growth over time.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/user-id-fans-overall-new-history", "userId": "5a73c5fa4eacab4c4ccc9778"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/user-id-fans-overall-new-history', {'userId': '5a73c5fa4eacab4c4ccc9778'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/user-id-fans-overall-new-history", {
  "userId": "5a73c5fa4eacab4c4ccc9778"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/user-id-fans-overall-new-history", sandbase.Params{
	"userId": "5a73c5fa4eacab4c4ccc9778",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/user-id-fans-overall-new-history` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | KOL's user ID.  |
| `dateType` | string |  | Time range for data. one of: `DAY_30`, `DAY_90`; default `"DAY_30"` |
| `increaseType` | string |  | Type of growth data. one of: `FANS_TOTAL`, `FANS_INCREASE`; default `"FANS_TOTAL"` |

## Details

Get Xiaohongshu Pugongying follower history for a creator over the selected 30- or 90-day period. Use it to track total followers or new-follower growth over time.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/user-id-fans-overall-new-history" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "5a73c5fa4eacab4c4ccc9778"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | KOL's user ID. |
| `dateType` | string | No | Time range for data. |
| `increaseType` | string | No | Type of growth data. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/user-id-fans-overall-new-history.json`](../../../../catalog/models/xiaohongshu/pgy-v2/user-id-fans-overall-new-history.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/user-id-fans-overall-new-history
