# Reddit User Comments API: pricing, parameters and code examples

`reddit/app/user-comments` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of comments submitted by a specified Reddit user. Supports multiple sorting options, customizable page sizes, and pagination tokens.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/user-comments", "username": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/user-comments', {'username': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/user-comments", {
  "username": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/user-comments", sandbase.Params{
	"username": "example",
})
```

Same call via the path form: `POST /v1/api/reddit/app/user-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort method, options: NEW (newest), TOP (top rated), HOT (hot), CONTROVERSIAL (controversial)  |
| `after` | string |  | Pagination parameter for fetching next page  |
| `username` | string | yes | Reddit username  |
| `page_size` | integer |  | Number of comments per page, default 25  |
| `need_format` | boolean |  | Whether to clean and format the data  |

## Details

Retrieve comments from a Reddit account using the `username` parameter. Results can be sorted by criteria such as newest, top rated, or hot.

### Use cases

- Review comment history for a specific Reddit user account.
- Analyze user participation and feedback trends across communities.
- Monitor top-rated and controversial contributions from targeted profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/user-comments" \
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
| `page_size` | integer | No | Number of comments per page, default 25 |
| `need_format` | boolean | No | Whether to clean and format the data |

### Notes

- Supported `sort` options include NEW, TOP, HOT, and CONTROVERSIAL.
- `page_size` sets the comment count per request and defaults to 25.
- Use `after` to retrieve the next page of results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/user-comments.json`](../../../../catalog/models/reddit/app/user-comments.json) · Store page: https://www.sandbase.ai/model/reddit/app/user-comments
