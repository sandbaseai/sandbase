# AliExpress Product Search API: pricing, parameters and code examples

`aliexpress/search/products` · data API · AliExpress · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Search AliExpress products by keyword with sort, category, brand, price, locale, region and currency filters.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aliexpress/search/products"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aliexpress/search/products', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aliexpress/search/products", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aliexpress/search/products", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/aliexpress/search/products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Product search query.  |
| `loc` | string |  | Location filter for product search results.  |
| `attr` | string |  | Product attribute filter for search results.  |
| `page` | string |  | One-based page number for pagination.  |
| `sort` | string |  | Sort order for product search results. one of: `default`, `salesDesc`, `priceAsc`, `priceDesc`; default `"default"` |
| `catId` | string |  | Category ID used to filter product search results.  |
| `locale` | string |  | Locale used for the AliExpress response.  |
| `region` | string |  | AliExpress marketplace region.  |
| `brandId` | string |  | Brand ID used to filter product search results.  |
| `currency` | string |  | Currency code used for product prices.  |
| `endPrice` | number |  | Maximum product price filter, inclusive.  |
| `switches` | string |  | Search switches used to select optional result features.  |
| `startPrice` | number |  | Minimum product price filter, inclusive.  |

## Details

Search AliExpress products by keyword with sort, category, brand, price, locale, region and currency filters.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aliexpress/search/products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "phone case"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | No | Product search query. |
| `page` | string | No | One-based page number for pagination. |
| `sort` | string | No | Sort order for product search results. |
| `catId` | string | No | Category ID used to filter product search results. |
| `brandId` | string | No | Brand ID used to filter product search results. |
| `loc` | string | No | Location filter for product search results. |
| `switches` | string | No | Search switches used to select optional result features. |
| `attr` | string | No | Product attribute filter for search results. |
| `startPrice` | number | No | Minimum product price filter, inclusive. |
| `endPrice` | number | No | Maximum product price filter, inclusive. |
| `locale` | string | No | Locale used for the AliExpress response. |
| `region` | string | No | AliExpress marketplace region. |
| `currency` | string | No | Currency code used for product prices. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/aliexpress/search/products.json`](../../../../catalog/models/aliexpress/search/products.json) · Store page: https://www.sandbase.ai/model/aliexpress/search/products
