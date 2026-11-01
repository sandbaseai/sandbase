# TikTok Creator Video Analytics Summary

`tiktok/creator/video-analytics-summary` · api · TikTok

Returns a video performance overview for a TikTok Shop creator account over a time range. Provides metrics including video count, views, new followers, and generated GMV.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/video-analytics-summary"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/video-analytics-summary', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/video-analytics-summary", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/video-analytics-summary", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/creator/video-analytics-summary` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `proxy` |  |  | Optional HTTP proxy address, can be omitted if not used  |

## Details

Retrieve aggregated video analytics for a TikTok Shop creator account, with an optional `proxy` setting.

### Use cases

- Track video views and follower growth across creator campaigns.
- Monitor generated GMV driven by creator videos.
- Assess creator account performance over 30-day windows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/creator/video-analytics-summary" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `proxy` | string | No | Optional HTTP proxy address, can be omitted if not used |

### Notes

- An optional HTTP proxy address can be specified using `proxy`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Creator Account Health Status](/model/tiktok/creator/account-health-status): Returns the health status of a TikTok Shop creator account.
- [TikTok Creator Account Insights Overview](/model/tiktok/creator/account-insights-overview): Retrieves performance metrics for a TikTok Shop creator account, including revenue, exposure, clicks, and orders for the specified month.
- [TikTok Creator Account Violations](/model/tiktok/creator/account-violation-list): Returns the violation history and enforcement actions for a TikTok Shop creator account.

---
Machine-readable: [`catalog/models/tiktok/creator/video-analytics-summary.json`](../../../../catalog/models/tiktok/creator/video-analytics-summary.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/video-analytics-summary
