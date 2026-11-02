# TikTok User Follower List API: pricing, parameters and code examples

`tiktok/app-v3/user-follower-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the follower list for a specified TikTok profile. Supports paging with timestamp and token parameters, requiring either a numeric user ID or secure user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-follower-list", "count": 20, "sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-follower-list', {'count': 20, 'sec_user_id': 'MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-follower-list", {
  "count": 20,
  "sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-follower-list", sandbase.Params{
	"count": 20,
	"sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-follower-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number, do not exceed 20, keep it fixed.  |
| `user_id` | string |  | User ID, this is a pure numeric version of the user ID (one of user_id and sec_user_id)  |
| `min_time` | integer |  | Minimum time for paging, use default value 0 for the first request, and use the min_time value returned by the last request for subsequent requests.  |
| `page_token` | string |  | Page token, use default value "" for the first request, and use the page_token value returned by the last request for subsequent requests.  |
| `sec_user_id` | string |  | User sec_user_id, this is a mixed letter and number version ID (one of user_id and sec_user_id)  |

## Details

Retrieve followers for a specific TikTok account by providing either `user_id` or `sec_user_id`.

### Use cases

- Inspect the follower community of a target TikTok creator.
- Page through account followers for audience research.
- Monitor network growth by retrieving recent follower profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-follower-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number, do not exceed 20, keep it fixed. |
| `user_id` | string | No | User ID, this is a pure numeric version of the user ID (one of user_id and sec_user_id) |
| `min_time` | integer | No | Minimum time for paging, use default value 0 for the first request, and use the min_time value returned by the last request for subsequent requests. |
| `page_token` | string | No | Page token, use default value "" for the first request, and use the page_token value returned by the last request for subsequent requests. |
| `sec_user_id` | string | No | User sec_user_id, this is a mixed letter and number version ID (one of user_id and sec_user_id) |

### Notes

- Requires one of `user_id` (numeric) or `sec_user_id` (alphanumeric).
- Set `count` up to 20 per request.
- Paginate using the `min_time` and `page_token` values returned from previous calls.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-follower-list.json`](../../../../catalog/models/tiktok/app-v3/user-follower-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-follower-list
