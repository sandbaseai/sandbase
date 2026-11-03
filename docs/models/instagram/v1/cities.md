# Instagram Cities by Country API: pricing, parameters and code examples

`instagram/v1/cities` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of Instagram cities and regions for a specified country code. Allows developers to look up location identifiers by passing pagination parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/cities", "country_code": "US"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/cities', {'country_code': 'US'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/cities", {
  "country_code": "US"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/cities", sandbase.Params{
	"country_code": "US",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/cities` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default 1 default `1`; range 1– |
| `country_code` | string | yes | Country code, e.g. US, CN, JP  |

## Details

Look up cities and regions within a specific country by passing `country_code` and optional `page` parameters.

### Use cases

- Look up Instagram city identifiers for a target country.
- Populate location filters based on country-level selections.
- Browse regional location directories page by page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/cities" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"country_code": "US"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country_code` | string | Yes | Country code, e.g. |
| `page` | integer | No | Page number, default 1 |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "city_list": [
    {
      "id": "c2753900",
      "name": "Downtown-PennQuarter-Chinatown"
    }
  ]
}
```

### Notes

- The `country_code` parameter accepts two-letter country codes such as US, CN, or JP.
- Use `page` for pagination, which defaults to 1.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.
- [Instagram Location Posts (V1)](/apis/instagram/v1/location-posts): Returns posts tagged at a designated location.

---
Machine-readable: [`catalog/models/instagram/v1/cities.json`](../../../../catalog/models/instagram/v1/cities.json) · Store page: https://www.sandbase.ai/model/instagram/v1/cities
