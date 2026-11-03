# Tripadvisor Search API: pricing, parameters and code examples

`tripadvisor/search` · data API · Tripadvisor · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

Search Tripadvisor hotels, restaurants, attractions and places by keyword.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripadvisor/search", "q": "hotels in Austin Texas"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripadvisor/search', {'q': 'hotels in Austin Texas'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripadvisor/search", {
  "q": "hotels in Austin Texas"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripadvisor/search", sandbase.Params{
	"q": "hotels in Austin Texas",
})
```

Same call via the path form: `POST /v1/api/tripadvisor/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Search text, 1 to 500 characters.  |
| `lat` | number |  | Search center latitude from -90 through 90. Requires lon.  |
| `lon` | number |  | Search center longitude from -180 through 180. Requires lat.  |
| `num` | integer |  | Maximum number of search_results, 1 through 30, including any leading exact match. default `30` |
| `start` | integer |  | Result offset from 0 through 10,000. Offsets and positions count any leading exact match. default `0` |
| `geo_id` | integer |  | Tripadvisor geography ID to search within.  |
| `locale` | string |  | Lowercase language code with an optional uppercase country, such as en or en-US. default `"en-US"` |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `place_type` | string |  | Restrict results to one entity type. one of: `all`, `accommodation`, `attraction`, `attraction_product`, `eatery`, `geo`; default `"all"` |
| `tripadvisor_domain` | string |  | Supported first-party localized Tripadvisor hostname, such as www.tripadvisor.co.uk.  |

## Details

Returns Tripadvisor search results for a keyword query, such as hotels, restaurants, attractions and places. The only required input is `q`. You can narrow results with `geo_id`, `lat` and `lon`, `place_type` or a localized Tripadvisor domain.

### Use cases

- Build a list of hotels in a city with ratings and review counts to compare them.
- Find the Tripadvisor `place_id` and page link for a named business before looking up more detail.
- Collect restaurants or attractions near a latitude and longitude using `lat`, `lon` and `place_type`.
- Run the same query on a schedule to see how the review count and rating of a set of properties change.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tripadvisor/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "hotels in Austin Texas"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Search text, 1 to 500 characters. |
| `geo_id` | integer | No | Tripadvisor geography ID to search within. |
| `lat` | number | No | Search center latitude from -90 through 90. Requires lon. |
| `locale` | string | No | Lowercase language code with an optional uppercase country, such as en or en-US. |
| `lon` | number | No | Search center longitude from -180 through 180. Requires lat. |
| `num` | integer | No | Maximum number of search_results, 1 through 30, including any leading exact match. |
| `place_type` | string | No | Restrict results to one entity type. |
| `start` | integer | No | Result offset from 0 through 10,000. Offsets and positions count any leading exact match. |
| `timeout` | number | No | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the cal |
| `tripadvisor_domain` | string | No | Supported first-party localized Tripadvisor hostname, such as www.tripadvisor.co.uk. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "map_previews": [],
  "pagination": {},
  "search_information": {
    "results_on_page": 30,
    "total_results": 2000
  },
  "search_results": [
    {
      "description": "Located in Downtown Austin's vibrant Second Street District, Austin Proper Hotel…",
      "detail_type": "Hotel",
      "highlighted_spans": [
        {
          "length": 6,
          "offset": 3
        }
      ],
      "image": {
        "max_height": 2667,
        "max_width": 4000,
        "thumbnail": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/35/01/4d/b9/outdoor-pool…",
        "url_template": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/35/01/4d/b9/outdoor-pool…"
      },
      "link": "https://www.tripadvisor.com/Hotel_Review-g30196-d18941405-Reviews-Austin_Proper_…",
      "location": "Austin, Texas",
      "max_rating": 5,
      "mention_count": 16,
      "place_id": "18941405",
      "position": 1,
      "position_in_page": 1,
      "rating": 4.6
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `search_results[].title` | Name of the place, such as a hotel, restaurant or attraction. |
| `search_results[].place_id` | Tripadvisor ID of the place, given as a string. It matches the number after `-d` in the `link` URL. |
| `search_results[].type / search_results[].detail_type` | Entity type of the result. `type` is a code such as `ACCOMMODATION` and `detail_type` is a label such as `Hotel`. |
| `search_results[].rating / search_results[].max_rating` | Average rating of the place and the top of the rating scale, which is `5` in this response. |
| `search_results[].reviews` | Number of reviews for the place. |
| `search_results[].link` | Full Tripadvisor page URL for the place. |
| `search_results[].location` | City or region text shown for the place, such as `Austin, Texas`. |
| `search_results[].position / search_results[].position_in_page` | Rank of the result across the whole result set and within the current page. |
| `search_results[].thumbnail / search_results[].image.url_template` | Photo URL for the result. In `url_template`, replace `{width}` and `{height}` to request a size. |
| `search_information.total_results / search_information.results_on_page` | Total number of matches for the query and the number of results returned in this response. |

### Notes

- Page through results with `start` (offset) and `num` (up to 30 results in one response).
- Use `place_type` to limit results to one type: `accommodation`, `attraction`, `attraction_product`, `eatery` or `geo`.
- `place_id` is a numeric string. The same value appears after `-d` in the `link` URL.
- To read guest reviews for a result, use [Tripadvisor Reviews](/apis/tripadvisor/reviews) next.

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/tripadvisor/search.json`](../../../catalog/models/tripadvisor/search.json) · Store page: https://www.sandbase.ai/model/tripadvisor/search
