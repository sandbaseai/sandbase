# Amazon Search API: pricing, parameters and code examples

`amazon/search` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Search Amazon by keyword: organic results with ASIN, title, price, old price, rating, reviews, Prime and delivery info, plus sponsored products and pagination.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/search", "k": "wireless earbuds"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/search', {'k': 'wireless earbuds'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/search", {
  "k": "wireless earbuds"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/search", sandbase.Params{
	"k": "wireless earbuds",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/amazon/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `k` | string \\| number \\| boolean | yes | The query you want to search. You can use anything that you would use in a regular Amazon search. This parameter can't be used with the `node` parameter.  |
| `s` |  |  | Sorting results. Available options: `relevanceblender` - Featured (default) `price-asc-rank` - Price: Low to High `price-desc-rank` - Price: High to Low `review-rank` - Avg. Customer Review `date-desc-rank` - Newest…  |
| `dc` |  |  | The exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to `true` to exclude these results, or `false` to include them (default).  |
| `rh` | string \\| number \\| boolean |  | Items filtering based on their attributes. The structure is a list of `key:value` pairs separated by `,`. For example `n:16318031,p_n_cpf_eligible:21512497011,p_72:1248897011` to filter for products in **Coffee**…  |
| `node` | string \\| number \\| boolean |  | Specifies the category for Amazon search results. You can find the appropriate node value by browsing Amazon’s website and accessing a specific category. The node ID is typically included in the URL after the format…  |
| `page` | string \\| number \\| boolean |  | The page number. It's used for pagination. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.).  |
| `device` | string \\| number \\| boolean |  | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `language` | string \\| number \\| boolean |  | The language to use for the Amazon search. It's a locale name represented as _. (e.g., on amazon.com `en_US` for English, `es_US` for Spanish, or on amazon.co.jp `ja_JP` for Japanese). Head to Amazon languages for a…  |
| `delivery_zip` | string \\| number \\| boolean |  | ZIP Postal code. To filter the shipping products by a selected area.  |
| `amazon_domain` | string \\| number \\| boolean |  | The Amazon domain to use. It defaults to `amazon.com`. Head to Amazon domains for a full list of supported Amazon domains.  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `shipping_location` | string \\| number \\| boolean |  | Shipping country. To filter the shipping products by a selected country.  |

## Details

Search Amazon by keyword: organic results with ASIN, title, price, old price, rating, reviews, Prime and delivery info, plus sponsored products and pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/amazon/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"k": "wireless earbuds"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `k` | string/number/boolean | Yes | The query you want to search. You can use anything that you would use in a regular Amazon search. This parameter can't be used with the `node` parameter. |
| `amazon_domain` | string/number/boolean | No | The Amazon domain to use. It defaults to `amazon.com`. Head to Amazon domains for a full list of supported Amazon domains. |
| `dc` | any | No | The exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to `true` to exclude these results, or `false` to include them (default). |
| `delivery_zip` | string/number/boolean | No | ZIP Postal code. To filter the shipping products by a selected area. |
| `device` | string/number/boolean | No | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | string/number/boolean | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `language` | string/number/boolean | No | The language to use for the Amazon search. It's a locale name represented as _. (e.g., on amazon.com `en_US` for English, `es_US` for Spanish, or on amazon.co.jp `ja_JP` for Japanese). Head to Amazon … |
| `node` | string/number/boolean | No | Specifies the category for Amazon search results. You can find the appropriate node value by browsing Amazon’s website and accessing a specific category. The node ID is typically included in the URL a… |
| `page` | string/number/boolean | No | The page number. It's used for pagination. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). |
| `rh` | string/number/boolean | No | Items filtering based on their attributes. The structure is a list of `key:value` pairs separated by `,`. For example `n:16318031,p_n_cpf_eligible:21512497011,p_72:1248897011` to filter for products i… |
| `s` | any | No | Sorting results. Available options: `relevanceblender` - Featured (default) `price-asc-rank` - Price: Low to High `price-desc-rank` - Price: High to Low `review-rank` - Avg. Customer Review `date-desc… |
| `shipping_location` | string/number/boolean | No | Shipping country. To filter the shipping products by a selected country. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/amazon/search.json`](../../../catalog/models/amazon/search.json) · Store page: https://www.sandbase.ai/model/amazon/search
