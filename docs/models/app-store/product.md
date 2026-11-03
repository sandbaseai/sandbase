# App Store Product API: pricing, parameters and code examples

`app-store/product` · data API · App Store · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** async

Read an iOS or Mac app's details, version history, ratings, privacy, and related apps.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "app-store/product", "product_id": "570060128"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('app-store/product', {'product_id': '570060128'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("app-store/product", {
  "product_id": "570060128"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "app-store/product", sandbase.Params{
	"product_id": "570060128",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/app-store/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | string |  | App product type; only 'app' is supported. one of: `app` |
| `country` | string |  | Two-letter Apple storefront country, such as 'us' or 'gb' ('uk' is accepted). Default 'us'.  |
| `product_id` | string | yes | Positive decimal Apple app identifier, such as '570060128'.  |

## Details

Returns the App Store page data for one app: title, developer, rating, version history, privacy labels, screenshots, review samples, and related apps. It needs an Apple app ID as `product_id` and takes an optional storefront `country`.

### Use cases

- Track an app's release cadence by reading `version_history` for version numbers, dates, and release notes.
- Compare a competitor's star distribution with your own app using `ratings_and_reviews.rating_distribution`.
- Audit which data types an app says it collects by reading the `privacy.cards` categories.
- Find competing apps through the `you_may_also_like` and `more_by_this_developer` lists.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/app-store/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "570060128", "country": "us", "type": "app"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Positive decimal Apple app identifier, such as '570060128'. |
| `country` | string | No | Two-letter Apple storefront country, such as 'us' or 'gb' ('uk' is accepted). Default 'us'. |
| `type` | string | No | App product type; only 'app' is supported. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "age_rating": "4+",
  "description": "Learn a new language, chess & more with the world's most downloaded education ap…",
  "developer": {
    "link": "https://apps.apple.com/us/developer/duolingo/id570060151",
    "name": "Duolingo"
  },
  "featured_in": [
    {
      "description": "Master a new skill and make Duo proud.",
      "description_title": "5 Tips for Duolingo Domination",
      "image": "https://is1-ssl.mzstatic.com/image/thumb/Features221/v4/75/d4/f7/75d4f7e6-5481-b…",
      "link": "https://apps.apple.com/us/iphone/story/id1748181882",
      "title": "TRY NOW"
    }
  ],
  "id": "570060128",
  "in_app_purchases": "In‑App Purchases",
  "information": {
    "age_rating": {
      "rating": "4+"
    },
    "compatibility": [
      {}
    ],
    "in_app_purchases": []
  },
  "ipad_screenshots": [
    "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/76/6d/5b/766d5b1d-c0…"
  ],
  "iphone_screenshots": [
    "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/6e/ef/30/6eef3023-de…"
  ],
  "logo": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/29/f8/76/29f8764d-ab…",
  "more_by_this_developer": {
    "apps": [
      {
        "category": "Interactive Stories for Kids",
        "id": 1440502568,
        "link": "https://apps.apple.com/us/app/learn-to-read-duolingo-abc/id1440502568",
        "logo": "https://is1-ssl.mzstatic.com/image/thumb/Purple126/v4/98/01/13/980113b8-da7c-7c2…",
        "name": "Learn to Read - Duolingo ABC"
      }
    ],
    "see_all_link": "https://apps.apple.com/us/developer/duolingo/id570060151"
  },
  "price": "Get"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title / snippet` | The app name and its short subtitle as shown on the store page. |
| `rating / rating_count` | The average star rating as a number, and the rating total as display text such as `5.6M Ratings`. |
| `ratings_and_reviews.rating_distribution` | An object with the number of ratings at each star level. The keys run from `1_star` to `5_star`. |
| `ratings_and_reviews.review_examples[].review_title / review_text / rating / review_date / username` | A few sample reviews with the star value and an ISO 8601 timestamp. |
| `version_history[].release_version / release_date / release_notes` | One entry per release, with the version number, the release date as `YYYY-MM-DD`, and the notes text. |
| `developer.name / developer.link` | The developer name and the link to its App Store developer page. |
| `privacy.cards[].title / categories` | Each card is a privacy group, such as data used to track you. `categories` lists the data types in that group. |
| `privacy.privacy_policy_link` | The link to the developer's privacy policy. |
| `you_may_also_like.apps[].id / name / link` | Related apps shown on the page, with their app ID, name, and store link. |
| `more_by_this_developer.apps[].id / name / link` | Other apps from the same developer, with their app ID, name, and store link. |

### Notes

- Get `product_id` from the number after `id` in an App Store URL, such as `570060128` in `.../id570060128`.
- Use [App Store Search](/apis/app-store/search) to find an app ID from a keyword.
- Use [App Store Reviews](/apis/app-store/reviews) to read more reviews than the few in `review_examples`.
- IDs in `you_may_also_like.apps[].id` and `more_by_this_developer.apps[].id` can be used as `product_id` in a new call.

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/app-store/product.json`](../../../catalog/models/app-store/product.json) · Store page: https://www.sandbase.ai/model/app-store/product
