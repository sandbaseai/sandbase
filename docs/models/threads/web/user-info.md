# Threads User Profile API: pricing, parameters and code examples

`threads/web/user-info` · data API · Threads · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Get a Threads (Meta) user profile by username: name, bio, follower count and verification status.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/user-info", "username": "nasa"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/user-info', {'username': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/user-info", {
  "username": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/user-info", sandbase.Params{
	"username": "nasa",
})
```

Same call via the path form: `POST /v1/api/threads/web/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Username, for example: lilbieber, can be obtained from the user's homepage link, for example: lilbieber in https://www.threads.net/@lilbieber  |

## Details

Returns the public Threads profile for one username. It includes the display name, biography, follower count, verification flag, profile pictures and profile tags. The only input is the `username`.

### Use cases

- Track the `follower_count` of a brand or creator account on Threads over time.
- Check `is_verified` and `text_post_app_is_private` before adding an account to an outreach list.
- Turn a list of Threads handles into names, bios and numeric user IDs for a CRM.
- Download profile pictures in several sizes for a creator directory.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "nasa"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Username, for example: lilbieber, can be obtained from the user's homepage link, for example: lilbieber in https://www.threads.net/@lilbieber |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "user": {
    "bio_links": [],
    "biography": "Making the seemingly impossible, possible. ✨",
    "follower_count": 12785840,
    "friendship_status": null,
    "full_name": "NASA",
    "gating": null,
    "has_onboarded_to_text_post_app": true,
    "hd_profile_pic_versions": [
      {
        "height": 320,
        "url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-19/669747085_18089786557960…",
        "width": 320
      }
    ],
    "id": "28829152388",
    "is_verified": true,
    "pk": "28829152388",
    "platform_newsletter_info": null
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user.username / user.full_name` | The account handle and the display name shown on the profile. |
| `user.biography` | The profile bio as plain text. |
| `user.follower_count` | Number of followers the account has. |
| `user.is_verified` | `true` when the account has a verification badge. |
| `user.id / user.pk` | The numeric user ID as a string. Both fields hold the same value in this response. |
| `user.text_post_app_is_private` | `true` when the account is private. `false` means the profile is public. |
| `user.profile_pic_url` | URL of a small profile picture. |
| `user.hd_profile_pic_versions[].url` | URL of a larger profile picture. Use `height` and `width` to pick the size. |
| `user.profile_tags.edges[].node.display_name` | Name of a tag or community linked to the profile, such as `Space Threads`. |
| `user.bio_links` | List of links in the profile bio. It is empty when the account has none. |

### Notes

- Take the `username` from the profile link. In `https://www.threads.net/@lilbieber`, the value is `lilbieber`.
- Many fields, such as `friendship_status` and `gating`, can return `null`.
- To look up a user by numeric ID instead, use [Threads User Info by ID](/apis/threads/web/user-info-by-id).
- To read the account's content, call [Threads User Posts](/apis/threads/web/user-posts).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Get post detail](/apis/threads/web/post-detail): Get Threads post detail.
- [Get post detail V2(supports URL)](/apis/threads/web/post-detail-v2): Get Threads post detail (supports short code and full URL).
- [Search profiles](/apis/threads/web/search-profiles): Search Threads user profiles.

---
Machine-readable: [`catalog/models/threads/web/user-info.json`](../../../../catalog/models/threads/web/user-info.json) · Store page: https://www.sandbase.ai/model/threads/web/user-info
