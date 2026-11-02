# Xiaohongshu (RED) User Profile Information API: pricing, parameters and code examples

`xiaohongshu/web-v3/user-info` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** sync

Returns public profile details and interaction metrics for a specific Xiaohongshu account based on the provided user ID.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/web-v3/user-info", "user_id": "5e3a8ee700000000010070c6"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/web-v3/user-info', {'user_id': '5e3a8ee700000000010070c6'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/web-v3/user-info", {
  "user_id": "5e3a8ee700000000010070c6"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/web-v3/user-info", sandbase.Params{
	"user_id": "5e3a8ee700000000010070c6",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/web-v3/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User ID  |

## Details

Retrieve public profile details and interaction statistics for an account using `user_id`.

### Use cases

- Inspect Xiaohongshu user engagement and follower metrics.
- Display public creator statistics in external dashboards.
- Verify profile information for Xiaohongshu accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/web-v3/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "5e3a8ee700000000010070c6"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "interactions": [
      {
        "count": "10+",
        "i18n_count": "10+",
        "name": "关注",
        "type": "follows"
      }
    ]
  }
}
```

### Notes

- The `user_id` parameter specifies the target Xiaohongshu account identifier.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Homepage Feed](/model/xiaohongshu/web-v3/homefeed): Retrieves recommended notes from the Xiaohongshu homepage feed.
- [Xiaohongshu (RED) Homepage Categories](/model/xiaohongshu/web-v3/homefeed-categories): Returns a list of available homefeed category channels on Xiaohongshu (RED).
- [Xiaohongshu (RED) Web Note Details](/model/xiaohongshu/web-v3/note-detail): Returns detailed information for a specific Xiaohongshu note using its identifier and security token obtained from a web share link.

---
Machine-readable: [`catalog/models/xiaohongshu/web-v3/user-info.json`](../../../../catalog/models/xiaohongshu/web-v3/user-info.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/web-v3/user-info
