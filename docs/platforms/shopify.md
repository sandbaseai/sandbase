# Shopify API: 4 endpoints with pricing and code examples

Call 4 Shopify endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`shopify/product`](../models/shopify/product.md) | Look up one product on any public Shopify store by its handle or product page URL and get title, vendor, type, tags, description, price… | about $0.00085 per call |
| [`shopify/products`](../models/shopify/products.md) | List the products of any public Shopify store by its domain, a page at a time, with title, vendor, type, tags, price range, sale price,… | about $0.00085 per call |
| [`shopify/search`](../models/shopify/search.md) | Search one public Shopify store's products by keyword with the store's own search and get its top matches with title, vendor, type, tags,… | about $0.00085 per call |
| [`shopify/store`](../models/shopify/store.md) | Look up any public Shopify store by its domain and get its name, description, currency, country and city, the countries it ships to, its… | about $0.00085 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shopify/product", "store": "allbirds.com", "product": "mens-strider"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
