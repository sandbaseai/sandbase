# Walmart Product API: pricing, parameters and code examples

`walmart/product` · data API · Walmart · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.001 per call · **Modes:** sync

Fetch a Walmart product page by URL and get full product details (title, price, availability, ratings, images, and specs) in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.001**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "walmart/product", "url": "https://www.walmart.com/ip/Apple-AirPods-Pro-2/5689919121"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('walmart/product', {'url': 'https://www.walmart.com/ip/Apple-AirPods-Pro-2/5689919121'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("walmart/product", {
  "url": "https://www.walmart.com/ip/Apple-AirPods-Pro-2/5689919121"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "walmart/product", sandbase.Params{
	"url": "https://www.walmart.com/ip/Apple-AirPods-Pro-2/5689919121",
})
```

Same call via the path form: `POST /v1/api/walmart/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Walmart product page URL.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `productId`, and it is served only by a source that returns every…  |

## Details

Fetch a Walmart product page by URL and get full product details (title, price, availability, ratings, images, and specs) in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "walmart/product", "url": "https://www.walmart.com/ip/Apple-AirPods-Pro-2/5689919121"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Walmart product page URL. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `productId`, and it is served only by a source that returns every one  |

### Pricing

Billed at the actual cost of each call, about $0.001 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/walmart/product.json`](../../../catalog/models/walmart/product.json) · Store page: https://www.sandbase.ai/model/walmart/product
