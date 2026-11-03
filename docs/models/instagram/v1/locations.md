# Instagram City Locations API: pricing, parameters and code examples

`instagram/v1/locations` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of Instagram location points for a designated city. Filter results using the city identifier and paginate through records by page number.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/locations", "city_id": "c2791472"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/locations', {'city_id': 'c2791472'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/locations", {
  "city_id": "c2791472"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/locations", sandbase.Params{
	"city_id": "c2791472",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/locations` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default 1 range 1– |
| `city_id` | string | yes | City ID (from fetch_cities API)  |

## Details

Query location listings across Instagram by supplying a `city_id`. Supports pagination via the `page` parameter.

### Use cases

- Discover popular spots and venues within a specific city.
- Collect location IDs for geo-targeted Instagram content analysis.
- Map out regional venues and businesses listed on the platform.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/locations" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"city_id": "c2791472"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `city_id` | string | Yes | City ID (from fetch_cities API) |
| `page` | integer | No | Page number, default 1 |

### Notes

- Obtain the required `city_id` from the city search endpoint.
- Pagination is controlled via `page`, which defaults to 1.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/locations.json`](../../../../catalog/models/instagram/v1/locations.json) · Store page: https://www.sandbase.ai/model/instagram/v1/locations
