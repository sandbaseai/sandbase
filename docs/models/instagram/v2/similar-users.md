# Instagram Similar Users (V2)

`instagram/v2/similar-users` · api · Instagram

Returns recommended similar accounts based on Instagram's recommendation algorithm. Accepts an Instagram username or numeric user ID.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/similar-users", "user_id": "18527", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/similar-users', {'user_id': '18527', 'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/similar-users", {
  "user_id": "18527",
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/similar-users", sandbase.Params{
	"user_id": "18527",
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/similar-users` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User ID (either username or user_id required)  |
| `username` | string |  | Username (either username or user_id required)  |

## Details

Use this endpoint to retrieve recommended accounts similar to a target profile using `username` or `user_id`.

### Use cases

- Discover comparable influencer accounts for brand partnerships.
- Explore related profiles within a specific niche or community.
- Automate competitor audience and account discovery.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/similar-users" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | No | User ID (either username or user_id required) |
| `username` | string | No | Username (either username or user_id required) |

### Notes

- Either `user_id` or `username` must be provided.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/similar-users.json`](../../../../catalog/models/instagram/v2/similar-users.json) · Store page: https://www.sandbase.ai/model/instagram/v2/similar-users
