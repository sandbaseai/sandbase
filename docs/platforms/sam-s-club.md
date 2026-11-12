# Sam's Club API: 2 endpoints with pricing and code examples

Call 2 Sam's Club endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`sams-club/product`](../models/sams-club/product.md) | Fetch a SamsClub.com product by URL and get title, member price, stock, brand, model, UPC, rating, description, and images in one… | about $0.00319 per call |
| [`sams-club/search`](../models/sams-club/search.md) | Search SamsClub.com by keyword with optional sort, price-range, and page filters and get title, member price, stock, and rating for each… | about $0.00319 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sams-club/product", "url": "https://www.samsclub.com/ip/Bounty-Select-A-Size-2-Ply-Paper-Towels-12-Rolls-110-sheets-roll/18040450426"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
