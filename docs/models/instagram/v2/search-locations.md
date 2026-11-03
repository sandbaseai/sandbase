# Instagram Location Search API: pricing, parameters and code examples

`instagram/v2/search-locations` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Searches Instagram locations matching a specified query term. Returns a list of place candidates with their IDs, names, and Facebook place identifiers.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/search-locations", "keyword": "paris"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/search-locations', {'keyword': 'paris'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/search-locations", {
  "keyword": "paris"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/search-locations", sandbase.Params{
	"keyword": "paris",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/search-locations` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword (location name, city, etc.)  |

## Details

Returns a list of Instagram locations that match a search term. You send a `keyword` such as a place name or city, and each result includes an ID, name, coordinates, and a Facebook place ID.

### Use cases

- Find the Instagram location ID for a landmark, hotel, or city before pulling posts tagged there.
- Build a place autocomplete that maps typed text to Instagram location entries.
- Plot candidate places on a map using the returned latitude and longitude.
- Tell apart places with similar names by comparing their `address` and `city` values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/search-locations" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "paris"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (location name, city, etc.) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "count": 30,
    "items": [
      {
        "address": "3655 Las Vegas Blvd S",
        "city": "",
        "external_source": "facebook_places",
        "facebook_places_id": 203320451997,
        "id": "203320451997",
        "latitude": 36.112384416244,
        "longitude": -115.17106896803,
        "name": "Paris Las Vegas Hotel & Casino",
        "short_name": "Paris Las Vegas Hotel & Casino"
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of location results returned for the keyword. |
| `data.items[].id` | Instagram location ID as a string. Use it as the location identifier in other location calls. |
| `data.items[].name / data.items[].short_name` | Display name of the place. In the sample, both fields hold the same value. |
| `data.items[].facebook_places_id` | Numeric Facebook place identifier for the location. It matches `id` for some results and differs for others. |
| `data.items[].latitude / data.items[].longitude` | Coordinates of the place in decimal degrees. |
| `data.items[].address` | Street address of the place. It is an empty string when none is available. |
| `data.items[].city` | City label for the place, such as `Paris, France`. It is an empty string when none is available. |
| `data.items[].external_source` | Source label for the place record. The sample shows `facebook_places`. |

### Notes

- The `keyword` parameter is the only input. It takes a location name or city, for example `paris`.
- Results can include places that only contain the keyword in the name, such as a hotel in Las Vegas, so check `latitude`, `longitude`, and `city` before you pick one.
- Use `id` as a string. Do not use `facebook_places_id` in its place, because the two values can differ.
- To find locations near a point instead of by name, use [Instagram Location Search by Coordinates (V2)](/apis/instagram/v2/search-by-coordinates). To get posts for a chosen place, use [Instagram Location Posts (V2)](/apis/instagram/v2/location-posts).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/search-locations.json`](../../../../catalog/models/instagram/v2/search-locations.json) · Store page: https://www.sandbase.ai/model/instagram/v2/search-locations
