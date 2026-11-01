# Bilibili User Published Videos

`bilibili/user-video-list` · api · Bilibili

Get videos published by a Bilibili user identified by UID, with an optional continuation parameter from a prior response. Use it to browse a creator's uploads or continue through their video list.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/user-video-list", "uid": "546195"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/user-video-list', {'uid': '546195'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/user-video-list", {
  "uid": "546195"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/user-video-list", sandbase.Params{
	"uid": "546195",
})
```

Same call via the path form: `POST /v1/api/bilibili/user-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Bilibili User ID (UID).  |
| `param` | string |  | Pagination parameter from previous response.  |

## Details

Get videos published by a Bilibili user identified by UID, with an optional continuation parameter from a prior response. Use it to browse a creator's uploads or continue through their video list.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/user-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "546195"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | Bilibili User ID (UID). |
| `param` | string | No | Pagination parameter from previous response. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/bilibili/user-video-list.json`](../../../catalog/models/bilibili/user-video-list.json) · Store page: https://www.sandbase.ai/model/bilibili/user-video-list
