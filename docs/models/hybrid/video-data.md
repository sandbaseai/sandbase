# Universal Video Link Parser API: pricing, parameters and code examples

`hybrid/video-data` · data API · Hybrid · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Parse a shared video link from Douyin, TikTok and other supported platforms and get the video details, author and no-watermark media URLs.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hybrid/video-data", "url": "https://v.douyin.com/L4FJNR3/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hybrid/video-data', {'url': 'https://v.douyin.com/L4FJNR3/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hybrid/video-data", {
  "url": "https://v.douyin.com/L4FJNR3/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hybrid/video-data", sandbase.Params{
	"url": "https://v.douyin.com/L4FJNR3/",
})
```

Same call via the path form: `POST /v1/api/hybrid/video-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | url  |
| `minimal` | boolean |  | Whether to return minimal data default `false` |
| `base64_url` | boolean |  | Base64 encoding URL default `false` |

## Details

Parse a shared video link from Douyin, TikTok and other supported platforms and get the video details, author and no-watermark media URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/hybrid/video-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://v.douyin.com/L4FJNR3/", "minimal": false, "base64_url": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | url |
| `base64_url` | boolean | No | Base64 encoding URL |
| `minimal` | boolean | No | Whether to return minimal data |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/hybrid/video-data.json`](../../../catalog/models/hybrid/video-data.json) · Store page: https://www.sandbase.ai/model/hybrid/video-data
