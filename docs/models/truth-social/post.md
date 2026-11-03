# Truth Social Post API: pricing, parameters and code examples

`truth-social/post` · data API · Truth Social · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Get a single Truth Social post by its URL - text, author, engagement (likes, comments, shares), and timestamp as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "truth-social/post", "url": "https://truthsocial.com/@realDonaldTrump/posts/116824551176646175"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('truth-social/post', {'url': 'https://truthsocial.com/@realDonaldTrump/posts/116824551176646175'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("truth-social/post", {
  "url": "https://truthsocial.com/@realDonaldTrump/posts/116824551176646175"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "truth-social/post", sandbase.Params{
	"url": "https://truthsocial.com/@realDonaldTrump/posts/116824551176646175",
})
```

Same call via the path form: `POST /v1/api/truth-social/post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Truth Social post URL, e.g. "https://truthsocial.com/@realDonaldTrump/posts/116824551176646175".  |

## Details

Returns one Truth Social post as JSON: its text, author details, like, comment and share counts, attached media, and a creation timestamp. The only input is the full post URL in `url`.

### Use cases

- Track how many likes, comments and shares a specific post has gathered.
- Archive the text and media files of a post before it is edited or removed.
- Check whether an account that posted is verified before citing the post.
- Add post text and engagement numbers to a news or monitoring dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/truth-social/post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://truthsocial.com/@realDonaldTrump/posts/116824551176646175"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Truth Social post URL, e.g. "https://truthsocial.com/@realDonaldTrump/posts/116824551176646175". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "avatarUrl": "https://static-assets-1.truthsocial.com/tmtg:prime-ts-assets/accounts/avatars/10…",
    "comments": 594,
    "createdUtc": 1782601183,
    "displayName": "Donald J. Trump",
    "id": "116824551176646175",
    "image": "https://static-assets-1.truthsocial.com/tmtg:prime-ts-assets/media_attachments/f…",
    "likes": 15764,
    "mediaUrls": [
      "https://static-assets-1.truthsocial.com/tmtg:prime-ts-assets/media_attachments/f…"
    ],
    "shares": 3961,
    "text": "RT: https://truthsocial.com/users/realDonaldTrump/statuses/116824550355095950",
    "username": "realDonaldTrump",
    "verified": true
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the post was located. A lookup that finds nothing returns `false`. |
| `data.id` | ID of the post. It matches the last part of the post URL. |
| `data.text` | Text of the post. A repost can show only a `RT:` prefix followed by a link to the original status. |
| `data.username / data.displayName` | Handle of the author and the name shown on the profile. |
| `data.verified` | `true` if the author account is verified. |
| `data.likes / data.comments / data.shares` | Engagement counts for the post. |
| `data.createdUtc` | Time the post was created, as a Unix timestamp in seconds. |
| `data.mediaUrls[]` | Links to the full-size media files attached to the post. |
| `data.image` | Link to a smaller preview image of the attached media. |
| `data.avatarUrl` | Link to the author's profile picture. |

### Notes

- Copy the post URL from the Truth Social site. It has the form `https://truthsocial.com/@<username>/posts/<id>`.
- Use the result from `outputs[0].data`. Check `found` first, since a missing post returns `found: false` instead of an error.
- To see more from the same author, call [Truth Social User Posts](/apis/truth-social/user-posts). For account details, call [Truth Social Profile](/apis/truth-social/profile).

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/truth-social/post.json`](../../../catalog/models/truth-social/post.json) · Store page: https://www.sandbase.ai/model/truth-social/post
