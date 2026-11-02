# Douyin Item Report Detail API: pricing, parameters and code examples

`douyin/xingtu-v2/item-report-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call · **Modes:** sync

Get Item Report Detail on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.002 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/item-report-detail", "item_id": "7372484719365098803"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/item-report-detail', {'item_id': '7372484719365098803'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/item-report-detail", {
  "item_id": "7372484719365098803"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/item-report-detail", sandbase.Params{
	"item_id": "7372484719365098803",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/item-report-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video (item) ID  |

## Details

Get Item Report Detail on Douyin. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/item-report-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7372484719365098803"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video (item) ID |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/item-report-detail.json`](../../../../catalog/models/douyin/xingtu-v2/item-report-detail.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/item-report-detail
