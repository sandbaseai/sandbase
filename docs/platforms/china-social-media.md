# China Social Media API: 1 endpoints with pricing and code examples

Call 1 China Social Media endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`cn-social/search`](../models/cn-social/search.md) | Search recent posts and articles across Chinese news sites, Weibo, WeChat, Zhihu, Douyin, Xiaohongshu, Bilibili and Kuaishou by keyword,… | $0.028571 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "cn-social/search"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
