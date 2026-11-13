# Foreplay API: 4 endpoints with pricing and code examples

Call 4 Foreplay endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`foreplay/ad-search`](../models/foreplay/ad-search.md) | Search the Foreplay library of live and past social ads from Facebook, Instagram, TikTok, YouTube and more by keyword, format, platform,… | about $0.0525 per call |
| [`foreplay/brand-ads`](../models/foreplay/brand-ads.md) | List the social ads a brand has run by Foreplay brand ID, with creative, copy, platforms, run dates and landing page, filtered by format,… | about $0.0525 per call |
| [`foreplay/brand-analytics`](../models/foreplay/brand-analytics.md) | Get ad analytics for a brand by Foreplay brand ID: active and total ads, formats, platforms, launch cadence and longest-running creatives… | about $0.1225 per call |
| [`foreplay/brands-by-domain`](../models/foreplay/brands-by-domain.md) | Find the advertiser brands Foreplay tracks for a website domain, with brand ID, name, logo and ad counts, to use in brand ad lookups. | about $0.0175 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "foreplay/ad-search"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
