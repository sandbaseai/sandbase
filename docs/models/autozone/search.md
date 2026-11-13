# AutoZone Search API: pricing, parameters and code examples

`autozone/search` · data API · AutoZone · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search AutoZone auto parts by keyword, optionally for a specific vehicle and store, with part number, brand, price, rating and availability.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "autozone/search", "q": "oil filter"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('autozone/search', {'q': 'oil filter'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("autozone/search", {
  "q": "oil filter"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "autozone/search", sandbase.Params{
	"q": "oil filter",
})
```

Same call via the path form: `POST /v1/api/autozone/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the query you want to search. You can use anything that you would use in a regular AutoZone search (e.g., `oil filter`, `brake pads`, or a part number like `S9972`).  |
| `ps` | string |  | Parameter defines the number of results per page, between `1` and `100`. It defaults to `24`.  |
| `page` | string |  | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.).  |
| `sort` | string |  | Parameter defines the sorting of the results. It defaults to `featured`. Available options: `featured` - Featured `price_low` - Price (low to high) `price_high` - Price (high to low) `recently_added` - Recently Added…  |
| `facet` | string |  | Parameter defines the filters to apply. It's a comma-separated list of filter values (e.g., `sub_brand_name_display_s:Duralast,avg_rating_range_ss:2~4 TO *~4 and up` for **Duralast** with **4 stars and up**). Filter…  |
| `store_id` | string |  | Parameter defines the AutoZone store to search (e.g., `4254`). The store changes the order of the results and adds their `in_store_pickup` availability. It defaults to `6997`, the store AutoZone uses when no store is…  |
| `max_price` | string |  | Parameter defines the maximum price of the products, in whole US dollars (e.g., `50`).  |
| `min_price` | string |  | Parameter defines the minimum price of the products, in whole US dollars (e.g., `20`).  |
| `vehicle_make` | string |  | Parameter defines the make of the vehicle, as named on AutoZone (e.g., `Toyota`). Parameter requires `vehicle_year` and `vehicle_model` parameters to also be set.  |
| `vehicle_type` | string |  | Parameter defines the type of the vehicle. It defaults to `car_truck` when `vehicle_year`, `vehicle_make`, and `vehicle_model` are set. Available options: `car_truck` - Car & Truck `motorcycle` - Motorcycle…  |
| `vehicle_year` | string |  | Parameter defines the year of the vehicle to find parts for (e.g., `2015`). Parameter requires `vehicle_make` and `vehicle_model` parameters to also be set.  |
| `vehicle_model` | string |  | Parameter defines the model of the vehicle, as named on AutoZone (e.g., `Camry`). Parameter requires `vehicle_year` and `vehicle_make` parameters to also be set.  |
| `vehicle_engine` | string |  | Parameter defines the engine of the vehicle, as named on AutoZone (e.g., `4 Cylinders 2.5L GAS`). Parameter requires `vehicle_year`, `vehicle_make`, and `vehicle_model` parameters to also be set.  |
| `include_filters` | string |  | Parameter defines whether to include the `filters` of the search in the JSON response, with the values to use in `facet`. It can be set to `true` or `false` (default).  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `vehicle_submodel` | string |  | Parameter defines the submodel of the vehicle, as named on AutoZone (e.g., `LE`). Without it, parts that only fit some submodels have a `fitment: needs_more_info`. Parameter requires `vehicle_year`, `vehicle_make`, and…  |

## Details

Search AutoZone auto parts by keyword, optionally for a specific vehicle and store, with part number, brand, price, rating and availability.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/autozone/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "oil filter"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the query you want to search. You can use anything that you would use in a regular AutoZone search (e.g., `oil filter`, `brake pads`, or a part number like `S9972`). |
| `store_id` | string | No | Parameter defines the AutoZone store to search (e.g., `4254`). The store changes the order of the results and adds their `in_store_pickup` availability. It defaults to `6997`, the store AutoZone uses when no store is selected. |
| `vehicle_year` | string | No | Parameter defines the year of the vehicle to find parts for (e.g., `2015`). Parameter requires `vehicle_make` and `vehicle_model` parameters to also be set. |
| `vehicle_make` | string | No | Parameter defines the make of the vehicle, as named on AutoZone (e.g., `Toyota`). Parameter requires `vehicle_year` and `vehicle_model` parameters to also be set. |
| `vehicle_model` | string | No | Parameter defines the model of the vehicle, as named on AutoZone (e.g., `Camry`). Parameter requires `vehicle_year` and `vehicle_make` parameters to also be set. |
| `vehicle_engine` | string | No | Parameter defines the engine of the vehicle, as named on AutoZone (e.g., `4 Cylinders 2.5L GAS`). Parameter requires `vehicle_year`, `vehicle_make`, and `vehicle_model` parameters to also be set. |
| `vehicle_submodel` | string | No | Parameter defines the submodel of the vehicle, as named on AutoZone (e.g., `LE`). Without it, parts that only fit some submodels have a `fitment: needs_more_info`. Parameter requires `vehicle_year`, `vehicle_make`, and `vehicle_model` param |
| `vehicle_type` | string | No | Parameter defines the type of the vehicle. It defaults to `car_truck` when `vehicle_year`, `vehicle_make`, and `vehicle_model` are set. Available options: `car_truck` - Car & Truck `motorcycle` - Motorcycle `recreational` - Recreational Par |
| `sort` | string | No | Parameter defines the sorting of the results. It defaults to `featured`. Available options: `featured` - Featured `price_low` - Price (low to high) `price_high` - Price (high to low) `recently_added` - Recently Added `rating_high` - Custome |
| `facet` | string | No | Parameter defines the filters to apply. It's a comma-separated list of filter values (e.g., `sub_brand_name_display_s:Duralast,avg_rating_range_ss:2~4 TO *~4 and up` for **Duralast** with **4 stars and up**). Filter values are available in  |
| `min_price` | string | No | Parameter defines the minimum price of the products, in whole US dollars (e.g., `20`). |
| `max_price` | string | No | Parameter defines the maximum price of the products, in whole US dollars (e.g., `50`). |
| `page` | string | No | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). |
| `ps` | string | No | Parameter defines the number of results per page, between `1` and `100`. It defaults to `24`. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `include_filters` | string | No | Parameter defines whether to include the `filters` of the search in the JSON response, with the values to use in `facet`. It can be set to `true` or `false` (default). |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/autozone/search.json`](../../../catalog/models/autozone/search.json) · Store page: https://www.sandbase.ai/model/autozone/search
