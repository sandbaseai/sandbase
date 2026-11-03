# Instagram Similar Users (V2) API: pricing, parameters and code examples

`instagram/v2/similar-users` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns recommended similar accounts based on Instagram's recommendation algorithm. Accepts an Instagram username or numeric user ID.

## Pricing

- **$0.002 per call** (USD)
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

Returns a list of Instagram accounts that Instagram recommends as similar to a given account. You pass either a `username` or a numeric `user_id`.

### Use cases

- Find comparable creators to shortlist for a brand partnership.
- Build a list of accounts in the same niche as a seed profile.
- Map related accounts around a competitor to see who shares its audience space.
- Expand a list of tracked accounts by adding the recommended ones.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/similar-users" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram", "user_id": "18527"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | No | User ID (either username or user_id required) |
| `username` | string | No | Username (either username or user_id required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "count": 78,
    "items": [
      {
        "full_name": "Sergei Kosenko",
        "id": "56499608746",
        "is_private": false,
        "is_verified": true,
        "profile_pic_url": "https://scontent-arn2-1.cdninstagram.com/v/t51.82787-19/541225038_18032030669880…",
        "username": "mr.thank.you"
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of similar accounts returned for the target account. |
| `data.items[].username` | Handle of the recommended account. Use it as the `username` input for other Instagram calls. |
| `data.items[].id` | Numeric ID of the recommended account, returned as a string. Use it as the `user_id` input. |
| `data.items[].full_name` | Display name shown on the recommended profile. |
| `data.items[].is_verified` | `true` if the recommended account has a verified badge. |
| `data.items[].is_private` | `true` if the recommended account is private. |
| `data.items[].profile_pic_url` | Link to a 320x320 profile picture of the recommended account. |

### Notes

- Send either `username` or `user_id`. The example uses `instagram` and `18527`, which belong to the same account.
- The response has no pagination parameters. All recommended accounts come back in `data.items`.
- The response gives only basic identity fields. Call [Instagram User Profile](/apis/instagram/v2/user-info) with a returned `username` for full profile details.
- Profile picture links in `profile_pic_url` are long signed URLs, so download or store the image soon after you fetch it.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/similar-users.json`](../../../../catalog/models/instagram/v2/similar-users.json) · Store page: https://www.sandbase.ai/model/instagram/v2/similar-users
