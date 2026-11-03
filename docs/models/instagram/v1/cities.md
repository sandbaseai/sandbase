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

Returns a paged list of Instagram cities and regions for one country. You pass a `country_code` such as `US`, and each city comes back with an `id`, a `name` and a `slug`.

### Use cases

- Build a city picker for a chosen country using the returned `name` values.
- Collect Instagram city `id` values to use in later location lookups.
- Walk through every city of a country by requesting one page after another.
- Match a city `slug` against your own location data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/cities" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"country_code": "US"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country_code` | string | Yes | Country code, e.g. US, CN, JP |
| `page` | integer | No | Page number, default 1 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attempts": "0",
  "city_list": [
    {
      "id": "c2753900",
      "name": "Downtown-PennQuarter-Chinatown",
      "slug": "downtown-pennquarter-chinatown-united-states"
    }
  ],
  "country_info": {
    "id": "US",
    "name": "United States",
    "slug": "united-states"
  },
  "next_page": 2,
  "status": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `city_list[].id` | Instagram identifier of the city or region. The sample values start with `c`, for example `c2420379`. |
| `city_list[].name` | Name of the city or region. Spaces are removed in the sample values, for example `LosAngeles`. |
| `city_list[].slug` | Lowercase, hyphenated name with the country name added at the end, for example `losangeles-united-states`. |
| `country_info.id / country_info.name / country_info.slug` | Country that the list belongs to. In the sample, `id` is `US`, `name` is `United States` and `slug` is `united-states`. |
| `next_page` | Number of the next page, `2` in the sample. Pass it as `page` to get more cities. |
| `status` | Boolean that is `true` when the request succeeded. |

### Notes

- `country_code` is required. It is a two-letter code such as `US`, `CN` or `JP`.
- `page` starts at `1`. Send the `next_page` value from the response to get the following page.
- The city `id` and `slug` values are location identifiers. To see the locations inside a city, try [Instagram City Locations](/apis/instagram/v1/locations).
- To get details for a single location, call [Instagram Location Details (V1)](/apis/instagram/v1/location-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.
- [Instagram Location Posts (V1)](/apis/instagram/v1/location-posts): Returns posts tagged at a designated location.

---
Machine-readable: [`catalog/models/instagram/v1/cities.json`](../../../../catalog/models/instagram/v1/cities.json) · Store page: https://www.sandbase.ai/model/instagram/v1/cities
