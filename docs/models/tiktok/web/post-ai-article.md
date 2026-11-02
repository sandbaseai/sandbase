# TikTok AI-generated article of a single video API: pricing, parameters and code examples

`tiktok/web/post-ai-article` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get AI-generated article of a single video on TikTok. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/post-ai-article", "itemId": "7651935877744168194"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/post-ai-article', {'itemId': '7651935877744168194'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/post-ai-article", {
  "itemId": "7651935877744168194"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/post-ai-article", sandbase.Params{
	"itemId": "7651935877744168194",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/post-ai-article` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | Video id  |

## Details

Get AI-generated article of a single video on TikTok. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/post-ai-article" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "7651935877744168194"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | Video id |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/tiktok/web/post-ai-article.json`](../../../../catalog/models/tiktok/web/post-ai-article.json) · Store page: https://www.sandbase.ai/model/tiktok/web/post-ai-article
