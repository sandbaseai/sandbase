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

Retrieve the communities where a specific user is most active by providing their `username`. Use `need_format` to toggle cleaned response output.

### Use cases

- Analyze user interest patterns across Reddit communities.
- Evaluate an author's topical engagement across subreddits.
- Gather community participation data for user research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/user-active-subreddits" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "spez"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Reddit username |
| `need_format` | boolean | No | Whether to clean and format the data |

### Notes

- Set `need_format` to true to clean and format the returned data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/user-active-subreddits.json`](../../../../catalog/models/reddit/app/user-active-subreddits.json) · Store page: https://www.sandbase.ai/model/reddit/app/user-active-subreddits
