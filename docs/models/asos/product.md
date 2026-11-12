# ASOS Product API: pricing, parameters and code examples

`asos/product` · data API · ASOS · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0009 per call · **Modes:** sync

Fetch an ASOS product by URL from any of its 11 country stores and get title, price, brand, colour, description, images, and per-size stock in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0009**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "asos/product", "url": "https://www.asos.com/pullbear/pullbear-casual-trainers-in-white/prd/211299341"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('asos/product', {'url': 'https://www.asos.com/pullbear/pullbear-casual-trainers-in-white/prd/211299341'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("asos/product", {
  "url": "https://www.asos.com/pullbear/pullbear-casual-trainers-in-white/prd/211299341"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "asos/product", sandbase.Params{
	"url": "https://www.asos.com/pullbear/pullbear-casual-trainers-in-white/prd/211299341",
})
```

Same call via the path form: `POST /v1/api/asos/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | ASOS product page URL, e.g. https://www.asos.com/pullbear/pullbear-casual-trainers-in-white/prd/211299341, or the short form https://www.asos.com/prd/211299341. The store is read from the URL path (/us/, /au/, /de/ and…  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `sizeGuide`, and it is served only by a source that returns every…  |

## Details

Fetch an ASOS product by URL from any of its 11 country stores and get title, price, brand, colour, description, images, and per-size stock in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "asos/product", "url": "https://www.asos.com/pullbear/pullbear-casual-trainers-in-white/prd/211299341"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | ASOS product page URL, e.g. https://www.asos.com/pullbear/pullbear-casual-trainers-in-white/prd/211299341, or the short form https://www.asos.com/prd/211299341. The store is read from the URL path (/us/, /au/, /de/ and s |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `sizeGuide`, and it is served only by a source that returns every one  |

### Pricing

Billed at the actual cost of each call, about $0.0009 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/asos/product.json`](../../../catalog/models/asos/product.json) · Store page: https://www.sandbase.ai/model/asos/product
