# Douyin Xingtu Creator Link Metrics API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-author-link-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) creator-link metrics for a specified creator, content channel, and industry category. Use it to review creator link information in an industry context.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-link-info", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-link-info', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-link-info", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-link-info", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-link-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |
| `industryTag` | string |  | Industry tag. one of: `ALL`, `ELECTRONICS_AND_APPLIANCES`, `SHOPPING`, `FOOD_AND_BEVERAGE`, `CLOTHING_AND_ACCESSORIES`, `HEALTHCARE_AND_MEDICAL`, `MEDICAL_INSTITUTIONS`, `HOME_AND_BUILDING_MATERIALS`, `LOCAL_SERVICES`, `BUSINESS_SERVICES`, `CULTURE_SPORTS_ENTERTAINMENT`, `BEAUTY_SERVICES` …; default `"ALL"` |

## Details

Get Douyin Creator Marketplace (Xingtu) creator-link metrics for a specified creator, content channel, and industry category. Use it to review creator link information in an industry context.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-link-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `platform` | string | No | Platform type. |
| `industryTag` | string | No | Industry tag. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-link-info.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-link-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-link-info
