# Target Product API: pricing, parameters and code examples

`target/product` · data API · Target · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Fetch a Target.com product by URL and get title, price, brand, rating, description, and images in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "target/product", "url": "https://www.target.com/p/mr-coffee-12c-programmable-drip-coffee-maker-stainless-steel-finish/-/A-91863920"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('target/product', {'url': 'https://www.target.com/p/mr-coffee-12c-programmable-drip-coffee-maker-stainless-steel-finish/-/A-91863920'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("target/product", {
  "url": "https://www.target.com/p/mr-coffee-12c-programmable-drip-coffee-maker-stainless-steel-finish/-/A-91863920"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "target/product", sandbase.Params{
	"url": "https://www.target.com/p/mr-coffee-12c-programmable-drip-coffee-maker-stainless-steel-finish/-/A-91863920",
})
```

Same call via the path form: `POST /v1/api/target/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Target product page URL; the TCIN after /A- identifies the product (e.g. https://www.target.com/p/-/A-91863920).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `availability`, and it is served only by a source that returns every…  |

## Details

Fetch a Target.com product by URL and get title, price, brand, rating, description, and images in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "target/product", "url": "https://www.target.com/p/mr-coffee-12c-programmable-drip-coffee-maker-stainless-steel-finish/-/A-91863920"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Target product page URL; the TCIN after /A- identifies the product (e.g. https://www.target.com/p/-/A-91863920). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `availability`, and it is served only by a source that returns every o |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/target/product.json`](../../../catalog/models/target/product.json) · Store page: https://www.sandbase.ai/model/target/product
