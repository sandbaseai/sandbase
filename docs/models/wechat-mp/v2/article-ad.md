# WeChat MP Article Ads

`wechat-mp/v2/article-ad` · api · WeChat MP

Returns embedded ad slot information for a specified WeChat MP article URL. Supports choosing between the full raw response or a flattened ad list.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/article-ad", "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/article-ad', {'url': 'https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/article-ad", {
  "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/article-ad", sandbase.Params{
	"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/article-ad` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=full raw response; False=flattened ad list. default `true` |
| `url` | string | yes | WeChat MP article URL. E.g. `https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw` (this article has no ads, returns empty)  |

## Details

Look up embedded ad slot information from a WeChat MP post by providing `url`. Use `raw` to choose between a full payload or a flattened list.

### Use cases

- Inspect ad placements embedded inside a specific WeChat MP article.
- Extract ad slot details for commercial content analysis.
- Audit ad presence across WeChat MP posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/article-ad" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | WeChat MP article URL. |
| `raw` | boolean | No | Optional, default True. |

### Notes

- Set `raw` to `false` to receive a flattened ad list instead of the default full response.
- Requires a valid WeChat MP article URL passed in `url`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat MP Account Articles](/model/wechat-mp/v2/account-articles): Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time, including video and audi…
- [WeChat MP Account Profile](/model/wechat-mp/v2/account-profile): Retrieves the profile details of an official WeChat account, including name, avatar, signature, and verification entity type using its official account ID.
- [WeChat MP Article Comments](/model/wechat-mp/v2/article-comments): Get the comments on a WeChat official account article from its URL: comment text, likes, time and commenter region, with cursor pagination.

---
Machine-readable: [`catalog/models/wechat-mp/v2/article-ad.json`](../../../../catalog/models/wechat-mp/v2/article-ad.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/article-ad
