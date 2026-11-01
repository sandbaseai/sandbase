# Home Depot Search

`home-depot/search` · api · Home Depot

Search Home Depot products by keyword with price, brand, model number, rating, delivery and pickup availability, filters and pagination.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "home-depot/search", "q": "cordless drill"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('home-depot/search', {'q': 'cordless drill'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("home-depot/search", {
  "q": "cordless drill"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "home-depot/search", sandbase.Params{
	"q": "cordless drill",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/home-depot/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string \\| number \\| boolean | yes | The search query. You can use anything that you would use in a regular The Home Depot search.  |
| `ps` | string \\| number \\| boolean |  | Determines the number of items per page. There are scenarios where The Home Depot overrides the `ps` value. By default, The Home Depot returns `24` (maximum allowed value) results.  |
| `nao` | string \\| number \\| boolean |  | Defines offset for products result. A single page contains 24 products. First page offset is 0, second -> 24, third -> 48 and so on.  |
| `page` | string \\| number \\| boolean |  | Value is used to get the items on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). This parameter is common for both US and CA…  |
| `sort` |  |  | Results sorted by different options in Home Depot Canada. It can be set to: `price-asc`: Price Low to High, `price-desc`: Price High to Low, `reviewAvgRating`: Top Rated, `relevance`: Recommended (Default)  |
| `store` | string \\| number \\| boolean |  | Store ID to filter the products by the specific store only in Home Depot Canada. The default store is Gatineau (`7140`). See all Home Depot Canada stores  |
| `filter` | string \\| number \\| boolean |  | Used to pass filter tokens divided by dash (-) in Home Depot Canada. Filter tokens can be obtained from API response  |
| `minmax` | string \\| number \\| boolean |  | Defines lower and upper bound for price in CAD. Parameter is only used in the Home Depot Canada. Example: `price:[100 TO 500]`(Between $100 to $500) Example: `price:[100 TO *]`(Minimum $100) Example: `price:[0 TO…  |
| `country` | string \\| number \\| boolean |  | The country to use for the Home Depot search. Only United States(`us`), and Canada(`ca`) are supported.  |
| `hd_sort` |  |  | Results sorted by different options in Home Depot US. It can be set to: `top_sellers`: Top Sellers, `price_low_to_high`: Price Low to High, `price_high_to_low`: Price High to Low, `top_rated`: Top Rated, `best_match`:…  |
| `pagesize` | string \\| number \\| boolean |  | Determines the number of items per page in the Home Depot Canada. By default, the Home Depot Canada returns `40` (maximum allowed value) results.  |
| `store_id` | string \\| number \\| boolean |  | Store ID to filter the products by the specific store only. See all Home Depot stores  |
| `lowerbound` | string \\| number \\| boolean |  | Defines lower bound for price in USD.  |
| `upperbound` | string \\| number \\| boolean |  | Defines upper bound for price in USD.  |
| `delivery_zip` | string \\| number \\| boolean |  | ZIP Postal code. To filter the shipping products by a selected area.  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `hd_filter_tokens` | string \\| number \\| boolean |  | Used to pass filter tokens divided by comma. Filter tokens can be obtained from API response  |

## Details

Search Home Depot products by keyword with price, brand, model number, rating, delivery and pickup availability, filters and pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/home-depot/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "cordless drill"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string/number/boolean | Yes | The search query. You can use anything that you would use in a regular The Home Depot search. |
| `country` | string/number/boolean | No | The country to use for the Home Depot search. Only United States(`us`), and Canada(`ca`) are supported. |
| `delivery_zip` | string/number/boolean | No | ZIP Postal code. To filter the shipping products by a selected area. |
| `filter` | string/number/boolean | No | Used to pass filter tokens divided by dash (-) in Home Depot Canada. Filter tokens can be obtained from API response |
| `hd_filter_tokens` | string/number/boolean | No | Used to pass filter tokens divided by comma. Filter tokens can be obtained from API response |
| `hd_sort` | any | No | Results sorted by different options in Home Depot US. It can be set to: `top_sellers`: Top Sellers, `price_low_to_high`: Price Low to High, `price_high_to_low`: Price High to Low, `top_rated`: Top Rat… |
| `json_restrictor` | string/number/boolean | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `lowerbound` | string/number/boolean | No | Defines lower bound for price in USD. |
| `minmax` | string/number/boolean | No | Defines lower and upper bound for price in CAD. Parameter is only used in the Home Depot Canada. Example: `price:[100 TO 500]`(Between $100 to $500) Example: `price:[100 TO *]`(Minimum $100) Example: … |
| `nao` | string/number/boolean | No | Defines offset for products result. A single page contains 24 products. First page offset is 0, second -> 24, third -> 48 and so on. |
| `page` | string/number/boolean | No | Value is used to get the items on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). This parameter is common fo… |
| `pagesize` | string/number/boolean | No | Determines the number of items per page in the Home Depot Canada. By default, the Home Depot Canada returns `40` (maximum allowed value) results. |
| `ps` | string/number/boolean | No | Determines the number of items per page. There are scenarios where The Home Depot overrides the `ps` value. By default, The Home Depot returns `24` (maximum allowed value) results. |
| `sort` | any | No | Results sorted by different options in Home Depot Canada. It can be set to: `price-asc`: Price Low to High, `price-desc`: Price High to Low, `reviewAvgRating`: Top Rated, `relevance`: Recommended (Def… |
| `store` | string/number/boolean | No | Store ID to filter the products by the specific store only in Home Depot Canada. The default store is Gatineau (`7140`). See all Home Depot Canada stores |
| `store_id` | string/number/boolean | No | Store ID to filter the products by the specific store only. See all Home Depot stores |
| `upperbound` | string/number/boolean | No | Defines upper bound for price in USD. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/home-depot/search.json`](../../../catalog/models/home-depot/search.json) · Store page: https://www.sandbase.ai/model/home-depot/search
