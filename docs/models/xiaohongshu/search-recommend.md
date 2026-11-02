# Xiaohongshu Keyword Suggestions API: pricing, parameters and code examples

`xiaohongshu/search-recommend` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.020833 per call · **Modes:** sync

Get Xiaohongshu (RedNote) search keyword suggestions for a submitted seed term. Use it to expand query sets, refine content-research searches, and plan SEO or programmatic SEO keyword coverage.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/search-recommend", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/search-recommend', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/search-recommend", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/search-recommend", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/search-recommend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword.  |

## Details

Get Xiaohongshu (RedNote) search keyword suggestions for a submitted seed term. Use it to expand query sets, refine content-research searches, and plan SEO or programmatic SEO keyword coverage.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/search-recommend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "美食"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/search-recommend.json`](../../../catalog/models/xiaohongshu/search-recommend.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/search-recommend
