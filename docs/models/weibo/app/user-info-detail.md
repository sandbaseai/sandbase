# Weibo User Profile Details (App)

`weibo/app/user-info-detail` · api · Weibo

Returns comprehensive profile information for a Weibo user, including verification status, account level, and tags based on the specified user ID.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-info-detail", "uid": "8431518763"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-info-detail', {'uid': '8431518763'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-info-detail", {
  "uid": "8431518763"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-info-detail", sandbase.Params{
	"uid": "8431518763",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-info-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |

## Details

Retrieves detailed Weibo user profile data by supplying a target `uid`. It delivers advanced account metadata beyond standard basic profiles.

### Use cases

- Retrieve verification status and badges for Weibo creator accounts.
- Inspect detailed user metadata, tags, and account levels.
- Enrich social intelligence and creator analysis dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-info-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "8431518763"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "items": [
    {
      "category": "group",
      "type": "grid",
      "header": {
        "category": "cell",
        "type": "avatarInfo"
      }
    }
  ]
}
```

### Notes

- Requires a valid Weibo user identifier in `uid`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo App AI Smart Search](/model/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/model/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/model/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/user-info-detail.json`](../../../../catalog/models/weibo/app/user-info-detail.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-info-detail
