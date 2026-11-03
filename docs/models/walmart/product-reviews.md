# Walmart Product Reviews API: pricing, parameters and code examples

`walmart/product-reviews` · data API · Walmart · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Get Walmart product reviews by product ID: overall rating, ratings histogram, top positive and negative reviews, and paginated review text with photos.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "walmart/product-reviews", "product_id": "20349310960"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('walmart/product-reviews', {'product_id': '20349310960'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("walmart/product-reviews", {
  "product_id": "20349310960"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "walmart/product-reviews", sandbase.Params{
	"product_id": "20349310960",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/walmart/product-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string \\| number \\| boolean |  | Value is used to get the reviews on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.).  |
| `sort` | string \\| number \\| boolean |  | Sorting reviews. It can be set to: `relevancy`, `helpful`, `submission-desc`, `submission-asc`, `rating-desc`, `rating-asc`  |
| `rating` |  |  | Filtering reviews by rating. It can be set to: `1`: 1-star, `2`: 2-star, `3`: 3-star, `4`: 4-star, `5`: 5-star.  |
| `product_id` | string \\| number \\| boolean | yes | The unique product identifier to get reviews of a specific product. You need to pass the `us_item_id`. It can be found from either Organic Results API or Product API results.  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Returns customer reviews for one Walmart product, along with the overall rating, a star-rating histogram, the top positive and top negative review, and a page of review text. It needs a Walmart product ID (`product_id`), which is the `us_item_id`.

### Use cases

- Track how shoppers rate a laptop or other product by reading the star counts in `ratings`.
- Pull 1-star reviews with the `rating` filter to find common complaints about a product.
- Compare the `top_positive` and `top_negative` reviews to see the main praise and the main problem at a glance.
- Collect review text page by page to run sentiment analysis on a single product.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/walmart/product-reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "20349310960"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | ['string', 'number', 'boolean'] | Yes | The unique product identifier to get reviews of a specific product. You need to pass the `us_item_id`. It can be found from either Organic Results API or Product API results. |
| `json_restrictor` | ['string', 'number', 'boolean'] | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `page` | ['string', 'number', 'boolean'] | No | Value is used to get the reviews on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). |
| `rating` | string | No | Filtering reviews by rating. It can be set to: `1`: 1-star, `2`: 2-star, `3`: 3-star, `4`: 4-star, `5`: 5-star. |
| `sort` | ['string', 'number', 'boolean'] | No | Sorting reviews. It can be set to: `relevancy`, `helpful`, `submission-desc`, `submission-asc`, `rating-desc`, `rating-asc` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "overall_rating": 4.4,
  "pagination": {
    "current": 1,
    "next": "https://www.walmart.com/reviews/product/20349310960?sort=relevancy&page=2",
    "other_pages": {
      "2": "https://www.walmart.com/reviews/product/20349310960?sort=relevancy&page=2",
      "3": "https://www.walmart.com/reviews/product/20349310960?sort=relevancy&page=3",
      "4": "https://www.walmart.com/reviews/product/20349310960?sort=relevancy&page=4",
      "5": "https://www.walmart.com/reviews/product/20349310960?sort=relevancy&page=5",
      "6": "https://www.walmart.com/reviews/product/20349310960?sort=relevancy&page=6",
      "9": "https://www.walmart.com/reviews/product/20349310960?sort=relevancy&page=9"
    }
  },
  "product": {
    "categories": [
      {
        "name": "Electronics",
        "url": "https://www.walmart.com/cp/electronics/3944"
      }
    ],
    "name": "Acer Chromebook 315 15.6\" Touchscreen Laptop FHD 1920x1080 Intel N50 8GB RAM 128…",
    "url": "https://www.walmart.com/ip/Acer-Chromebook-315-15-6-Touchscreen-Laptop-FHD-1920x…"
  },
  "ratings": [
    {
      "count": 74,
      "stars": 1
    }
  ],
  "reviews": [
    {
      "customer_type": [
        "VerifiedPurchaser"
      ],
      "negative_feedback": 0,
      "position": 1,
      "positive_feedback": 2,
      "rating": 5,
      "review_submission_time": "10/8/2026",
      "text": "Bought this on sale for $199 to replace an over 7year old Acer Chromebook that's…",
      "title": "Chromebook",
      "user_nickname": "Brian"
    }
  ],
  "search_metadata": {
    "cached": false,
    "created_at": "2026-11-03 07:45:07 UTC",
    "id": "6ae991038b84161e987a4392",
    "processed_at": "2026-11-03 07:45:07 UTC",
    "status": "Success",
    "total_time_taken": 0.68,
    "walmart_product_reviews_url": "https://www.walmart.com/reviews/product/20349310960?sort=relevancy&page=1"
  },
  "search_parameters": {
    "engine": "walmart_product_reviews",
    "product_id": "20349310960"
  },
  "serpapi_pagination": {
    "current": 1,
    "next": {
      "endpoint": "/walmart/product-reviews",
      "queryParams": {
        "page": "2",
        "product_id": "20349310960",
        "sort": "relevancy"
      }
    },
    "next_link": {
      "endpoint": "/walmart/product-reviews",
      "queryParams": {
        "page": "2",
        "product_id": "20349310960",
        "sort": "relevancy"
      }
    },
    "other_pages": {
      "2": {
        "endpoint": "/walmart/product-reviews",
        "queryParams": {
          "page": "2",
          "product_id": "20349310960",
          "sort": "relevancy"
        }
      },
      "3": {
        "endpoint": "/walmart/product-reviews",
        "queryParams": {
          "page": "3",
          "product_id": "20349310960",
          "sort": "relevancy"
        }
      },
      "4": {
        "endpoint": "/walmart/product-reviews",
        "queryParams": {
          "page": "4",
          "product_id": "20349310960",
          "sort": "relevancy"
        }
      },
      "5": {
        "endpoint": "/walmart/product-reviews",
        "queryParams": {
          "page": "5",
          "product_id": "20349310960",
          "sort": "relevancy"
        }
      },
      "6": {
        "endpoint": "/walmart/product-reviews",
        "queryParams": {
          "page": "6",
          "product_id": "20349310960",
          "sort": "relevancy"
        }
      },
      "9": {
        "endpoint": "/walmart/product-reviews",
        "queryParams": {
          "page": "9",
          "product_id": "20349310960",
          "sort": "relevancy"
        }
      }
    }
  },
  "top_negative": {
    "customer_type": [
      "VerifiedPurchaser"
    ],
    "negative_feedback": 0,
    "positive_feedback": 0,
    "rating": 1,
    "review_submission_time": "10/30/2026",
    "text": "We went to the store to return this laptop.And they said we had to go back into …",
    "user_nickname": "Peggy"
  },
  "top_positive": {
    "customer_type": [
      "IncentivizedReviewYes"
    ],
    "negative_feedback": 0,
    "positive_feedback": 3,
    "rating": 5,
    "review_submission_time": "7/27/2026",
    "text": "I am so thankful for this one! The touch features just glide and work without is…",
    "title": "Highly recommend",
    "user_nickname": "TiffanyT"
  },
  "total_count": 807
}
```

### Response fields

| Field | Meaning |
|---|---|
| `overall_rating` | Average star rating for the product, for example `4.4`. |
| `total_count` | Total number of reviews for the product. |
| `ratings[].stars / ratings[].count` | Histogram rows. Each row gives a star level and the number of reviews at that level. |
| `reviews[].rating / reviews[].title / reviews[].text` | Star rating, headline and body text of each review on the current page. Long text may be shortened. |
| `reviews[].user_nickname / reviews[].review_submission_time` | Display name of the reviewer and the date the review was submitted, in `M/D/YYYY` format. |
| `reviews[].positive_feedback / reviews[].negative_feedback` | Counts of positive and negative feedback votes the review received. |
| `reviews[].customer_type` | List of labels on the reviewer, such as `VerifiedPurchaser`, `Staff` or `IncentivizedReviewYes`. |
| `top_positive / top_negative` | The review Walmart highlights as the top positive one and the top negative one. They have the same fields as items in `reviews`. |
| `product.name / product.url / product.categories[]` | Name and page URL of the product, plus its category path with each category's `name` and `url`. |
| `pagination.current / pagination.next / pagination.other_pages` | Current page number and Walmart review page URLs for other pages. |

### Notes

- Get `product_id` from the `us_item_id` in [Walmart Search](/apis/walmart/search) or [Walmart Product Page](/apis/walmart/scrape/product) results.
- Set `page` to get more reviews. The `serpapi_pagination.next.queryParams` object shows the parameters for the next page.
- Use `sort` with values such as `helpful` or `submission-desc` to change review order, and `rating` to filter by star level.
- Use `json_restrictor` to return only the fields you need.

### Pricing

$0.015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/walmart/product-reviews.json`](../../../catalog/models/walmart/product-reviews.json) · Store page: https://www.sandbase.ai/model/walmart/product-reviews
