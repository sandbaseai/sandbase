# 1688 Category Info

`1688/category/info` · api · 1688

Get a 1688 category and its child categories by category ID, or the root categories when no ID is given.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/category/info"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/category/info', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/category/info", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/category/info", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/1688/category/info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `catId` | string |  | 1688 platform category ID.  |

## Details

Get a 1688 category and its child categories by category ID, or the root categories when no ID is given.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/category/info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `catId` | string | No | 1688 platform category ID. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/1688/category/info.json`](../../../../catalog/models/1688/category/info.json) · Store page: https://www.sandbase.ai/model/1688/category/info
