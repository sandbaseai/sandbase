# Instagram City Locations API: pricing, parameters and code examples

`instagram/v1/locations` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of Instagram location points for a designated city. Filter results using the city identifier and paginate through records by page number.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/locations", "city_id": "c2791472"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/locations', {'city_id': 'c2791472'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/locations", {
  "city_id": "c2791472"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/locations", sandbase.Params{
	"city_id": "c2791472",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/locations` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default 1 range 1– |
| `city_id` | string | yes | City ID (from fetch_cities API)  |

## Details

Returns a page of Instagram location points for one city, each with an ID, a name, and a slug. It needs a `city_id`, such as `c2791472`, and takes an optional `page` number.

### Use cases

- List well-known venues in a city, such as arenas, museums, and markets, to build a local points-of-interest list.
- Collect location IDs for a city to feed into location-based post lookups.
- Page through a city's locations to build a dataset of place names for geo-targeted content research.
- Check which city and country a `city_id` belongs to by reading the returned city and country details.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/locations" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"city_id": "c2791472"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `city_id` | string | Yes | City ID (from fetch_cities API) |
| `page` | integer | No | Page number, default 1 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attempts": "0",
  "city_info": {
    "id": "c2791472",
    "name": "LosAngelesCounty",
    "slug": "losangelescounty-united-states"
  },
  "country_info": {
    "id": "US",
    "name": "United States",
    "slug": "united-states"
  },
  "location_list": [
    {
      "id": "1639313",
      "name": "Crypto.com Arena",
      "slug": "cryptocom-arena"
    }
  ],
  "next_page": 2,
  "status": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `location_list[].id` | Instagram ID of the location. Use it to look up that location in other location APIs. |
| `location_list[].name` | Display name of the location, for example `Crypto.com Arena`. |
| `location_list[].slug` | URL-style short name of the location. |
| `city_info.id / city_info.name / city_info.slug` | ID, name, and slug of the city the locations belong to. The name can appear without spaces, for example `LosAngelesCounty`. |
| `country_info.id / country_info.name / country_info.slug` | Country code, name, and slug for the city. |
| `next_page` | Page number to send as `page` to get the next set of locations. |
| `status` | `true` when the request succeeded. |

### Notes

- Get `city_id` from [Instagram Cities by Country](/apis/instagram/v1/cities). City IDs look like `c2791472`.
- To page through results, repeat the call with `page` set to the value of `next_page`.
- Pass a `location_list[].id` to [Instagram Location Details (V1)](/apis/instagram/v1/location-info) for more detail on a place, or to [Instagram Location Posts (V1)](/apis/instagram/v1/location-posts) for its posts.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/locations.json`](../../../../catalog/models/instagram/v1/locations.json) · Store page: https://www.sandbase.ai/model/instagram/v1/locations
