# Google Play Games Search API: pricing, parameters and code examples

`google-play/games` · data API · Google Play · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

Search Google Play games by keyword or browse game categories and top charts.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-play/games"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-play/games', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-play/games", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-play/games", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/google-play/games` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | At most 2,048 UTF-8 bytes.  |
| `gl` | string |  | Two-letter country code. default `"us"` |
| `hl` | string |  | Storefront language, such as en, de, or zh-TW. Maximum 32 characters. default `"en"` |
| `chart` | string |  | Chart identifier such as topselling_free, topselling_paid, or topgrossing. Excludes q and all pagination selectors. Apps and games charts require phone or an omitted store_device.  |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `store_device` | string |  | Omit for the default phone storefront. An explicit selection excludes q and category. one of: `phone`, `tablet`, `tv`, `chromebook`, `watch`, `windows` |
| `games_category` | string |  | Native game category identifier, such as GAME_PUZZLE. Excludes q and an explicit store_device.  |
| `see_more_token` | string |  | Open a result collection using its returned token and the same parameters. Excludes the other pagination selectors and chart.  |
| `next_page_token` | string |  | Use the returned next_page_token with the same parameters. Excludes chart, section_page_token, and see_more_token.  |
| `section_page_token` | string |  | Continue one result group using its returned token and the same parameters. Excludes the other pagination selectors and chart.  |

## Details

This API returns Google Play games that match a keyword, a game category, or a top chart. Send a search term in `q`, or use `chart` or `games_category` to browse. Each result lists the game's developer, category, download band, price, and rating.

### Use cases

- Find chess apps on Google Play and compare their download bands and ratings.
- Track which games appear in the `topselling_free` or `topgrossing` chart for a country.
- List all games in a category such as `GAME_PUZZLE` to see who publishes them.
- Build a list of `product_id` values to feed into a details or reviews lookup.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-play/games" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "chess"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `chart` | string | No | Chart identifier such as topselling_free, topselling_paid, or topgrossing. Excludes q and all pagination selectors. Apps and games charts require phone or an omitted store_device. |
| `games_category` | string | No | Native game category identifier, such as GAME_PUZZLE. Excludes q and an explicit store_device. |
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
  "organic_results": [
    {
      "items": [
        {
          "author": "Chess.com",
          "category": "Board",
          "currency": "USD",
          "downloads": "100,000,000+",
          "extracted_price": 0.0,
          "link": "https://play.google.com/store/apps/details?id=com.chess",
          "product_id": "com.chess",
          "rating": 4.6958847
        }
      ]
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `organic_results[].items[]` | One game result. Results are grouped in lists under `organic_results`. |
| `organic_results[].items[].product_id` | The app package name, such as `com.chess`. It is also the `id` value in the `link` URL. |
| `organic_results[].items[].link` | URL of the game's Google Play store page. |
| `organic_results[].items[].author` | Name of the developer or publisher shown for the game. |
| `organic_results[].items[].category` | Game category label, such as `Board`. |
| `organic_results[].items[].downloads` | Download band shown on the store, as text such as `100,000,000+`. |
| `organic_results[].items[].extracted_price / organic_results[].items[].currency` | Price as a number and its currency code. A value of `0.0` means the game has no purchase price. |
| `organic_results[].items[].rating` | Average star rating as a decimal number. Some games have no `rating` field. |
| `organic_results[].items[].description` | Short store description, cut off with an ellipsis. It appears only on some results. |

### Notes

- Use either `q`, `chart`, or `games_category`. The parameter descriptions say `chart` and `games_category` exclude `q`.
- To get the next page, send the returned `next_page_token` with the same parameters. `section_page_token` and `see_more_token` work the same way for a result group or collection.
- Pass a `product_id` to [Google Play Product Details](/apis/google-play/product) for full details, or to [Google Play Reviews](/apis/google-play/reviews) for user reviews.
- Use [Google Play App Search](/apis/google-play/apps) to search non-game apps.

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/google-play/games.json`](../../../catalog/models/google-play/games.json) · Store page: https://www.sandbase.ai/model/google-play/games
