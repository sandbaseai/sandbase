# Twitter (X) User Followers API: pricing, parameters and code examples

`twitter/web/user-followers` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves follower profiles for a specified Twitter (X) account, including follower counts and verification statuses. Supports pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-followers", "screen_name": "NASA"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-followers', {'screen_name': 'NASA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-followers", {
  "screen_name": "NASA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-followers", sandbase.Params{
	"screen_name": "NASA",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the last request  |
| `screen_name` | string | yes | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk  |

## Details

Returns a page of follower profiles for a public Twitter (X) account. It needs the account's `screen_name` and returns each follower's name, handle, ID, and follower count, plus a cursor for the next page.

### Use cases

- Sample the accounts that follow a brand or agency profile to see who its audience is.
- Find large or Blue-verified accounts among the followers of a target profile.
- Export follower handles and IDs page by page for audience analysis.
- Compare follower lists of two accounts by matching on `user_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"screen_name": "NASA"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `screen_name` | string | Yes | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk |
| `cursor` | string | No | Cursor, default is None, used for paging, obtained from the last request |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "followers": [
    {
      "affiliates": [],
      "blue_verified": true,
      "business_account": null,
      "can_dm": null,
      "created_at": "Thu Apr 23 21:53:30 +0000 2009",
      "description": null,
      "followers_count": 41933560,
      "friends_count": null,
      "location": "Earth",
      "media_count": null,
      "name": "SpaceX",
      "profile_image": "https://pbs.twimg.com/profile_images/1697749409851985920/HbrI04tM_normal.jpg"
    }
  ],
  "followers_count": 92289815,
  "more_users": true,
  "next_cursor": "1880822017849790130|2117523445288796127",
  "status": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `followers[].screen_name / followers[].name` | The follower's handle and display name. |
| `followers[].user_id` | The follower's numeric account ID, returned as a string. |
| `followers[].followers_count` | How many followers this follower account has. |
| `followers[].blue_verified / followers[].verified` | Verification flags for the follower. A profile can be `blue_verified` while `verified` is `false`. |
| `followers[].created_at` | When the follower account was created, in a format like `Thu Apr 23 21:53:30 +0000 2009`. |
| `followers[].location` | Location text from the follower's profile. |
| `followers[].affiliates` | Affiliation data for the follower. It is an empty list when there is none, and an object with a `label` (for example a business badge) when the account is linked to an organization. |
| `followers_count` | Follower total for the target account (the `screen_name` you sent). |
| `more_users` | `true` when more follower pages are available. |
| `next_cursor` | Cursor string to pass as `cursor` in the next request. |

### Notes

- Take `screen_name` from the profile URL. For https://twitter.com/NASA, use `NASA`.
- To get the next page, send the `next_cursor` value as `cursor` and keep the same `screen_name`. Stop when `more_users` is `false`.
- Fields such as `description`, `friends_count`, `media_count`, and `statuses_count` came back as `null` in this response, so do not rely on them here.
- To see who an account follows instead, call [Twitter (X) User Followings](/apis/twitter/web/user-followings).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Twitter (X) Latest Tweet Comments](/apis/twitter/web/latest-post-comments): Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.
- [Twitter (X) Tweet Comments](/apis/twitter/web/post-comments): Returns comment threads and replies under a specified tweet.
- [Twitter (X) Retweet User List](/apis/twitter/web/retweet-user-list): Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.

---
Machine-readable: [`catalog/models/twitter/web/user-followers.json`](../../../../catalog/models/twitter/web/user-followers.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-followers
