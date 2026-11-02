# TikTok Shop User Showcase API: pricing, parameters and code examples

`tiktok-shop/user-showcase` · data API · TikTok Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List the TikTok Shop products a creator showcases (title, price, rating, and sales per product).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-shop/user-showcase", "handle": "mrtiktokreviews"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-shop/user-showcase', {'handle': 'mrtiktokreviews'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-shop/user-showcase", {
  "handle": "mrtiktokreviews"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-shop/user-showcase", sandbase.Params{
	"handle": "mrtiktokreviews",
})
```

Same call via the path form: `POST /v1/api/tiktok-shop/user-showcase` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination token for retrieving subsequent product pages.  |
| `handle` | string | yes | The handle of the TikTok user (e.g. mrtiktokreviews).  |
| `region` | string |  | Geographical region for proxy placement (defaults to US).  |

## Details

List the TikTok Shop products a creator showcases (title, price, rating, and sales per product).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/user-showcase" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "mrtiktokreviews"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | The handle of the TikTok user (e.g. mrtiktokreviews). |
| `cursor` | string | No | Pagination token for retrieving subsequent product pages. |
| `region` | string | No | Geographical region for proxy placement (defaults to US). |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok-shop/user-showcase.json`](../../../catalog/models/tiktok-shop/user-showcase.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/user-showcase
