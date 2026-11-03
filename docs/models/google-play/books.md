# Google Play Books Search API: pricing, parameters and code examples

`google-play/books` · data API · Google Play · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

Search Google Play ebooks and audiobooks by keyword or browse categories and charts.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-play/books"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-play/books', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-play/books", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-play/books", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/google-play/books` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | At most 2,048 UTF-8 bytes.  |
| `gl` | string |  | Two-letter country code. default `"us"` |
| `hl` | string |  | Storefront language, such as en, de, or zh-TW. Maximum 32 characters. default `"en"` |
| `age` | string |  | Children's age range. Requires books_category=coll_1689. one of: `AGE_RANGE1`, `AGE_RANGE2`, `AGE_RANGE3` |
| `chart` | string |  | Chart identifier such as topselling_free, topselling_paid, or topgrossing. Excludes q and all pagination selectors. Apps and games charts require phone or an omitted store_device.  |
| `price` | integer |  | 1 for free books or 2 for paid books. Requires q.  |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `books_category` | string |  | Native book category identifier, such as coll_1689 for children's books. Excludes q.  |
| `see_more_token` | string |  | Open a result collection using its returned token and the same parameters. Excludes the other pagination selectors and chart.  |
| `next_page_token` | string |  | Use the returned next_page_token with the same parameters. Excludes chart, section_page_token, and see_more_token.  |
| `section_page_token` | string |  | Continue one result group using its returned token and the same parameters. Excludes the other pagination selectors and chart.  |

## Details

Returns Google Play book results for a keyword, grouped into sections such as series, ebooks and audiobooks. You send a search term in `q`, or you browse with `books_category` or `chart`. Each item has a title or author, a link and price data.

### Use cases

- Compare ebook and audiobook prices for a title across the Google Play storefront.
- List every book in a series, such as Dune, with its position in the series.
- Build a catalog of a author's works with links to each Google Play page.
- Track discounts by comparing `extracted_original_price` with `extracted_price` on audiobooks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-play/books" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "Dune"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `age` | string | No | Children's age range. Requires books_category=coll_1689. |
| `books_category` | string | No | Native book category identifier, such as coll_1689 for children's books. Excludes q. |
| `chart` | string | No | Chart identifier such as topselling_free, topselling_paid, or topgrossing. Excludes q and all pagination selectors. Apps and games charts require phone or an omitted store_device. |
| `gl` | string | No | Two-letter country code. |
| `hl` | string | No | Storefront language, such as en, de, or zh-TW. Maximum 32 characters. |
| `next_page_token` | string | No | Use the returned next_page_token with the same parameters. Excludes chart, section_page_token, and see_more_token. |
| `price` | integer | No | 1 for free books or 2 for paid books. Requires q. |
| `q` | string | No | At most 2,048 UTF-8 bytes. |
| `section_page_token` | string | No | Continue one result group using its returned token and the same parameters. Excludes the other pagination selectors and chart. |
| `see_more_token` | string | No | Open a result collection using its returned token and the same parameters. Excludes the other pagination selectors and chart. |
| `timeout` | number | No | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the cal |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "organic_results": [
    {
      "items": [
        {
          "extension": "8 items",
          "format": "Ebook series",
          "link": "https://play.google.com/store/books/series?id=av3XFwAAABC86M",
          "product_id": "av3XFwAAABC86M",
          "thumbnail": "https://play-lh.googleusercontent.com/DO9D9mcmQJ8OXHXGOFyfQWRKgzoTlKbw1Epd4kHRZm…",
          "title": "Dune"
        }
      ],
      "see_more_link": "https://play.google.com/store/books/collection/cluster?gsr=SlBqLGhVcU5uUGxzV1VxN…",
      "see_more_token": "eyJ2Ijox…",
      "title": "Series"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `organic_results[]` | One result group. Each group has a `title` such as `Series`, `Ebooks` or `Audiobooks`, and a list of `items`. |
| `organic_results[].items[].title` | Name of the item. Series items include it; book items in this response do not. |
| `organic_results[].items[].author / category` | Author name and genre label of a book or audiobook. |
| `organic_results[].items[].link` | Google Play URL for the item. Book and audiobook links contain an `id` query value. |
| `organic_results[].items[].product_id` | ID of a series item. It also appears in the series `link`. |
| `organic_results[].items[].format / extension` | `format` names the item type, such as `Ebook series`. `extension` gives extra detail, such as `8 items` for a series or `Book 1` for an ebook. |
| `organic_results[].items[].price / extracted_price / currency` | Price as display text, as a number, and its currency code, such as `$9.99`, `9.99` and `USD`. |
| `organic_results[].items[].original_price / extracted_original_price` | List price before a discount, as text and as a number. Audiobooks show it next to a lower `extracted_price`. |
| `organic_results[].section_page_token / see_more_token` | Tokens for loading more items in this group or opening its full collection. |
| `organic_results[].see_more_link` | Google Play URL of the full collection for this group. |

### Notes

- Pass `section_page_token` or `see_more_token` back with the same parameters to continue one group. Do not combine it with `chart`.
- `q` excludes `chart` and `books_category`. `price` (`1` free, `2` paid) requires `q`.
- `age` works only with `books_category=coll_1689`.
- Not every item has every field. Series items have no price, and some books have no `description`.

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/google-play/books.json`](../../../catalog/models/google-play/books.json) · Store page: https://www.sandbase.ai/model/google-play/books
