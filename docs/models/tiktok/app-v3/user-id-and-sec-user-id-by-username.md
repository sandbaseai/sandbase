# TikTok User ID by Username API: pricing, parameters and code examples

`tiktok/app-v3/user-id-and-sec-user-id-by-username` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the user_id and sec_user_id associated with a specific TikTok username. Provide a profile username to resolve account identifiers.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-id-and-sec-user-id-by-username", "username": "tiktok"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-id-and-sec-user-id-by-username', {'username': 'tiktok'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-id-and-sec-user-id-by-username", {
  "username": "tiktok"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-id-and-sec-user-id-by-username", sandbase.Params{
	"username": "tiktok",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-id-and-sec-user-id-by-username` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Username  |

## Details

Look up account identifiers for a TikTok profile using the `username` parameter. This endpoint returns both `user_id` and `sec_user_id` values.

### Use cases

- Resolve TikTok account identifiers from a public username.
- Retrieve required security IDs for downstream profile calls.
- Map user handles to unique IDs for analytics tracking.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-id-and-sec-user-id-by-username" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "tiktok"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Username |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "sec_user_id": "<user>",
  "user_id": "<user>"
}
```

### Notes

- Requires a valid account handle passed to `username`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-id-and-sec-user-id-by-username.json`](../../../../catalog/models/tiktok/app-v3/user-id-and-sec-user-id-by-username.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-id-and-sec-user-id-by-username
