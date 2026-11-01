# TikTok Video Associated Product List

`tiktok/creator/video-associated-product-list` · api · TikTok

Returns products tied to specified TikTok Shop videos along with promotional performance metrics. Filter results by video IDs and an optional query start date.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/video-associated-product-list", "item_ids": "<item_ids>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/video-associated-product-list', {'item_ids': '<item_ids>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/video-associated-product-list", {
  "item_ids": "<item_ids>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/video-associated-product-list", sandbase.Params{
	"item_ids": "<item_ids>",
})
```

Same call via the path form: `POST /v1/api/tiktok/creator/video-associated-product-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `proxy` |  |  | Optional HTTP Proxy Address  |
| `item_ids` | array | yes | Video ID List  |
| `start_date` | string |  | Query Start Date, e.g. '04-01-2025'  |

## Details

Retrieve TikTok Shop products linked to specific videos using `item_ids`. You can also filter promotional metrics from a specific time using `start_date`.

### Use cases

- Analyze promotional product performance across specific TikTok videos.
- Track which TikTok Shop items are linked to creator video content.
- Inspect product sales indicators starting from a specified date.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/creator/video-associated-product-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_ids": "<item_ids>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_ids` | array | Yes | Video ID List |
| `proxy` | string | No | Optional HTTP Proxy Address |
| `start_date` | string | No | Query Start Date, e.g. '04-01-2025' |

### Notes

- `item_ids` accepts an array of video IDs to look up.
- `start_date` specifies the query start date, formatted such as '04-01-2025'.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Creator Account Health Status](/model/tiktok/creator/account-health-status): Returns the health status of a TikTok Shop creator account.
- [TikTok Creator Account Insights Overview](/model/tiktok/creator/account-insights-overview): Retrieves performance metrics for a TikTok Shop creator account, including revenue, exposure, clicks, and orders for the specified month.
- [TikTok Creator Account Violations](/model/tiktok/creator/account-violation-list): Returns the violation history and enforcement actions for a TikTok Shop creator account.

---
Machine-readable: [`catalog/models/tiktok/creator/video-associated-product-list.json`](../../../../catalog/models/tiktok/creator/video-associated-product-list.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/video-associated-product-list
