# Google Play Product Details API: pricing, parameters and code examples

`google-play/product` · data API · Google Play · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

Details of a Google Play app, game, ebook, audiobook or movie by product ID: rating, downloads, price, developer and description.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-play/product", "product_id": "com.duolingo"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-play/product', {'product_id': 'com.duolingo'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-play/product", {
  "product_id": "com.duolingo"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-play/product", sandbase.Params{
	"product_id": "com.duolingo",
})
```

Same call via the path form: `POST /v1/api/google-play/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Two-letter country code. default `"us"` |
| `hl` | string |  | Storefront language, such as en, de, or zh-TW. Maximum 32 characters. default `"en"` |
| `store` | string |  | Product catalog containing this identifier. one of: `apps`, `books`, `audiobooks`, `movies`, `tv`; default `"apps"` |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `season_id` | string |  | Native season identifier, such as tvseason-OVPad1njPzI.P. Requires store=tv.  |
| `product_id` | string | yes | Native Google Play product identifier, with 1 to 512 letters, digits, underscores, dots, or hyphens.  |

## Details

Returns the Google Play store listing for one product, such as an app, game, ebook, audiobook, movie or TV show. It needs a `product_id` like `com.duolingo`, and the `store` parameter selects the catalog (default `apps`).

### Use cases

- Track an app's rating, review count and download count over time.
- Check an app's price, in-app purchase range and content rating before listing it in a catalog.
- Review the permissions and data safety entries of an app for a compliance check.
- Find developer contact details and competing apps from the similar apps lists.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-play/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "com.duolingo"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Native Google Play product identifier, with 1 to 512 letters, digits, underscores, dots, or hyphens. |
| `gl` | string | No | Two-letter country code. |
| `hl` | string | No | Storefront language, such as en, de, or zh-TW. Maximum 32 characters. |
| `season_id` | string | No | Native season identifier, such as tvseason-OVPad1njPzI.P. Requires store=tv. |
| `store` | string | No | Product catalog containing this identifier. |
| `timeout` | number | No | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the cal |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "about_this_app": {
    "content_rating": "Everyone",
    "downloads": "500,000,000+",
    "in_app_purchases": "$0.99 - $239.99 per item",
    "interactive_elements": "Users Interact, In-App Purchases",
    "offered_by": "Duolingo",
    "released_on": "May 29, 2013",
    "short_description": "Make language learning fun with Spanish, French, English, chess, math & music.",
    "snippet": "Learn a new language, chess, math & more with the world’s most downloaded educat…",
    "updated_on": "Nov 3, 2026"
  },
  "badges": [
    {
      "name": "#1 top free education"
    }
  ],
  "categories": [
    {
      "category_id": "EDUCATION",
      "link": "https://play.google.com/store/apps/category/EDUCATION",
      "name": "Education"
    }
  ],
  "data_safety": [
    {
      "subtext": "App activity, App info and performance, and Device or other IDs",
      "text": "This app may share these data types with third parties"
    }
  ],
  "developer_contact": {
    "address": "5900 Penn Ave\nPittsburgh, PA 15206\nUnited States",
    "alternative_email": "android@duolingo.com",
    "name": "Duolingo, Inc.",
    "phone_number": "+1 412-567-6602",
    "privacy_policy": "https://www.duolingo.com/privacy",
    "support_email": "super-support@duolingo.com",
    "website": "https://www.duolingo.com/help/support-request"
  },
  "media": {
    "images": [
      "https://play-lh.googleusercontent.com/twmCellsRXWs4bZsSXRv19x-3BIp19FzlQPdu_Va-z…"
    ]
  },
  "permissions": [
    {
      "name": "Identity",
      "permissions": [
        "find accounts on the device"
      ]
    }
  ],
  "product_info": {
    "authors": [
      {
        "link": "https://play.google.com/store/apps/dev?id=6957685454452609502",
        "name": "Duolingo"
      }
    ],
    "content_rating": {
      "text": "Everyone",
      "thumbnail": "https://play-lh.googleusercontent.com/IciOnDFecb5Xt50Q2jlcNC0LPI7LEGxNojroo-s3Ao…"
    },
    "download_count": 992196960,
    "downloads": "500M+",
    "editors_choice": true,
    "extensions": [
      "Contains ads"
    ],
    "offers": [
      {
        "currency": "USD",
        "extracted_price": 0.0,
        "link": "https://play.google.com/store/apps/details?id=com.duolingo&rdid=com.duolingo&fea…",
        "text": "Install"
      }
    ],
    "product_id": "com.duolingo",
    "rating": 4.7465396,
    "reviews": 51551173,
    "thumbnail": "https://play-lh.googleusercontent.com/tw_coGKgk1K_zO-Ypf9zBKV1s-KT3dYN1MIUxIqtnb…",
    "title": "Duolingo: Learn Languages"
  },
  "ratings": [
    {
      "count": 945867,
      "stars": 1
    }
  ],
  "released_on": "May 29, 2013",
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
  "similar_results": [
    {
      "items": [
        {
          "author": "Duolingo",
          "category": "Education",
          "currency": "USD",
          "description": "From the creators behind Duolingo, the world’s #1 education app, comes Duolingo …",
          "downloads": "10,000,000+",
          "extracted_price": 0.0,
          "link": "https://play.google.com/store/apps/details?id=com.duolingo.literacy",
          "product_id": "com.duolingo.literacy"
        }
      ],
      "see_more_link": "https://play.google.com/store/apps/dev?id=6957685454452609502",
      "title": "More by Duolingo"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `product_info.title` | Name of the product as shown on its store page. |
| `product_info.rating / product_info.reviews` | Average star rating and total number of reviews. |
| `product_info.downloads / product_info.download_count` | Download count as a short label such as `500M+` and as a number. |
| `product_info.offers[]` | Ways to get the product. Each row has `text`, `extracted_price` and `currency`, so a free app shows `Install` with a price of `0.0`. |
| `about_this_app.in_app_purchases` | Price range of in-app purchases, as text. |
| `ratings[].stars / ratings[].count` | Number of ratings given at each star level. |
| `developer_contact.name / developer_contact.support_email / developer_contact.website` | Developer name and support contact details. |
| `permissions[].name / permissions[].permissions` | Permission groups the app asks for, with the actions in each group. |
| `reviews[].rating / reviews[].snippet / reviews[].likes / reviews[].version` | A sample review with its star rating, a text excerpt, helpful votes and the app version it refers to. |
| `similar_results[].items[].product_id` | Product ID of a related app. Each group has a `title` such as `Similar apps` and a `see_more_link`. |

### Notes

- The `product_id` for an app is the `id` value in its Google Play URL, for example `com.duolingo`.
- Set `store` to `books`, `audiobooks`, `movies` or `tv` for other catalogs. `season_id` works only with `store=tv`.
- Review `date` and `iso_date` values use ISO 8601 format, such as `2026-09-16T12:36:24Z`. The sample here is a short list. For more reviews, use [Google Play Reviews](/apis/google-play/reviews).
- To find product IDs by keyword, use [Google Play App Search](/apis/google-play/apps).

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/google-play/product.json`](../../../catalog/models/google-play/product.json) · Store page: https://www.sandbase.ai/model/google-play/product
