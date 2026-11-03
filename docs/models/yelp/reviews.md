# Yelp Reviews API: pricing, parameters and code examples

`yelp/reviews` · data API · Yelp · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

Public reviews of a Yelp business by place ID: rating, text, date and reviewer, with paging and sorting.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yelp/reviews", "place_id": "dDz2erKJ_Z2HMur0tQ_iJA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yelp/reviews', {'place_id': 'dDz2erKJ_Z2HMur0tQ_iJA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yelp/reviews", {
  "place_id": "dDz2erKJ_Z2HMur0tQ_iJA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yelp/reviews", sandbase.Params{
	"place_id": "dDz2erKJ_Z2HMur0tQ_iJA",
})
```

Same call via the path form: `POST /v1/api/yelp/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Not supported: Yelp does not offer review text filtering. Any value returns 422 unsupported_parameter.  |
| `hl` | string |  | Review language: a two-letter code with an optional two-letter region, such as en or fr-FR. default `"en"` |
| `num` | integer |  | Number of reviews, 1 through 49. default `49` |
| `start` | integer |  | Review offset from 0 through 10,000. default `0` |
| `rating` | string |  | Comma-separated star ratings to include, each from 1 through 5.  |
| `sortby` | string |  | Review order. one of: `relevance_desc`, `date_desc`, `date_asc`, `rating_desc`, `rating_asc`, `elites_desc`; default `"relevance_desc"` |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `place_id` | string | yes | Encoded Yelp business ID: letters, numbers, underscores, and hyphens.  |
| `yelp_domain` | string |  | Supported first-party localized Yelp hostname, such as www.yelp.co.uk. Links in the response use this hostname.  |
| `not_recommended` | boolean |  | Not supported: Yelp does not expose its not-recommended reviews. true returns 422 unsupported_parameter. default `false` |
| `not_recommended_start` | integer |  | Not supported, because not_recommended is not supported. Any value returns 400.  |

## Details

Returns public reviews for one Yelp business, plus the business's average rating, rating counts and total review count. It needs a `place_id`, the encoded Yelp business ID.

### Use cases

- Pull the newest reviews for a restaurant with `sortby` set to `date_desc` to track recent customer feedback.
- Collect only 1 and 2 star reviews with the `rating` filter to find common complaints.
- Match owner replies to reviews to check how often and how fast a business responds.
- Compare reviewers by Elite status and review count to weigh feedback from experienced Yelp users.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yelp/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"place_id": "dDz2erKJ_Z2HMur0tQ_iJA", "num": 10}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `place_id` | string | Yes | Encoded Yelp business ID: letters, numbers, underscores, and hyphens. |
| `hl` | string | No | Review language: a two-letter code with an optional two-letter region, such as en or fr-FR. |
| `not_recommended` | boolean | No | Not supported: Yelp does not expose its not-recommended reviews. true returns 422 unsupported_parameter. |
| `not_recommended_start` | integer | No | Not supported, because not_recommended is not supported. Any value returns 400. |
| `num` | integer | No | Number of reviews, 1 through 49. |
| `q` | string | No | Not supported: Yelp does not offer review text filtering. Any value returns 422 unsupported_parameter. |
| `rating` | string | No | Comma-separated star ratings to include, each from 1 through 5. |
| `sortby` | string | No | Review order. |
| `start` | integer | No | Review offset from 0 through 10,000. |
| `timeout` | number | No | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the cal |
| `yelp_domain` | string | No | Supported first-party localized Yelp hostname, such as www.yelp.co.uk. Links in the response use this hostname. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "pagination": {},
  "review_languages": [
    {
      "count": 744,
      "hl": "en"
    }
  ],
  "reviews": [
    {
      "comment": {
        "language": "en",
        "text": "Came to Cosmic with a friend. He suggested a Mexican food truck that is here. An…"
      },
      "date": "2026-10-19T19:24:08Z",
      "feedback": {
        "cool": 29,
        "funny": 7,
        "useful": 33
      },
      "id": "bsc5JqLCP_A_MDzzPvWFKw",
      "link": "https://www.yelp.com/biz/cosmic-austin?hrid=bsc5JqLCP_A_MDzzPvWFKw",
      "local_date": "2026-10-19T14:24:08-05:00",
      "owner_replies": [
        {
          "comment": "Hi Shannon! We’re so happy to hear you had such a wonderful time at Cosmic Pickl…",
          "date": "2026-10-30T15:28:27Z",
          "id": "gl4nV95_RbQ3lDY5CkWgUA",
          "owner": {
            "id": "u8musB2-qjtyiQVRiLxZ_w",
            "name": "Kayla F.",
            "role": "OWNER",
            "thumbnail": "https://s3-media0.fl.yelpcdn.com/buphoto/podUt4nzIePyrReXIS-CpQ/90s.jpg"
          }
        }
      ],
      "photos": [
        {
          "caption": "Here for Sunday funday drinks.",
          "helpful": 0,
          "id": "2EsUyPlJKgfDYKSYVyBGIw",
          "link": "https://s3-media0.fl.yelpcdn.com/bphoto/2EsUyPlJKgfDYKSYVyBGIw/o.jpg",
          "thumbnail": "https://s3-media0.fl.yelpcdn.com/bphoto/2EsUyPlJKgfDYKSYVyBGIw/348s.jpg"
        }
      ],
      "position": 1,
      "rating": 5,
      "reactions": [
        {
          "count": 38,
          "label": "Helpful",
          "type": "HELPFUL"
        }
      ],
      "user": {
        "address": "Austin, TX",
        "elite_year": "26",
        "friends": 5000,
        "link": "https://www.yelp.com/user_details?userid=jT-pOXB4mpUA5N9Lu0ZN-g",
        "name": "Shannon G.",
        "photos": 14036,
        "reviews": 1073,
        "thumbnail": "https://s3-media0.fl.yelpcdn.com/photo/CkN3QEuWbjsATCyDPCDaXg/180s.jpg"
      }
    }
  ],
  "search_information": {
    "business": "Cosmic",
    "rating": 4.6,
    "rating_distribution": [
      {
        "count": 22,
        "rating": 1
      }
    ],
    "total_results": 744
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `search_information.business / rating / total_results` | Business name, its average star rating and the total number of reviews. |
| `search_information.rating_distribution[]` | Number of reviews (`count`) for each star `rating`. |
| `review_languages[].hl / count` | Language code and the number of reviews written in that language. |
| `reviews[].id / link` | Review ID and a link to the review on Yelp. |
| `reviews[].rating` | Star rating given in the review. |
| `reviews[].comment.text / language` | Review text and its language code. Long text may be cut. |
| `reviews[].date / local_date` | Time the review was posted, in UTC (`date`) and with a local offset (`local_date`). |
| `reviews[].feedback.useful / funny / cool` | Number of votes the review received in each category. |
| `reviews[].owner_replies[]` | Replies from the business owner, each with `comment`, `date` and the `owner` name and role. |
| `reviews[].user.name / reviews / friends / elite_year` | Reviewer name, how many reviews and friends they have, and their Elite year. |

### Notes

- Find the `place_id` with [Yelp Business Search](/apis/yelp/search).
- Page through reviews with `start` (offset) and `num` (1 through 49). `reviews[].position` shows the order within the result.
- `pagination` came back empty in this response, so track the offset yourself and compare it to `search_information.total_results`.
- `q` and `not_recommended` are not supported and return an error.

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/yelp/reviews.json`](../../../catalog/models/yelp/reviews.json) · Store page: https://www.sandbase.ai/model/yelp/reviews
