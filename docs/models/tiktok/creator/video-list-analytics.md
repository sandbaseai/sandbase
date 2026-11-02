# TikTok Creator Video List Analytics API: pricing, parameters and code examples

`tiktok/creator/video-list-analytics` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns video records and performance metrics for a TikTok Shop creator within a specific date range. Supports pagination and custom sorting rules.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/video-list-analytics"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/video-list-analytics', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/video-list-analytics", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/video-list-analytics", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/creator/video-list-analytics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default is the first page `0`  |
| `proxy` |  |  | Optional HTTP proxy address, can be omitted if not used  |
| `rules` | string |  | List sorting rule. Default VIDEO_LIST_PUBLISH_TIME (sorted by publish time)  |
| `start_date` | string |  | Query start date, formatted as 'MM-DD-YYYY', e.g., '04-01-2025'  |

## Details

Returns a paginated list of videos and performance metrics for a creator account starting from `start_date`. Configure sorting criteria using the `rules` parameter.

### Use cases

- Review creator video performance metrics across specific date ranges.
- Track content metrics over time using paginated query results.
- Sort creator video lists by posting time or other supported ordering rules.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/creator/video-list-analytics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number, default is the first page `0` |
| `proxy` | string | No | Optional HTTP proxy address, can be omitted if not used |
| `rules` | string | No | List sorting rule. |
| `start_date` | string | No | Query start date, formatted as 'MM-DD-YYYY', e.g., '04-01-2025' |

### Notes

- Set `page` to step through results, defaulting to `0`.
- Format `start_date` as 'MM-DD-YYYY'.
- Sort results using `rules`, which defaults to `VIDEO_LIST_PUBLISH_TIME`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Creator Account Health Status](/model/tiktok/creator/account-health-status): Returns the health status of a TikTok Shop creator account.
- [TikTok Creator Account Insights Overview](/model/tiktok/creator/account-insights-overview): Retrieves performance metrics for a TikTok Shop creator account, including revenue, exposure, clicks, and orders for the specified month.
- [TikTok Creator Account Violations](/model/tiktok/creator/account-violation-list): Returns the violation history and enforcement actions for a TikTok Shop creator account.

---
Machine-readable: [`catalog/models/tiktok/creator/video-list-analytics.json`](../../../../catalog/models/tiktok/creator/video-list-analytics.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/video-list-analytics
