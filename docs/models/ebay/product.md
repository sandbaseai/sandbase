# eBay Product API: pricing, parameters and code examples

`ebay/product` · data API · eBay · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Get an eBay product by product ID: title, price, condition, quantity sold, item specifics, media, shipping, returns and seller details.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ebay/product", "product_id": "326405504746"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ebay/product', {'product_id': '326405504746'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ebay/product", {
  "product_id": "326405504746"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ebay/product", sandbase.Params{
	"product_id": "326405504746",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ebay/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `lang` | string \\| number \\| boolean |  | The language to use for the search. Normally, it defaults to `en-US`, but some locales use localized interface (Japan, Argentina etc.) so override might be helpful. This parameter available only for `United States`…  |
| `locale` | string \\| number \\| boolean |  | From where you want the search to originate from. Head to the eBay locales for a full list of supported locales.  |
| `product_id` | string \\| number \\| boolean | yes | An ID of the product to get results for. Normally, it can be found in product link from search results: `https://www.ebay.com/itm/{product_id}`  |
| `ebay_domain` | string \\| number \\| boolean |  | The eBay domain to use. It defaults to `ebay.com`. Head to the eBay domains for a full list of supported domains.  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `shipping_country` | string \\| number \\| boolean |  | The shipping country to use for shipping data calculation. Head to the eBay shipping countries for a full list of supported countries.  |

## Details

Get an eBay product by product ID: title, price, condition, quantity sold, item specifics, media, shipping, returns and seller details.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ebay/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "326405504746"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string/number/boolean | Yes | An ID of the product to get results for. Normally, it can be found in product link from search results: `https://www.ebay.com/itm/{product_id}` |
| `ebay_domain` | string/number/boolean | No | The eBay domain to use. It defaults to `ebay.com`. Head to the eBay domains for a full list of supported domains. |
| `json_restrictor` | string/number/boolean | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `lang` | string/number/boolean | No | The language to use for the search. Normally, it defaults to `en-US`, but some locales use localized interface (Japan, Argentina etc.) so override might be helpful. This parameter available only for `… |
| `locale` | string/number/boolean | No | From where you want the search to originate from. Head to the eBay locales for a full list of supported locales. |
| `shipping_country` | string/number/boolean | No | The shipping country to use for shipping data calculation. Head to the eBay shipping countries for a full list of supported countries. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ebay/product.json`](../../../catalog/models/ebay/product.json) · Store page: https://www.sandbase.ai/model/ebay/product
