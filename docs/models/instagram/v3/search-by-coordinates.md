# Instagram Location Search by Coordinates (V3) API: pricing, parameters and code examples

`instagram/v3/search-by-coordinates` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns nearby Instagram locations matching specific GPS coordinates. Provide latitude and longitude coordinates to discover venues and their external IDs.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/search-by-coordinates", "latitude": 0, "longitude": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/search-by-coordinates', {'latitude': 0, 'longitude': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/search-by-coordinates", {
  "latitude": 0,
  "longitude": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/search-by-coordinates", sandbase.Params{
	"latitude": 0,
	"longitude": 0,
})
```

Same call via the path form: `POST /v1/api/instagram/v3/search-by-coordinates` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `latitude` | number | yes | Latitude  |
| `longitude` | number | yes | Longitude  |

## Details

Returns Instagram locations near a GPS point. Send `latitude` and `longitude` as numbers. Each result has a place name, a short address, its coordinates, and an external ID.

### Use cases

- Find the Instagram location entries closest to a point on a map.
- Collect external location IDs for venues near a store, hotel, or event site.
- Match a GPS coordinate from a photo or device to a named place.
- Build a list of nearby venue names and addresses for a given area.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/search-by-coordinates" \
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
  "rank_token": "",
  "request_id": "8e894d90a3294616bf6c3cbfc3cb8d09",
  "status": "ok",
  "venues": [
    {
      "address": "<0.1mi · 新北市中和橋和路15號",
      "external_id": "482775614919229",
      "external_id_source": "facebook_places",
      "lat": 0.0,
      "lng": 0.0,
      "name": "萱子的秘密小屋"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `venues[]` | List of nearby locations returned for the coordinates. |
| `venues[].name` | Display name of the venue. |
| `venues[].address` | Address text for the venue. It starts with a distance label such as `<0.1mi`, followed by the street address. |
| `venues[].external_id` | ID of the venue in the external places source. Keep it as a string. |
| `venues[].external_id_source` | Name of the source that the `external_id` belongs to, for example `facebook_places`. |
| `venues[].lat / venues[].lng` | Latitude and longitude of the venue. |
| `status` | Request status. The value `ok` means the call succeeded. |
| `request_id` | ID of this request. |
| `rank_token` | Ranking token for the result set. It was an empty string in this response. |

### Notes

- Both `latitude` and `longitude` are required and must be numbers.
- The request has no pagination parameters.
- The example request used `0` and `0`, and the returned `lat` and `lng` values were also `0.0`. Use your own coordinates to see venues around a real place.
- To get details for a venue, pass its ID to [Instagram Location Details (V3)](/apis/instagram/v3/location-info). To see posts tagged there, use [Instagram Location Posts (V3)](/apis/instagram/v3/location-posts).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/search-by-coordinates.json`](../../../../catalog/models/instagram/v3/search-by-coordinates.json) · Store page: https://www.sandbase.ai/model/instagram/v3/search-by-coordinates
