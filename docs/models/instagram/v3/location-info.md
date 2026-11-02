# Instagram Location Details (V3) API: pricing, parameters and code examples

`instagram/v3/location-info` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns detailed place information including name, address, coordinates, and nearby places for an Instagram location. Queries are based on a specific location ID.

## Pricing

- **$0.012 per call** (USD)
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

Retrieve detailed metadata for an Instagram place by passing its numeric `location_id`. You can also configure `show_nearby` to include adjacent locations.

### Use cases

- Look up geographical coordinates and street addresses for Instagram places.
- Discover nearby points of interest associated with a venue.
- Enrich location-tagged post analysis with structured place metadata.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/location-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"location_id": "<location_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location_id` | string | Yes | Location ID (numeric) |
| `show_nearby` | boolean | No | Whether to show nearby places (default true) |

### Notes

- Obtain `location_id` values from place search endpoints or post metadata.
- `show_nearby` defaults to true.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/location-info.json`](../../../../catalog/models/instagram/v3/location-info.json) · Store page: https://www.sandbase.ai/model/instagram/v3/location-info
