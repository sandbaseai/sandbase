# TikTok Creator Account Insights Overview

`tiktok/creator/account-insights-overview` · api · TikTok

Retrieves performance metrics for a TikTok Shop creator account, including revenue, exposure, clicks, and orders for the specified month.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/account-insights-overview"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/account-insights-overview', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/account-insights-overview", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/account-insights-overview", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/creator/account-insights-overview` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `proxy` |  |  | Optional HTTP proxy address. Leave empty if not needed.  |
| `start_date` | string |  | Query start date in 'MM-DD-YYYY' format, e.g. '04-01-2025'  |

## Details

Query aggregate performance insights for a TikTok Shop creator account using the optional `start_date` parameter.

### Use cases

- Review monthly revenue and order counts for a TikTok Shop creator.
- Track exposure and click metrics across creator accounts.
- Analyze monthly creator performance trends.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/creator/account-insights-overview" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `proxy` | string | No | Optional HTTP proxy address. |
| `start_date` | string | No | Query start date in 'MM-DD-YYYY' format, e.g. '04-01-2025' |

### Notes

- `start_date` accepts dates in 'MM-DD-YYYY' format and aggregates data across that entire month.
- Use `proxy` to direct requests through a custom HTTP proxy.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Creator Account Health Status](/model/tiktok/creator/account-health-status): Returns the health status of a TikTok Shop creator account.
- [TikTok Creator Account Violations](/model/tiktok/creator/account-violation-list): Returns the violation history and enforcement actions for a TikTok Shop creator account.
- [TikTok Creator Account Info](/model/tiktok/creator/creator-account-info): Returns basic profile details for a TikTok Shop creator account, including username, avatar URLs, account ID, region, partner bindings, and permissions.

---
Machine-readable: [`catalog/models/tiktok/creator/account-insights-overview.json`](../../../../catalog/models/tiktok/creator/account-insights-overview.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/account-insights-overview
