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

Look up nearby Instagram venues by supplying `latitude` and `longitude` coordinates. The response lists location names alongside their external location IDs.

### Use cases

- Find Instagram venue tags near specific geographic coordinates.
- Identify external location IDs for regional spots and landmarks.
- Enrich geographic mapping tools with nearby Instagram place data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/search-by-coordinates" \
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
  "venues": [
    {
      "external_id": "469499352918885",
      "name": "Đặng Viring Specialty Coffee"
    }
  ]
}
```

### Notes

- Requires both `latitude` and `longitude` numeric coordinates.
- Returns a list of venues containing external identifiers and place names.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/search-by-coordinates.json`](../../../../catalog/models/instagram/v3/search-by-coordinates.json) · Store page: https://www.sandbase.ai/model/instagram/v3/search-by-coordinates
