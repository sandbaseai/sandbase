# Zillow Search API: pricing, parameters and code examples

`zillow/search` · data API · Zillow · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search Zillow listings by region or map bounds with status, price, beds, baths, home type and size filters, returning address, price, Zestimate and listing links.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zillow/search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zillow/search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zillow/search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zillow/search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/zillow/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `beds` | string |  | Parameter defines the number of bedrooms. Provide a single number for a minimum (e.g., `2` for 2+ bedrooms), or two comma-separated numbers for a min/max range (e.g., `1,3`). To set a maximum only, omit the first…  |
| `page` | string |  | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.).  |
| `pets` | string |  | Parameter defines the pet policies the rentals must have. It's a comma-separated list of options (e.g., `cats,small_dogs`). `no_pets` cannot be combined with the other options. It only applies when `status_type` is…  |
| `sqft` | string |  | Parameter defines the square footage of the properties to show. Provide a single number for a minimum (e.g., `1250`), or two comma-separated numbers for a min/max range (e.g., `1250,3000`). To set a maximum only, omit…  |
| `view` | string |  | Parameter defines the views the properties must have. It's a comma-separated list of options (e.g., `city,water`). Available options: `city` - City `mountain` - Mountain `park` - Park `water` - Water  |
| `baths` | string |  | Parameter defines the number of bathrooms. Provide a single number for a minimum (e.g., `2` for 2+ bathrooms), or two comma-separated numbers for a min/max range (e.g., `1,3`). To set a maximum only, omit the first…  |
| `price` | string |  | Parameter defines the price range of the properties to show. Provide a single number for a minimum (e.g., `100000`), or two comma-separated numbers for a min/max range (e.g., `100000,400000`). To set a maximum only,…  |
| `space` | string |  | Parameter defines the type of rental space to show. It only applies when `status_type` is `rent`. It defaults to `entire_place`. Available options: `any` - Any `entire_place` - Entire place `room` - Room for rent  |
| `tours` | string |  | Parameter defines the tour options the properties must have. It's a comma-separated list of options (e.g., `open_house,3d_tour`). It only applies when `status_type` is `sale`. Available options: `open_house` - Must…  |
| `hoa_max` | string |  | Parameter defines the maximum HOA (Homeowners Association) fee of the properties to show. Set it to `0` to only show properties with no HOA fee. It defaults to any HOA fee. It only applies when `status_type` is `sale`…  |
| `sort_by` | string |  | Parameter defines the sorting order of the results. It defaults to `globalrelevanceex` (Homes for You). Available options: `globalrelevanceex` - Homes for You `featured` - Verified Source `priced` - Price (high to low)…  |
| `basement` | string |  | Parameter defines the type of basement the properties must have. It's a comma-separated list of options (e.g., `finished,unfinished`). It only applies when `status_type` is `sale` or `sold`. Available options:…  |
| `keywords` | string |  | Parameter defines the keywords to filter the results by. It's a comma-separated list of keywords (e.g., `yard` or `pool, bbq`).  |
| `lot_size` | string |  | Parameter defines the lot size of the properties to show, in square feet. Provide a single number for a minimum (e.g., `21780`), or two comma-separated numbers for a min/max range (e.g., `21780,217800`). To set a…  |
| `amenities` | string |  | Parameter defines the amenities the properties must have. It's a comma-separated list of options (e.g., `ac,pool`). The available options depend on `status_type`. Options when `status_type` is `sale` or `sold`: `ac` -… one of: `ac`, `pool`, `waterfront`, `in_unit_laundry`, `parking`, `ac`, `utilities_included`, `elevator`, `basement`, `dishwasher`, `fitness_center`, `hardwood_floor` … |
| `home_type` | string |  | Parameter defines the types of homes to show. It's a comma-separated list acting as the complete selection: only the listed types are shown, and every other type is excluded (e.g., `house,condo` only shows houses and… one of: `house`, `townhome`, `multi_family`, `condo`, `lot_land`, `apartment`, `manufactured`, `house`, `apartment_condo`, `townhome` |
| `region_id` | string |  | Parameter defines the Zillow region ID for the area you want to search in. A region can be a city, neighborhood, ZIP Code, county, or state (e.g., `10221` for Austin, TX). To find a Region ID, go to Zillow, search for…  |
| `has_garage` | string |  | Parameter defines whether to only show properties with a garage. It can be set to `true` to only show properties with a garage, or `false` (default) to show all properties.  |
| `map_bounds` | string |  | Parameter defines the GPS coordinates of the map area to search in, so only properties within these bounds are shown. Its value must be 4 comma-separated numbers matching the following format: `north` + `,` + `east` +…  |
| `year_built` | string |  | Parameter defines the year the properties were built. Provide a single year for a minimum (e.g., `2000`), or two comma-separated years for a min/max range (e.g., `2000,2010`). To set a maximum only, omit the first year…  |
| `age_55_plus` | string |  | Parameter defines how to handle 55+ communities. It defaults to `include`. Available options: `include` - Include 55+ communities `exclude` - Exclude 55+ communities `only` - Only show 55+ communities  |
| `status_type` | string |  | Parameter defines the type of properties to show. It defaults to `sale`. It also determines which filters are applicable. Available options: `sale` - For sale `rent` - For rent `sold` - Sold  |
| `listing_type` | string |  | Parameter defines the complete list of listing types to show, comma-separated: only the listed types are included, and all others are excluded. It only applies when `status_type` is `sale`. When not set, it defaults to…  |
| `move_in_date` | string |  | Parameter defines the latest move-in date of the rentals to show: only rentals available on or before the date are shown. Provide a date in `YYYY-MM-DD` format (e.g., `2026-07-22`). It only applies when `status_type`…  |
| `single_story` | string |  | Parameter defines whether to only show single-story properties. It can be set to `true` to only show single-story properties, or `false` (default) to show all properties.  |
| `parking_spots` | string |  | Parameter defines the minimum number of parking spots the properties must have (e.g., `2` for 2+ parking spots). It only applies when `status_type` is `sale` or `sold`.  |
| `listing_status` | string |  | Parameter defines the complete list of listing statuses to show, comma-separated: only the listed statuses are included, and all others are excluded. It only applies when `status_type` is `sale`. When not set, it…  |
| `time_on_zillow` | string |  | Parameter defines the maximum time the properties have been listed on Zillow. Provide a number of days (e.g., `14` for 14 days), or one of the supported month values: `6m`, `12m`, `24m`, or `36m`. It defaults to any…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `price_reduction` | string |  | Parameter defines whether to only show properties with a price reduction. It can be set to `true` to only show properties with a price reduction, or `false` (default) to show all properties.  |
| `listing_features` | string |  | Parameter defines the listing features the rentals must have. It's a comma-separated list of options (e.g., `3d_tour,instant_tour`). It only applies when `status_type` is `rent`. Available options: `3d_tour` - Must…  |
| `short_term_lease` | string |  | Parameter defines whether to only show rentals with a short-term lease available. It can be set to `true` to only show them, or `false` (default) to show all rentals. It only applies when `status_type` is `rent`.  |
| `hide_no_date_listings` | string |  | Parameter defines whether to hide rentals that don't specify an availability date. It can be set to `true` to hide them, or `false` (default) to show them. It's meant to be used together with `move_in_date`, and only…  |

## Details

Search Zillow listings by region or map bounds with status, price, beds, baths, home type and size filters, returning address, price, Zestimate and listing links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zillow/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"region_id": "10221"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `region_id` | string | No | Parameter defines the Zillow region ID for the area you want to search in. A region can be a city, neighborhood, ZIP Code, county, or state (e.g., `10221` for Austin, TX). To find a Region ID, go to Zillow, search for the area you want, and |
| `map_bounds` | string | No | Parameter defines the GPS coordinates of the map area to search in, so only properties within these bounds are shown. Its value must be 4 comma-separated numbers matching the following format: `north` + `,` + `east` + `,` + `south` + `,` +  |
| `status_type` | string | No | Parameter defines the type of properties to show. It defaults to `sale`. It also determines which filters are applicable. Available options: `sale` - For sale `rent` - For rent `sold` - Sold |
| `price` | string | No | Parameter defines the price range of the properties to show. Provide a single number for a minimum (e.g., `100000`), or two comma-separated numbers for a min/max range (e.g., `100000,400000`). To set a maximum only, omit the first number (e |
| `beds` | string | No | Parameter defines the number of bedrooms. Provide a single number for a minimum (e.g., `2` for 2+ bedrooms), or two comma-separated numbers for a min/max range (e.g., `1,3`). To set a maximum only, omit the first number (e.g., `,3`). |
| `baths` | string | No | Parameter defines the number of bathrooms. Provide a single number for a minimum (e.g., `2` for 2+ bathrooms), or two comma-separated numbers for a min/max range (e.g., `1,3`). To set a maximum only, omit the first number (e.g., `,3`). |
| `home_type` | string | No | Parameter defines the types of homes to show. It's a comma-separated list acting as the complete selection: only the listed types are shown, and every other type is excluded (e.g., `house,condo` only shows houses and condos). To exclude a s |
| `sqft` | string | No | Parameter defines the square footage of the properties to show. Provide a single number for a minimum (e.g., `1250`), or two comma-separated numbers for a min/max range (e.g., `1250,3000`). To set a maximum only, omit the first number (e.g. |
| `year_built` | string | No | Parameter defines the year the properties were built. Provide a single year for a minimum (e.g., `2000`), or two comma-separated years for a min/max range (e.g., `2000,2010`). To set a maximum only, omit the first year (e.g., `,2010`). |
| `has_garage` | string | No | Parameter defines whether to only show properties with a garage. It can be set to `true` to only show properties with a garage, or `false` (default) to show all properties. |
| `single_story` | string | No | Parameter defines whether to only show single-story properties. It can be set to `true` to only show single-story properties, or `false` (default) to show all properties. |
| `age_55_plus` | string | No | Parameter defines how to handle 55+ communities. It defaults to `include`. Available options: `include` - Include 55+ communities `exclude` - Exclude 55+ communities `only` - Only show 55+ communities |
| `amenities` | string | No | Parameter defines the amenities the properties must have. It's a comma-separated list of options (e.g., `ac,pool`). The available options depend on `status_type`. Options when `status_type` is `sale` or `sold`: `ac` - Must have A/C `pool` - |
| `view` | string | No | Parameter defines the views the properties must have. It's a comma-separated list of options (e.g., `city,water`). Available options: `city` - City `mountain` - Mountain `park` - Park `water` - Water |
| `price_reduction` | string | No | Parameter defines whether to only show properties with a price reduction. It can be set to `true` to only show properties with a price reduction, or `false` (default) to show all properties. |
| `time_on_zillow` | string | No | Parameter defines the maximum time the properties have been listed on Zillow. Provide a number of days (e.g., `14` for 14 days), or one of the supported month values: `6m`, `12m`, `24m`, or `36m`. It defaults to any time. |
| `keywords` | string | No | Parameter defines the keywords to filter the results by. It's a comma-separated list of keywords (e.g., `yard` or `pool, bbq`). |
| `hoa_max` | string | No | Parameter defines the maximum HOA (Homeowners Association) fee of the properties to show. Set it to `0` to only show properties with no HOA fee. It defaults to any HOA fee. It only applies when `status_type` is `sale` or `sold`. |
| `parking_spots` | string | No | Parameter defines the minimum number of parking spots the properties must have (e.g., `2` for 2+ parking spots). It only applies when `status_type` is `sale` or `sold`. |
| `lot_size` | string | No | Parameter defines the lot size of the properties to show, in square feet. Provide a single number for a minimum (e.g., `21780`), or two comma-separated numbers for a min/max range (e.g., `21780,217800`). To set a maximum only, omit the firs |
| `basement` | string | No | Parameter defines the type of basement the properties must have. It's a comma-separated list of options (e.g., `finished,unfinished`). It only applies when `status_type` is `sale` or `sold`. Available options: `finished` - Finished `unfinis |
| `listing_type` | string | No | Parameter defines the complete list of listing types to show, comma-separated: only the listed types are included, and all others are excluded. It only applies when `status_type` is `sale`. When not set, it defaults to `owner,agent,new_cons |
| `listing_status` | string | No | Parameter defines the complete list of listing statuses to show, comma-separated: only the listed statuses are included, and all others are excluded. It only applies when `status_type` is `sale`. When not set, it defaults to `active,coming_ |
| `tours` | string | No | Parameter defines the tour options the properties must have. It's a comma-separated list of options (e.g., `open_house,3d_tour`). It only applies when `status_type` is `sale`. Available options: `open_house` - Must have open house `3d_tour` |
| `space` | string | No | Parameter defines the type of rental space to show. It only applies when `status_type` is `rent`. It defaults to `entire_place`. Available options: `any` - Any `entire_place` - Entire place `room` - Room for rent |
| `move_in_date` | string | No | Parameter defines the latest move-in date of the rentals to show: only rentals available on or before the date are shown. Provide a date in `YYYY-MM-DD` format (e.g., `2026-07-22`). It only applies when `status_type` is `rent`. Rentals with |
| `hide_no_date_listings` | string | No | Parameter defines whether to hide rentals that don't specify an availability date. It can be set to `true` to hide them, or `false` (default) to show them. It's meant to be used together with `move_in_date`, and only applies when `status_ty |
| `pets` | string | No | Parameter defines the pet policies the rentals must have. It's a comma-separated list of options (e.g., `cats,small_dogs`). `no_pets` cannot be combined with the other options. It only applies when `status_type` is `rent`. Available options |
| `listing_features` | string | No | Parameter defines the listing features the rentals must have. It's a comma-separated list of options (e.g., `3d_tour,instant_tour`). It only applies when `status_type` is `rent`. Available options: `3d_tour` - Must have 3D Tour `accepts_app |
| `short_term_lease` | string | No | Parameter defines whether to only show rentals with a short-term lease available. It can be set to `true` to only show them, or `false` (default) to show all rentals. It only applies when `status_type` is `rent`. |
| `sort_by` | string | No | Parameter defines the sorting order of the results. It defaults to `globalrelevanceex` (Homes for You). Available options: `globalrelevanceex` - Homes for You `featured` - Verified Source `priced` - Price (high to low) `pricea` - Price (low |
| `page` | string | No | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/zillow/search.json`](../../../catalog/models/zillow/search.json) · Store page: https://www.sandbase.ai/model/zillow/search
