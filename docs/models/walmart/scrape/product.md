# Walmart Product Page API: pricing, parameters and code examples

`walmart/scrape/product` · data API · Walmart · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Extract structured data from a Walmart product page URL: name, current and list price, stock, delivery estimate, ratings and seller details.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "walmart/scrape/product", "url": "https://www.walmart.com/ip/HP-14-Laptop/17581855155"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('walmart/scrape/product', {'url': 'https://www.walmart.com/ip/HP-14-Laptop/17581855155'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("walmart/scrape/product", {
  "url": "https://www.walmart.com/ip/HP-14-Laptop/17581855155"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "walmart/scrape/product", sandbase.Params{
	"url": "https://www.walmart.com/ip/HP-14-Laptop/17581855155",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/walmart/scrape/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Walmart page URL, e.g. https://www.walmart.com/ip/HP-14-Laptop/17581855155  |
| `country` | string |  | Walmart marketplace country code, e.g. 'us', 'ca', 'mx' (default 'us').  |
| `storeId` | string |  | Walmart store ID for localized inventory.  |
| `zipCode` | string |  | US zip code used to determine local product availability.  |

## Details

Extract structured data from a Walmart product page URL: name, current and list price, stock, delivery estimate, ratings and seller details.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/walmart/scrape/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.walmart.com/ip/HP-14-Laptop/17581855155"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Walmart page URL, e.g. https://www.walmart.com/ip/HP-14-Laptop/17581855155 |
| `country` | string | No | Walmart marketplace country code, e.g. 'us', 'ca', 'mx' (default 'us'). |
| `storeId` | string | No | Walmart store ID for localized inventory. |
| `zipCode` | string | No | US zip code used to determine local product availability. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/walmart/scrape/product.json`](../../../../catalog/models/walmart/scrape/product.json) · Store page: https://www.sandbase.ai/model/walmart/scrape/product
