# Xiaohongshu PGY live blogger square API: pricing, parameters and code examples

`xiaohongshu/pgy/live-blogger-list` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

PGY live blogger square on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/live-blogger-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/live-blogger-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/live-blogger-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/live-blogger-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/live-blogger-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ecom` | object |  | E-commerce conversion filters  |
| `fans` | object |  | Fans purchasing power filters  |
| `live` | object |  | Live activity & performance filters  |
| `seed` | integer |  | Paging seed, echo back from previous page default `0` |
| `buyer` | object |  | Buyer group & persona filters  |
| `flags` | object |  | Platform recommendation flags  |
| `category` | object |  | Category filters  |
| `page_num` | integer |  | Page, 1-250 default `1` |
| `nick_name` | string |  | Search by nickname  |
| `page_size` | integer |  | Page size, 1-20 default `20` |

## Details

PGY live blogger square on Xiaohongshu. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/live-blogger-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"page_num": 1, "page_size": 20, "seed": 0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `buyer` | object | No | Buyer group & persona filters |
| `category` | object | No | Category filters |
| `ecom` | object | No | E-commerce conversion filters |
| `fans` | object | No | Fans purchasing power filters |
| `flags` | object | No | Platform recommendation flags |
| `live` | object | No | Live activity & performance filters |
| `nick_name` | string | No | Search by nickname |
| `page_num` | integer | No | Page, 1-250 |
| `page_size` | integer | No | Page size, 1-20 |
| `seed` | integer | No | Paging seed, echo back from previous page |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/live-blogger-list.json`](../../../../catalog/models/xiaohongshu/pgy/live-blogger-list.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/live-blogger-list
