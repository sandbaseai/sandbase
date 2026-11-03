# Reddit User Posts API: pricing, parameters and code examples

`reddit/app/user-posts` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of posts submitted by a specified Reddit user. Results can be sorted by new, top, hot, or controversial order with optional formatting.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/user-posts", "after": "", "need_format": false, "sort": "NEW", "username": "spez"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/user-posts', {'after': '', 'need_format': False, 'sort': 'NEW', 'username': 'spez'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/user-posts", {
  "after": "",
  "need_format": false,
  "sort": "NEW",
  "username": "spez"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/user-posts", sandbase.Params{
	"after": "",
	"need_format": false,
	"sort": "NEW",
	"username": "spez",
})
```

Same call via the path form: `POST /v1/api/reddit/app/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort method, options: NEW (newest), TOP (top rated), HOT (hot), CONTROVERSIAL (controversial) default `"NEW"` |
| `after` | string |  | Pagination parameter for fetching next page default `""` |
| `username` | string | yes | Reddit username  |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |

## Details

Retrieve submissions submitted by a specific account using the `username` parameter, with support for custom sort orders and pagination.

### Use cases

- Analyze submission history and activity for a Reddit account.
- Display a profile feed of posts submitted by an author.
- Track top-rated or controversial submissions from specific users.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "spez"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Reddit username |
| `sort` | string | No | Sort method, options: NEW (newest), TOP (top rated), HOT (hot), CONTROVERSIAL (controversial) |
| `after` | string | No | Pagination parameter for fetching next page |
| `need_format` | boolean | No | Whether to clean and format the data |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "postFeed": {
    "elements": {
      "edges": [
        {
          "node": {
            "__typename": "ProfilePost",
            "commentCount": 473,
            "id": "t3_1vgbkge",
            "isScoreHidden": false,
            "permalink": "/user/spez/comments/1vgbkge/modernizing_reddits_infrastructure_with_you/",
            "postTitle": "Modernizing Reddit’s infrastructure with you"
          }
        }
      ]
    }
  }
}
```

### Notes

- `sort` options include NEW, TOP, HOT, and CONTROVERSIAL.
- Use `after` to retrieve the next page of user submissions.
- Set `need_format` to true to clean and format the output data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/user-posts.json`](../../../../catalog/models/reddit/app/user-posts.json) · Store page: https://www.sandbase.ai/model/reddit/app/user-posts
