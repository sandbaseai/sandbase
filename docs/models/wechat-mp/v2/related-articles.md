# WeChat MP Related Articles

`wechat-mp/v2/related-articles` · api · WeChat MP

Retrieves the list of related articles displayed at the bottom of a WeChat MP post using its link. Supports choosing between raw and simplified response formats.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/related-articles", "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/related-articles', {'url': 'https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/related-articles", {
  "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/related-articles", sandbase.Params{
	"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/related-articles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=full raw response; False=simplified projection. default `true` |
| `url` | string | yes | WeChat MP article URL (long or short form). E.g. `https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw` (this article has related articles disabled, returns empty)  |

## Details

Pass a WeChat MP article link via `url` to retrieve recommended related posts. Use `raw` to control whether the output contains the full raw data or a simplified projection.

### Use cases

- Discover recommended content linked to a target WeChat MP article.
- Collect related article links for automated content mapping.
- Analyze contextual recommendations across official WeChat accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/related-articles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | WeChat MP article URL (long or short form). |
| `raw` | boolean | No | Optional, default True. |

### Notes

- `url` accepts either long or short form WeChat MP article links.
- `raw` defaults to true for the full raw response, or false for a simplified projection.
- Articles with related recommendations disabled return an empty result.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat MP Account Articles](/model/wechat-mp/v2/account-articles): Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time, including video and audi…
- [WeChat MP Account Profile](/model/wechat-mp/v2/account-profile): Retrieves the profile details of an official WeChat account, including name, avatar, signature, and verification entity type using its official account ID.
- [WeChat MP Article Ads](/model/wechat-mp/v2/article-ad): Returns embedded ad slot information for a specified WeChat MP article URL.

---
Machine-readable: [`catalog/models/wechat-mp/v2/related-articles.json`](../../../../catalog/models/wechat-mp/v2/related-articles.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/related-articles
