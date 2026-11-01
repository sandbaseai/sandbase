# Meijer Product Page

`meijer/scrape/product` · api · Meijer

Extract structured data from a Meijer product page URL: price, availability and product details, optionally localized by ZIP code.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meijer/scrape/product", "url": "https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meijer/scrape/product', {'url': 'https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meijer/scrape/product", {
  "url": "https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meijer/scrape/product", sandbase.Params{
	"url": "https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/meijer/scrape/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Meijer page URL, e.g. https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html  |
| `zipCode` | string |  | ZIP or postal code used for localized pricing and availability.  |

## Details

Extract structured data from a Meijer product page URL: price, availability and product details, optionally localized by ZIP code.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/meijer/scrape/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Meijer page URL, e.g. https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html |
| `zipCode` | string | No | ZIP or postal code used for localized pricing and availability. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/meijer/scrape/product.json`](../../../../catalog/models/meijer/scrape/product.json) · Store page: https://www.sandbase.ai/model/meijer/scrape/product
