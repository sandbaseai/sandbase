# TikTok Creator Showcase Product List

`tiktok/creator/showcase-product-list` · api · TikTok

Returns the list of products displayed in a TikTok Shop creator showcase. Supports pagination controls via offset and item count.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/showcase-product-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/showcase-product-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/showcase-product-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/showcase-product-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/creator/showcase-product-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number of products per page (default 20)  |
| `proxy` |  |  | Optional HTTP proxy address  |
| `offset` | integer |  | Pagination offset (default 0)  |

## Details

Retrieves products featured in a creator's TikTok Shop showcase using pagination parameters `count` and `offset`.

### Use cases

- Track items currently promoted in a creator showcase.
- Collect showcase catalog listings for ecommerce analytics.
- Audit products displayed across creator storefronts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/creator/showcase-product-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number of products per page (default 20) |
| `proxy` | string | No | Optional HTTP proxy address |
| `offset` | integer | No | Pagination offset (default 0) |

### Notes

- Use `count` to set the number of products per page (default 20).
- Use `offset` to handle result pagination (default 0).
- Supports an optional `proxy` HTTP address.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Creator Account Health Status](/model/tiktok/creator/account-health-status): Returns the health status of a TikTok Shop creator account.
- [TikTok Creator Account Insights Overview](/model/tiktok/creator/account-insights-overview): Retrieves performance metrics for a TikTok Shop creator account, including revenue, exposure, clicks, and orders for the specified month.
- [TikTok Creator Account Violations](/model/tiktok/creator/account-violation-list): Returns the violation history and enforcement actions for a TikTok Shop creator account.

---
Machine-readable: [`catalog/models/tiktok/creator/showcase-product-list.json`](../../../../catalog/models/tiktok/creator/showcase-product-list.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/showcase-product-list
