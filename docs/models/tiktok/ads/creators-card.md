# TikTok Creators card API: pricing, parameters and code examples

`tiktok/ads/creators-card` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get creators card on TikTok. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/creators-card"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/creators-card', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/creators-card", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/creators-card", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/ads/creators-card` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cookie` | string |  | Custom Cookie string (optional)  |
| `tt_uids` | array |  | Creator ID list  |
| `creator_type` | integer |  | Creator type default `2` |
| `need_loader_list` | array |  | Data module IDs, empty for all  |

## Details

Get creators card on TikTok. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/creators-card" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tt_uids": ["6532037588893564929"], "creator_type": 1, "need_loader_list": [101, 102, 103, 104, 105, 106, 107, 125]}'
```

The result is returned in `outputs[0].data`. `tt_uids` takes creator ids (`creatorID` from Top Contents List). `creator_type` 1 returns creator cards.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cookie` | string | No | Custom Cookie string (optional) |
| `creator_type` | integer | No | Creator type |
| `need_loader_list` | array | No | Data module IDs, empty for all |
| `tt_uids` | array | No | Creator ID list |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/tiktok/ads/creators-card.json`](../../../../catalog/models/tiktok/ads/creators-card.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/creators-card
