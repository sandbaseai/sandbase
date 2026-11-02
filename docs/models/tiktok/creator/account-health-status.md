# TikTok Creator Account Health Status API: pricing, parameters and code examples

`tiktok/creator/account-health-status` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the health status of a TikTok Shop creator account. Provides the 90-day health score and accumulated violation points to evaluate account standing.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/account-health-status"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/account-health-status', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/account-health-status", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/account-health-status", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/creator/account-health-status` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `proxy` |  |  | Optional HTTP proxy address, can be omitted if not needed  |

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
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `proxy` | string | No | Optional HTTP proxy address, can be omitted if not needed |

### Notes

- The `proxy` parameter accepts an optional HTTP proxy address.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Creator Account Insights Overview](/model/tiktok/creator/account-insights-overview): Retrieves performance metrics for a TikTok Shop creator account, including revenue, exposure, clicks, and orders for the specified month.
- [TikTok Creator Account Violations](/model/tiktok/creator/account-violation-list): Returns the violation history and enforcement actions for a TikTok Shop creator account.
- [TikTok Creator Account Info](/model/tiktok/creator/creator-account-info): Returns basic profile details for a TikTok Shop creator account, including username, avatar URLs, account ID, region, partner bindings, and permissions.

---
Machine-readable: [`catalog/models/tiktok/creator/account-health-status.json`](../../../../catalog/models/tiktok/creator/account-health-status.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/account-health-status
