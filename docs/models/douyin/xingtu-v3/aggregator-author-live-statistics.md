# Douyin Xingtu Live Statistics

`douyin/xingtu-v3/aggregator-author-live-statistics` · api · Douyin

Get Douyin Creator Marketplace (Xingtu) live-stream statistics for a creator, with live-room, period, marketplace-order, and flow filters. Use it to compare live-streaming creators for campaign planning.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/aggregator-author-live-statistics", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/aggregator-author-live-statistics', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/aggregator-author-live-statistics", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/aggregator-author-live-statistics", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/aggregator-author-live-statistics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `period` | string |  | Live data time period. one of: `DAY_30`, `DAY_90` |
| `flowType` | string |  | Flow type filter. one of: `EXCLUDE`, `INCLUDE` |
| `liveType` | string |  | Live room type filter. one of: `ALL`, `GAME`, `ECOMMERCE`, `OTHER` |
| `oAuthorId` | string | yes | Author's unique ID.  |
| `onlyStarOrder` | boolean |  | Whether to include only Xingtu marketplace orders. default `false` |

## Details

Get Douyin Creator Marketplace (Xingtu) live-stream statistics for a creator, with live-room, period, marketplace-order, and flow filters. Use it to compare live-streaming creators for campaign planning.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/aggregator-author-live-statistics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `liveType` | string | No | Live room type filter. |
| `period` | string | No | Live data time period. |
| `onlyStarOrder` | boolean | No | Whether to include only Xingtu marketplace orders. |
| `flowType` | string | No | Flow type filter. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/aggregator-author-live-statistics.json`](../../../../catalog/models/douyin/xingtu-v3/aggregator-author-live-statistics.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/aggregator-author-live-statistics
