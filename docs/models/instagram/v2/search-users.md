# Instagram User Search (V2) API: pricing, parameters and code examples

`instagram/v2/search-users` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Searches for Instagram users matching a specified keyword. Returns a list of user accounts including user IDs, usernames, full names, and profile picture URLs.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/search-users", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/search-users', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/search-users", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/search-users", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/search-users` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword  |

## Details

Returns a list of Instagram accounts that match a search keyword. Each item has the account ID, username, full name, profile picture URL and a few status flags. The only input is `keyword`.

### Use cases

- Find the Instagram account of a brand or person from its name, such as `openai`.
- Collect account IDs and usernames to pass to other Instagram APIs.
- Check which matching accounts are verified before choosing one to track.
- Build an account picker that shows display names and profile pictures.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/search-users" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "count": 50,
    "items": [
      {
        "aigm_account_label_info": {
          "is_auto_detected": false,
          "is_enabled": false,
          "is_manually_enabled": false
        },
        "full_name": "OpenAI",
        "has_anonymous_profile_picture": false,
        "id": "45374573700",
        "is_private": false,
        "is_ring_creator": false,
        "is_verified": true,
        "latest_reel_media": 1793643587,
        "profile_pic_id": "3973928817672774008",
        "profile_pic_url": "https://scontent-bru2-1.cdninstagram.com/v/t51.82787-19/788716177_18115256264517…",
        "show_ring_award": false,
        "unseen_count": 0
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of users in the result. The sample response shows `50`. |
| `data.items[].id` | Instagram user ID as a string. Use it to identify the account in other calls. |
| `data.items[].username` | The account handle, without the `@`. |
| `data.items[].full_name` | Display name shown on the profile. |
| `data.items[].is_verified` | `true` when the account has a verified badge. |
| `data.items[].is_private` | `true` when the account is private. |
| `data.items[].profile_pic_url` | URL of a small profile picture. The URL carries query parameters. |
| `data.items[].profile_pic_id` | ID of the current profile picture. |
| `data.items[].latest_reel_media` | Number that looks like a Unix timestamp in seconds, for the latest story reel. It is `0` when the sample shows no value. |
| `data.items[].has_anonymous_profile_picture` | `true` when the account uses the default profile picture. |

### Notes

- Pass any name, brand or handle fragment in `keyword`. The request has no pagination parameter.
- `id` is a numeric string. Keep it as a string to avoid losing digits.
- To get full profile details for an account you found, call [Instagram User Profile](/apis/instagram/v2/user-info).
- To find accounts related to one you already have, call [Instagram Similar Users (V2)](/apis/instagram/v2/similar-users).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/search-users.json`](../../../../catalog/models/instagram/v2/search-users.json) · Store page: https://www.sandbase.ai/model/instagram/v2/search-users
