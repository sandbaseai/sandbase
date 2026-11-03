# Instagram User Search (V3) API: pricing, parameters and code examples

`instagram/v3/search-users` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Searches for Instagram accounts matching a keyword query and returns user profiles including account IDs, full names, and usernames.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/search-users", "query": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/search-users', {'query': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/search-users", {
  "query": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/search-users", sandbase.Params{
	"query": "openai",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/search-users` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword  |
| `rank_token` | string |  | Rank token from previous search response for pagination  |

## Details

Searches Instagram accounts that match a keyword and returns a list of matching user summaries. Each entry has the account ID, username, full name, verification and privacy flags, and a profile picture URL. The only required input is `query`.

### Use cases

- Find the official Instagram account for a brand by searching its name and checking `is_verified`.
- Build a list of candidate accounts for a keyword to review for influencer or competitor research.
- Collect account IDs from a name search to pass to profile, posts or followers APIs.
- Filter out private accounts before you plan further lookups, using `is_private`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/search-users" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword |
| `rank_token` | string | No | Rank token from previous search response for pagination |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "3a2645473ed1f",
  "count": 30,
  "items": [
    {
      "full_name": "OpenAI",
      "id": "45374573700",
      "is_private": false,
      "is_verified": true,
      "pk": "45374573700",
      "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/788716177_18115256264517…",
      "username": "openai"
    }
  ],
  "rank_token": null,
  "users": [
    {
      "full_name": "OpenAI",
      "id": "45374573700",
      "is_private": false,
      "is_verified": true,
      "pk": "45374573700",
      "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/788716177_18115256264517…",
      "username": "openai"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[]` | Matching user accounts for the query. The `users` list holds the same entries. |
| `count` | Number of results returned in this response. |
| `items[].username` | The account handle, such as `openai`. |
| `items[].full_name` | The display name shown on the profile. |
| `items[].id / items[].pk` | The numeric account ID as a string. Both keys hold the same value in the sample. |
| `items[].is_verified` | `true` when the account carries a verified badge. |
| `items[].is_private` | `true` when the account is private. |
| `items[].profile_pic_url` | URL of a small profile picture for the account. |
| `rank_token` | Token for the next page of results. It is `null` in this response. |

### Notes

- Search by brand or person name, then match on `username` and `is_verified` to pick the right account.
- For pagination, pass the `rank_token` from a previous response as `rank_token` in the next request.
- Use the `id` value with [Instagram User Profile (V3)](/apis/instagram/v3/user-profile) or [Instagram User Posts (V3)](/apis/instagram/v3/user-posts) to get more detail on an account.
- To find accounts related to one you already have, try [Instagram Similar Users (V3)](/apis/instagram/v3/similar-users).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/search-users.json`](../../../../catalog/models/instagram/v3/search-users.json) · Store page: https://www.sandbase.ai/model/instagram/v3/search-users
