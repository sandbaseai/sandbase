# Douyin Xingtu Showcase Items

`douyin/xingtu-v3/author-author-show-items-v2` · api · Douyin

Get Douyin Creator Marketplace (Xingtu) showcase items for a creator, with content-channel, assignment, and flow filters. Use it to review a creator's marketplace showcase during commerce campaign planning.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/author-author-show-items-v2", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/author-author-show-items-v2', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/author-author-show-items-v2", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/author-author-show-items-v2", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/author-author-show-items-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `flowType` | string |  | Flow type filter. one of: `EXCLUDE`, `INCLUDE`; default `"EXCLUDE"` |
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |
| `onlyAssign` | boolean |  | Whether to only include assigned items. default `false` |

## Details

Get Douyin Creator Marketplace (Xingtu) showcase items for a creator, with content-channel, assignment, and flow filters. Use it to review a creator's marketplace showcase during commerce campaign planning.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/author-author-show-items-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `platform` | string | No | Platform type. |
| `onlyAssign` | boolean | No | Whether to only include assigned items. |
| `flowType` | string | No | Flow type filter. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/author-author-show-items-v2.json`](../../../../catalog/models/douyin/xingtu-v3/author-author-show-items-v2.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/author-author-show-items-v2
