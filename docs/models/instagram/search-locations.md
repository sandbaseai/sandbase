# Instagram Location Search API: pricing, parameters and code examples

`instagram/search-locations` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Search Instagram locations by keyword and return each place's id, name, address and coordinates.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/search-locations", "query": "Eiffel Tower"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/search-locations', {'query': 'Eiffel Tower'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/search-locations", {
  "query": "Eiffel Tower"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/search-locations", sandbase.Params{
	"query": "Eiffel Tower",
})
```

Same call via the path form: `POST /v1/api/instagram/search-locations` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Place name, address or city to search for.  |

## Details

This API searches Instagram locations by keyword. It needs one `query` (a place name, address or city) and returns matching places with an `id`, name, address, city and coordinates.

### Use cases

- Find the Instagram location `id` for a landmark so you can pull posts tagged there.
- Map a place name to latitude and longitude from Instagram's own location data.
- List the different Instagram places that share a name, such as several places called Eiffel Tower.
- Check how a venue is named on Instagram before you track it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/search-locations" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "Eiffel Tower"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Place name, address or city to search for. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "locations": [
      {
        "address": "Champ-de-Mars",
        "city": "",
        "id": "103912118089363",
        "latitude": 48.85824768693,
        "longitude": 2.2944650859978,
        "name": "Eiffel Tower, Paris, France",
        "shortName": "Eiffel Tower"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.locations[].id` | Instagram location ID as a string. Use it to look up posts or details for that place. |
| `data.locations[].name` | Full display name of the place, sometimes with city and country, such as `Eiffel Tower, Paris, France`. |
| `data.locations[].shortName` | Shorter name of the place without the city or country. |
| `data.locations[].address` | Street or area address of the place. It can be an empty string. |
| `data.locations[].city` | City of the place. It can be an empty string. |
| `data.locations[].latitude / data.locations[].longitude` | Coordinates of the place in decimal degrees. |
| `found` | `true` when the search returned at least one location. |

### Notes

- Several results can share the same name but sit in different cities, so check `city`, `latitude` and `longitude` before you pick an `id`.
- `address` and `city` are often empty strings. Use `name` and the coordinates when they are.
- Pass the chosen `id` to [Instagram Location Posts](/apis/instagram/location-posts) to get posts tagged at that place.
- Use [Instagram Location Details (V1)](/apis/instagram/v1/location-info) to get more detail about a single location.

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/search-locations.json`](../../../catalog/models/instagram/search-locations.json) · Store page: https://www.sandbase.ai/model/instagram/search-locations
