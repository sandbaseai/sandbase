# Instagram Location Search by Coordinates (V2) API: pricing, parameters and code examples

`instagram/v2/search-by-coordinates` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns nearby Instagram locations matching specified geographic coordinates. Queries require both latitude and longitude values to discover place names and identifiers.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/search-by-coordinates", "latitude": 0, "longitude": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/search-by-coordinates', {'latitude': 0, 'longitude': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/search-by-coordinates", {
  "latitude": 0,
  "longitude": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/search-by-coordinates", sandbase.Params{
	"latitude": 0,
	"longitude": 0,
})
```

Same call via the path form: `POST /v1/api/instagram/v2/search-by-coordinates` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `latitude` | number | yes | Latitude  |
| `longitude` | number | yes | Longitude  |

## Details

Returns a list of Instagram locations near a pair of coordinates. Each item has a place name, an ID, and the latitude and longitude. The request needs `latitude` and `longitude` as numbers.

### Use cases

- Find the Instagram location ID for a venue when you only have its GPS coordinates.
- Build a list of nearby places for a map or check-in picker from a device position.
- Match a store or hotel address to its Instagram place entry before collecting posts tagged there.
- Check which place names Instagram lists around a given point.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/search-by-coordinates" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"latitude": 0, "longitude": 0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `latitude` | number | Yes | Latitude |
| `longitude` | number | Yes | Longitude |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "count": 25,
    "items": [
      {
        "address": "<0.1mi · 新北市中和橋和路15號",
        "category": "",
        "city": null,
        "hours": [],
        "id": "482775614919229",
        "id_source": "facebook_places",
        "latitude": 0,
        "longitude": 0,
        "name": "萱子的秘密小屋",
        "phone": "",
        "website": "",
        "zip": null
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of location items in the response. |
| `data.items[].id` | Identifier of the location. Use it to look up posts tagged at that place. |
| `data.items[].id_source` | Source system of the ID. The sample values are `facebook_places`. |
| `data.items[].name` | Display name of the place. |
| `data.items[].address` | Street address text. It can start with a distance prefix such as `<0.1mi ·`. |
| `data.items[].latitude / data.items[].longitude` | Coordinates of the place. In the sample response both are `0`. |
| `data.items[].category / data.items[].phone / data.items[].website` | Optional place details. They are empty strings when no value is set. |
| `data.items[].city / data.items[].zip` | City and postal code. Both are `null` in the sample response. |
| `data.items[].hours` | List of opening hours. It is empty in the sample response. |

### Notes

- Both `latitude` and `longitude` are required numbers.
- Many fields such as `category`, `phone`, `website`, `city` and `zip` can be empty or `null`, so check them before use.
- Pass a location `id` to [Instagram Location Posts (V2)](/apis/instagram/v2/location-posts) to get posts for that place.
- To find a place by name instead of coordinates, use [Instagram Location Search](/apis/instagram/v2/search-locations).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/search-by-coordinates.json`](../../../../catalog/models/instagram/v2/search-by-coordinates.json) · Store page: https://www.sandbase.ai/model/instagram/v2/search-by-coordinates
