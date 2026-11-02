# TikTok Video Audience Stats API: pricing, parameters and code examples

`tiktok/creator/video-audience-stats` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns audience profile statistics for a TikTok video by ID, covering gender, age, and regional breakdowns. Supports filtering starting from an optional date.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/video-audience-stats", "item_id": "7350810998023949599"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/video-audience-stats', {'item_id': '7350810998023949599'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/video-audience-stats", {
  "item_id": "7350810998023949599"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/video-audience-stats", sandbase.Params{
	"item_id": "7350810998023949599",
})
```

Same call via the path form: `POST /v1/api/tiktok/creator/video-audience-stats` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `proxy` |  |  | Optional HTTP Proxy Address  |
| `item_id` | string | yes | Video ID  |
| `start_date` | string |  | Query Start Date, e.g. '04-01-2025'  |

## Details

Provide a video ID via `item_id` to retrieve audience demographics such as gender, age, and location distribution. Use `start_date` to set the beginning of the reporting timeframe.

### Use cases

- Analyze audience demographics for specific TikTok videos.
- Evaluate viewer geographic distribution for marketing campaigns.
- Assess age and gender metrics to guide content strategy.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/creator/video-audience-stats" \
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

- Supply the target video ID in `item_id`.
- Filter the start of the query window using `start_date` with formats such as '04-01-2025'.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Creator Account Health Status](/model/tiktok/creator/account-health-status): Returns the health status of a TikTok Shop creator account.
- [TikTok Creator Account Insights Overview](/model/tiktok/creator/account-insights-overview): Retrieves performance metrics for a TikTok Shop creator account, including revenue, exposure, clicks, and orders for the specified month.
- [TikTok Creator Account Violations](/model/tiktok/creator/account-violation-list): Returns the violation history and enforcement actions for a TikTok Shop creator account.

---
Machine-readable: [`catalog/models/tiktok/creator/video-audience-stats.json`](../../../../catalog/models/tiktok/creator/video-audience-stats.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/video-audience-stats
