# Hybrid API: 1 endpoints with pricing and code examples

Call 1 Hybrid endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`hybrid/video-data`](../models/hybrid/video-data.md) | Parse a shared video link from Douyin, TikTok and other supported platforms and get the video details, author and no-watermark media URLs. | $0.001 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hybrid/video-data", "url": "https://v.douyin.com/L4FJNR3/"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
