# Pipixia User Follower List

`pipixia/app/user-follower-list` · api · Pipixia

Returns a list of followers for a specified Pipixia user account. Supports pagination through cursor tokens to navigate subsequent pages.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/user-follower-list", "user_id": "3602444694069495"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/user-follower-list', {'user_id': '3602444694069495'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/user-follower-list", {
  "user_id": "3602444694069495"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/user-follower-list", sandbase.Params{
	"user_id": "3602444694069495",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/user-follower-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page.  |
| `user_id` | string | yes | AKA user id, can be obtained from the share link.  |

## Details

Call this endpoint to retrieve follower profiles for a target account using `user_id`. Manage multi-page results using the `cursor` parameter.

### Use cases

- Review the audience and followers of a specific Pipixia creator.
- Track follower growth and inspect connected user accounts.
- Browse through paginated follower records for community analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/user-follower-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3602444694069495"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | AKA user id, can be obtained from the share link. |
| `cursor` | string | No | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "users": [
      {
        "id": 4322496105,
        "name": "皮皮侠65505942",
        "status": 0,
        "vote_count": 0
      }
    ]
  }
}
```

### Notes

- Obtain `user_id` from the account share link.
- Pagination defaults to 0 for `cursor`, which accepts the `loadmore_cursor` value from the previous page response.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hashtag Details](/model/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/model/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/model/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/user-follower-list.json`](../../../../catalog/models/pipixia/app/user-follower-list.json) · Store page: https://www.sandbase.ai/model/pipixia/app/user-follower-list
