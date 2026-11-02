# Xiaohongshu PGY blogger note cases v2 (cross-platform) API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-notes-v2` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get PGY blogger note cases v2 (cross-platform) on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-notes-v2", "user_id": "5c668b3e0000000012021605"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-notes-v2', {'user_id': '5c668b3e0000000012021605'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-notes-v2", {
  "user_id": "5c668b3e0000000012021605"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-notes-v2", sandbase.Params{
	"user_id": "5c668b3e0000000012021605",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-notes-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Blogger user ID  |
| `note_type` | integer |  | Note type one of: `0`, `1`, `2`; default `0` |
| `page_size` | integer |  | Page size, 1-8 (fixed at 8 on PGY web) default `8` |
| `order_type` | integer |  | Sort one of: `1`, `2`, `3`; default `1` |
| `page_number` | integer |  | Page number, from 1 default `1` |

## Details

Get PGY blogger note cases v2 (cross-platform) on Xiaohongshu. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-notes-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "5c668b3e0000000012021605", "page_number": 1, "page_size": 8, "note_type": 0, "order_type": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Blogger user ID |
| `note_type` | integer | No | Note type |
| `order_type` | integer | No | Sort |
| `page_number` | integer | No | Page number, from 1 |
| `page_size` | integer | No | Page size, 1-8 (fixed at 8 on PGY web) |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-notes-v2.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-notes-v2.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-notes-v2
