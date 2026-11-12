# Sam's Club Product API: pricing, parameters and code examples

`sams-club/product` · data API · Sam's Club · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00319 per call · **Modes:** sync

Fetch a SamsClub.com product by URL and get title, member price, stock, brand, model, UPC, rating, description, and images in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00319**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sams-club/product", "url": "https://www.samsclub.com/ip/Bounty-Select-A-Size-2-Ply-Paper-Towels-12-Rolls-110-sheets-roll/18040450426"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('sams-club/product', {'url': 'https://www.samsclub.com/ip/Bounty-Select-A-Size-2-Ply-Paper-Towels-12-Rolls-110-sheets-roll/18040450426'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("sams-club/product", {
  "url": "https://www.samsclub.com/ip/Bounty-Select-A-Size-2-Ply-Paper-Towels-12-Rolls-110-sheets-roll/18040450426"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "sams-club/product", sandbase.Params{
	"url": "https://www.samsclub.com/ip/Bounty-Select-A-Size-2-Ply-Paper-Towels-12-Rolls-110-sheets-roll/18040450426",
})
```

Same call via the path form: `POST /v1/api/sams-club/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Sam's Club product page URL, e.g. https://www.samsclub.com/ip/Bounty-Select-A-Size-2-Ply-Paper-Towels-12-Rolls-110-sheets-roll/18040450426. Prices and stock are those of Sam's Club's default club.  |

## Details

Fetch a SamsClub.com product by URL and get title, member price, stock, brand, model, UPC, rating, description, and images in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "sams-club/product", "url": "https://www.samsclub.com/ip/Bounty-Select-A-Size-2-Ply-Paper-Towels-12-Rolls-110-sheets-roll/18040450426"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Sam's Club product page URL, e.g. https://www.samsclub.com/ip/Bounty-Select-A-Size-2-Ply-Paper-Towels-12-Rolls-110-sheets-roll/18040450426. Prices and stock are those of Sam's Club's default club. |

### Pricing

Billed at the actual cost of each call, about $0.00319 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/sams-club/product.json`](../../../catalog/models/sams-club/product.json) · Store page: https://www.sandbase.ai/model/sams-club/product
