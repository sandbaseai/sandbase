# TikTok User Profile Details API: pricing, parameters and code examples

`tiktok/app-v3/user-profile` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns profile information for a specified TikTok user. Lookups can be performed using a numeric user ID, username, or sec_user_id.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-profile", "unique_id": "srlechuza2.0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-profile', {'unique_id': 'srlechuza2.0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-profile", {
  "unique_id": "srlechuza2.0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-profile", sandbase.Params{
	"unique_id": "srlechuza2.0",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User uid, optional parameter, pure number, if used, please keep sec_user_id and unique_id empty. default `""` |
| `unique_id` | string |  | User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user information, unique_id is also the user's username, if used, please keep sec_user_id and user_id empty. default `""` |
| `sec_user_id` | string |  | User sec_user_id default `""` |

## Details

Retrieve detailed user profile data from TikTok by querying with `user_id`, `unique_id`, or `sec_user_id`.

### Use cases

- Look up public account metrics and profile details by username.
- Resolve numeric TikTok user identifiers to profile data.
- Inspect TikTok account information using a sec_user_id string.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | No | User uid, optional parameter, pure number, if used, please keep sec_user_id and unique_id empty. |
| `unique_id` | string | No | User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user information, unique_id is also the user's username, if used, please keep… |
| `sec_user_id` | string | No | User sec_user_id |

### Notes

- Pass only one identifier at a time; if using `user_id`, leave `sec_user_id` and `unique_id` empty.
- If `sec_user_id` is empty, use `unique_id` (the username) while keeping `user_id` empty.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-profile.json`](../../../../catalog/models/tiktok/app-v3/user-profile.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-profile
