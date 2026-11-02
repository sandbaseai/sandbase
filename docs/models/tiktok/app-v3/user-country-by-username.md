# TikTok User Country by Username API: pricing, parameters and code examples

`tiktok/app-v3/user-country-by-username` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the registered country code, user IDs, and username modification timestamp for a specified TikTok profile using their username.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-country-by-username", "username": "tiktok"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-country-by-username', {'username': 'tiktok'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-country-by-username", {
  "username": "tiktok"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-country-by-username", sandbase.Params{
	"username": "tiktok",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-country-by-username` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Username, which can be obtained from the user's homepage link, for example: https://www.tiktok.com/@tiktok, the username is tiktok.  |

## Details

Look up account location details for a TikTok user based on their `username`. The response includes the user's registered country code and internal identifiers.

### Use cases

- Identify the country where a TikTok account is registered.
- Verify creator geographic details for regional marketing campaigns.
- Retrieve internal user identifiers alongside country information.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-country-by-username" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "tiktok"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Username, which can be obtained from the user's homepage link, for example: https://www.tiktok.com/@tiktok, the username is tiktok. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "country": "US",
  "sec_user_id": "<user>",
  "user_id": "<user>",
  "username": "<user>",
  "username_modify_time": 1791290369
}
```

### Notes

- The `username` parameter can be obtained directly from the profile URL, such as the handle following the @ symbol.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-country-by-username.json`](../../../../catalog/models/tiktok/app-v3/user-country-by-username.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-country-by-username
