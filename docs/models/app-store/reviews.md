# App Store Reviews API: pricing, parameters and code examples

`app-store/reviews` · data API · App Store · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** async

Read Apple App Store reviews for an app in one storefront country, page by page.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "app-store/reviews", "product_id": "570060128"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('app-store/reviews', {'product_id': '570060128'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("app-store/reviews", {
  "product_id": "570060128"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "app-store/reviews", sandbase.Params{
	"product_id": "570060128",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/app-store/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | One-based page number. Exhausted pages return an empty review list. Default 1. range 1–2147483647 |
| `sort` | string |  | 'mostrecent' or 'mosthelpful'. The Mac storefront always returns newest first. Default 'mostrecent'. one of: `mostrecent`, `mosthelpful` |
| `country` | string |  | Two-letter Apple storefront country, such as 'us' or 'gb' ('uk' is accepted). Default 'us'.  |
| `product_id` | string | yes | Positive decimal Apple app identifier, such as '570060128'.  |

## Details

Returns Apple App Store reviews for one app in one storefront country. You pass the numeric Apple app ID as `product_id`. Each call returns one page of reviews with rating, title, text, author and app version.

### Use cases

- Track new 1-star and 2-star reviews for your app to catch bugs after a release.
- Pull reviews for a competitor app and compare complaints by app version.
- Export reviews from several storefront countries to compare feedback across markets.
- Sort by `mosthelpful` to find the issues that other users agree with most.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/app-store/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "570060128"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Positive decimal Apple app identifier, such as '570060128'. |
| `country` | string | No | Two-letter Apple storefront country, such as 'us' or 'gb' ('uk' is accepted). Default 'us'. |
| `page` | integer | No | One-based page number. Exhausted pages return an empty review list. Default 1. |
| `sort` | string | No | 'mostrecent' or 'mosthelpful'. The Mac storefront always returns newest first. Default 'mostrecent'. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "litescrape_pagination": {
    "current": {
      "endpoint": "/app-store/reviews",
      "queryParams": {
        "country": "us",
        "page": 1,
        "product_id": "570060128",
        "sort": "mostrecent"
      }
    },
    "next": {
      "endpoint": "/app-store/reviews",
      "queryParams": {
        "country": "us",
        "page": 2,
        "product_id": "570060128",
        "sort": "mostrecent"
      }
    }
  },
  "reviews": [
    {
      "author": {
        "author_id": "18461997",
        "name": "Anti-Propagandist"
      },
      "id": "14740253307",
      "position": 1,
      "rating": 1,
      "review_date": "Nov 02, 2026",
      "reviewed_version": "Version 7.146.1",
      "text": "I've loved this app for years, and have been a subscriber as well, but for both …",
      "title": "Can't ever get help from a human..."
    }
  ],
  "search_information": {
    "results_count": 25,
    "total_page_count": 16010
  },
  "search_metadata": {
    "created_at": "2026-11-03T07:27:07.922447+00:00",
    "id": "0d6cad836d28803924d19d2e",
    "processed_at": "2026-11-03T07:27:07.988746+00:00",
    "status": "Success",
    "total_time_taken": 0.067
  },
  "search_parameters": {
    "country": "us",
    "page": 1,
    "product_id": "570060128",
    "sort": "mostrecent"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `reviews[].id` | ID of the review. |
| `reviews[].rating` | Star rating given in the review, as a whole number. |
| `reviews[].title / reviews[].text` | Headline and body of the review. Long text may be shortened. |
| `reviews[].review_date` | Date of the review as a text string, for example `Nov 02, 2026`. |
| `reviews[].reviewed_version` | App version the reviewer used, for example `Version 7.146.1`. |
| `reviews[].author.name / reviews[].author.author_id` | Display name and ID of the reviewer. |
| `reviews[].position` | Position of the review within the returned page, starting at 1. |
| `search_information.results_count` | Number of reviews returned on this page. |
| `search_information.total_page_count` | Total number of pages available for this app, country and sort. |
| `litescrape_pagination.next.queryParams` | Parameters to send for the next page, including the incremented `page` value. |

### Notes

- Find the `product_id` with [App Store Search](/apis/app-store/search) or in the app's App Store URL after `id`. [App Store Product](/apis/app-store/product) returns details for the same app.
- To read more reviews, raise `page` by one on each call. Exhausted pages return an empty `reviews` list.
- `review_date` is a text string in the form `Nov 02, 2026`, not an ISO timestamp.
- The response echoes the values used in `search_parameters`, so you can see the applied defaults for `country`, `page` and `sort`.

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/app-store/reviews.json`](../../../catalog/models/app-store/reviews.json) · Store page: https://www.sandbase.ai/model/app-store/reviews
