# Weibo Post Detail (App) API: pricing, parameters and code examples

`weibo/app/status-detail` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed post information from the Weibo app based on a specified post identifier. Use this endpoint to inspect post metadata and actions.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/status-detail", "status_id": "5016922058656962"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/status-detail', {'status_id': '5016922058656962'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/status-detail", {
  "status_id": "5016922058656962"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/status-detail", sandbase.Params{
	"status_id": "5016922058656962",
})
```

Same call via the path form: `POST /v1/api/weibo/app/status-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `status_id` | string | yes | Post ID (required)  |

## Details

Retrieve detailed status information from the Weibo mobile application using a specific `status_id`.

### Use cases

- Inspect detailed metadata for an individual Weibo status.
- Access custom action configurations linked to a specific post.
- Track specific Weibo posts by their unique identifier.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/status-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"status_id": "5016922058656962"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `status_id` | string | Yes | Post ID (required) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "detailInfo": {
    "extend": {
      "custom_action_list": [
        {
          "type": "mblog_menus_comment_manager"
        }
      ]
    }
  }
}
```

### Notes

- Requires a valid `status_id` representing the target post identifier.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo App AI Smart Search](/model/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/model/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/model/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/status-detail.json`](../../../../catalog/models/weibo/app/status-detail.json) · Store page: https://www.sandbase.ai/model/weibo/app/status-detail
