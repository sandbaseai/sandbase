# Instagram Post Likers API: pricing, parameters and code examples

`instagram/post-likers` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0024 per call · **Modes:** sync

List the accounts that liked a public Instagram post, one page of likers per call, with each liker's handle, display name, verified flag and avatar.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0024**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/post-likers", "url": "https://www.instagram.com/reel/DWzrfE2kaY8/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/post-likers', {'url': 'https://www.instagram.com/reel/DWzrfE2kaY8/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/post-likers", {
  "url": "https://www.instagram.com/reel/DWzrfE2kaY8/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/post-likers", sandbase.Params{
	"url": "https://www.instagram.com/reel/DWzrfE2kaY8/",
})
```

Same call via the path form: `POST /v1/api/instagram/post-likers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Canonical URL of a public Instagram post or reel.  |

## Details

This API returns one page of accounts that liked a public Instagram post or reel, plus the total like count. It needs the canonical post or reel URL as input.

### Use cases

- Build a list of engaged accounts for a competitor's reel to study who responds to their content.
- Check which liked accounts are verified to spot notable people engaging with a post.
- Compare `totalLikes` across several posts to track how a post performs.
- Export liker handles and user IDs to match against an existing customer or follower list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/post-likers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/reel/DWzrfE2kaY8/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Canonical URL of a public Instagram post or reel. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "likers": [
      {
        "avatarUrl": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/878759530_18441459568194…",
        "displayName": "Rosana Zana",
        "private": true,
        "userId": "5900162333",
        "username": "rosanaos2",
        "verified": false
      }
    ],
    "totalLikes": 7832
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.totalLikes` | Total number of likes on the post. This can be larger than the number of likers returned in one page. |
| `data.likers[].username` | Instagram handle of the account that liked the post. |
| `data.likers[].displayName` | Display name shown on the liker's profile. |
| `data.likers[].userId` | Numeric Instagram user ID of the liker, returned as a string. |
| `data.likers[].verified` | Whether the liker's account carries the verified badge. |
| `data.likers[].private` | Whether the liker's account is private. |
| `data.likers[].avatarUrl` | Link to the liker's profile picture. |
| `found` | `true` when the post was found. A lookup that finds nothing returns `false`. |

### Notes

- Copy the `url` from the post or reel address in Instagram, for example `https://www.instagram.com/reel/DWzrfE2kaY8/`.
- The request takes only `url`. There is no pagination parameter, so each call returns a single page of likers.
- Use [Instagram Post Details](/apis/instagram/post-detail) to get details about the post itself, and [Instagram Post Comment List](/apis/instagram/post-comments) to read its comments.

### Pricing

Billed at the actual cost of each call, about $0.0024 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/post-likers.json`](../../../catalog/models/instagram/post-likers.json) · Store page: https://www.sandbase.ai/model/instagram/post-likers
