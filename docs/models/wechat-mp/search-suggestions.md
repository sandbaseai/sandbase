# WeChat MP Search Suggestions API: pricing, parameters and code examples

`wechat-mp/search-suggestions` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.111111 per call · **Modes:** sync

Get WeChat search suggestions for a keyword, optionally scoped by a supported business type. Use it to expand or refine a query before a targeted WeChat search.

## Pricing

- **$0.111111 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/search-suggestions", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/search-suggestions', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/search-suggestions", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/search-suggestions", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/search-suggestions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Keyword used to fetch WeChat search suggestions.  |
| `businessType` | string |  | WeChat search business type used to scope suggestion results. one of: `ALL`, `ACCOUNT`, `ARTICLE`, `CHANNEL`, `MOMENTS`, `LIVE`, `EMOJI`, `AUDIO`, `BOOK`, `WECHAT_INDEX`, `NEWS`, `MINI_PROGRAM` …; default `"ALL"` |

## Details

Get WeChat search suggestions for a keyword, optionally scoped by a supported business type. Use it to expand or refine a query before a targeted WeChat search.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/search-suggestions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword used to fetch WeChat search suggestions. |
| `businessType` | string | No | WeChat search business type used to scope suggestion results. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/wechat-mp/search-suggestions.json`](../../../catalog/models/wechat-mp/search-suggestions.json) · Store page: https://www.sandbase.ai/model/wechat-mp/search-suggestions
