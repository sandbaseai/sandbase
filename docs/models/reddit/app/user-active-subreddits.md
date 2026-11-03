# Reddit User Active Subreddits API: pricing, parameters and code examples

`reddit/app/user-active-subreddits` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of Reddit communities where a specified user participates most actively. Supports optional response formatting.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/user-active-subreddits", "username": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/user-active-subreddits', {'username': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/user-active-subreddits", {
  "username": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/user-active-subreddits", sandbase.Params{
	"username": "example",
})
```

Same call via the path form: `POST /v1/api/reddit/app/user-active-subreddits` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Reddit username  |
| `need_format` | boolean |  | Whether to clean and format the data  |

## Details

Returns the Reddit communities where a given user is most active. It needs a Reddit `username`, such as `spez`. The sample call for `spez` returned the user object with `activeSubreddits` set to `null`.

### Use cases

- Check which subreddits a Reddit user is listed as active in.
- Confirm that a username resolves to a Redditor record before you call other user APIs.
- Compare the `activeSubreddits` value across several usernames to see which accounts have data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/user-active-subreddits" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "spez"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Reddit username |
| `need_format` | boolean | No | Whether to clean and format the data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "redditorInfoByName": {
    "__typename": "Redditor",
    "activeSubreddits": null
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `redditorInfoByName` | The user record that matches the `username` you sent. |
| `redditorInfoByName.__typename` | The object type. The value `Redditor` confirms the lookup found a Reddit user account. |
| `redditorInfoByName.activeSubreddits` | The list of communities where the user is most active. It is `null` in the sample response for `spez`, so no active subreddits came back for that call. |

### Notes

- Send `username` without the `u/` prefix, as in the example `spez`.
- Handle a `null` value in `activeSubreddits` in your code, since the sample response for `spez` returned no list.
- To see what a user posts or comments, call [Reddit User Posts](/apis/reddit/app/user-posts) or [Reddit User Comments](/apis/reddit/app/user-comments).
- For account details, call [Reddit App User Profile](/apis/reddit/app/user-profile).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/user-active-subreddits.json`](../../../../catalog/models/reddit/app/user-active-subreddits.json) · Store page: https://www.sandbase.ai/model/reddit/app/user-active-subreddits
