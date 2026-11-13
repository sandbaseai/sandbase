# Amazon Fresh Search API: pricing, parameters and code examples

`amazon/fresh` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search Amazon Fresh grocery products for a delivery ZIP code, with title, price, unit price, rating and availability.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/fresh", "delivery_zip": "10001"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/fresh', {'delivery_zip': '10001'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/fresh", {
  "delivery_zip": "10001"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/fresh", sandbase.Params{
	"delivery_zip": "10001",
})
```

Same call via the path form: `POST /v1/api/amazon/fresh` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `k` | string |  | Parameter defines the query you want to search. You can use anything that you would use in a regular Amazon Fresh search. This parameter can't be used with the `node` parameter.  |
| `s` | string |  | Parameter is used for sorting results. It defaults to `relevanceblender` (Featured). Available options: `relevanceblender` - Featured `price-asc-rank` - Price: Low to High `price-desc-rank` - Price: High to Low…  |
| `dc` | string |  | Parameter defines the exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to `true` to exclude these results, or `false` to include them (default).  |
| `rh` | string |  | Parameter defines items filtering based on their attributes. The structure is a list of `key:value` pairs separated by `,`. For example `n:16318981,p_n_program_participation:17428820011` to filter for products in the…  |
| `node` | string |  | Parameter defines the Amazon Fresh department to browse without a search query. For example, `16318981` for **Fresh Fruits** on `amazon.com`. Department IDs are the `n:` values in `filters.department[].rh` (e.g.,…  |
| `page` | string |  | Parameter defines the page number. It's used for pagination. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.).  |
| `device` | string |  | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `language` | string |  | Parameter defines the language to use for the Amazon Fresh search. It's a locale name represented as <language>_<REGION>. (e.g., on amazon.com `en_US` for English, `es_US` for Spanish, or on amazon.co.jp `ja_JP` for…  |
| `delivery_zip` | string | yes | Parameter defines the ZIP or postal code of the delivery location. Amazon Fresh shows the products, prices, and delivery options available at that location. For example, `10001` on `amazon.com`, `EC1A 1BB` on…  |
| `amazon_domain` | string |  | Parameter defines the Amazon domain to use. It defaults to `amazon.com`. Amazon Fresh is available on `amazon.com`, `amazon.co.uk`, `amazon.co.jp`, `amazon.it`, and `amazon.es`.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search Amazon Fresh grocery products for a delivery ZIP code, with title, price, unit price, rating and availability.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/amazon/fresh" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"k": "milk", "delivery_zip": "10001"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `delivery_zip` | string | Yes | Parameter defines the ZIP or postal code of the delivery location. Amazon Fresh shows the products, prices, and delivery options available at that location. For example, `10001` on `amazon.com`, `EC1A 1BB` on `amazon.co.uk`, or `100-0001` o |
| `k` | string | No | Parameter defines the query you want to search. You can use anything that you would use in a regular Amazon Fresh search. This parameter can't be used with the `node` parameter. |
| `amazon_domain` | string | No | Parameter defines the Amazon domain to use. It defaults to `amazon.com`. Amazon Fresh is available on `amazon.com`, `amazon.co.uk`, `amazon.co.jp`, `amazon.it`, and `amazon.es`. |
| `language` | string | No | Parameter defines the language to use for the Amazon Fresh search. It's a locale name represented as <language>_<REGION>. (e.g., on amazon.com `en_US` for English, `es_US` for Spanish, or on amazon.co.jp `ja_JP` for Japanese). Head to Amazo |
| `s` | string | No | Parameter is used for sorting results. It defaults to `relevanceblender` (Featured). Available options: `relevanceblender` - Featured `price-asc-rank` - Price: Low to High `price-desc-rank` - Price: High to Low `review-rank` - Avg. Customer |
| `node` | string | No | Parameter defines the Amazon Fresh department to browse without a search query. For example, `16318981` for **Fresh Fruits** on `amazon.com`. Department IDs are the `n:` values in `filters.department[].rh` (e.g., `n:16318981`). To switch de |
| `rh` | string | No | Parameter defines items filtering based on their attributes. The structure is a list of `key:value` pairs separated by `,`. For example `n:16318981,p_n_program_participation:17428820011` to filter for products in the **Fresh Fruits** depart |
| `dc` | string | No | Parameter defines the exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to `true` to exclude these results, or `false` to include them (default). |
| `page` | string | No | Parameter defines the page number. It's used for pagination. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). |
| `device` | string | No | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/amazon/fresh.json`](../../../catalog/models/amazon/fresh.json) · Store page: https://www.sandbase.ai/model/amazon/fresh
