# Douyin Xingtu Content Keyword Analysis API: pricing, parameters and code examples

`douyin/xingtu-v3/gauthor-author-content-hot-keywords` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.020833 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) content keyword analysis for a specified creator. Use it to identify recurring content themes during creator positioning research.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/gauthor-author-content-hot-keywords", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/gauthor-author-content-hot-keywords', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/gauthor-author-content-hot-keywords", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/gauthor-author-content-hot-keywords", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/gauthor-author-content-hot-keywords` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Get Douyin Creator Marketplace (Xingtu) content keyword analysis for a specified creator. Use it to identify recurring content themes during creator positioning research.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/gauthor-author-content-hot-keywords" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/gauthor-author-content-hot-keywords.json`](../../../../catalog/models/douyin/xingtu-v3/gauthor-author-content-hot-keywords.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/gauthor-author-content-hot-keywords
