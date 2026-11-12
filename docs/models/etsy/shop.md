# Etsy Shop API: pricing, parameters and code examples

`etsy/shop` · data API · Etsy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0009 per call · **Modes:** sync

Look up one Etsy shop by name and get its id, location, sales, active listings, rating, reviews count, followers, description, logo and banner in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0009**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "etsy/shop", "shopName": "StudioStelleHD"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('etsy/shop', {'shopName': 'StudioStelleHD'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("etsy/shop", {
  "shopName": "StudioStelleHD"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "etsy/shop", sandbase.Params{
	"shopName": "StudioStelleHD",
})
```

Same call via the path form: `POST /v1/api/etsy/shop` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `shopName` | string | yes | Etsy shop name, as in the shop URL (https://www.etsy.com/shop/<name>), e.g. StudioStelleHD. The Etsy Search and Etsy Product SKUs return it as shopName.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `followers`, and it is served only by a source that returns every…  |

## Details

Look up one Etsy shop by name and get its id, location, sales, active listings, rating, reviews count, followers, description, logo and banner in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "etsy/shop", "shopName": "StudioStelleHD"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shopName` | string | Yes | Etsy shop name, as in the shop URL (https://www.etsy.com/shop/<name>), e.g. StudioStelleHD. The Etsy Search and Etsy Product SKUs return it as shopName. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `followers`, and it is served only by a source that returns every one  |

### Pricing

Billed at the actual cost of each call, about $0.0009 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/etsy/shop.json`](../../../catalog/models/etsy/shop.json) · Store page: https://www.sandbase.ai/model/etsy/shop
