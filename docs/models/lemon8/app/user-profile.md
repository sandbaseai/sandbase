# Lemon8 User Profile Details API: pricing, parameters and code examples

`lemon8/app/user-profile` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns profile information for a specified Lemon8 user. The query requires a unique user identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/user-profile", "user_id": "7217844966059656197"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/user-profile', {'user_id': '7217844966059656197'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/user-profile", {
  "user_id": "7217844966059656197"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/user-profile", sandbase.Params{
	"user_id": "7217844966059656197",
})
```

Same call via the path form: `POST /v1/api/lemon8/app/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User ID, can be obtained from the interface `/lemon8/app/get_user_id`  |

## Details

Access profile details for a specific Lemon8 account using the `user_id` parameter.

### Use cases

- Inspect profile details of a Lemon8 user account.
- Display account information within social analytics dashboards.
- Verify user details retrieved from identity lookup endpoints.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "7217844966059656197"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID, can be obtained from the interface `/lemon8/app/get_user_id` |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "server_time": "1791290353.18"
}
```

### Notes

- The `user_id` value can be obtained from the `/lemon8/app/get_user_id` endpoint.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Lemon8 Discover Page Banners](/model/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/model/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/model/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.

---
Machine-readable: [`catalog/models/lemon8/app/user-profile.json`](../../../../catalog/models/lemon8/app/user-profile.json) · Store page: https://www.sandbase.ai/model/lemon8/app/user-profile
