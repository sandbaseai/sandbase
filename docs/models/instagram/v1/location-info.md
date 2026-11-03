# Instagram Location Details (V1) API: pricing, parameters and code examples

`instagram/v1/location-info` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/location-info", "location_id": "703457703"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/location-info', {'location_id': '703457703'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/location-info", {
  "location_id": "703457703"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/location-info", sandbase.Params{
	"location_id": "703457703",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/location-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `location_id` | string | yes | Location ID  |

## Details

Returns metadata for one Instagram location, including its name, category, coordinates, and the number of posts tagged there. It needs a single `location_id`.

### Use cases

- Show the name and map position of a place that appears on an Instagram post.
- Compare how many posts are tagged at different locations using `media_count`.
- Check whether a location has address, phone, or business profile data before you use it.
- Find the `slug` for a location to build a readable label in a report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/location-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"location_id": "703457703"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location_id` | string | Yes | Location ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attempts": "30",
  "location_info": {
    "category": "Country/Region",
    "hours": {
      "status": ""
    },
    "ig_business": {
      "profile": null
    },
    "lat": -25.751409,
    "lng": 28.203527,
    "location_address": "",
    "location_city": "",
    "location_id": "703457703",
    "location_zip": "",
    "media_count": 78252,
    "name": "NewYork. America",
    "phone": ""
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `location_info.name` | Display name of the location. It is the name users see when they tag the place. |
| `location_info.location_id` | ID of the location, returned as a string. It matches the `location_id` you sent. |
| `location_info.slug` | URL-style name of the location, in lowercase with hyphens. |
| `location_info.category` | Type of place, for example `Country/Region`. |
| `location_info.lat / location_info.lng` | Latitude and longitude of the location in decimal degrees. |
| `location_info.media_count` | Number of posts tagged at this location. |
| `location_info.location_address / location_info.location_city / location_info.location_zip` | Street address, city, and postal code. These can be empty strings when the location has no address data. |
| `location_info.phone` | Contact phone number. It is an empty string when none is listed. |
| `location_info.price_range` | Price range value for the location. It is `0` in this response. |
| `location_info.ig_business.profile` | Linked Instagram business profile. It is `null` when the location has none. |

### Notes

- Coordinates and name come from the location record. In the sample, the name is `NewYork. America` while the coordinates are at `-25.751409`, `28.203527`, so check that they fit your use.
- To get posts tagged at this place, call [Instagram Location Posts (V1)](/apis/instagram/v1/location-posts) with the same location ID.
- To find location IDs by city, use [Instagram City Locations](/apis/instagram/v1/locations). To find them by name, use [Instagram Location Search](/apis/instagram/search-locations).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Posts (V1)](/apis/instagram/v1/location-posts): Returns posts tagged at a designated location.

---
Machine-readable: [`catalog/models/instagram/v1/location-info.json`](../../../../catalog/models/instagram/v1/location-info.json) · Store page: https://www.sandbase.ai/model/instagram/v1/location-info
