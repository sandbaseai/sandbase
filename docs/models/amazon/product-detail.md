# Amazon Product Details API: pricing, parameters and code examples

`amazon/product-detail` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get details for an Amazon product identified by ASIN in a selected country marketplace. Use it to look up a known listing for catalog review, product comparison, or downstream commerce analysis.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/product-detail", "asin": "B0D1XD1ZV3"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/product-detail', {'asin': 'B0D1XD1ZV3'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/product-detail", {
  "asin": "B0D1XD1ZV3"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/product-detail", sandbase.Params{
	"asin": "B0D1XD1ZV3",
})
```

Same call via the path form: `POST /v1/api/amazon/product-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `asin` | string | yes | ASIN (Amazon Standard Identification Number).  |
| `country` | string |  | Country code for the Amazon product. one of: `US`, `AU`, `BR`, `CA`, `CN`, `FR`, `DE`, `IN`, `IT`, `MX`, `NL`, `SG` …; default `"US"` |

## Details

Get details for an Amazon product identified by ASIN in a selected country marketplace. Use it to look up a known listing for catalog review, product comparison, or downstream commerce analysis.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/amazon/product-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin": "B0D1XD1ZV3"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `asin` | string | Yes | ASIN (Amazon Standard Identification Number). |
| `country` | string | No | Country code for the Amazon product. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/amazon/product-detail.json`](../../../catalog/models/amazon/product-detail.json) · Store page: https://www.sandbase.ai/model/amazon/product-detail
