# TikTok Creator Account Health Status API: pricing, parameters and code examples

`tiktok/creator/account-health-status` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call · **Modes:** sync

Returns the health status of a TikTok Shop creator account. Provides the 90-day health score and accumulated violation points to evaluate account standing.

## Pricing

- **$0.001 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/account-health-status", "cookie": "<cookie>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/account-health-status', {'cookie': '<cookie>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/account-health-status", {
  "cookie": "<cookie>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/account-health-status", sandbase.Params{
	"cookie": "<cookie>",
})
```

Same call via the path form: `POST /v1/api/tiktok/creator/account-health-status` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `proxy` |  |  | Optional HTTP proxy address, can be omitted if not needed  |
| `cookie` | string | yes | Cookie string of your own logged-in TikTok Shop creator account (from your browser session on the TikTok Shop / Seller Center site). Sent to the upstream for this request only and never stored by SandBase.  |

## Details

Access the health metrics and violation points for a TikTok Shop creator account. An optional `proxy` address can be configured for request routing.

### Use cases

- Monitor creator account standing over the past 90 days.
- Track accumulated violation points to avoid platform restrictions.
- Evaluate creator risk before initiating campaign collaborations.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/creator/account-health-status" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cookie": "<YOUR_TIKTOK_SHOP_COOKIE>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cookie` | string | Yes | Cookie string of your own logged-in TikTok Shop creator account. Used for this request only and never stored |
| `proxy` | string | No | Optional HTTP proxy address, can be omitted if not needed |

### Notes

- Requires `cookie` from your own TikTok Shop creator account. The data returned belongs to that account; this API cannot look up other creators. SandBase forwards the cookie for this synchronous request only and does not store it in call history or logs, so async mode and retries are not supported.
- The `proxy` parameter accepts an optional HTTP proxy address.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/tiktok/creator/account-health-status.json`](../../../../catalog/models/tiktok/creator/account-health-status.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/account-health-status
