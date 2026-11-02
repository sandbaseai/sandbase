# Bilibili User homepage video data V2 API: pricing, parameters and code examples

`bilibili/web/user-post-videos-v2` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get user homepage video data V2 on Bilibili. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/user-post-videos-v2", "uid": "178360345"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/user-post-videos-v2', {'uid': '178360345'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/user-post-videos-v2", {
  "uid": "178360345"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/user-post-videos-v2", sandbase.Params{
	"uid": "178360345",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/user-post-videos-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pn` | integer |  | Page number, no cap default `1` |
| `ps` | integer |  | Page size, max 100 default `30` |
| `uid` | string | yes | Uid  |
| `keyword` | string |  | Keyword, empty returns all  |

## Details

Get user homepage video data V2 on Bilibili. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/user-post-videos-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "178360345", "pn": 1, "ps": 30}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes |  |
| `keyword` | string | No | Keyword, empty returns all |
| `pn` | integer | No | Page number, no cap |
| `ps` | integer | No | Page size, max 100 |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/bilibili/web/user-post-videos-v2.json`](../../../../catalog/models/bilibili/web/user-post-videos-v2.json) · Store page: https://www.sandbase.ai/model/bilibili/web/user-post-videos-v2
