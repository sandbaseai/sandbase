# Xiaohongshu Hot Inspiration Feed API: pricing, parameters and code examples

`xiaohongshu/creator-hot-inspiration-feed` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.020833 per call · **Modes:** sync

Get the Xiaohongshu (RedNote) creator center hot inspiration feed with cursor pagination. Use it to discover inspiration for content planning and explore further pages of creative ideas.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/creator-hot-inspiration-feed"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/creator-hot-inspiration-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/creator-hot-inspiration-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/creator-hot-inspiration-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/creator-hot-inspiration-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Leave empty for the first request. For the next page, pass the cursor value returned by the previous response.  |

## Details

Get the Xiaohongshu (RedNote) creator center hot inspiration feed with cursor pagination. Use it to discover inspiration for content planning and explore further pages of creative ideas.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/creator-hot-inspiration-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Leave empty for the first request. For the next page, pass the cursor value returned by the previous response. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/creator-hot-inspiration-feed.json`](../../../catalog/models/xiaohongshu/creator-hot-inspiration-feed.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/creator-hot-inspiration-feed
