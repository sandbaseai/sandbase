# Threads User Info by ID API: pricing, parameters and code examples

`threads/web/user-info-by-id` · data API · Threads · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns detailed Threads user profile information based on a specified user ID. Ideal for retrieving public account metadata directly through web identifiers.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/user-info-by-id", "user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/user-info-by-id', {'user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/user-info-by-id", {
  "user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/user-info-by-id", sandbase.Params{
	"user_id": "example",
})
```

Same call via the path form: `POST /v1/api/threads/web/user-info-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User ID, for example: 67027868801, can be obtained from user profile API or post data  |

## Details

Returns the public Threads profile for one account. You send the numeric `user_id` and get the username, full name, follower count, verification flag, and profile picture URLs.

### Use cases

- Turn a `user_id` found in post data into a username and display name.
- Track the follower count of a public figure's Threads account over time.
- Check whether an account is verified or private before you pull its posts.
- Download profile pictures in more than one size for a profile card.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/user-info-by-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "67027868801"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID, for example: 67027868801, can be obtained from user profile API or post data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "user": {
    "account_badges": [],
    "account_warning": null,
    "bio_links": [],
    "biography": "",
    "eligible_for_text_app_activation_badge": false,
    "follower_count": 15705343,
    "friendship_status": null,
    "full_name": "Justin Bieber",
    "gating": null,
    "hd_profile_pic_versions": [
      {
        "height": 320,
        "url": "https://scontent-phx1-1.cdninstagram.com/v/t51.2885-19/573323465_121982546330221…",
        "width": 320
      }
    ],
    "hide_text_app_activation_badge_on_text_app": false,
    "id": "67027868801"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user.id / user.pk` | The numeric ID of the account, returned as a string. Both fields hold the same value in this response. |
| `user.username` | The account handle on Threads, for example `lilbieber`. |
| `user.full_name` | The display name shown on the profile. |
| `user.follower_count` | The number of followers the account has. |
| `user.is_verified` | `true` when the account carries a verified badge. |
| `user.text_post_app_is_private` | `true` when the Threads account is private. |
| `user.biography` | The profile bio text. It can be an empty string when the account has no bio. |
| `user.profile_pic_url` | URL of the profile picture. |
| `user.hd_profile_pic_versions[].url` | URL of a larger profile picture version. Each item also gives `width` and `height` in the same object. |
| `user.is_threads_only_user` | `true` when the account exists only on Threads. |

### Notes

- Get `user_id` from a post object or from the [Threads User Profile](/apis/threads/web/user-info) API.
- Pass `user_id` as a string of digits, for example `67027868801`.
- To list what the account has published, call [Threads User Posts](/apis/threads/web/user-posts) next.
- Some fields, such as `friendship_status` and `gating`, can be `null`, and `bio_links` can be an empty list.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Threads Post Detail](/apis/threads/web/post-detail): Returns detailed information for a specific Threads post using its numeric ID.
- [Threads Post Detail (V2)](/apis/threads/web/post-detail-v2): Returns detailed information for a specific Threads post.
- [Threads Profile Search](/apis/threads/web/search-profiles): Searches Threads user profiles based on a specified text query string.

---
Machine-readable: [`catalog/models/threads/web/user-info-by-id.json`](../../../../catalog/models/threads/web/user-info-by-id.json) · Store page: https://www.sandbase.ai/model/threads/web/user-info-by-id
