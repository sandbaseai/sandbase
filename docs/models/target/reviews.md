# Target Reviews API: pricing, parameters and code examples

`target/reviews` · data API · Target · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Pull a page of 10 customer reviews for any Target.com product by URL, newest first or by helpfulness or rating: rating, title, text, date, reviewer, and verified-buyer badge.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "target/reviews", "url": "https://www.target.com/p/mr-coffee-12c-programmable-drip-coffee-maker-stainless-steel-finish/-/A-91863920"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('target/reviews', {'url': 'https://www.target.com/p/mr-coffee-12c-programmable-drip-coffee-maker-stainless-steel-finish/-/A-91863920'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("target/reviews", {
  "url": "https://www.target.com/p/mr-coffee-12c-programmable-drip-coffee-maker-stainless-steel-finish/-/A-91863920"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "target/reviews", sandbase.Params{
	"url": "https://www.target.com/p/mr-coffee-12c-programmable-drip-coffee-maker-stainless-steel-finish/-/A-91863920",
})
```

Same call via the path form: `POST /v1/api/target/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Target product page URL; the TCIN after /A- identifies the product (e.g. https://www.target.com/p/-/A-91863920).  |
| `page` | integer |  | 1-based page of 10 reviews. Each page is billed as one request; keep url and sort the same while walking pages. default `1`; range 1– |
| `sort` | string |  | Review order: recent (newest first, the default), helpful, rating_high, or rating_low (e.g. helpful). one of: `recent`, `helpful`, `rating_high`, `rating_low`; default `"recent"` |

## Details

Pull a page of 10 customer reviews for any Target.com product by URL, newest first or by helpfulness or rating: rating, title, text, date, reviewer, and verified-buyer badge.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "target/reviews", "url": "https://www.target.com/p/mr-coffee-12c-programmable-drip-coffee-maker-stainless-steel-finish/-/A-91863920"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Target product page URL; the TCIN after /A- identifies the product (e.g. https://www.target.com/p/-/A-91863920). |
| `page` | integer | No | 1-based page of 10 reviews. Each page is billed as one request; keep url and sort the same while walking pages. Default `1`. |
| `sort` | string | No | Review order: recent (newest first, the default), helpful, rating_high, or rating_low (e.g. helpful). One of: `recent`, `helpful`, `rating_high`, `rating_low`. |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/target/reviews.json`](../../../catalog/models/target/reviews.json) · Store page: https://www.sandbase.ai/model/target/reviews
