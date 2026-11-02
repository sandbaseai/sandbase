# WeChat MP Article Detail API: pricing, parameters and code examples

`wechat-mp/v2/article-detail` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** sync

Get a WeChat official account (MP) article from its URL: title, author, account, publish time, cover, full text and HTML content, and album info.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/article-detail", "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/article-detail', {'url': 'https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/article-detail", {
  "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/article-detail", sandbase.Params{
	"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/article-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified projection.  |
| `url` | string | yes | WeChat MP article URL (`https://mp.weixin.qq.com/s/…` or long URL with `__biz`). E.g. `https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw`  |

## Details

Pass a WeChat MP article URL (`https://mp.weixin.qq.com/s/…`) and get the article as structured JSON, including the full text, title, account name and publish time.

### Use cases

- Archive or index WeChat articles for search and RAG.
- Monitor coverage published by official accounts.
- Extract clean text for summarization.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/article-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw", "raw": false}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | WeChat MP article URL (`https://mp.weixin.qq.com/s/…` or long URL with `__biz`). |
| `raw` | boolean | No | Optional, default True. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw",
  "content": {
    "title": "“老黄骗人”！5070首批评测：说好1/3价格赛4090，实际不如4070Ti",
    "nick_name": "量子位",
    "alias": "QbitAI",
    "create_time": "2025-03-05 12:22",
    "desc": "博主：史上最差70系列",
    "lang": "zh_CN",
    "content_text": "金磊 发自 凹非寺 量子位 | 公众号 QbitAI 一夜之间，RTX 5070被网友们喷成“史上最差的70系列”了。 这咋回事呢？ 因为…",
    "cdn_url": "https://mmbiz.qpic.cn/mmbiz_jpg/YicUhk5aAGtB8zqMsOsFEsStNXL…",
    "appmsgalbuminfo": "{…}"
  }
}
```

### Notes

- Both short links (`/s/…`) and long links with `__biz` are supported.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat MP Account Articles](/model/wechat-mp/v2/account-articles): Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time, including video and audi…
- [Get WeChat MP Account Profile](/model/wechat-mp/v2/account-profile): Pass a `gh_username` to get the official account profile: name / avatar / description / verification entity type, etc..
- [Get WeChat MP Article Ads](/model/wechat-mp/v2/article-ad): Pass an article URL to get the embedded ad slot info of the article..

---
Machine-readable: [`catalog/models/wechat-mp/v2/article-detail.json`](../../../../catalog/models/wechat-mp/v2/article-detail.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/article-detail
