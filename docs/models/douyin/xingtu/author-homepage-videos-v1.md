# Douyin Author Homepage Videos V1 API: pricing, parameters and code examples

`douyin/xingtu/author-homepage-videos-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Author Homepage Videos V1 on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/author-homepage-videos-v1", "oAuthorId": "7386881810501730341"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/author-homepage-videos-v1', {'oAuthorId': '7386881810501730341'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/author-homepage-videos-v1", {
  "oAuthorId": "7386881810501730341"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/author-homepage-videos-v1", sandbase.Params{
	"oAuthorId": "7386881810501730341",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/author-homepage-videos-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starts from 1, 20 items per page default `1` |
| `oAuthorId` | string | yes | Xingtu author ID  |
| `videoType` | string |  | PERSONAL/XINGTU / Traffic type: ALL/PERSONAL/XINGTU default `"ALL"` |
| `onlyAssign` | boolean |  | Only return assigned videos default `false` |

## Details

Get Author Homepage Videos V1 on Douyin. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/author-homepage-videos-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "7386881810501730341", "page": 1, "videoType": "ALL", "onlyAssign": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Xingtu author ID |
| `onlyAssign` | boolean | No | Only return assigned videos |
| `page` | integer | No | Page number, starts from 1, 20 items per page |
| `videoType` | string | No | PERSONAL/XINGTU / Traffic type: ALL/PERSONAL/XINGTU |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu/author-homepage-videos-v1.json`](../../../../catalog/models/douyin/xingtu/author-homepage-videos-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/author-homepage-videos-v1
