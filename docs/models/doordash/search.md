# DoorDash Search API: pricing, parameters and code examples

`doordash/search` · data API · DoorDash · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search DoorDash stores and dishes by keyword and delivery address, with store name, rating, delivery fee, ETA and menu items.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "doordash/search", "q": "pizza", "address": "Austin, TX"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('doordash/search', {'q': 'pizza', 'address': 'Austin, TX'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("doordash/search", {
  "q": "pizza",
  "address": "Austin, TX"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "doordash/search", sandbase.Params{
	"q": "pizza",
	"address": "Austin, TX",
})
```

Same call via the path form: `POST /v1/api/doordash/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the search query. You can use anything that you would use in a regular DoorDash search (e.g., `pizza`, `sushi`, or `milk`), up to 15 words.  |
| `page` | string |  | Parameter defines the page number of the results (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, etc.). Each page covers 50 stores. With `deals`, `fastest`, or `min_rating`, there's a…  |
| `deals` | string |  | Parameter defines whether to only show the stores with deals (e.g., `$5 off on $25+`), like the Deals filter of DoorDash. It can be set to `true` or `false` (default).  |
| `pickup` | string |  | Parameter defines whether to only show the stores offering pickup, with their pickup time and drive time instead of their delivery time and fee, like switching DoorDash from Delivery to Pickup. It can be set to `true`…  |
| `address` | string | yes | Parameter defines the delivery address to search stores around, like the address set on DoorDash. It can be a street address (e.g., `350 5th Ave, New York, NY 10118`) or a ZIP or postal code (e.g., `10001`). Addresses…  |
| `fastest` | string |  | Parameter defines whether to only show the stores delivering the fastest, like the Fastest filter of DoorDash. It can be set to `true` or `false` (default).  |
| `min_rating` | string |  | Parameter defines the minimum rating of the stores, like the Ratings filter of DoorDash. Available options: `4.5` - Over 4.5 `4.6` - Over 4.6 `4.7` - Over 4.7 `4.8` - Over 4.8 `4.9` - Over 4.9  |
| `store_type` | string |  | Parameter defines the type of stores to search, like the tabs of the DoorDash search page. By default, DoorDash searches all types of stores, except for some product searches, where it picks a type itself (e.g., `pets`…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search DoorDash stores and dishes by keyword and delivery address, with store name, rating, delivery fee, ETA and menu items.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/doordash/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "pizza", "address": "Austin, TX"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the search query. You can use anything that you would use in a regular DoorDash search (e.g., `pizza`, `sushi`, or `milk`), up to 15 words. |
| `address` | string | Yes | Parameter defines the delivery address to search stores around, like the address set on DoorDash. It can be a street address (e.g., `350 5th Ave, New York, NY 10118`) or a ZIP or postal code (e.g., `10001`). Addresses in the United States,  |
| `store_type` | string | No | Parameter defines the type of stores to search, like the tabs of the DoorDash search page. By default, DoorDash searches all types of stores, except for some product searches, where it picks a type itself (e.g., `pets` for `dog food`). Use  |
| `min_rating` | string | No | Parameter defines the minimum rating of the stores, like the Ratings filter of DoorDash. Available options: `4.5` - Over 4.5 `4.6` - Over 4.6 `4.7` - Over 4.7 `4.8` - Over 4.8 `4.9` - Over 4.9 |
| `deals` | string | No | Parameter defines whether to only show the stores with deals (e.g., `$5 off on $25+`), like the Deals filter of DoorDash. It can be set to `true` or `false` (default). |
| `fastest` | string | No | Parameter defines whether to only show the stores delivering the fastest, like the Fastest filter of DoorDash. It can be set to `true` or `false` (default). |
| `pickup` | string | No | Parameter defines whether to only show the stores offering pickup, with their pickup time and drive time instead of their delivery time and fee, like switching DoorDash from Delivery to Pickup. It can be set to `true` or `false` (default). |
| `page` | string | No | Parameter defines the page number of the results (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, etc.). Each page covers 50 stores. With `deals`, `fastest`, or `min_rating`, there's a single page, like on  |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/doordash/search.json`](../../../catalog/models/doordash/search.json) · Store page: https://www.sandbase.ai/model/doordash/search
