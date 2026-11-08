# TikTok Creator Showcase Product List API: pricing, parameters and code examples

`tiktok/creator/showcase-product-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call · **Modes:** sync

Returns the list of products displayed in a TikTok Shop creator showcase. Supports pagination controls via offset and item count.

## Pricing

- **$0.001 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/showcase-product-list", "cookie": "<cookie>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/showcase-product-list', {'cookie': '<cookie>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/showcase-product-list", {
  "cookie": "<cookie>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/showcase-product-list", sandbase.Params{
	"cookie": "<cookie>",
})
```

Same call via the path form: `POST /v1/api/tiktok/creator/showcase-product-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number of products per page (default 20)  |
| `proxy` |  |  | Optional HTTP proxy address  |
| `cookie` | string | yes | Cookie string of your own logged-in TikTok Shop creator account (from your browser session on the TikTok Shop / Seller Center site). Sent to the upstream for this request only and never stored by SandBase.  |
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
  -d '{"cookie": "<YOUR_TIKTOK_SHOP_COOKIE>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cookie` | string | Yes | Cookie string of your own logged-in TikTok Shop creator account. Used for this request only and never stored |
| `count` | integer | No | Number of products per page (default 20) |
| `proxy` | string | No | Optional HTTP proxy address |
| `offset` | integer | No | Pagination offset (default 0) |

### Notes

- Requires `cookie` from your own TikTok Shop creator account. The data returned belongs to that account; this API cannot look up other creators. SandBase forwards the cookie for this synchronous request only and does not store it in call history or logs, so async mode and retries are not supported.
- Use `count` to set the number of products per page (default 20).
- Use `offset` to handle result pagination (default 0).
- Supports an optional `proxy` HTTP address.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/tiktok/creator/showcase-product-list.json`](../../../../catalog/models/tiktok/creator/showcase-product-list.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/showcase-product-list
