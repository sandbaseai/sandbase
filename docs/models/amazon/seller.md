# Amazon Seller API: pricing, parameters and code examples

`amazon/seller` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Look up one Amazon seller by seller ID and get its name, star rating, positive feedback percentage, feedback counts for the last 30 days, 90 days, 12 months and lifetime, and its registered business name and address in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/seller", "sellerId": "A11V4PRB7HXYNG"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/seller', {'sellerId': 'A11V4PRB7HXYNG'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/seller", {
  "sellerId": "A11V4PRB7HXYNG"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/seller", sandbase.Params{
	"sellerId": "A11V4PRB7HXYNG",
})
```

Same call via the path form: `POST /v1/api/amazon/seller` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Amazon marketplace to read, as its domain (e.g. amazon.co.uk); omit it for amazon.com. one of: `amazon.com`, `amazon.co.uk`, `amazon.de`, `amazon.fr`, `amazon.it`, `amazon.es`, `amazon.nl`, `amazon.se`, `amazon.pl`, `amazon.ca`, `amazon.com.mx`, `amazon.com.br` … |
| `sellerId` | string | yes | Amazon seller ID, the value after seller= in a seller page URL (https://www.amazon.com/sp?seller=<id>), e.g. A11V4PRB7HXYNG.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `businessName`, and it is served only by a source that returns every…  |

## Details

Look up one Amazon seller by seller ID and get its name, star rating, positive feedback percentage, feedback counts for the last 30 days, 90 days, 12 months and lifetime, and its registered business name and address in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "amazon/seller", "sellerId": "A11V4PRB7HXYNG"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sellerId` | string | Yes | Amazon seller ID, the value after seller= in a seller page URL (https://www.amazon.com/sp?seller=<id>), e.g. A11V4PRB7HXYNG. |
| `region` | string | No | Amazon marketplace to read, as its domain (e.g. amazon.co.uk); omit it for amazon.com. One of: `amazon.com`, `amazon.co.uk`, `amazon.de`, `amazon.fr`, `amazon.it`, `amazon.es`, `amazon.nl`, `amazon.se`, `amazon.pl`, `ama |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `businessName`, and it is served only by a source that returns every o |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/amazon/seller.json`](../../../catalog/models/amazon/seller.json) · Store page: https://www.sandbase.ai/model/amazon/seller
