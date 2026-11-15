# Eastmoney Hot Conditions API: pricing, parameters and code examples

`eastmoney/hot-conditions` · data API · Eastmoney · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get curated hot screening conditions that are currently trending on EastMoney's stock screener. Each condition includes a title, full query question, stock count, change percentage, and tags. Supports pagination via last_ids.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "eastmoney/hot-conditions"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('eastmoney/hot-conditions', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("eastmoney/hot-conditions", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "eastmoney/hot-conditions", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/eastmoney/hot-conditions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `last_ids` | string |  | JSON array of last seen IDs for pagination (e.g. '[141,77,80]'). Omit for first page.  |
| `page_size` | integer |  | Number of hot conditions to return per page. default `4` |

## Details

Get curated hot screening conditions that are currently trending on EastMoney's stock screener. Each condition includes a title, full query question, stock count, change percentage, and tags. Supports pagination via last_ids.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "eastmoney/hot-conditions", "last_ids": "", "page_size": 4}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `last_ids` | string | No | JSON array of last seen IDs for pagination (e.g. '[141,77,80]'). Omit for first page. |
| `page_size` | integer | No | Number of hot conditions to return per page. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/eastmoney/hot-conditions.json`](../../../catalog/models/eastmoney/hot-conditions.json) · Store page: https://www.sandbase.ai/model/eastmoney/hot-conditions
