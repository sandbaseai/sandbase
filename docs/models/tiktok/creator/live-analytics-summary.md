# TikTok Stream Analytics Summary API: pricing, parameters and code examples

`tiktok/creator/live-analytics-summary` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns streaming performance metrics for a TikTok Shop account over a monthly period. Accepts an optional `start_date` to review broadcast analytics for a calendar month.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/live-analytics-summary"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/live-analytics-summary', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/live-analytics-summary", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/live-analytics-summary", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/creator/live-analytics-summary` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `proxy` |  |  | Optional HTTP proxy address, can be omitted if not used  |
| `start_date` | string |  | Query start date in the format `MM-DD-YYYY`, e.g., `04-01-2025`  |

## Details

Retrieve performance analytics for TikTok Shop broadcasts by specifying `start_date` in `MM-DD-YYYY` format. You can also supply an optional `proxy` to route requests.

### Use cases

- Review monthly broadcast performance and audience metrics.
- Analyze TikTok Shop stream results across specific calendar months.
- Benchmark sales and engagement trends across consecutive streaming periods.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/creator/live-analytics-summary" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `proxy` | string | No | Optional HTTP proxy address, can be omitted if not used |
| `start_date` | string | No | Query start date in the format `MM-DD-YYYY`, e.g., `04-01-2025` |

### Notes

- Format `start_date` as `MM-DD-YYYY`, which defaults to covering the entire calendar month starting from that date.
- An optional HTTP proxy address can be passed via `proxy`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Creator Account Health Status](/model/tiktok/creator/account-health-status): Returns the health status of a TikTok Shop creator account.
- [TikTok Creator Account Insights Overview](/model/tiktok/creator/account-insights-overview): Retrieves performance metrics for a TikTok Shop creator account, including revenue, exposure, clicks, and orders for the specified month.
- [TikTok Creator Account Violations](/model/tiktok/creator/account-violation-list): Returns the violation history and enforcement actions for a TikTok Shop creator account.

---
Machine-readable: [`catalog/models/tiktok/creator/live-analytics-summary.json`](../../../../catalog/models/tiktok/creator/live-analytics-summary.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/live-analytics-summary
