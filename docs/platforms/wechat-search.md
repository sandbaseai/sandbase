# WeChat Search API: 5 endpoints with pricing and code examples

Call 5 WeChat Search endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`wechat-search/search-account`](../models/wechat-search/search-account.md) | Search WeChat Official Accounts by keyword with page-number pagination and one result per page. Use it to find an account by name or… | $0.057143 per call |
| [`wechat-search/search-article`](../models/wechat-search/search-article.md) | Search WeChat Official Account articles by keyword with publish-time and sort filters plus page, offset, and continuation-state pagination. | $0.114286 per call |
| [`wechat-search/search-miniprogram`](../models/wechat-search/search-miniprogram.md) | Search WeChat Mini Programs by keyword with page, offset, and continuation-state pagination. Use it to discover mini programs related to a… | $0.114286 per call |
| [`wechat-search/v2/search`](../models/wechat-search/v2/search.md) | Search WeChat with one endpoint: official account articles, accounts, Channels videos, live streams, news and more. Filter by vertical,… | $0.01 per call (free daily quota) |
| [`wechat-search/v2/search-videos`](../models/wechat-search/v2/search-videos.md) | Search WeChat Channels videos by keyword with duration, sort (relevance, newest, most liked) and publish-time filters. Returns titles,… | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-search/search-account", "keyword": "人工智能"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
