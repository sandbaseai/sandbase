# Instagram Location Details (V3) API: pricing, parameters and code examples

`instagram/v3/location-info` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns detailed place information including name, address, coordinates, and nearby places for an Instagram location. Queries are based on a specific location ID.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/location-info", "location_id": "1016248898"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/location-info', {'location_id': '1016248898'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/location-info", {
  "location_id": "1016248898"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/location-info", sandbase.Params{
	"location_id": "1016248898",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/location-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `location_id` | string | yes | Location ID (numeric)  |
| `show_nearby` | boolean |  | Whether to show nearby places (default true)  |

## Details

Returns details for one Instagram location, such as its name, city, address, and coordinates. It needs a numeric `location_id`. It can also list nearby places when `show_nearby` is on.

### Use cases

- Resolve a numeric Instagram location ID into a readable place name and city.
- Link an Instagram location to an outside place record using `external_id`.
- Label location-tagged posts with a place name before you analyze them.
- Check whether a location has coordinates and a street address on file.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/location-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"location_id": "1016248898"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location_id` | string | Yes | Location ID (numeric) |
| `show_nearby` | boolean | No | Whether to show nearby places (default true) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "3cda064c29f93",
  "address": "",
  "city": "Changwon",
  "external_id": 144811708967490,
  "external_id_source": null,
  "id": "1016248898",
  "lat": null,
  "lng": null,
  "location": {
    "address": "",
    "city": "Changwon",
    "external_id": 144811708967490,
    "external_id_source": null,
    "id": "1016248898",
    "lat": null,
    "lng": null,
    "name": "창원",
    "pk": "1016248898"
  },
  "name": "창원",
  "nearby_locations": [],
  "pk": "1016248898"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `name` | Display name of the location. In this response it is `창원`, written in Korean. |
| `city` | City the location belongs to, for example `Changwon`. |
| `id / pk` | The Instagram location ID as a string. Both hold the same value as the `location_id` you sent. |
| `address` | Street address text. It can be an empty string when none is on file. |
| `lat / lng` | Latitude and longitude of the place. Both are `null` when the location has no coordinates. |
| `external_id` | Numeric ID of the place in an outside source. `external_id_source` names that source and can be `null`. |
| `nearby_locations` | List of nearby places. It is empty here, and may be empty for locations with no neighbors. |
| `location` | Nested copy of the main place fields: `name`, `city`, `address`, `lat`, `lng`, `id`, `pk` and `external_id`. |

### Notes

- Set `show_nearby` to `false` if you do not need the `nearby_locations` list.
- Find a `location_id` with [Instagram Location Search by Coordinates (V3)](/apis/instagram/v3/search-by-coordinates).
- Call [Instagram Location Posts (V3)](/apis/instagram/v3/location-posts) next to get posts tagged at this location.

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/location-info.json`](../../../../catalog/models/instagram/v3/location-info.json) · Store page: https://www.sandbase.ai/model/instagram/v3/location-info
