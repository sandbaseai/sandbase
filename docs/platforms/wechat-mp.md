# WeChat MP API: 18 endpoints with pricing and code examples

Call 18 WeChat MP endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`wechat-mp/account-basic-info`](../models/wechat-mp/account-basic-info.md) | Get basic profile information for a WeChat Official Account by account name. Use it to identify or enrich a known account before article,… | $0.142857 per call |
| [`wechat-mp/account-history-articles`](../models/wechat-mp/account-history-articles.md) | Get historical posts for a WeChat Official Account by username, with cursor pagination and article, video, audio, or image content tabs.… | $0.042857 per call |
| [`wechat-mp/article-comment`](../models/wechat-mp/article-comment.md) | Get top-level comments for a WeChat Official Account article by URL, with an optional buffer cursor for pagination. Use it to review… | $0.028571 per call |
| [`wechat-mp/article-detail`](../models/wechat-mp/article-detail.md) | Get a WeChat Official Account article by URL with selectable plain-text or rich-text content mode. Use it to collect a known article in… | $0.021429 per call |
| [`wechat-mp/article-metrics`](../models/wechat-mp/article-metrics.md) | Get basic interaction metrics for a WeChat Official Account article URL that ends with #rd or #wechat_redirect. Use it to perform a… | $0.021429 per call |
| [`wechat-mp/convert-article-link`](../models/wechat-mp/convert-article-link.md) | Expands a WeChat Official Account article link to its resolved long-form destination. Use it to normalize a short or intermediate link… | $0.014286 per call (free daily quota) |
| [`wechat-mp/search-suggestions`](../models/wechat-mp/search-suggestions.md) | Get WeChat search suggestions for a keyword, optionally scoped by a supported business type. Use it to expand or refine a query before a… | $0.114286 per call |
| [`wechat-mp/search-wechat-index`](../models/wechat-mp/search-wechat-index.md) | Query WeChat Index for a keyword. Use it to examine trend interest within WeChat before planning content, campaigns, or further article… | $0.114286 per call |
| [`wechat-mp/v2/account-articles`](../models/wechat-mp/v2/account-articles.md) | Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time,… | $0.01 per call (free daily quota) |
| [`wechat-mp/v2/account-profile`](../models/wechat-mp/v2/account-profile.md) | Retrieves the profile details of an official WeChat account, including name, avatar, signature, and verification entity type using its… | $0.01 per call (free daily quota) |
| [`wechat-mp/v2/article-ad`](../models/wechat-mp/v2/article-ad.md) | Returns embedded ad slot information for a specified WeChat MP article URL. Supports choosing between the full raw response or a flattened… | $0.01 per call (free daily quota) |
| [`wechat-mp/v2/article-comments`](../models/wechat-mp/v2/article-comments.md) | Get the comments on a WeChat official account article from its URL: comment text, likes, time and commenter region, with cursor pagination. | $0.01 per call (free daily quota) |
| [`wechat-mp/v2/article-detail`](../models/wechat-mp/v2/article-detail.md) | Get a WeChat official account (MP) article from its URL: title, author, account, publish time, cover, full text and HTML content, and… | $0.01 per call (free daily quota) |
| [`wechat-mp/v2/article-detail-h5`](../models/wechat-mp/v2/article-detail-h5.md) | Get WeChat MP Article Detail (H5, Recommended) on WeChat MP. Returns the platform data as structured JSON. | $0.01 per call |
| [`wechat-mp/v2/article-stats`](../models/wechat-mp/v2/article-stats.md) | Get the engagement metrics of a WeChat official account article from its URL: reads, likes, "wow" count, shares, favorites and comments. | $0.01 per call (free daily quota) |
| [`wechat-mp/v2/article-stats-h5`](../models/wechat-mp/v2/article-stats-h5.md) | Get WeChat MP Article Stats (H5) on WeChat MP. Returns the platform data as structured JSON. | $0.01 per call |
| [`wechat-mp/v2/comment-replies`](../models/wechat-mp/v2/comment-replies.md) | Returns second-level replies under a specific WeChat MP article comment using the article url and comment identifiers. Supports pagination… | $0.01 per call (free daily quota) |
| [`wechat-mp/v2/related-articles`](../models/wechat-mp/v2/related-articles.md) | Retrieves the list of related articles displayed at the bottom of a WeChat MP post using its link. Supports choosing between raw and… | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/account-basic-info", "name": "人民日报"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
