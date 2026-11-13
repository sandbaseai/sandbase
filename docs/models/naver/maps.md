# Naver Maps Search API: pricing, parameters and code examples

`naver/maps` · data API · Naver · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search places on Naver Maps by keyword around a location, with name, category, rating, reviews, address, phone and booking options.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "naver/maps", "query": "카페"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('naver/maps', {'query': '카페'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("naver/maps", {
  "query": "카페"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "naver/maps", sandbase.Params{
	"query": "카페",
})
```

Same call via the path form: `POST /v1/api/naver/maps` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Naver Maps returns up to 70 results per page,…  |
| `query` | string | yes | Parameter defines the query you want to search. You can use anything that you would use in a regular Naver Maps search.  |
| `adults` | string |  | Parameter defines the number of adults. It's used together with `check_in_date` and `check_out_date`, and ignored without them. `adults` and `children` can add up to 15 guests, the most Naver Maps allows.  |
| `center` | string |  | Parameter defines the coordinates of the point in South Korea to search around, as `latitude,longitude` (e.g. `35.1796,129.0756` for Busan). The `distance` of each result is measured from this point. Naver Maps…  |
| `coupon` | string |  | Parameter defines whether to only show places with a coupon. It can be set to `true` or `false` (default). Hospitals, pharmacies, animal hospitals, convenience stores, movie theaters, gas stations, and franchise lists…  |
| `sort_by` | string |  | Parameter defines the order of the results. By default, results come in the order of the Naver Maps list. Options: `distance` - Distance Lists of franchise branches, such as 스타벅스, are already sorted by distance, and… one of: `distance` |
| `bookable` | string |  | Parameter defines whether to only show places that can be booked on Naver. It can be set to `true` or `false` (default). Pharmacies, convenience stores, movie theaters, gas stations, franchise lists, and accommodations…  |
| `children` | string |  | Parameter defines the number of children. It's used together with `check_in_date` and `check_out_date`, and ignored without them. Naver Maps has a single guest count, so children are added to adults: `adults=2` and…  |
| `open_state` | string |  | Parameter defines the open state of the places. Options: `now` - Open now It applies to restaurants and cafes, hospitals, pharmacies, animal hospitals, gyms and other leisure places, and attractions such as parks. The… one of: `now` |
| `check_in_date` | string |  | Parameter defines the check-in date. The format is **YYYY-MM-DD** (e.g., `2026-12-12`). It must be used together with `check_out_date`. Dates apply to accommodation lists, such as 펜션, 캠핑장, and 글램핑. With dates, Naver…  |
| `check_out_date` | string |  | Parameter defines the check-out date. The format is **YYYY-MM-DD** (e.g., `2026-12-14`). It must be used together with `check_in_date`, and be later than it.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `wheelchair_accessible` | string |  | Parameter defines whether to only show places with a wheelchair accessible entrance. It can be set to `true` or `false` (default). Convenience stores, movie theaters, gas stations, and franchise lists ignore it.  |

## Details

Search places on Naver Maps by keyword around a location, with name, category, rating, reviews, address, phone and booking options.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/naver/maps" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "카페"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Parameter defines the query you want to search. You can use anything that you would use in a regular Naver Maps search. |
| `center` | string | No | Parameter defines the coordinates of the point in South Korea to search around, as `latitude,longitude` (e.g. `35.1796,129.0756` for Busan). The `distance` of each result is measured from this point. Naver Maps searches around Seoul City Ha |
| `sort_by` | string | No | Parameter defines the order of the results. By default, results come in the order of the Naver Maps list. Options: `distance` - Distance Lists of franchise branches, such as 스타벅스, are already sorted by distance, and mart lists keep their ow |
| `open_state` | string | No | Parameter defines the open state of the places. Options: `now` - Open now It applies to restaurants and cafes, hospitals, pharmacies, animal hospitals, gyms and other leisure places, and attractions such as parks. The other lists ignore it. |
| `bookable` | string | No | Parameter defines whether to only show places that can be booked on Naver. It can be set to `true` or `false` (default). Pharmacies, convenience stores, movie theaters, gas stations, franchise lists, and accommodations ignore it. Mart lists |
| `coupon` | string | No | Parameter defines whether to only show places with a coupon. It can be set to `true` or `false` (default). Hospitals, pharmacies, animal hospitals, convenience stores, movie theaters, gas stations, and franchise lists ignore it. |
| `wheelchair_accessible` | string | No | Parameter defines whether to only show places with a wheelchair accessible entrance. It can be set to `true` or `false` (default). Convenience stores, movie theaters, gas stations, and franchise lists ignore it. |
| `check_in_date` | string | No | Parameter defines the check-in date. The format is **YYYY-MM-DD** (e.g., `2026-12-12`). It must be used together with `check_out_date`. Dates apply to accommodation lists, such as 펜션, 캠핑장, and 글램핑. With dates, Naver Maps only returns the pl |
| `check_out_date` | string | No | Parameter defines the check-out date. The format is **YYYY-MM-DD** (e.g., `2026-12-14`). It must be used together with `check_in_date`, and be later than it. |
| `adults` | string | No | Parameter defines the number of adults. It's used together with `check_in_date` and `check_out_date`, and ignored without them. `adults` and `children` can add up to 15 guests, the most Naver Maps allows. |
| `children` | string | No | Parameter defines the number of children. It's used together with `check_in_date` and `check_out_date`, and ignored without them. Naver Maps has a single guest count, so children are added to adults: `adults=2` and `children=1` search for 3 |
| `page` | string | No | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Naver Maps returns up to 70 results per page, and up to 300 results ( |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/naver/maps.json`](../../../catalog/models/naver/maps.json) · Store page: https://www.sandbase.ai/model/naver/maps
