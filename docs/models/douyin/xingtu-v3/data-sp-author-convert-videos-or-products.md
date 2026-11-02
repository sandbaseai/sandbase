# Douyin Xingtu Conversion Resources API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-author-convert-videos-or-products` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.020833 per call · **Modes:** sync

List Douyin Creator Marketplace (Xingtu) conversion-related videos or products for a creator, with industry, period, resource-type, and page filters. Use it to review commerce examples before creator selection.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-convert-videos-or-products", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-convert-videos-or-products', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-convert-videos-or-products", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-convert-videos-or-products", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-convert-videos-or-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number. default `1` |
| `range` | string |  | Time range. one of: `DAY_30`, `DAY_90`; default `"DAY_30"` |
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |
| `detailType` | string |  | Resource type. one of: `VIDEO`, `PRODUCT`; default `"VIDEO"` |
| `industryId` | string |  | Industry category. one of: `ALL`, `ELECTRONICS_AND_APPLIANCES`, `SHOPPING`, `FOOD_AND_BEVERAGE`, `CLOTHING_AND_ACCESSORIES`, `HEALTHCARE_AND_MEDICAL`, `MEDICAL_INSTITUTIONS`, `HOME_AND_BUILDING_MATERIALS`, `LOCAL_SERVICES`, `BUSINESS_SERVICES`, `CULTURE_SPORTS_ENTERTAINMENT`, `BEAUTY_SERVICES` …; default `"ALL"` |

## Details

List Douyin Creator Marketplace (Xingtu) conversion-related videos or products for a creator, with industry, period, resource-type, and page filters. Use it to review commerce examples before creator selection.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-convert-videos-or-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `platform` | string | No | Platform type. |
| `industryId` | string | No | Industry category. |
| `range` | string | No | Time range. |
| `detailType` | string | No | Resource type. |
| `page` | integer | No | Page number. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-convert-videos-or-products.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-convert-videos-or-products.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-convert-videos-or-products
