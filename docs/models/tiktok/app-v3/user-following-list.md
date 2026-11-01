# TikTok User Following List

`tiktok/app-v3/user-following-list` · api · TikTok

Returns a list of accounts followed by a target TikTok user. Query using either a numeric user ID or a sec_user_id with support for token and timestamp pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-following-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-following-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-following-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-following-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-following-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number, do not exceed 20, keep it fixed.  |
| `user_id` | string |  | User ID, this is a pure numeric version of the user ID (one of user_id and sec_user_id)  |
| `min_time` | integer |  | Minimum time for paging, use default value 0 for the first request, and use the min_time value returned by the last request for subsequent requests.  |
| `page_token` | string |  | Page token, use default value "" for the first request, and use the page_token value returned by the last request for subsequent requests.  |
| `sec_user_id` | string |  | User sec_user_id, this is a mixed letter and number version ID (one of user_id and sec_user_id)  |

## Details

Retrieve the list of accounts followed by a user using either `user_id` or `sec_user_id`. Manage pagination across requests using `page_token` and `min_time`.

### Use cases

- Inspect the accounts followed by a target profile.
- Map out user connections and social network graphs.
- Track an influencer's followed accounts over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-following-list" \
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

- Requires either `user_id` or `sec_user_id` to identify the target account.
- Supports pagination using `page_token` and `min_time` returned by the preceding response.
- The `count` parameter must not exceed 20.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-following-list.json`](../../../../catalog/models/tiktok/app-v3/user-following-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-following-list
