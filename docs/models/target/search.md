# Target Search

`target/search` · api · Target

Search Target products by keyword with TCIN, brand, price, sale price, rating, reviews and pickup, delivery and shipping availability.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "target/search", "q": "wireless earbuds"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('target/search', {'q': 'wireless earbuds'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("target/search", {
  "q": "wireless earbuds"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "target/search", sandbase.Params{
	"q": "wireless earbuds",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/target/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string \\| number \\| boolean | yes | The query you want to search. You can use anything that you would use in a regular Target search (e.g., `coffee`, `65 inch tv`, or `lego star wars`).  |
| `page` | string \\| number \\| boolean |  | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Target returns up to 24 results per page, plus…  |
| `sort` |  |  | The sorting of the results. It defaults to `relevance`. Available options: `relevance` - Relevance `featured` - Featured `price_low` - Price: low to high `price_high` - Price: high to low `rating_high` - Guest rating…  |
| `facet` | string \\| number \\| boolean |  | The filters to apply, like Target's filters (e.g., deals, brands, sizes, colors, or guest ratings). It's a comma-separated list of filter IDs (e.g., `5tdv0,4yagy` for Sale and Dark Roast). Filter IDs are available in…  |
| `spelling` |  |  | Whether to fix the spelling of misspelled queries, like Target. It can be set to `true` (default) to search for the spelling fix (e.g., `coffee` for `cofee`), as shown in `search_information.spelling_fix`, or `false`…  |
| `store_id` | string \\| number \\| boolean |  | The Target store to get prices and availability for, like the store selected on Target (e.g., `1375` for Mpls Nicollet Mall, MN). The store ID is the number at the end of the store's page URL on Target (e.g.,…  |
| `max_price` | string \\| number \\| boolean |  | The maximum price of the products, in US dollars (e.g., `50`).  |
| `min_price` | string \\| number \\| boolean |  | The minimum price of the products, in US dollars (e.g., `10`).  |
| `category_id` | string \\| number \\| boolean |  | The category to search in (e.g., `hz89j` for Kitchen & Dining). Category IDs are available in the `Category` filter of the results when `include_filters` is set to `true`.  |
| `delivery_zip` | string \\| number \\| boolean |  | The US ZIP code to deliver to (e.g., `10001`). It's used for the shipping dates and the same day delivery availability. It defaults to the location of the store.  |
| `include_filters` |  |  | Whether to include the `filters` of the search in the JSON response, with the IDs to use in `facet` and `category_id`. It can be set to `true` or `false` (default).  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search Target products by keyword with TCIN, brand, price, sale price, rating, reviews and pickup, delivery and shipping availability.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/target/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "wireless earbuds"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string/number/boolean | Yes | The query you want to search. You can use anything that you would use in a regular Target search (e.g., `coffee`, `65 inch tv`, or `lego star wars`). |
| `category_id` | string/number/boolean | No | The category to search in (e.g., `hz89j` for Kitchen & Dining). Category IDs are available in the `Category` filter of the results when `include_filters` is set to `true`. |
| `delivery_zip` | string/number/boolean | No | The US ZIP code to deliver to (e.g., `10001`). It's used for the shipping dates and the same day delivery availability. It defaults to the location of the store. |
| `facet` | string/number/boolean | No | The filters to apply, like Target's filters (e.g., deals, brands, sizes, colors, or guest ratings). It's a comma-separated list of filter IDs (e.g., `5tdv0,4yagy` for Sale and Dark Roast). Filter IDs … |
| `include_filters` | any | No | Whether to include the `filters` of the search in the JSON response, with the IDs to use in `facet` and `category_id`. It can be set to `true` or `false` (default). |
| `json_restrictor` | string/number/boolean | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `max_price` | string/number/boolean | No | The maximum price of the products, in US dollars (e.g., `50`). |
| `min_price` | string/number/boolean | No | The minimum price of the products, in US dollars (e.g., `10`). |
| `page` | string/number/boolean | No | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Target returns up to 24 resul… |
| `sort` | any | No | The sorting of the results. It defaults to `relevance`. Available options: `relevance` - Relevance `featured` - Featured `price_low` - Price: low to high `price_high` - Price: high to low `rating_high… |
| `spelling` | any | No | Whether to fix the spelling of misspelled queries, like Target. It can be set to `true` (default) to search for the spelling fix (e.g., `coffee` for `cofee`), as shown in `search_information.spelling_… |
| `store_id` | string/number/boolean | No | The Target store to get prices and availability for, like the store selected on Target (e.g., `1375` for Mpls Nicollet Mall, MN). The store ID is the number at the end of the store's page URL on Targe… |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/target/search.json`](../../../catalog/models/target/search.json) · Store page: https://www.sandbase.ai/model/target/search
