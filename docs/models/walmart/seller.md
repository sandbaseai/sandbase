# Walmart Seller API: pricing, parameters and code examples

`walmart/seller` · data API · Walmart · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get a Walmart marketplace seller page by seller ID, with seller profile, rating, review count and the seller's product listings.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "walmart/seller", "catalog_seller_id": "101025813"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('walmart/seller', {'catalog_seller_id': '101025813'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("walmart/seller", {
  "catalog_seller_id": "101025813"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "walmart/seller", sandbase.Params{
	"catalog_seller_id": "101025813",
})
```

Same call via the path form: `POST /v1/api/walmart/seller` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Parameter defines the page number. Walmart returns up to `40` products per page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Maximum `page`…  |
| `sort` | string |  | Parameter defines the sorting of the seller's products. It defaults to `best_match`. Available options: `best_match` - Best match `price_low` - Price: low to high `price_high` - Price: high to low `best_seller` - Best…  |
| `facet` | string |  | Parameter defines items filtering based on their attributes. The structure is a list of `key:value` pairs separated by `\|\|`. The key and value are separated by `:` (e.g., `brand:Sony\|\|color:Black`).  |
| `include_filters` | string |  | Include `filters` to the JSON response. Set to `true` to enable or `false` to disable (default).  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `catalog_seller_id` | string | yes | Parameter defines the Walmart seller to get results for. It's the number after `/seller/` in the seller page link (e.g., `101025813` in `https://www.walmart.com/seller/101025813`), and the `catalog_seller_id` in our…  |

## Details

Get a Walmart marketplace seller page by seller ID, with seller profile, rating, review count and the seller's product listings.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/walmart/seller" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"catalog_seller_id": "101025813"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `catalog_seller_id` | string | Yes | Parameter defines the Walmart seller to get results for. It's the number after `/seller/` in the seller page link (e.g., `101025813` in `https://www.walmart.com/seller/101025813`), and the `catalog_seller_id` in our Walmart Search API, Walm |
| `sort` | string | No | Parameter defines the sorting of the seller's products. It defaults to `best_match`. Available options: `best_match` - Best match `price_low` - Price: low to high `price_high` - Price: high to low `best_seller` - Best seller `rating_high` - |
| `facet` | string | No | Parameter defines items filtering based on their attributes. The structure is a list of `key:value` pairs separated by `//`. The key and value are separated by `:` (e.g., `brand:Sony//color:Black`). |
| `page` | string | No | Parameter defines the page number. Walmart returns up to `40` products per page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Maximum `page` value is `100`, while  |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `include_filters` | string | No | Include `filters` to the JSON response. Set to `true` to enable or `false` to disable (default). |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/walmart/seller.json`](../../../catalog/models/walmart/seller.json) · Store page: https://www.sandbase.ai/model/walmart/seller
