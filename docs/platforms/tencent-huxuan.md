# Tencent Huxuan API: 3 endpoints with pricing and code examples

Call 3 Tencent Huxuan endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`tencent-huxuan/finder-publisher-rank-finder-content`](../models/tencent-huxuan/finder-publisher-rank-finder-content.md) | List QQ Huxuan hot Video Account content by month and creator category, with six descending sort metrics and page-number pagination. Use… | $0.042857 per call |
| [`tencent-huxuan/finder-publisher-search`](../models/tencent-huxuan/finder-publisher-search.md) | Search or browses QQ Huxuan Video Account creators by optional nickname keyword with page-number pagination. Use it to discover and… | $0.071429 per call |
| [`tencent-huxuan/mp-publisher-search`](../models/tencent-huxuan/mp-publisher-search.md) | Search or browses QQ Huxuan Official Account creators by optional nickname or account keyword with page-number pagination. Use it to… | $0.071429 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent-huxuan/finder-publisher-rank-finder-content"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
