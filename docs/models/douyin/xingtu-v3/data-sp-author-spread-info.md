# Douyin Xingtu Spread Metrics

`douyin/xingtu-v3/data-sp-author-spread-info` · api · Douyin

Get Douyin Creator Marketplace (Xingtu) spread metrics for a creator, with channel, period, video-type, assignment, and flow filters. Use it to compare creator spread performance during campaign planning.

## Pricing

- **$0.069444 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-spread-info", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-spread-info', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-spread-info", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-spread-info", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-spread-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | string |  | Video type. one of: `PERSONAL_VIDEO`, `XINTU_VIDEO`; default `"PERSONAL_VIDEO"` |
| `range` | string |  | Time range. one of: `DAY_30`, `DAY_90`; default `"DAY_30"` |
| `flowType` | string |  | Flow type filter. one of: `EXCLUDE`, `INCLUDE`; default `"EXCLUDE"` |
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |
| `onlyAssign` | boolean |  | Whether to only include assigned videos. default `false` |

## Details

Get Douyin Creator Marketplace (Xingtu) spread metrics for a creator, with channel, period, video-type, assignment, and flow filters. Use it to compare creator spread performance during campaign planning.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-spread-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `platform` | string | No | Platform type. |
| `range` | string | No | Time range. |
| `type` | string | No | Video type. |
| `onlyAssign` | boolean | No | Whether to only include assigned videos. |
| `flowType` | string | No | Flow type filter. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-spread-info.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-spread-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-spread-info
