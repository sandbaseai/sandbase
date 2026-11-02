# WeChat MP Article Comments API: pricing, parameters and code examples

`wechat-mp/v2/article-comments` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** sync

Get the comments on a WeChat official account article from its URL: comment text, likes, time and commenter region, with cursor pagination.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/article-comments", "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/article-comments', {'url': 'https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/article-comments", {
  "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/article-comments", sandbase.Params{
	"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/article-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=full raw comment objects; False=simplified comment view. default `true` |
| `url` | string | yes | WeChat MP article URL (`https://mp.weixin.qq.com/s/…`). E.g. `https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw`  |
| `buffer` |  |  | Optional, default empty. Pagination cursor; leave empty for the first page, pass `buffer` from the previous response for the next page. default `""` |

## Details

Pass a WeChat MP article URL and get its featured comments, one page at a time.

### Use cases

- Analyze reader reactions to articles.
- Collect feedback on sponsored content.
- Monitor comments on competitor articles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/article-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw", "raw": false}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | WeChat MP article URL (`https://mp.weixin.qq.com/s/…`). |
| `raw` | boolean | No | Optional, default True. |
| `buffer` | string | No | Optional, default empty. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "has_more": true,
  "buffer": "<buffer>",
  "comments": [
    {
      "content_id": "6255846262940111556",
      "create_time": 1741148719,
      "like_num": 87,
      "content": "所谓的软件优化要是真能提升性能的话，老黄他敢卖只有一组128流处理器的游戏卡",
      "nick_name": "<user>",
      "ip_wording": "浙江"
    }
  ]
}
```

### Notes

- Paginate with `buffer`; `has_more` false means the last page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat MP Account Articles](/model/wechat-mp/v2/account-articles): Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time, including video and audi…
- [WeChat MP Article Detail](/model/wechat-mp/v2/article-detail): Get a WeChat official account (MP) article from its URL: title, author, account, publish time, cover, full text and HTML content, and album info.
- [WeChat MP Article Stats](/model/wechat-mp/v2/article-stats): Get the engagement metrics of a WeChat official account article from its URL: reads, likes, "wow" count, shares, favorites and comments.

---
Machine-readable: [`catalog/models/wechat-mp/v2/article-comments.json`](../../../../catalog/models/wechat-mp/v2/article-comments.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/article-comments
