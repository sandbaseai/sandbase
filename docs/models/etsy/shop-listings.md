# Etsy Shop Listings API: pricing, parameters and code examples

`etsy/shop-listings` · data API · Etsy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0009 per call · **Modes:** sync

List one Etsy shop's active listings by shop name, a page at a time, and get title, price, original price and image for each listing in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0009**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "etsy/shop-listings", "shopName": "StudioStelleHD"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('etsy/shop-listings', {'shopName': 'StudioStelleHD'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("etsy/shop-listings", {
  "shopName": "StudioStelleHD"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "etsy/shop-listings", sandbase.Params{
	"shopName": "StudioStelleHD",
})
```

Same call via the path form: `POST /v1/api/etsy/shop-listings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-based results page of the shop's listings. Each page is billed as one request. default `1`; range 1–250 |
| `shopName` | string | yes | Etsy shop name, as in the shop URL (https://www.etsy.com/shop/<name>), e.g. StudioStelleHD. The Etsy Search and Etsy Product SKUs return it as shopName.  |

## Details

List one Etsy shop's active listings by shop name, a page at a time, and get title, price, original price and image for each listing in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "etsy/shop-listings", "shopName": "StudioStelleHD"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shopName` | string | Yes | Etsy shop name, as in the shop URL (https://www.etsy.com/shop/<name>), e.g. StudioStelleHD. The Etsy Search and Etsy Product SKUs return it as shopName. |
| `page` | integer | No | 1-based results page of the shop's listings. Each page is billed as one request. Default `1`. |

### Pricing

Billed at the actual cost of each call, about $0.0009 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/etsy/shop-listings.json`](../../../catalog/models/etsy/shop-listings.json) · Store page: https://www.sandbase.ai/model/etsy/shop-listings
