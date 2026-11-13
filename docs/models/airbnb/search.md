# Airbnb Search API: pricing, parameters and code examples

`airbnb/search` · data API · Airbnb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search Airbnb stays by location and dates, with listing name, price, rating, reviews, room type, photos and coordinates.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "airbnb/search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('airbnb/search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("airbnb/search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "airbnb/search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/airbnb/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Parameter defines the destination to search for. You can use anything that you would use in a regular Airbnb search: a city, a region, a neighborhood, an address, or a landmark (e.g., `Austin, TX`, `Lake Tahoe`, or…  |
| `beds` | string |  | Parameter defines the minimum number of beds.  |
| `luxe` | string |  | Parameter defines whether to only show Airbnb Luxe places, luxury homes with elevated design. It can be set to `true` or `false` (default).  |
| `page` | string |  | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Airbnb returns up to 18 results per page, and…  |
| `pets` | string |  | Parameter defines the number of pets. When set, only places allowing pets are shown.  |
| `adults` | string |  | Parameter defines the number of adults (ages 13 or above).  |
| `infants` | string |  | Parameter defines the number of infants (under 2).  |
| `bedrooms` | string |  | Parameter defines the minimum number of bedrooms.  |
| `children` | string |  | Parameter defines the number of children (ages 2 to 12).  |
| `currency` | string |  | Parameter defines the currency of the returned prices. It defaults to the currency of the Airbnb domain (e.g., `USD` for `airbnb.com`, or `EUR` for `airbnb.fr`). Head to the Airbnb currencies page for a full list of…  |
| `amenities` | string |  | Parameter defines the amenities the places must have. It's a comma-separated list of options (e.g., `wifi,pool,free_parking`). Head to the Airbnb amenities page for a full list of supported amenities.  |
| `bathrooms` | string |  | Parameter defines the minimum number of bathrooms.  |
| `max_price` | string |  | Parameter defines the maximum trip price, including all fees, like Airbnb's price range filter (e.g., `2000`). It's in the currency of the results. When dates aren't set, it applies to a 5-night stay.  |
| `min_price` | string |  | Parameter defines the minimum trip price, including all fees, like Airbnb's price range filter (e.g., `500`). It's in the currency of the results. When dates aren't set, it applies to a 5-night stay.  |
| `room_type` | string |  | Parameter defines the type of place to show. It defaults to any type. Available options: `entire_home` - Entire home `private_room` - Private room To only show hotels, use `hotel` in `property_types`.  |
| `map_bounds` | string |  | Parameter defines the GPS coordinates of the map area to search in, like moving the map on Airbnb. Only places within these bounds are shown. Its value must be 4 comma-separated numbers matching the following format:…  |
| `instant_book` | string |  | Parameter defines whether to only show places that can be booked without waiting for the host's approval. It can be set to `true` or `false` (default).  |
| `airbnb_domain` | string |  | Parameter defines the Airbnb domain to use. The domain sets the language, the region, and the default currency of the results (e.g., `airbnb.co.uk` for English (United Kingdom) in GBP, or `fr.airbnb.ca` for French…  |
| `check_in_date` | string |  | Parameter defines the check-in date. The format is **YYYY-MM-DD** (e.g., `2026-12-12`). It must be used together with `check_out_date`. When dates aren't set, Airbnb suggests dates for each place (usually a 5-night…  |
| `self_check_in` | string |  | Parameter defines whether to only show places with self check-in. It can be set to `true` or `false` (default).  |
| `check_out_date` | string |  | Parameter defines the check-out date. The format is **YYYY-MM-DD** (e.g., `2026-12-16`). It must be used together with `check_in_date`, and be later than it.  |
| `guest_favorite` | string |  | Parameter defines whether to only show Guest favorites, the most loved homes on Airbnb according to guests. It can be set to `true` or `false` (default).  |
| `host_languages` | string |  | Parameter defines the languages the host must speak. It's a comma-separated list of language codes (e.g., `en,es`). Head to the Airbnb host languages page for a full list of supported languages.  |
| `property_types` | string |  | Parameter defines the property types to show. It's a comma-separated list of options (e.g., `house,guesthouse`). Available options: `house` - House `apartment` - Apartment `guesthouse` - Guesthouse `hotel` - Hotel  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `accessibility_features` | string |  | Parameter defines the accessibility features the places must have. It's a comma-separated list of options (e.g., `step_free_access,step_free_shower`). Head to the Airbnb accessibility features page for a full list of…  |

## Details

Search Airbnb stays by location and dates, with listing name, price, rating, reviews, room type, photos and coordinates.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/airbnb/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "Austin, Texas"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | No | Parameter defines the destination to search for. You can use anything that you would use in a regular Airbnb search: a city, a region, a neighborhood, an address, or a landmark (e.g., `Austin, TX`, `Lake Tahoe`, or `Paris, France`). Either  |
| `map_bounds` | string | No | Parameter defines the GPS coordinates of the map area to search in, like moving the map on Airbnb. Only places within these bounds are shown. Its value must be 4 comma-separated numbers matching the following format: `north` + `,` + `east`  |
| `airbnb_domain` | string | No | Parameter defines the Airbnb domain to use. The domain sets the language, the region, and the default currency of the results (e.g., `airbnb.co.uk` for English (United Kingdom) in GBP, or `fr.airbnb.ca` for French (Canada) in CAD). It defau |
| `currency` | string | No | Parameter defines the currency of the returned prices. It defaults to the currency of the Airbnb domain (e.g., `USD` for `airbnb.com`, or `EUR` for `airbnb.fr`). Head to the Airbnb currencies page for a full list of supported currency codes |
| `check_in_date` | string | No | Parameter defines the check-in date. The format is **YYYY-MM-DD** (e.g., `2026-12-12`). It must be used together with `check_out_date`. When dates aren't set, Airbnb suggests dates for each place (usually a 5-night stay), and returns prices |
| `check_out_date` | string | No | Parameter defines the check-out date. The format is **YYYY-MM-DD** (e.g., `2026-12-16`). It must be used together with `check_in_date`, and be later than it. |
| `adults` | string | No | Parameter defines the number of adults (ages 13 or above). |
| `children` | string | No | Parameter defines the number of children (ages 2 to 12). |
| `infants` | string | No | Parameter defines the number of infants (under 2). |
| `pets` | string | No | Parameter defines the number of pets. When set, only places allowing pets are shown. |
| `room_type` | string | No | Parameter defines the type of place to show. It defaults to any type. Available options: `entire_home` - Entire home `private_room` - Private room To only show hotels, use `hotel` in `property_types`. |
| `min_price` | string | No | Parameter defines the minimum trip price, including all fees, like Airbnb's price range filter (e.g., `500`). It's in the currency of the results. When dates aren't set, it applies to a 5-night stay. |
| `max_price` | string | No | Parameter defines the maximum trip price, including all fees, like Airbnb's price range filter (e.g., `2000`). It's in the currency of the results. When dates aren't set, it applies to a 5-night stay. |
| `bedrooms` | string | No | Parameter defines the minimum number of bedrooms. |
| `beds` | string | No | Parameter defines the minimum number of beds. |
| `bathrooms` | string | No | Parameter defines the minimum number of bathrooms. |
| `property_types` | string | No | Parameter defines the property types to show. It's a comma-separated list of options (e.g., `house,guesthouse`). Available options: `house` - House `apartment` - Apartment `guesthouse` - Guesthouse `hotel` - Hotel |
| `amenities` | string | No | Parameter defines the amenities the places must have. It's a comma-separated list of options (e.g., `wifi,pool,free_parking`). Head to the Airbnb amenities page for a full list of supported amenities. |
| `accessibility_features` | string | No | Parameter defines the accessibility features the places must have. It's a comma-separated list of options (e.g., `step_free_access,step_free_shower`). Head to the Airbnb accessibility features page for a full list of supported accessibility |
| `host_languages` | string | No | Parameter defines the languages the host must speak. It's a comma-separated list of language codes (e.g., `en,es`). Head to the Airbnb host languages page for a full list of supported languages. |
| `instant_book` | string | No | Parameter defines whether to only show places that can be booked without waiting for the host's approval. It can be set to `true` or `false` (default). |
| `self_check_in` | string | No | Parameter defines whether to only show places with self check-in. It can be set to `true` or `false` (default). |
| `guest_favorite` | string | No | Parameter defines whether to only show Guest favorites, the most loved homes on Airbnb according to guests. It can be set to `true` or `false` (default). |
| `luxe` | string | No | Parameter defines whether to only show Airbnb Luxe places, luxury homes with elevated design. It can be set to `true` or `false` (default). |
| `page` | string | No | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Airbnb returns up to 18 results per page, and up to 15 pages. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/airbnb/search.json`](../../../catalog/models/airbnb/search.json) · Store page: https://www.sandbase.ai/model/airbnb/search
