# Capterra Product Reviews API: pricing, parameters and code examples

`capterra/product-reviews` · data API · Capterra · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retrieve user reviews for a software product. Returns paginated reviews with title, date, overall rating, pros, and cons text (up to 25 reviews per page).

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "capterra/product-reviews", "product_id": "155928", "product_name": "Zoho-CRM"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('capterra/product-reviews', {'product_id': '155928', 'product_name': 'Zoho-CRM'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("capterra/product-reviews", {
  "product_id": "155928",
  "product_name": "Zoho-CRM"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "capterra/product-reviews", sandbase.Params{
	"product_id": "155928",
	"product_name": "Zoho-CRM",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/capterra/product-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number of reviews to retrieve. range -9007199254740991–9007199254740991 |
| `product_id` | string | yes | The numeric product ID (e.g. '155928'). Available from get_category_products or search_software results.  |
| `product_name` | string | yes | The URL slug of the product (e.g. 'Zoho-CRM', 'HubSpot-CRM'). Available from get_category_products or search_software results.  |

## Details

Returns user reviews for a software product listed on Capterra. Each review has a title, date, overall rating, pros text, and cons text. You send the numeric `product_id` and the URL slug `product_name`, with an optional `page` number.

### Use cases

- Collect written pros and cons for a CRM product to compare it against competitors.
- Track how the overall rating of a product changes across review dates.
- Feed review text into a sentiment or topic analysis of what users like and dislike.
- Build a feed of the newest reviews for a vendor to share with a sales or product team.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/capterra/product-reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "155928", "product_name": "Zoho-CRM", "page": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | The numeric product ID (e.g. '155928'). Available from get_category_products or search_software results. |
| `product_name` | string | Yes | The URL slug of the product (e.g. 'Zoho-CRM', 'HubSpot-CRM'). Available from get_category_products or search_software results. |
| `page` | integer | No | Page number of reviews to retrieve. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "page": "1",
    "product_id": "155928",
    "reviews": [
      {
        "cons": "Creating custom pipelines was a bit complex when I was a new user, but now since…",
        "date": "October 28, 2026",
        "pros": "I give thumbs up to the vendor because they make sure that I get leads from ever…",
        "rating": "4.0",
        "title": "Account & Contact Management GURU of 2026"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.reviews[].title` | Headline the reviewer gave the review. Some reviews have no title, so the key can be missing. |
| `data.reviews[].date` | Date of the review as text, for example `October 28, 2026`. |
| `data.reviews[].rating` | Overall rating given by the reviewer, returned as a string such as `4.0`. |
| `data.reviews[].pros` | Reviewer's text about what they liked. Long text may be cut short with an ellipsis. |
| `data.reviews[].cons` | Reviewer's text about what they disliked. Long text may be cut short with an ellipsis. |
| `data.page` | Page number of reviews that this response covers, returned as a string. |
| `data.product_id` | The product ID the reviews belong to, echoing the request. |

### Notes

- Get `product_id` and `product_name` from [Capterra Search Software](/apis/capterra/search-software) or [Capterra Category Products](/apis/capterra/category-products).
- Use `page` to step through results. Each page returns reviews in the order shown, with up to 25 reviews.
- Call [Capterra Product Details](/apis/capterra/product-details) for product-level information beyond individual reviews.
- `rating` and `page` come back as strings, so convert them to numbers if you need to sort or calculate.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/capterra/product-reviews.json`](../../../catalog/models/capterra/product-reviews.json) · Store page: https://www.sandbase.ai/model/capterra/product-reviews
