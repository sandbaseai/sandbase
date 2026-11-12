# Amazon Products by ASIN API: pricing, parameters and code examples

`amazon/asins` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0033 per call · **Modes:** sync

Look up to 10 Amazon products in one call by ASIN (title, brand, price, ratings, images, and attributes) as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0033**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/asins", "asins": ["B09G9FPHY6"]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/asins', {'asins': ['B09G9FPHY6']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/asins", {
  "asins": [
    "B09G9FPHY6"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/asins", sandbase.Params{
	"asins": []any{"B09G9FPHY6"},
})
```

Same call via the path form: `POST /v1/api/amazon/asins` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `asins` | array | yes | Up to 10 Amazon ASINs to look up (e.g. ["B0CHX1W1XY", "B09G9FPHY6"]).  |
| `limit` | integer |  | Maximum number of results to return (1-10, default 10). You are billed per result returned, so a lower limit costs less. range 1–10 |
| `amazonDomain` | string |  | Amazon marketplace domain to fetch products from (e.g. amazon.com, amazon.de, amazon.co.uk). default `"amazon.com"` |

## Details

Look up to 10 Amazon products in one call by ASIN (title, brand, price, ratings, images, and attributes) as normalized JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "amazon/asins", "asins": ["B09G9FPHY6"], "limit": 3}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `asins` | array | Yes | Up to 10 Amazon ASINs to look up (e.g. ["B0CHX1W1XY", "B09G9FPHY6"]). |
| `amazonDomain` | string | No | Amazon marketplace domain to fetch products from (e.g. amazon.com, amazon.de, amazon.co.uk). Default `"amazon.com"`. |
| `limit` | integer | No | Maximum number of results to return (1-10, default 10). You are billed per result returned, so a lower limit costs less. |

### Pricing

Billed at the actual cost of each call: about $0.0033 per asin returned, up to $0.033 per request (about $0.0033 for the request above). A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/amazon/asins.json`](../../../catalog/models/amazon/asins.json) · Store page: https://www.sandbase.ai/model/amazon/asins
