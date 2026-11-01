# TikTok Shop Creator

`tiktok-shop/creator` · api · TikTok Shop

TikTok Shop creator performance by handle: GMV range, promoted product count, brand collaborations, follower age/gender/location demographics, category GMV split, and video versus live engagement.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0055**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-shop/creator", "handle": "golinutrition"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-shop/creator', {'handle': 'golinutrition'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-shop/creator", {
  "handle": "golinutrition"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-shop/creator", sandbase.Params{
	"handle": "golinutrition",
})
```

Same call via the path form: `POST /v1/api/tiktok-shop/creator` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | TikTok handle of the creator or shop account, without the @ (e.g. golinutrition).  |
| `region` | string |  | Country code of the TikTok Shop market. Only the US market is served; creators in other markets are not available. one of: `us`, `US`; default `"us"` |

## Details

TikTok Shop creator performance by handle: GMV range, promoted product count, brand collaborations, follower age/gender/location demographics, category GMV split, and video versus live engagement.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/creator" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "golinutrition"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | TikTok handle of the creator or shop account, without the @ (e.g. golinutrition). |
| `region` | string | No | Country code of the TikTok Shop market. Only the US market is served; creators in other markets are not available. One of: `us`, `US`. Default `"us"`. |

### Pricing

Billed at the actual cost of each call, usually $0.0055 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok-shop/creator.json`](../../../catalog/models/tiktok-shop/creator.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/creator
