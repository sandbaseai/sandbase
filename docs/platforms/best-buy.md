# Best Buy API: 3 endpoints with pricing and code examples

Call 3 Best Buy endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`best-buy/product`](../models/best-buy/product.md) | Fetch a BestBuy.com product by URL and get title, price, brand, model, UPC, rating, description, and images in one normalized response. | about $0.00085 per call |
| [`best-buy/reviews`](../models/best-buy/reviews.md) | Pull a page of 10 customer reviews for any BestBuy.com product by URL, newest first or by relevance, helpfulness, or rating: rating,… | about $0.00085 per call |
| [`best-buy/search`](../models/best-buy/search.md) | Search BestBuy.com by keyword with optional sort, price-range, and page filters and get title, price, rating, and brand for each product… | about $0.0009 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "best-buy/product", "url": "https://www.bestbuy.com/product/apple-airpods-5-true-wireless-active-noise-cancelling-earbuds-with-wireless-charging-case-white/JJGCQP634G/sku/6376564"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
