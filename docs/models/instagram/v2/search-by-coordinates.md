# Instagram Location Search by Coordinates (V2)

`instagram/v2/search-by-coordinates` · api · Instagram

Returns nearby Instagram locations matching specified geographic coordinates. Queries require both latitude and longitude values to discover place names and identifiers.

## Pricing

- **$0.003 per call** (USD)
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

Locate nearby Instagram places by providing geographic coordinates via `latitude` and `longitude`. The endpoint returns matching location records along with their IDs and names.

### Use cases

- Discover Instagram location IDs for places near specific GPS coordinates.
- Tag posts with accurate local venues based on device coordinates.
- Map physical business locations to corresponding Instagram place entries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/search-by-coordinates" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"latitude": 0, "longitude": 0}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `latitude` | number | Yes | Latitude |
| `longitude` | number | Yes | Longitude |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "items": [
      {
        "id": "469499352918885",
        "name": "Đặng Viring Specialty Coffee"
      }
    ]
  }
}
```

### Notes

- Both `latitude` and `longitude` are required numerical inputs.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/search-by-coordinates.json`](../../../../catalog/models/instagram/v2/search-by-coordinates.json) · Store page: https://www.sandbase.ai/model/instagram/v2/search-by-coordinates
