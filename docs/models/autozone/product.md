# AutoZone Product API: pricing, parameters and code examples

`autozone/product` · data API · AutoZone · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get an AutoZone part by product ID with brand, part number, price, specifications, warranty, vehicle fitment and store availability.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "autozone/product", "product_id": "992113"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('autozone/product', {'product_id': '992113'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("autozone/product", {
  "product_id": "992113"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "autozone/product", sandbase.Params{
	"product_id": "992113",
})
```

Same call via the path form: `POST /v1/api/autozone/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `store_id` | string |  | Parameter defines the AutoZone store to get the in-store pickup availability for, shown as `in_store_pickup` (e.g., `4254` for 10633 US Hwy 290 E, Manor, TX). The store ID is the store number shown as Store # in…  |
| `product_id` | string | yes | Parameter defines the AutoZone product to get. The product ID is the number at the end of the product's page URL on AutoZone (e.g., `832327` for `https://www.autozone.com/p/duralast-gold-battery-24f-dlg/832327`).  |
| `vehicle_make` | string |  | Parameter defines the make of the vehicle, as named on AutoZone (e.g., `Toyota`). Parameter requires `vehicle_year` and `vehicle_model` parameters to also be set.  |
| `vehicle_type` | string |  | Parameter defines the type of the vehicle. It defaults to `car_truck` when `vehicle_year`, `vehicle_make`, and `vehicle_model` are set. Available options: `car_truck` - Car & Truck `motorcycle` - Motorcycle…  |
| `vehicle_year` | string |  | Parameter defines the year of the vehicle to check the fitment of the product for (e.g., `2015`). Parameter requires `vehicle_make` and `vehicle_model` parameters to also be set.  |
| `vehicle_model` | string |  | Parameter defines the model of the vehicle, as named on AutoZone (e.g., `Camry`). Parameter requires `vehicle_year` and `vehicle_make` parameters to also be set.  |
| `vehicle_token` | string |  | Parameter defines the vehicle with the token of an AutoZone Search API search for it, from `search_information.vehicle.vehicle_token` or the `the API_link` of its results, without looking the vehicle up on AutoZone.…  |
| `vehicle_engine` | string |  | Parameter defines the engine of the vehicle, as named on AutoZone (e.g., `4 Cylinders 2.5L GAS`). Parameter requires `vehicle_year`, `vehicle_make`, and `vehicle_model` parameters to also be set.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `vehicle_submodel` | string |  | Parameter defines the submodel of the vehicle, as named on AutoZone (e.g., `LE`). Without it, products that only fit some submodels have a `fitment: needs_more_info`. Parameter requires `vehicle_year`, `vehicle_make`,…  |

## Details

Get an AutoZone part by product ID with brand, part number, price, specifications, warranty, vehicle fitment and store availability.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/autozone/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "992113"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Parameter defines the AutoZone product to get. The product ID is the number at the end of the product's page URL on AutoZone (e.g., `832327` for `https://www.autozone.com/p/duralast-gold-battery-24f-dlg/832327`). |
| `store_id` | string | No | Parameter defines the AutoZone store to get the in-store pickup availability for, shown as `in_store_pickup` (e.g., `4254` for 10633 US Hwy 290 E, Manor, TX). The store ID is the store number shown as Store # in AutoZone's store details. |
| `vehicle_year` | string | No | Parameter defines the year of the vehicle to check the fitment of the product for (e.g., `2015`). Parameter requires `vehicle_make` and `vehicle_model` parameters to also be set. |
| `vehicle_make` | string | No | Parameter defines the make of the vehicle, as named on AutoZone (e.g., `Toyota`). Parameter requires `vehicle_year` and `vehicle_model` parameters to also be set. |
| `vehicle_model` | string | No | Parameter defines the model of the vehicle, as named on AutoZone (e.g., `Camry`). Parameter requires `vehicle_year` and `vehicle_make` parameters to also be set. |
| `vehicle_engine` | string | No | Parameter defines the engine of the vehicle, as named on AutoZone (e.g., `4 Cylinders 2.5L GAS`). Parameter requires `vehicle_year`, `vehicle_make`, and `vehicle_model` parameters to also be set. |
| `vehicle_submodel` | string | No | Parameter defines the submodel of the vehicle, as named on AutoZone (e.g., `LE`). Without it, products that only fit some submodels have a `fitment: needs_more_info`. Parameter requires `vehicle_year`, `vehicle_make`, and `vehicle_model` pa |
| `vehicle_type` | string | No | Parameter defines the type of the vehicle. It defaults to `car_truck` when `vehicle_year`, `vehicle_make`, and `vehicle_model` are set. Available options: `car_truck` - Car & Truck `motorcycle` - Motorcycle `recreational` - Recreational Par |
| `vehicle_token` | string | No | Parameter defines the vehicle with the token of an AutoZone Search API search for it, from `search_information.vehicle.vehicle_token` or the `the API_link` of its results, without looking the vehicle up on AutoZone. Parameter can't be used  |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/autozone/product.json`](../../../catalog/models/autozone/product.json) · Store page: https://www.sandbase.ai/model/autozone/product
