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

Look up comprehensive details for an Instagram place by supplying the target `location_id`.

### Use cases

- Retrieve profile information for a specific venue or business location.
- Enrich geographical metadata for places tagged on Instagram.
- Verify place details using an existing location identifier.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/location-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"location_id": "703457703"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location_id` | string | Yes | Location ID |

### Notes

- Requires a valid `location_id` string.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/model/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/model/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Posts (V1)](/model/instagram/v1/location-posts): Returns posts tagged at a designated location.

---
Machine-readable: [`catalog/models/instagram/v1/location-info.json`](../../../../catalog/models/instagram/v1/location-info.json) · Store page: https://www.sandbase.ai/model/instagram/v1/location-info
