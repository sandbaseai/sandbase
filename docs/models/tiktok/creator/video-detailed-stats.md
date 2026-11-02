# TikTok Video Detailed Statistics API: pricing, parameters and code examples

`tiktok/creator/video-detailed-stats` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns segmented performance statistics for a TikTok video, including follower growth, completion rates, and engagement metrics.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/video-detailed-stats", "item_id": "7350810998023949599"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/video-detailed-stats', {'item_id': '7350810998023949599'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/video-detailed-stats", {
  "item_id": "7350810998023949599"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/video-detailed-stats", sandbase.Params{
	"item_id": "7350810998023949599",
})
```

Same call via the path form: `POST /v1/api/tiktok/creator/video-detailed-stats` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `proxy` |  |  | Optional HTTP Proxy Address  |
| `item_id` | string | yes | Video ID  |
| `start_date` | string |  | Query Start Date, e.g. '04-01-2025'  |

## Details

Retrieve detailed performance metrics for a specific TikTok video by providing its `item_id`. You can also filter the reporting period using `start_date`.

### Use cases

- Track daily or weekly engagement metrics for a single video.
- Analyze completion rates and follower growth over time.
- Measure audience response and product views from video content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/creator/video-detailed-stats" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7350810998023949599"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video ID |
| `proxy` | string | No | Optional HTTP Proxy Address |
| `start_date` | string | No | Query Start Date, e.g. '04-01-2025' |

### Notes

- Specify the target video using `item_id`.
- Provide `start_date` in month-day-year format (such as '04-01-2025') to set the query start date.
- An optional HTTP proxy can be configured using `proxy`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Creator Account Health Status](/model/tiktok/creator/account-health-status): Returns the health status of a TikTok Shop creator account.
- [TikTok Creator Account Insights Overview](/model/tiktok/creator/account-insights-overview): Retrieves performance metrics for a TikTok Shop creator account, including revenue, exposure, clicks, and orders for the specified month.
- [TikTok Creator Account Violations](/model/tiktok/creator/account-violation-list): Returns the violation history and enforcement actions for a TikTok Shop creator account.

---
Machine-readable: [`catalog/models/tiktok/creator/video-detailed-stats.json`](../../../../catalog/models/tiktok/creator/video-detailed-stats.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/video-detailed-stats
