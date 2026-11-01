# TikTok Shop Categories

`tiktok-shop/categories` · api · TikTok Shop

List the TikTok Shop category tree for a market: top-level categories with ids, slugs, and images, each with its child categories.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-shop/categories"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-shop/categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-shop/categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-shop/categories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok-shop/categories` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Country code of the TikTok Shop market whose category tree to list. Only US and VN publish a category tree. one of: `US`, `VN`; default `"US"` |

## Details

List the TikTok Shop category tree for a market: top-level categories with ids, slugs, and images, each with its child categories.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/categories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"region": "US"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `region` | string | No | Country code of the TikTok Shop market whose category tree to list. Only US and VN publish a category tree. One of: `US`, `VN`. Default `"US"`. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok-shop/categories.json`](../../../catalog/models/tiktok-shop/categories.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/categories
