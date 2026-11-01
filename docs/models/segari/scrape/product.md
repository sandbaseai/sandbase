# Segari Product Page

`segari/scrape/product` · api · Segari

Extract structured data from a Segari product page URL: price, availability and product details.

## Pricing

- **$0.024 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "segari/scrape/product", "url": "https://segari.id/p/telur-ayam-kampung-curah"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('segari/scrape/product', {'url': 'https://segari.id/p/telur-ayam-kampung-curah'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("segari/scrape/product", {
  "url": "https://segari.id/p/telur-ayam-kampung-curah"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "segari/scrape/product", sandbase.Params{
	"url": "https://segari.id/p/telur-ayam-kampung-curah",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/segari/scrape/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Segari page URL, e.g. https://segari.id/p/telur-ayam-kampung-curah  |

## Details

Extract structured data from a Segari product page URL: price, availability and product details.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/segari/scrape/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://segari.id/p/telur-ayam-kampung-curah"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Segari page URL, e.g. https://segari.id/p/telur-ayam-kampung-curah |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/segari/scrape/product.json`](../../../../catalog/models/segari/scrape/product.json) · Store page: https://www.sandbase.ai/model/segari/scrape/product
