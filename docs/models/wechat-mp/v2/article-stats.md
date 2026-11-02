# WeChat MP Article Stats API: pricing, parameters and code examples

`wechat-mp/v2/article-stats` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** sync

Get the engagement metrics of a WeChat official account article from its URL: reads, likes, "wow" count, shares, favorites and comments.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/article-stats", "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/article-stats', {'url': 'https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/article-stats", {
  "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/article-stats", sandbase.Params{
	"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/article-stats` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=full raw stats object (with `show_*` visibility flags); False=simplified counts only. default `true` |
| `url` | string | yes | WeChat MP article URL (`https://mp.weixin.qq.com/s/…`). E.g. `https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw`  |

## Details

Pass a WeChat MP article URL and get its interaction counts: reads, likes, wows, shares, favorites and comments.

### Use cases

- Measure the performance of articles you publish or sponsor.
- Benchmark competitor content.
- Track how an article spreads over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/article-stats" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw", "raw": false}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | WeChat MP article URL (`https://mp.weixin.qq.com/s/…`). |
| `raw` | boolean | No | Optional, default True. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "collect_count": 34,
  "comment_count": 28,
  "like_count": 22,
  "old_like_count": 111,
  "read_num": 28522,
  "share_count": 978,
  "star_num": 0
}
```

### Notes

- Set `raw` to `false` for simplified counts.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat MP Account Articles](/model/wechat-mp/v2/account-articles): Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time, including video and audi…
- [WeChat MP Article Comments](/model/wechat-mp/v2/article-comments): Get the comments on a WeChat official account article from its URL: comment text, likes, time and commenter region, with cursor pagination.
- [WeChat MP Article Detail](/model/wechat-mp/v2/article-detail): Get a WeChat official account (MP) article from its URL: title, author, account, publish time, cover, full text and HTML content, and album info.

---
Machine-readable: [`catalog/models/wechat-mp/v2/article-stats.json`](../../../../catalog/models/wechat-mp/v2/article-stats.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/article-stats
