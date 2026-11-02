# Amazon Product API: pricing, parameters and code examples

`amazon/product` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Get an Amazon product by ASIN: title, brand, price, rating, reviews, images, variants, availability, purchase options, about-this-item and description.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/product", "asin": "<asin>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/product', {'asin': '<asin>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/product", {
  "asin": "<asin>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/product", sandbase.Params{
	"asin": "<asin>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/amazon/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `asin` | string \\| number \\| boolean | yes | The Amazon Standard Identification Number (ASIN) of the product you want to retrieve. This is a unique identifier assigned to each product on Amazon.  |
| `device` | string \\| number \\| boolean |  | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `language` | string \\| number \\| boolean |  | The language to use for the Amazon search. It's a locale name represented as _. (e.g., on amazon.com `en_US` for English, `es_US` for Spanish, or on amazon.co.jp `ja_JP` for Japanese). Head to Amazon languages for a…  |
| `delivery_zip` | string \\| number \\| boolean |  | ZIP Postal code. To filter the shipping products by a selected area.  |
| `amazon_domain` | string \\| number \\| boolean |  | The Amazon domain to use. It defaults to `amazon.com`. Head to Amazon domains for a full list of supported Amazon domains.  |
| `other_sellers` | string \\| number \\| boolean |  | Include results from other sellers.  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `shipping_location` | string \\| number \\| boolean |  | Shipping country. To filter the shipping products by a selected country.  |
| `all_related_products` |  |  | Set to `true` to retrieve all items in `related_products` and `related_product_sections`, not just the first page. May yield better results but with a longer response time. Defaults to `false`.  |

## Details

Get an Amazon product by ASIN: title, brand, price, rating, reviews, images, variants, availability, purchase options, about-this-item and description.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/amazon/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin": "B0CP9YB3Q4"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `asin` | string/number/boolean | Yes | The Amazon Standard Identification Number (ASIN) of the product you want to retrieve. This is a unique identifier assigned to each product on Amazon. |
| `all_related_products` | any | No | Set to `true` to retrieve all items in `related_products` and `related_product_sections`, not just the first page. May yield better results but with a longer response time. Defaults to `false`. |
| `amazon_domain` | string/number/boolean | No | The Amazon domain to use. It defaults to `amazon.com`. Head to Amazon domains for a full list of supported Amazon domains. |
| `delivery_zip` | string/number/boolean | No | ZIP Postal code. To filter the shipping products by a selected area. |
| `device` | string/number/boolean | No | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | string/number/boolean | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `language` | string/number/boolean | No | The language to use for the Amazon search. It's a locale name represented as _. (e.g., on amazon.com `en_US` for English, `es_US` for Spanish, or on amazon.co.jp `ja_JP` for Japanese). Head to Amazon … |
| `other_sellers` | string/number/boolean | No | Include results from other sellers. |
| `shipping_location` | string/number/boolean | No | Shipping country. To filter the shipping products by a selected country. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/amazon/product.json`](../../../catalog/models/amazon/product.json) · Store page: https://www.sandbase.ai/model/amazon/product
