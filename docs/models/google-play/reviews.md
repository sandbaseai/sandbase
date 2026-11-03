# Google Play Reviews API: pricing, parameters and code examples

`google-play/reviews` · data API · Google Play · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** async

Get Google Play reviews for a product with rating, sort, platform, and paging.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-play/reviews", "product_id": "com.duolingo"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-play/reviews', {'product_id': 'com.duolingo'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-play/reviews", {
  "product_id": "com.duolingo"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-play/reviews", sandbase.Params{
	"product_id": "com.duolingo",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/google-play/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Two-letter country code. Default 'us'.  |
| `hl` | string |  | Storefront language, such as 'en', 'de', or 'zh-TW'. Default 'en'.  |
| `num` | integer |  | Number of reviews, 1-199. Default 40. range 1–199 |
| `store` | string |  | Product catalog containing this identifier. Default 'apps'. one of: `apps`, `books`, `audiobooks`, `movies`, `tv` |
| `rating` | integer |  | Only reviews with this star rating, 1-5. range 1–5 |
| `sort_by` |  |  | 1 most relevant, 2 newest, 3 by rating. Default 1.  |
| `platform` | string |  | Platform the reviews belong to. Default 'phone'. one of: `phone`, `tablet`, `watch`, `chromebook`, `tv` |
| `product_id` | string | yes | Native Google Play product identifier, such as 'com.duolingo'.  |
| `next_page_token` | string |  | Returned review continuation. Keep product, store, language, country, platform, rating, sort order, and count the same.  |

## Details

Returns user reviews for a Google Play product, such as an app, book, or movie. Each review has a star rating, a text snippet, a like count, and the app version. You pass a `product_id` such as `com.duolingo`.

### Use cases

- Track new complaints about an app by pulling the newest reviews with `sort_by` set to `2`.
- Read only 1-star reviews with `rating` set to `1` to find the most common bug reports.
- Compare feedback across app versions using the `version` field on each review.
- Collect reviews from different storefronts by changing `gl` and `hl`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-play/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "com.duolingo"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Native Google Play product identifier, such as 'com.duolingo'. |
| `gl` | string | No | Two-letter country code. Default 'us'. |
| `hl` | string | No | Storefront language, such as 'en', 'de', or 'zh-TW'. Default 'en'. |
| `next_page_token` | string | No | Returned review continuation. Keep product, store, language, country, platform, rating, sort order, and count the same. |
| `num` | integer | No | Number of reviews, 1-199. Default 40. |
| `platform` | string | No | Platform the reviews belong to. Default 'phone'. |
| `rating` | integer | No | Only reviews with this star rating, 1-5. |
| `sort_by` | string | No | 1 most relevant, 2 newest, 3 by rating. Default 1. |
| `store` | string | No | Product catalog containing this identifier. Default 'apps'. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "litescrape_pagination": {
    "current": {
      "endpoint": "/google-play/reviews",
      "queryParams": {
        "gl": "us",
        "hl": "en",
        "num": 40,
        "platform": "phone",
        "product_id": "com.duolingo",
        "sort_by": 1,
        "store": "apps"
      }
    },
    "next": {
      "endpoint": "/google-play/reviews",
      "queryParams": {
        "gl": "us",
        "hl": "en",
        "next_page_token": "eyJ2Ijox…",
        "num": 40,
        "platform": "phone",
        "product_id": "com.duolingo",
        "sort_by": 1,
        "store": "apps"
      }
    },
    "next_page_token": "eyJ2Ijox…"
  },
  "reviews": [
    {
      "avatar": "https://play-lh.googleusercontent.com/a/ACg8ocJtnPpg-JNwnWu_-3krborBic6awbrsvHhU…",
      "date": "2026-09-16T12:36:24Z",
      "id": "98cd315b-60ce-4e15-a68e-0619ea3f330f",
      "iso_date": "2026-09-16T12:36:24Z",
      "likes": 815,
      "rating": 1,
      "snippet": "I don't feel like I'm learning the language I signed up for. There are no speaki…",
      "title": "Lunae Strat",
      "version": "6.96.2"
    }
  ],
  "search_metadata": {
    "created_at": "2026-11-03T07:34:32.406096+00:00",
    "id": "d922cb813d116305007ac3b3",
    "processed_at": "2026-11-03T07:34:32.597521+00:00",
    "status": "Success",
    "total_time_taken": 0.191
  },
  "search_parameters": {
    "gl": "us",
    "hl": "en",
    "num": 40,
    "platform": "phone",
    "product_id": "com.duolingo",
    "sort_by": 1,
    "store": "apps"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `reviews[]` | List of reviews for the product. The list length follows the `num` parameter. |
| `reviews[].id` | Unique ID of the review, in UUID format. |
| `reviews[].title` | Display name shown with the review. It matches the reviewer's name, not a headline. |
| `reviews[].rating` | Star rating the user gave, from 1 to 5. |
| `reviews[].snippet` | Review text. Long reviews appear cut off with an ellipsis. |
| `reviews[].likes` | Number of likes the review received. |
| `reviews[].version` | App version the review refers to, such as `6.96.2`. |
| `reviews[].date / reviews[].iso_date` | Time the review was posted, as a UTC ISO 8601 timestamp. |
| `reviews[].avatar` | URL of the reviewer's profile image. |
| `litescrape_pagination.next_page_token` | Token for the next page of reviews. Pass it as `next_page_token` in the next call. |

### Notes

- Get the `product_id` from the product's Google Play URL (the value after `id=`) or from [Google Play App Search](/apis/google-play/apps).
- To page through results, send `litescrape_pagination.next_page_token` as `next_page_token`. Keep `product_id`, `store`, `hl`, `gl`, `platform`, `rating`, `sort_by`, and `num` the same.
- `litescrape_pagination.next.queryParams` holds the full set of parameters for the next request.
- For app details such as the description and overall rating, call [Google Play Product Details](/apis/google-play/product).

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/google-play/reviews.json`](../../../catalog/models/google-play/reviews.json) · Store page: https://www.sandbase.ai/model/google-play/reviews
