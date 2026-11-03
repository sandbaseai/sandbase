# Tripadvisor Reviews API: pricing, parameters and code examples

`tripadvisor/reviews` · data API · Tripadvisor · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

Public reviews of a Tripadvisor hotel, restaurant or attraction by place ID: rating, title, text, date and reviewer.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripadvisor/reviews", "place_id": 18941405}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripadvisor/reviews', {'place_id': 18941405})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripadvisor/reviews", {
  "place_id": 18941405
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripadvisor/reviews", sandbase.Params{
	"place_id": 18941405,
})
```

Same call via the path form: `POST /v1/api/tripadvisor/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `num` | integer |  | Number of reviews, 1 through 50. default `10` |
| `start` | integer |  | Review offset from 0 through 10,000. default `0` |
| `locale` | string |  | Lowercase language code with an optional uppercase country, such as en or en-US. default `"en-US"` |
| `sort_by` | string |  | Review order: recent (newest first) or relevance. one of: `recent`, `relevance`; default `"recent"` |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `place_id` | integer | yes | Numeric Tripadvisor place ID, up to 16 digits.  |
| `translate` | boolean |  | Request Tripadvisor's machine translation of reviews. default `false` |
| `tripadvisor_domain` | string |  | Supported first-party localized Tripadvisor hostname, such as www.tripadvisor.co.uk.  |

## Details

Returns public Tripadvisor reviews for one hotel, restaurant or attraction. You pass the numeric `place_id`. Each review includes the rating, title, text, dates, trip type and reviewer profile.

### Use cases

- Track new guest reviews of a hotel by sorting with `sort_by` set to `recent`.
- Pull review text and ratings for one place to run sentiment analysis.
- Compare how couples, families and business travelers rate the same hotel using `trip.type`.
- Build a review feed on a travel site with links back to each review page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tripadvisor/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"place_id": 18941405, "num": 5}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `place_id` | integer | Yes | Numeric Tripadvisor place ID, up to 16 digits. |
| `locale` | string | No | Lowercase language code with an optional uppercase country, such as en or en-US. |
| `num` | integer | No | Number of reviews, 1 through 50. |
| `sort_by` | string | No | Review order: recent (newest first) or relevance. |
| `start` | integer | No | Review offset from 0 through 10,000. |
| `timeout` | number | No | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the cal |
| `translate` | boolean | No | Request Tripadvisor's machine translation of reviews. |
| `tripadvisor_domain` | string | No | Supported first-party localized Tripadvisor hostname, such as www.tripadvisor.co.uk. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "pagination": {},
  "reviews": [
    {
      "created_date": "2026-11-01",
      "helpful_votes": 0,
      "id": "1084031574",
      "language": "en",
      "link": "https://www.tripadvisor.com/ShowUserReviews-g30196-d18941405-r1084031574-Austin_…",
      "max_rating": 5,
      "original_language": "en",
      "place": {
        "link": "https://www.tripadvisor.com/Hotel_Review-g30196-d18941405-Reviews-Austin_Proper_…",
        "place_id": "18941405",
        "title": "Austin Proper Hotel",
        "type": "ACCOMMODATION"
      },
      "position": 1,
      "published_date": "2026-11-01",
      "rating": 5,
      "status": "PUBLISHED"
    }
  ],
  "search_information": {
    "results_on_page": 5,
    "total_results": 1028
  },
  "sort": {
    "by": "DATE",
    "type": "DATE"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `reviews[].id` | Unique ID of the review, given as a string. |
| `reviews[].rating / reviews[].max_rating` | The star rating given by the reviewer and the highest possible rating. In this response the scale is 5. |
| `reviews[].title / reviews[].text` | The headline and body of the review. Long text may be shortened in the example. |
| `reviews[].created_date / reviews[].published_date` | Dates of the review in `YYYY-MM-DD` format. |
| `reviews[].trip.date / reviews[].trip.type` | The date of the stay and the kind of trip, such as `COUPLES`, `FAMILY` or `BUSINESS`. |
| `reviews[].user.name / reviews[].user.username / reviews[].user.link` | Display name, username and profile URL of the reviewer. Some reviews have no `username`. |
| `reviews[].user.country / reviews[].user.hometown / reviews[].user.contributions` | Where the reviewer is from, when given, and the number of contributions on their profile. |
| `reviews[].helpful_votes` | Number of helpful votes the review has received. |
| `reviews[].place.title / reviews[].place.type / reviews[].place.place_id` | Name, category (for example `ACCOMMODATION`) and ID of the reviewed place. |
| `search_information.total_results` | Total number of reviews available for this place. `results_on_page` shows how many came back in this call. |

### Notes

- Use [Tripadvisor Search](/apis/tripadvisor/search) to find the `place_id` of a place. It also appears in review links after `-d`, for example `d18941405`.
- To page through reviews, raise `start` by the value of `num`. `num` accepts 1 to 50.
- The `pagination` object was empty in this response, so use `start` and `search_information.total_results` to decide when to stop.
- The `sort.by` field shows the applied order. It returned `DATE` for the default `recent` sort.

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/tripadvisor/reviews.json`](../../../catalog/models/tripadvisor/reviews.json) · Store page: https://www.sandbase.ai/model/tripadvisor/reviews
