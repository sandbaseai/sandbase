# Weibo User Profile Information API: pricing, parameters and code examples

`weibo/app/user-info` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns basic profile information for a Weibo user, including nickname, avatar, biography, follower counts, and channel metadata, using a user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-info", "uid": "7648703289"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-info', {'uid': '7648703289'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-info", {
  "uid": "7648703289"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-info", sandbase.Params{
	"uid": "7648703289",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |

## Details

Retrieve Weibo user profile data and channel navigation details by providing a user ID via `uid`.

### Use cases

- Display Weibo creator profile details such as follower counts and biography.
- Extract channel configuration and tab parameters for a targeted user.
- Verify public Weibo user account metadata for analytics workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "7648703289"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "channelInfo": {
    "channels": [
      {
        "pageDataType": "flow",
        "title": "动态",
        "params": {
          "profileTabType": "profile",
          "profile_check_value": "timestamp:1791290328|profileUid:7648703289|token:29c4d9d1"
        },
        "theme": {
          "id": 18
        }
      }
    ]
  }
}
```

### Notes

- Requires `uid` representing the unique target Weibo user ID.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo App AI Smart Search](/model/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/model/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/model/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/user-info.json`](../../../../catalog/models/weibo/app/user-info.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-info
