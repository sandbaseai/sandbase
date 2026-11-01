# eBay Search

`ebay/search` · api · eBay

Search eBay listings by keyword with price, condition, shipping, bids, time left and seller, plus condition, format, price and location filters.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ebay/search", "_nkw": "iphone 15"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ebay/search', {'_nkw': 'iphone 15'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ebay/search", {
  "_nkw": "iphone 15"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ebay/search", sandbase.Params{
	"_nkw": "iphone 15",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ebay/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `_dmd` | string \\| number \\| boolean |  | The visual layout for displaying results. The available options are 'Grid' and 'List'.  |
| `_ipg` | string \\| number \\| boolean |  | The maximum number of results to return. There are three options: `60` (default), `120` and `240` results.  |
| `_nkw` | string \\| number \\| boolean | yes | The search query. You can use anything that you would use in a regular eBay search. `_nkw` parameter is optional when `category_id` parameter is specified.  |
| `_pgn` | string \\| number \\| boolean |  | The page number. It's used for pagination. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.).  |
| `_sop` | string \\| number \\| boolean |  | Results sorted by different options in the eBay. The default option is 'Best Match'. Head to the eBay sort options for a full list of supported sort options.  |
| `_blrs` | string \\| number \\| boolean |  | The exclusion of results from an auto-corrected query when the original query is spelled wrong. The recommended value for this parameter is `spell_auto_correct`. Omit `_blrs` if you want the search to include results…  |
| `_sasl` | string \\| number \\| boolean |  | The seller username(s) to filter results by. You can specify multiple sellers separated by commas (e.g. `iRobot,samsung`). Use with `_saslop` to control whether to include or exclude items from the specified seller(s).  |
| `_udhi` | string \\| number \\| boolean |  | The highest price of items that should be included in the results (e.g. `20` will only return items that have lower price than `20`).  |
| `_udlo` | string \\| number \\| boolean |  | The lowest price of items that should be included in the results (e.g. `10` will only return items that have higher price than `10`).  |
| `_salic` | string \\| number \\| boolean |  | The location based on country. Head to the eBay location options for a full list of supported countries.  |
| `_stpos` | string \\| number \\| boolean |  | The ZIP or Postal code. You can use it to filter the shipping products by a selected area.  |
| `_saslop` |  |  | Whether to include or exclude items from the seller(s) specified in `_sasl`. Available options: `1` - Only show items from sellers (default) `2` - Don't show items from sellers  |
| `show_only` | string |  | The list of filters you can apply to the results. Available options **(case-sensitive)**: `FR` - Free returns `RPA` - Returns accepted `AS` - Authorized seller `Savings` - Deals and savings `SaleItems` - Sale items…  |
| `LH_PrefLoc` | string \\| number \\| boolean |  | The preferred location. The available options are 'Domestic', 'Regional', and 'Worldwide'.  |
| `category_id` | string \\| number \\| boolean |  | The ID of a category where you want your search to be concentrated. ID values are accessible inside `categories` array, located in our JSON output (e.g. `categories[1].id`). You can search using `category_id` parameter…  |
| `ebay_domain` | string \\| number \\| boolean |  | The eBay domain to use. It defaults to `ebay.com`. Head to the eBay domains for a full list of supported eBay domains.  |
| `buying_format` |  |  | The buying format you can apply to the results. Available options **(case-sensitive)**: `Auction` - Auction `BIN` - Buy It Now `BO` - Accepts Offers  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `popular_filters` | string \\| number \\| boolean |  | Allows filtering items based on their attributes. The structure is a list of `key=value` pairs separated by `&` (e.g. `Brand=Nespresso&Size=L`). To pass multiple values for the same filter, join them with `\|` (e.g.…  |
| `LH_ItemCondition` | string \\| number \\| boolean |  | One or multiple product conditions to limit the search to. Condition is represented via numeric ID, e.g. `1000` for `New`. Multiple IDs should be joined with `\|` delimiter, e.g. `1000\|3000`. List of supported IDs can…  |

## Details

Search eBay listings by keyword with price, condition, shipping, bids, time left and seller, plus condition, format, price and location filters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ebay/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"_nkw": "iphone 15"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `_nkw` | string/number/boolean | Yes | The search query. You can use anything that you would use in a regular eBay search. `_nkw` parameter is optional when `category_id` parameter is specified. |
| `LH_ItemCondition` | string/number/boolean | No | One or multiple product conditions to limit the search to. Condition is represented via numeric ID, e.g. `1000` for `New`. Multiple IDs should be joined with `\|` delimiter, e.g. `1000\|3000`. List of… |
| `LH_PrefLoc` | string/number/boolean | No | The preferred location. The available options are 'Domestic', 'Regional', and 'Worldwide'. |
| `_blrs` | string/number/boolean | No | The exclusion of results from an auto-corrected query when the original query is spelled wrong. The recommended value for this parameter is `spell_auto_correct`. Omit `_blrs` if you want the search to… |
| `_dmd` | string/number/boolean | No | The visual layout for displaying results. The available options are 'Grid' and 'List'. |
| `_ipg` | string/number/boolean | No | The maximum number of results to return. There are three options: `60` (default), `120` and `240` results. |
| `_pgn` | string/number/boolean | No | The page number. It's used for pagination. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). |
| `_salic` | string/number/boolean | No | The location based on country. Head to the eBay location options for a full list of supported countries. |
| `_sasl` | string/number/boolean | No | The seller username(s) to filter results by. You can specify multiple sellers separated by commas (e.g. `iRobot,samsung`). Use with `_saslop` to control whether to include or exclude items from the sp… |
| `_saslop` | any | No | Whether to include or exclude items from the seller(s) specified in `_sasl`. Available options: `1` - Only show items from sellers (default) `2` - Don't show items from sellers |
| `_sop` | string/number/boolean | No | Results sorted by different options in the eBay. The default option is 'Best Match'. Head to the eBay sort options for a full list of supported sort options. |
| `_stpos` | string/number/boolean | No | The ZIP or Postal code. You can use it to filter the shipping products by a selected area. |
| `_udhi` | string/number/boolean | No | The highest price of items that should be included in the results (e.g. `20` will only return items that have lower price than `20`). |
| `_udlo` | string/number/boolean | No | The lowest price of items that should be included in the results (e.g. `10` will only return items that have higher price than `10`). |
| `buying_format` | any | No | The buying format you can apply to the results. Available options **(case-sensitive)**: `Auction` - Auction `BIN` - Buy It Now `BO` - Accepts Offers |
| `category_id` | string/number/boolean | No | The ID of a category where you want your search to be concentrated. ID values are accessible inside `categories` array, located in our JSON output (e.g. `categories[1].id`). You can search using `cate… |
| `ebay_domain` | string/number/boolean | No | The eBay domain to use. It defaults to `ebay.com`. Head to the eBay domains for a full list of supported eBay domains. |
| `json_restrictor` | string/number/boolean | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `popular_filters` | string/number/boolean | No | Allows filtering items based on their attributes. The structure is a list of `key=value` pairs separated by `&` (e.g. `Brand=Nespresso&Size=L`). To pass multiple values for the same filter, join them … |
| `show_only` | string | No | The list of filters you can apply to the results. Available options **(case-sensitive)**: `FR` - Free returns `RPA` - Returns accepted `AS` - Authorized seller `Savings` - Deals and savings `SaleItems… |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ebay/search.json`](../../../catalog/models/ebay/search.json) · Store page: https://www.sandbase.ai/model/ebay/search
