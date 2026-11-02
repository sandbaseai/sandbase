# Douyin Xingtu Video Distribution API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-author-video-distribution` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) video-distribution data for a specified creator and content channel. Use it to analyze how the creator's videos are distributed during campaign research.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-video-distribution", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-video-distribution', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-video-distribution", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-video-distribution", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-video-distribution` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Get Douyin Creator Marketplace (Xingtu) video-distribution data for a specified creator and content channel. Use it to analyze how the creator's videos are distributed during campaign research.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-video-distribution" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `platform` | string | No | Platform type. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-video-distribution.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-video-distribution.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-video-distribution
