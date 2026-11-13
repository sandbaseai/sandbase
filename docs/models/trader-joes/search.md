# Trader Joe's Search API: pricing, parameters and code examples

`trader-joes/search` · data API · Trader Joe's · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search Trader Joe's products by keyword with name, price, size, category and dietary tags, filtered by store and category.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trader-joes/search", "q": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('trader-joes/search', {'q': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("trader-joes/search", {
  "q": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "trader-joes/search", sandbase.Params{
	"q": "coffee",
})
```

Same call via the path form: `POST /v1/api/trader-joes/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the search query. You can use anything that you would use in a regular Trader Joe's search.  |
| `page` | string |  | Parameter defines the page number of the results (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, etc.). Trader Joe's returns up to 15 results per page.  |
| `tags` | string |  | Parameter defines the tags the products must all have, from the Trader Joe's "fun tags" like Date Night or Cheese Board. It's a comma-separated list of options (e.g., `date_night,cheese_board`). Head to the Trader…  |
| `sort_by` | string |  | Parameter defines the sorting order of the results. It defaults to relevance. Available options: `price_low_to_high` - Price Low to High `price_high_to_low` - Price High to Low `popularity` - Popularity  |
| `store_id` | string |  | Parameter defines the Trader Joe's store to search in, so only products sold in this store are returned (e.g., `454` for Austin - Northwest). Head to the Trader Joe's stores page for a full list of store IDs. When it…  |
| `category_id` | string |  | Parameter defines the category of the products (e.g., `194` for Coffee & Tea). Head to the Trader Joe's categories page for a full list of category IDs.  |
| `new_products` | string |  | Parameter defines whether to only show the products Trader Joe's marks as new. It can be set to `true` or `false` (default).  |
| `characteristics` | string |  | Parameter defines the characteristics the products must all have. It's a comma-separated list of options (e.g., `organic,vegan`). Available options: `kosher` - Kosher `organic` - Organic `gluten_free` - Gluten Free…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search Trader Joe's products by keyword with name, price, size, category and dietary tags, filtered by store and category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/trader-joes/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the search query. You can use anything that you would use in a regular Trader Joe's search. |
| `store_id` | string | No | Parameter defines the Trader Joe's store to search in, so only products sold in this store are returned (e.g., `454` for Austin - Northwest). Head to the Trader Joe's stores page for a full list of store IDs. When it isn't set, or when no s |
| `category_id` | string | No | Parameter defines the category of the products (e.g., `194` for Coffee & Tea). Head to the Trader Joe's categories page for a full list of category IDs. |
| `characteristics` | string | No | Parameter defines the characteristics the products must all have. It's a comma-separated list of options (e.g., `organic,vegan`). Available options: `kosher` - Kosher `organic` - Organic `gluten_free` - Gluten Free `vegan` - Vegan `antibiot |
| `tags` | string | No | Parameter defines the tags the products must all have, from the Trader Joe's "fun tags" like Date Night or Cheese Board. It's a comma-separated list of options (e.g., `date_night,cheese_board`). Head to the Trader Joe's tags page for a full |
| `new_products` | string | No | Parameter defines whether to only show the products Trader Joe's marks as new. It can be set to `true` or `false` (default). |
| `sort_by` | string | No | Parameter defines the sorting order of the results. It defaults to relevance. Available options: `price_low_to_high` - Price Low to High `price_high_to_low` - Price High to Low `popularity` - Popularity |
| `page` | string | No | Parameter defines the page number of the results (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, etc.). Trader Joe's returns up to 15 results per page. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/trader-joes/search.json`](../../../catalog/models/trader-joes/search.json) · Store page: https://www.sandbase.ai/model/trader-joes/search
