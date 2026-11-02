# Google Shopping Search API: pricing, parameters and code examples

`google-shopping/search` · data API · Google Shopping · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Search Google Shopping by keyword: product title, price, old price, store, rating, reviews, delivery and product ID, with price, sort and location filters.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-shopping/search", "q": "wireless earbuds"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-shopping/search', {'q': 'wireless earbuds'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-shopping/search", {
  "q": "wireless earbuds"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-shopping/search", sandbase.Params{
	"q": "wireless earbuds",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/google-shopping/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string \\| number \\| boolean | yes | The query you want to search. You can use anything that you would use in a regular Google Shopping search. This parameter is optional if using `shoprs` parameter.  |
| `gl` | string \\| number \\| boolean |  | The country to use for the Google search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google Shopping countries for a full list of…  |
| `hl` | string \\| number \\| boolean |  | The language to use for the Google Shopping search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region…  |
| `safe` | string \\| number \\| boolean |  | The level of filtering for adult content. It can be set to `active` or `off`, by default Google will omit explicit content.  |
| `uule` | string \\| number \\| boolean |  | The Google encoded location you want to use for the search. `uule` and `location` parameters can't be used together. For consistent results with coordinates-based `uule` parameter, a matching `gl` parameter is…  |
| `start` | string \\| number \\| boolean |  | Intended to define the result offset for pagination. Google Shopping's current layout does not support offset pagination: the `start` parameter is ignored and every request returns the first page of results (around 40…  |
| `device` | string \\| number \\| boolean |  | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `shoprs` | string \\| number \\| boolean |  | The parameter defines the token that includes metadata about query and search filter(s). Providing `q` parameter alongside the `shoprs` is **not** required. To apply multiple filters join them with `\|\|` separator, e.g.…  |
| `on_sale` | string \\| number \\| boolean |  | Show only products that are on sale. This parameter overrides corresponding filter embedded into `shoprs` parameter.  |
| `sort_by` |  |  | The sorting order of the results. Available options: `1` - Price: low to high `2` - Price: high to low This parameter overrides corresponding filter embedded into `shoprs` parameter.  |
| `max_price` | string \\| number \\| boolean |  | Upper bound of price range query. This parameter overrides corresponding filter embedded into `shoprs` parameter.  |
| `min_price` | string \\| number \\| boolean |  | Lower bound of price range query. This parameter overrides corresponding filter embedded into `shoprs` parameter.  |
| `free_shipping` | string \\| number \\| boolean |  | Show only products with free shipping. This parameter overrides corresponding filter embedded into `shoprs` parameter.  |
| `google_domain` | string \\| number \\| boolean |  | The Google domain to use. It defaults to `google.com`. Head to the Google domains for a full list of supported Google domains.  |
| `small_business` | string \\| number \\| boolean |  | Show only products from small business. This parameter overrides corresponding filter embedded into `shoprs` parameter.  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search Google Shopping by keyword: product title, price, old price, store, rating, reviews, delivery and product ID, with price, sort and location filters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-shopping/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "wireless earbuds"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string/number/boolean | Yes | The query you want to search. You can use anything that you would use in a regular Google Shopping search. This parameter is optional if using `shoprs` parameter. |
| `device` | string/number/boolean | No | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `free_shipping` | string/number/boolean | No | Show only products with free shipping. This parameter overrides corresponding filter embedded into `shoprs` parameter. |
| `gl` | string/number/boolean | No | The country to use for the Google search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google Shopping countries for a fu… |
| `google_domain` | string/number/boolean | No | The Google domain to use. It defaults to `google.com`. Head to the Google domains for a full list of supported Google domains. |
| `hl` | string/number/boolean | No | The language to use for the Google Shopping search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or thr… |
| `json_restrictor` | string/number/boolean | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `max_price` | string/number/boolean | No | Upper bound of price range query. This parameter overrides corresponding filter embedded into `shoprs` parameter. |
| `min_price` | string/number/boolean | No | Lower bound of price range query. This parameter overrides corresponding filter embedded into `shoprs` parameter. |
| `on_sale` | string/number/boolean | No | Show only products that are on sale. This parameter overrides corresponding filter embedded into `shoprs` parameter. |
| `safe` | string/number/boolean | No | The level of filtering for adult content. It can be set to `active` or `off`, by default Google will omit explicit content. |
| `shoprs` | string/number/boolean | No | The parameter defines the token that includes metadata about query and search filter(s). Providing `q` parameter alongside the `shoprs` is **not** required. To apply multiple filters join them with `\… |
| `small_business` | string/number/boolean | No | Show only products from small business. This parameter overrides corresponding filter embedded into `shoprs` parameter. |
| `sort_by` | any | No | The sorting order of the results. Available options: `1` - Price: low to high `2` - Price: high to low This parameter overrides corresponding filter embedded into `shoprs` parameter. |
| `start` | string/number/boolean | No | Intended to define the result offset for pagination. Google Shopping's current layout does not support offset pagination: the `start` parameter is ignored and every request returns the first page of r… |
| `uule` | string/number/boolean | No | The Google encoded location you want to use for the search. `uule` and `location` parameters can't be used together. For consistent results with coordinates-based `uule` parameter, a matching `gl` par… |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-shopping/search.json`](../../../catalog/models/google-shopping/search.json) · Store page: https://www.sandbase.ai/model/google-shopping/search
