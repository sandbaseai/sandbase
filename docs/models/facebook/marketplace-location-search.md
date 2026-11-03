# Facebook Marketplace Location Search API: pricing, parameters and code examples

`facebook/marketplace-location-search` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Resolve a place name to Facebook Marketplace locations with coordinates and metadata as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/marketplace-location-search", "query": "Austin"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/marketplace-location-search', {'query': 'Austin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/marketplace-location-search", {
  "query": "Austin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/marketplace-location-search", sandbase.Params{
	"query": "Austin",
})
```

Same call via the path form: `POST /v1/api/facebook/marketplace-location-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Location search query (e.g. a city name).  |

## Details

Returns a list of Facebook Marketplace locations that match a place name. Each result has a name, city, coordinates, postal code, and a page ID. The only input is the `query` string, such as a city name.

### Use cases

- Convert a city name typed by a user into coordinates for a map or a radius search.
- Find the `pageId` of a location so you can use it in other Facebook Marketplace lookups.
- Tell apart places that share a name, such as Austin in Illinois, Georgia, and Texas, by reading `subtitle` and `city`.
- Check whether Facebook knows a place name before you build a Marketplace search around it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/marketplace-location-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "Austin"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Location search query (e.g. a city name). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "locations": [
      {
        "city": "Chicago",
        "latitude": 41.894086,
        "longitude": -87.763202,
        "name": "Austin",
        "pageId": "108120015875983",
        "postalCode": "60644-1112",
        "subtitle": "Austin, IL · 25,642 people checked in here"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when at least one location matched the query. A search with no match returns `false`. |
| `data.locations[]` | List of matching locations. The top result is not always the one you want, so check each entry. |
| `data.locations[].name` | Display name of the location, such as `Austin` or `Austin, Texas`. |
| `data.locations[].city` | City tied to the location. It can differ from `name`, as in the `Austin` entry in `Chicago`. |
| `data.locations[].latitude / data.locations[].longitude` | Coordinates of the location in decimal degrees. |
| `data.locations[].pageId` | Facebook page ID of the location, returned as a string. |
| `data.locations[].postalCode` | Postal code of the location. Some values include the extra four digits, such as `60644-1112`. |
| `data.locations[].subtitle` | Short description of the location. It shows a state and check-in count for some places, or a type such as `City`. |

### Notes

- Send a city name or other place name as `query`. Add a state or region to the text if the first results are the wrong place.
- Treat `pageId` as a string. The values are long numeric IDs.
- To browse listings after you pick a location, call [Facebook Marketplace](/apis/facebook/marketplace).
- To read a single listing, use [Facebook Marketplace Item](/apis/facebook/marketplace-item).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/marketplace-location-search.json`](../../../catalog/models/facebook/marketplace-location-search.json) · Store page: https://www.sandbase.ai/model/facebook/marketplace-location-search
