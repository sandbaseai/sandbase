# DataForSEO Merchant Amazon Products API: pricing, parameters and code examples

`dataforseo/v3/merchant/amazon/products/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0033 per call · **Modes:** sync

Returns real-time advanced product data from Amazon merchant search results. Provides item details, ratings, seller information, and ranking positions.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0033**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/merchant/amazon/products/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/merchant/amazon/products/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/merchant/amazon/products/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/merchant/amazon/products/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/merchant/amazon/products/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Live Amazon search results for a keyword: each product's ASIN, title, price, rating, units bought last month, Amazon's Choice and Best Seller badges, and position on the results page, for a chosen Amazon marketplace.

### Use cases

- Track where products rank on Amazon for target keywords.
- Monitor competitor prices and ratings.
- Find best sellers in a niche.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/merchant/amazon/products/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "wireless earbuds", "location_code": 2840, "language_code": "en_US"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query. |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "tasks": [
    {
      "result": [
        {
          "keyword": "wireless earbuds",
          "se_results_count": 26638,
          "items_count": 139,
          "items": [
            {
              "type": "amazon_serp",
              "rank_absolute": 1,
              "data_asin": "B0BQPNMXQV",
              "price_from": 29.95,
              "currency": "USD",
              "rating": {
                "position": "left",
                "rating_max": 5,
                "rating_type": "Max5",
                "type": "rating_element",
                "value": 4.2,
                "votes_count": 41300
              },
              "bought_past_month": 10000,
              "is_amazon_choice": true,
              "is_best_seller": false,
              "url": "https://www.amazon.com/JBL-Vibe-Beam-Wireless-Headphones/dp/B0BQPNMXQV/ref=sr_1_1?crid=12Q4KVH9BL80&dib=eyJ2IjoiMSJ9.6RIJ1bUNpVXhigrCEYtY6VU5l_48G2dMjXvdpglJ0g25KHl8RDSsU6UZbroPlTL3urcZjYU4Y06bVG2FCVtQBYj158NS93gfv-M59qKqW6bj_T74QJouqnskxMGEkFBflx_3TvfWN9aXVmuvMwyGeGk63293aje2la2yOBN0Vs4g_ZCJ4wC5PQWJjSGzKyvuf_bS42hH_JsvIg7bMedd0u3DIjaBv69jKwtRM5MNKBM.zAmu3IQsZ9nvWsvZlRtwx3SNHQv62Bfa8Cr7Zg6oXbI&dib_tag=se&keywords=wireless+earbuds&qid=1793677000&sprefix=wireless%2Bearbuds%2Caps%2C148&sr=8-1",
              "title": "JBL Vibe Beam - True Wireless Earbuds - Black"
            }
          ]
        }
      ]
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].data_asin` | Product ASIN. |
| `items[].title / url` | Listing title and URL. |
| `items[].price_from / currency` | Price shown on the results page. |
| `items[].rating` | Star rating and number of ratings. |
| `items[].bought_past_month` | Units bought in the past month as shown by Amazon. |
| `items[].is_amazon_choice / is_best_seller` | Badges. |
| `items[].rank_absolute` | Position on the results page. |
| `items[].type` | `amazon_serp` for organic, `amazon_paid` for sponsored. |

### Notes

- `location_code` picks the marketplace (2840 = amazon.com); `language_code` uses Amazon's form such as `en_US`.
- For one product's full page use [Amazon ASIN](/apis/dataforseo/v3/merchant/amazon/asin/live/advanced).

### Pricing

Billed at the actual cost of each call, about $0.0033 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/merchant/amazon/products/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/merchant/amazon/products/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/merchant/amazon/products/live/advanced
