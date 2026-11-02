# Douyin Xingtu Creator Contract Base Info API: pricing, parameters and code examples

`douyin/xingtu-v3/aggregator-author-contract-base-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.020833 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) contract-related baseline information for a creator over a selectable 30- or 90-day period. Use it to review creator contract context during campaign planning.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/aggregator-author-contract-base-info", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/aggregator-author-contract-base-info', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/aggregator-author-contract-base-info", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/aggregator-author-contract-base-info", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/aggregator-author-contract-base-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `range` | string |  | Time range. one of: `DAY_30`, `DAY_90` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Get Douyin Creator Marketplace (Xingtu) contract-related baseline information for a creator over a selectable 30- or 90-day period. Use it to review creator contract context during campaign planning.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/aggregator-author-contract-base-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `range` | string | No | Time range. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/aggregator-author-contract-base-info.json`](../../../../catalog/models/douyin/xingtu-v3/aggregator-author-contract-base-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/aggregator-author-contract-base-info
