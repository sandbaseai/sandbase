# WeChat MP Article Comments API: pricing, parameters and code examples

`wechat-mp/article-comment` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.027778 per call · **Modes:** sync

Get top-level comments for a WeChat Official Account article by URL, with an optional buffer cursor for pagination. Use it to review reader discussion or continue through comment pages for a known article.

## Pricing

- **$0.027778 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/article-comment", "articleUrl": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/article-comment', {'articleUrl': 'http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/article-comment", {
  "articleUrl": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/article-comment", sandbase.Params{
	"articleUrl": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/article-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `buffer` | string |  | Comment pagination buffer returned by the previous response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.  |
| `articleUrl` | string | yes | WeChat Official Account article URL used to fetch top-level article comments.  |

## Details

Get top-level comments for a WeChat Official Account article by URL, with an optional buffer cursor for pagination. Use it to review reader discussion or continue through comment pages for a known article.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/article-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"articleUrl": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `articleUrl` | string | Yes | WeChat Official Account article URL used to fetch top-level article comments. |
| `buffer` | string | No | Comment pagination buffer returned by the previous response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/wechat-mp/article-comment.json`](../../../catalog/models/wechat-mp/article-comment.json) · Store page: https://www.sandbase.ai/model/wechat-mp/article-comment
