# WeChat MP WeChat Index Search API: pricing, parameters and code examples

`wechat-mp/search-wechat-index` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.114286 per call · **Modes:** sync

Query WeChat Index for a keyword. Use it to examine trend interest within WeChat before planning content, campaigns, or further article research.

## Pricing

- **$0.114286 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/search-wechat-index", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/search-wechat-index', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/search-wechat-index", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/search-wechat-index", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/search-wechat-index` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Keyword used to query WeChat Index trend signals.  |

## Details

Query WeChat Index for a keyword. Use it to examine trend interest within WeChat before planning content, campaigns, or further article research.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/search-wechat-index" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword used to query WeChat Index trend signals. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/wechat-mp/search-wechat-index.json`](../../../catalog/models/wechat-mp/search-wechat-index.json) · Store page: https://www.sandbase.ai/model/wechat-mp/search-wechat-index
