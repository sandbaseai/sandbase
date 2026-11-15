# TikTok Ads Library API: 3 endpoints with pricing and code examples

Call 3 TikTok Ads Library endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`tiktok-ads-library/ad-details`](../models/tiktok-ads-library/ad-details.md) | Get detailed information about a specific ad including advertiser info, targeting (location, age, gender), and creative assets. | $0.03 per call |
| [`tiktok-ads-library/search-ads`](../models/tiktok-ads-library/search-ads.md) | Search the TikTok Ad Library for ads matching a query (advertiser name or keyword). | $0.06 per call |
| [`tiktok-ads-library/supported-regions`](../models/tiktok-ads-library/supported-regions.md) | Get the list of supported regions/countries available for filtering in the TikTok Ad Library. Returns European region codes and names that… | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-ads-library/ad-details", "ad_id": "1880398616261842"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
