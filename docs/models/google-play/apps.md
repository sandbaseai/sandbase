# Google Play App Search API: pricing, parameters and code examples

`google-play/apps` · data API · Google Play · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

Search Google Play apps by keyword or browse categories and top charts, with rating, price and developer.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-play/apps"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-play/apps', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-play/apps", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-play/apps", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/google-play/apps` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | At most 2,048 UTF-8 bytes.  |
| `gl` | string |  | Two-letter country code. default `"us"` |
| `hl` | string |  | Storefront language, such as en, de, or zh-TW. Maximum 32 characters. default `"en"` |
| `age` | string |  | Children's age range. Requires apps_category=FAMILY. one of: `AGE_RANGE1`, `AGE_RANGE2`, `AGE_RANGE3` |
| `chart` | string |  | Chart identifier such as topselling_free, topselling_paid, or topgrossing. Excludes q and all pagination selectors. Apps and games charts require phone or an omitted store_device.  |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `store_device` | string |  | Omit for the default phone storefront. An explicit selection excludes q and category. one of: `phone`, `tablet`, `tv`, `chromebook`, `watch`, `car` |
| `apps_category` | string |  | Native app category identifier, such as MEDICAL. Excludes q and an explicit store_device.  |
| `see_more_token` | string |  | Open a result collection using its returned token and the same parameters. Excludes the other pagination selectors and chart.  |
| `next_page_token` | string |  | Use the returned next_page_token with the same parameters. Excludes chart, section_page_token, and see_more_token.  |
| `section_page_token` | string |  | Continue one result group using its returned token and the same parameters. Excludes the other pagination selectors and chart.  |

## Details

Returns Google Play app results for a keyword, a category, or a top chart. Each app has a title, developer, category, download band and price. A search with `q` also returns a highlighted best match with rating and review count.

### Use cases

- Find the Google Play listing and `product_id` for a known app name such as Duolingo.
- Build a list of competing or similar apps for a keyword and compare their download bands.
- Pull the top free, paid or grossing apps for a country with `chart` and `gl`.
- Browse one category such as `MEDICAL` to map the apps and developers in it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-play/apps" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "Duolingo"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `age` | string | No | Children's age range. Requires apps_category=FAMILY. |
| `apps_category` | string | No | Native app category identifier, such as MEDICAL. Excludes q and an explicit store_device. |
| `chart` | string | No | Chart identifier such as topselling_free, topselling_paid, or topgrossing. Excludes q and all pagination selectors. Apps and games charts require phone or an omitted store_device. |
| `gl` | string | No | Two-letter country code. |
| `hl` | string | No | Storefront language, such as en, de, or zh-TW. Maximum 32 characters. |
| `next_page_token` | string | No | Use the returned next_page_token with the same parameters. Excludes chart, section_page_token, and see_more_token. |
| `q` | string | No | At most 2,048 UTF-8 bytes. |
| `section_page_token` | string | No | Continue one result group using its returned token and the same parameters. Excludes the other pagination selectors and chart. |
| `see_more_token` | string | No | Open a result collection using its returned token and the same parameters. Excludes the other pagination selectors and chart. |
| `store_device` | string | No | Omit for the default phone storefront. An explicit selection excludes q and category. |
| `timeout` | number | No | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the cal |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "app_highlight": {
    "author": "Duolingo",
    "content_rating": {
      "text": "Everyone",
      "thumbnail": "https://play-lh.googleusercontent.com/IciOnDFecb5Xt50Q2jlcNC0LPI7LEGxNojroo-s3Ao…"
    },
    "description": "Make language learning fun with Spanish, French, English, chess, math & music.",
    "download_count": 992196960,
    "downloads": "500M+",
    "images": [
      "https://play-lh.googleusercontent.com/twmCellsRXWs4bZsSXRv19x-3BIp19FzlQPdu_Va-z…"
    ],
    "link": "https://play.google.com/store/apps/details?id=com.duolingo",
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
    "reviews": 51551171,
    "thumbnail": "https://play-lh.googleusercontent.com/tw_coGKgk1K_zO-Ypf9zBKV1s-KT3dYN1MIUxIqtnb…"
  },
  "organic_results": [
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
      "section_page_token": "eyJ2Ijox…"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `app_highlight.title / app_highlight.author` | Name and developer of the best match for the query. |
| `app_highlight.product_id` | Package ID of the best match, such as `com.duolingo`. Use it to look up the app elsewhere. |
| `app_highlight.rating / app_highlight.reviews` | Average star rating and number of reviews for the best match. |
| `app_highlight.downloads / app_highlight.download_count` | Download band as text (for example `500M+`) and as a number. |
| `app_highlight.offers[].extracted_price / app_highlight.offers[].currency` | Price as a number and its currency code. A value of `0.0` means the app is free to install. |
| `organic_results[].title` | Name of a result group, such as `Similar apps`. The first group in the sample has no title. |
| `organic_results[].items[].product_id / organic_results[].items[].link` | Package ID of the app and the link to its Google Play page. |
| `organic_results[].items[].author / organic_results[].items[].category` | Developer name and Google Play category of the app. |
| `organic_results[].items[].downloads` | Download band as text, such as `10,000,000+`. |
| `organic_results[].items[].extracted_price` | Price as a number. Read it with `currency`. |

### Notes

- Pass one of `q`, `chart` or `apps_category`. `chart` cannot be combined with `q` or with any pagination token.
- To get more apps from one result group, send its `section_page_token` with the same parameters. To open a full collection, send its `see_more_token` with the same parameters.
- Use `product_id` from the results to call [Google Play Product Details](/apis/google-play/product), or [Google Play Reviews](/apis/google-play/reviews) for user reviews.
- For games, use [Google Play Games Search](/apis/google-play/games).

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/google-play/apps.json`](../../../catalog/models/google-play/apps.json) · Store page: https://www.sandbase.ai/model/google-play/apps
