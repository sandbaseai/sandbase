# Lemon8 User Following List

`lemon8/app/user-following-list` · api · Lemon8

Returns the list of accounts followed by a specified Lemon8 user. Accepts a user identifier and supports cursor-based pagination for browsing results.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/user-following-list", "user_id": "<user_id>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/user-following-list', {'user_id': '<user_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/user-following-list", {
  "user_id": "<user_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/user-following-list", sandbase.Params{
	"user_id": "<user_id>",
})
```

Same call via the path form: `POST /v1/api/lemon8/app/user-following-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the cursor returned by the last request is used for subsequent requests.  |
| `user_id` | string | yes | User ID, can be obtained from the interface `/lemon8/app/get_user_id`  |

## Details

Retrieve the list of followed accounts for a given Lemon8 user by supplying `user_id`. Use `cursor` to paginate through subsequent pages of results.

### Use cases

- Inspect who a specific Lemon8 profile is following.
- Map social connections and account networks across Lemon8.
- Paginate through large following lists for audience research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/user-following-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "<user_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID, can be obtained from the interface `/lemon8/app/get_user_id` |
| `cursor` | string | No | Pagination parameter, can be obtained from the return result of the last request. |

### Notes

- The `user_id` can be obtained from the `/lemon8/app/get_user_id` endpoint.
- Leave `cursor` empty for the initial request, then pass the returned cursor to fetch subsequent pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Lemon8 Discover Page Banners](/model/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/model/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/model/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.

---
Machine-readable: [`catalog/models/lemon8/app/user-following-list.json`](../../../../catalog/models/lemon8/app/user-following-list.json) · Store page: https://www.sandbase.ai/model/lemon8/app/user-following-list
