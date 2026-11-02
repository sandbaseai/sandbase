# Amazon Best Sellers API: pricing, parameters and code examples

`amazon/best-sellers` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get the Amazon Best Sellers list for a category path in a chosen marketplace country, with rank, title, price, rating and ASIN, page by page.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/best-sellers", "category": "electronics"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/best-sellers', {'category': 'electronics'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/best-sellers", {
  "category": "electronics"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/best-sellers", sandbase.Params{
	"category": "electronics",
})
```

Same call via the path form: `POST /v1/api/amazon/best-sellers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `country` | string |  | Country code for the Amazon product. one of: `US`, `AU`, `BR`, `CA`, `CN`, `FR`, `DE`, `IN`, `IT`, `MX`, `NL`, `SG` …; default `"US"` |
| `category` | string | yes | Best Sellers category path taken from an Amazon Best Sellers URL. It may be a category slug or a nested category path.  |

## Details

Get the Amazon Best Sellers list for a category path in a chosen marketplace country, with rank, title, price, rating and ASIN, page by page.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/amazon/best-sellers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category": "electronics"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | Yes | Best Sellers category path taken from an Amazon Best Sellers URL. It may be a category slug or a nested category path. |
| `country` | string | No | Country code for the Amazon product. |
| `page` | integer | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/amazon/best-sellers.json`](../../../catalog/models/amazon/best-sellers.json) · Store page: https://www.sandbase.ai/model/amazon/best-sellers
