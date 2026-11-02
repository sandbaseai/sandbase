# Walmart Search API: pricing, parameters and code examples

`walmart/search` · data API · Walmart · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Search Walmart products by keyword with price, rating, reviews, seller and fulfillment badges, plus sorting, price filters and pagination.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "walmart/search", "query": "laptop"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('walmart/search', {'query': 'laptop'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("walmart/search", {
  "query": "laptop"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "walmart/search", sandbase.Params{
	"query": "laptop",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/walmart/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string \\| number \\| boolean |  | Value is used to get the items on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Maximum `page` value is `100`.  |
| `sort` | string \\| number \\| boolean |  | Sorting. (e.g. `price_low`, `price_high`, `best_seller`, `best_match`, `rating_high`, `new`). **Note:** `best_seller`, `rating_high`, and `new` are not supported for `walmart.com.mx`.  |
| `facet` | string \\| number \\| boolean |  | Items filtering based on their attributes. The structure is a list of `key:value` pairs separated by `\|\|`. The key and value are separated by `:`  |
| `nd_en` |  |  | Show results with NextDay delivery only. Set to `true` to enable or `false` (default) to disable. **Note:** not supported for `walmart.com.mx`.  |
| `query` | string \\| number \\| boolean | yes | The search query. You can use anything that you would use in a regular Walmart search. Either a `query` or a `cat_id` parameter is required.  |
| `cat_id` | string \\| number \\| boolean |  | Category on Walmart Search. (e.g. `0` (default) is all departments, `976759_976787` is 'Cookies', etc.). Either a `query` or a `cat_id` parameter is required. **Note:** not supported for `walmart.com.mx`.  |
| `device` | string \\| number \\| boolean |  | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `spelling` |  |  | Activate spelling fix. `true` (default) includes spelling fix, `false` searches without spelling fix.  |
| `store_id` | string \\| number \\| boolean |  | Store ID to filter the products by the specific store only. Head to the Walmart Stores Locations for a full list of supported stores. It's possible for the product pricing to differ between stores.  |
| `max_price` | string \\| number \\| boolean |  | Upper bound of price range query.  |
| `min_price` | string \\| number \\| boolean |  | Lower bound of price range query.  |
| `soft_sort` | string \\| number \\| boolean |  | Enables sort by relevance. Walmart is by default showing results sorted by relevance and using the `sort` option. Set to `false` to disable sort by Relevance. **Note:** not supported for `walmart.com.mx`.  |
| `walmart_domain` | string \\| number \\| boolean |  | The Walmart domain to use. It defaults to `walmart.com`. Head to the Walmart Stores for a full list of supported stores per domain.  |
| `include_filters` |  |  | Include `filters` to the JSON response. Set to `true` to enable or `false` to disable (default).  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search Walmart products by keyword with price, rating, reviews, seller and fulfillment badges, plus sorting, price filters and pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/walmart/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "laptop"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string/number/boolean | Yes | The search query. You can use anything that you would use in a regular Walmart search. Either a `query` or a `cat_id` parameter is required. |
| `cat_id` | string/number/boolean | No | Category on Walmart Search. (e.g. `0` (default) is all departments, `976759_976787` is 'Cookies', etc.). Either a `query` or a `cat_id` parameter is required. **Note:** not supported for `walmart.com.… |
| `device` | string/number/boolean | No | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `facet` | string/number/boolean | No | Items filtering based on their attributes. The structure is a list of `key:value` pairs separated by `\|\|`. The key and value are separated by `:` |
| `include_filters` | any | No | Include `filters` to the JSON response. Set to `true` to enable or `false` to disable (default). |
| `json_restrictor` | string/number/boolean | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `max_price` | string/number/boolean | No | Upper bound of price range query. |
| `min_price` | string/number/boolean | No | Lower bound of price range query. |
| `nd_en` | any | No | Show results with NextDay delivery only. Set to `true` to enable or `false` (default) to disable. **Note:** not supported for `walmart.com.mx`. |
| `page` | string/number/boolean | No | Value is used to get the items on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Maximum `page` value is `10… |
| `soft_sort` | string/number/boolean | No | Enables sort by relevance. Walmart is by default showing results sorted by relevance and using the `sort` option. Set to `false` to disable sort by Relevance. **Note:** not supported for `walmart.com.… |
| `sort` | string/number/boolean | No | Sorting. (e.g. `price_low`, `price_high`, `best_seller`, `best_match`, `rating_high`, `new`). **Note:** `best_seller`, `rating_high`, and `new` are not supported for `walmart.com.mx`. |
| `spelling` | any | No | Activate spelling fix. `true` (default) includes spelling fix, `false` searches without spelling fix. |
| `store_id` | string/number/boolean | No | Store ID to filter the products by the specific store only. Head to the Walmart Stores Locations for a full list of supported stores. It's possible for the product pricing to differ between stores. |
| `walmart_domain` | string/number/boolean | No | The Walmart domain to use. It defaults to `walmart.com`. Head to the Walmart Stores for a full list of supported stores per domain. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/walmart/search.json`](../../../catalog/models/walmart/search.json) · Store page: https://www.sandbase.ai/model/walmart/search
