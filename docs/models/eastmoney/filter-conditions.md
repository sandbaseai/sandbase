# Eastmoney Filter Conditions API: pricing, parameters and code examples

`eastmoney/filter-conditions` · data API · Eastmoney · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get the full hierarchical tree of filter conditions available for stock or fund screening. Returns all categories (范围, 基本面, 行情技术面, 消息面, 人气&涨停) with their children and parameter options.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "eastmoney/filter-conditions"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('eastmoney/filter-conditions', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("eastmoney/filter-conditions", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "eastmoney/filter-conditions", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/eastmoney/filter-conditions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string |  | Domain type for filtering. Accepted values: 'stock', 'fund'. default `"stock"` |

## Details

Get the full hierarchical tree of filter conditions available for stock or fund screening. Returns all categories (范围, 基本面, 行情技术面, 消息面, 人气&涨停) with their children and parameter options.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "eastmoney/filter-conditions", "domain": "stock"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | No | Domain type for filtering. Accepted values: 'stock', 'fund'. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/eastmoney/filter-conditions.json`](../../../catalog/models/eastmoney/filter-conditions.json) · Store page: https://www.sandbase.ai/model/eastmoney/filter-conditions
