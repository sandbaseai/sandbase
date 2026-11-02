# WeChat MP Article Detail (H5, Recommended) API: pricing, parameters and code examples

`wechat-mp/v2/article-detail-h5` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get WeChat MP Article Detail (H5, Recommended) on WeChat MP. Returns the platform data as structured JSON.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/article-detail-h5", "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/article-detail-h5', {'url': 'https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/article-detail-h5", {
  "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/article-detail-h5", sandbase.Params{
	"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/article-detail-h5` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | True=raw response; False=simplified parsed structure default `true` |
| `url` | string | yes | /mp.weixin.qq.com/s/WeChat MP article URL (https://mp.weixin.qq.com/s/… or long URL with __biz)  |

## Details

Get WeChat MP Article Detail (H5, Recommended) on WeChat MP. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/article-detail-h5" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw", "raw": true}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | /mp.weixin.qq.com/s/WeChat MP article URL (https://mp.weixin.qq.com/s/… or long URL with __biz) |
| `raw` | boolean | No | True=raw response; False=simplified parsed structure |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/wechat-mp/v2/article-detail-h5.json`](../../../../catalog/models/wechat-mp/v2/article-detail-h5.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/article-detail-h5
