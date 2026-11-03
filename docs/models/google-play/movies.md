# Google Play Movies API: pricing, parameters and code examples

`google-play/movies` · data API · Google Play · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** async

Search or browse movies, TV shows, episodes, categories, and charts on Google Play.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-play/movies"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-play/movies', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-play/movies", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-play/movies", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/google-play/movies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Search query, 1-2,048 bytes. Excludes category and chart; omit it to browse the storefront.  |
| `gl` | string |  | Two-letter country code. Default 'us'.  |
| `hl` | string |  | Storefront language, such as 'en', 'de', or 'zh-TW'. Default 'en'.  |
| `age` | string |  | Children's age range. Requires movies_category 'FAMILY'. one of: `AGE_RANGE1`, `AGE_RANGE2`, `AGE_RANGE3` |
| `chart` | string |  | Chart identifier such as 'topselling_free', 'topselling_paid', or 'topgrossing'. Excludes q and the pagination tokens.  |
| `see_more_token` | string |  | Open a result collection with its returned token and the same parameters.  |
| `movies_category` | string |  | Native category identifier, such as 'FAMILY'. Excludes q.  |
| `next_page_token` | string |  | Continue the listing with the returned next_page_token and the same parameters.  |
| `section_page_token` | string |  | Continue one result group with its returned token and the same parameters.  |

## Details

Returns Google Play movie listings grouped into storefront sections such as new releases, top selling, and rental offers. Each item has a title link, category, price, and content rating when available. No input is required: an empty request returns the default US English storefront, and `q`, `chart`, or `movies_category` narrow the listing.

### Use cases

- Track the price of new movie releases and rental offers in a given country storefront.
- Pull a top selling or top grossing chart to see which movies lead the Google Play ranking.
- Build a catalog of movie `product_id` values and genres to feed into a detail or review lookup.
- Compare the same storefront across `gl` and `hl` values to see how listings and prices differ by country.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-play/movies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `age` | string | No | Children's age range. Requires movies_category 'FAMILY'. |
| `chart` | string | No | Chart identifier such as 'topselling_free', 'topselling_paid', or 'topgrossing'. Excludes q and the pagination tokens. |
| `gl` | string | No | Two-letter country code. Default 'us'. |
| `hl` | string | No | Storefront language, such as 'en', 'de', or 'zh-TW'. Default 'en'. |
| `movies_category` | string | No | Native category identifier, such as 'FAMILY'. Excludes q. |
| `next_page_token` | string | No | Continue the listing with the returned next_page_token and the same parameters. |
| `q` | string | No | Search query, 1-2,048 bytes. Excludes category and chart; omit it to browse the storefront. |
| `section_page_token` | string | No | Continue one result group with its returned token and the same parameters. |
| `see_more_token` | string | No | Open a result collection with its returned token and the same parameters. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "charts": [
    {
      "chart": "topselling_paid",
      "title": "Top movies"
    }
  ],
  "litescrape_pagination": {
    "current": {
      "endpoint": "/google-play/movies",
      "queryParams": {
        "gl": "us",
        "hl": "en"
      }
    },
    "next": {
      "endpoint": "/google-play/movies",
      "queryParams": {
        "gl": "us",
        "hl": "en",
        "next_page_token": "eyJ2Ijox…"
      }
    },
    "next_page_token": "eyJ2Ijox…"
  },
  "organic_results": [
    {
      "items": [
        {
          "category": "Drama",
          "currency": "USD",
          "description": "JoJo thought she was done with her husband. Her husband disagreed. As she recall…",
          "extracted_price": 3.99,
          "link": "https://play.google.com/store/movies/details/The_Los_Angeles_Bakers?id=FT83s6l-6…",
          "price": "$3.99",
          "product_id": "FT83s6l-6kc.P",
          "thumbnail": "https://play-lh.googleusercontent.com/_pskGM9aVqpuruBqRWxVIcfFJ5NFIlCYPWdfL6Uck7…"
        }
      ],
      "litescrape_next_link": {
        "endpoint": "/google-play/movies",
        "queryParams": {
          "gl": "us",
          "hl": "en",
          "section_page_token": "eyJ2Ijox…"
        }
      },
      "litescrape_see_more_link": {
        "endpoint": "/google-play/movies",
        "queryParams": {
          "gl": "us",
          "hl": "en",
          "see_more_token": "eyJ2Ijox…"
        }
      },
      "section_page_token": "eyJ2Ijox…",
      "see_more_link": "https://play.google.com/store/movies/collection/cluster?clp=6gIkIiIKHHByb21vdGlv…",
      "see_more_token": "eyJ2Ijox…",
      "title": "New to buy or rent"
    }
  ],
  "search_metadata": {
    "created_at": "2026-11-03T07:34:30.835228+00:00",
    "google_play_url": "https://play.google.com/store/movies?hl=en&gl=us",
    "id": "f4d82ce88b796174f418da70",
    "processed_at": "2026-11-03T07:34:31.109938+00:00",
    "status": "Success",
    "total_time_taken": 0.275
  },
  "search_parameters": {
    "gl": "us",
    "hl": "en"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `organic_results[].title` | Name of a result section, such as `New to buy or rent` or `Top selling`. |
| `organic_results[].items[].product_id` | ID of the movie on Google Play. It also appears in the `id` query value of `link`. |
| `organic_results[].items[].link` | URL of the movie page on Google Play. |
| `organic_results[].items[].category` | Genre label of the movie, such as `Drama` or `Documentary`. |
| `organic_results[].items[].price / extracted_price / currency` | Price as display text (`$3.99`), the same price as a number (`3.99`), and the currency code. |
| `organic_results[].items[].content_rating` | Age rating such as `R` or `TV-PG`. Some items do not have it. |
| `organic_results[].items[].rating` | Numeric rating of the movie. Only some items include it. |
| `organic_results[].section_page_token / see_more_token` | Tokens to load more items in one section, or to open the full collection behind it. |
| `charts[].chart` | Chart identifier you can pass as the `chart` parameter, such as `topselling_paid`. |
| `litescrape_pagination.next_page_token` | Token to load the next page of the whole listing. |

### Notes

- To page through the whole listing, send `next_page_token` with the same `gl` and `hl` values.
- To page within one section, send its `section_page_token`. To open a full collection, send its `see_more_token`.
- Each section also returns ready-made `litescrape_next_link` and `litescrape_see_more_link` objects with the endpoint and query parameters for the follow-up call.
- Pass a `product_id` to [Google Play Product Details](/apis/google-play/product) to get more on a single title.

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/google-play/movies.json`](../../../catalog/models/google-play/movies.json) · Store page: https://www.sandbase.ai/model/google-play/movies
