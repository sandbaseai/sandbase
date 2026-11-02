# Pipixia User Information API: pricing, parameters and code examples

`pipixia/app/user-info` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Retrieves public profile details for a Pipixia user, including avatar image URLs. Takes a user identifier obtained from a share link.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/user-info", "user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/user-info', {'user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/user-info", {
  "user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/user-info", sandbase.Params{
	"user_id": "example",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | AKA user id, can be obtained from the share link.  |

## Details

Look up public Pipixia account information using a designated `user_id`. This endpoint returns profile elements such as avatar media URLs.

### Use cases

- Display Pipixia user avatar assets in community dashboards.
- Verify Pipixia user accounts by identifier.
- Enrich third-party user profiles with Pipixia public details.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3602444694069495"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | AKA user id, can be obtained from the share link. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "user_info": {
      "avatar": {
        "url_list": [
          {
            "url": "https://p6-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/ba804bc702db4d568d93d2ef2a8f…"
          }
        ]
      }
    }
  }
}
```

### Notes

- The `user_id` parameter can be obtained directly from the user's Pipixia share link.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hashtag Details](/model/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/model/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/model/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/user-info.json`](../../../../catalog/models/pipixia/app/user-info.json) · Store page: https://www.sandbase.ai/model/pipixia/app/user-info
