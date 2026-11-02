# TikTok Post Details API: pricing, parameters and code examples

`tiktok/post-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get details for a TikTok post identified by its post ID. Use it to look up a known TikTok video before content review, reporting, or related engagement analysis.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/post-detail", "postId": "6701927684605233153"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/post-detail', {'postId': '6701927684605233153'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/post-detail", {
  "postId": "6701927684605233153"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/post-detail", sandbase.Params{
	"postId": "6701927684605233153",
})
```

Same call via the path form: `POST /v1/api/tiktok/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `postId` | string | yes | The unique ID of the TikTok post.  |

## Details

Get details for a TikTok post identified by its post ID. Use it to look up a known TikTok video before content review, reporting, or related engagement analysis.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"postId": "6701927684605233153"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `postId` | string | Yes | The unique ID of the TikTok post. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/tiktok/post-detail.json`](../../../catalog/models/tiktok/post-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/post-detail
