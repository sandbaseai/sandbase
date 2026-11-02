# Reddit Subreddit Feed API: pricing, parameters and code examples

`reddit/app/subreddit-feed` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the post stream for a specified subreddit. Supports sorting methods, cursor pagination, and filters to exclude specific post IDs.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/subreddit-feed", "subreddit_name": "technology"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/subreddit-feed', {'subreddit_name': 'technology'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/subreddit-feed", {
  "subreddit_name": "technology"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/subreddit-feed", sandbase.Params{
	"subreddit_name": "technology",
})
```

Same call via the path form: `POST /v1/api/reddit/app/subreddit-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort method, options: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING default `"BEST"` |
| `after` | string |  | Pagination parameter for fetching next page default `""` |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `filter_posts` | array |  | List of post IDs to filter out default `[]` |
| `subreddit_name` | string | yes | Subreddit name (without r/ prefix), e.g., "pics", "funny"  |

## Details

Retrieve a list of posts from a target community feed by passing `subreddit_name`. You can configure feed order with `sort` and paginate through older items.

### Use cases

- Monitor community discussions and trending posts across specific subreddits.
- Retrieve sorted post listings by top, hot, or new criteria for content curation.
- Ingest subreddit feed data continuously into internal monitoring dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/subreddit-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"subreddit_name": "technology"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subreddit_name` | string | Yes | Subreddit name (without r/ prefix), e.g., "pics", "funny" |
| `sort` | string | No | Sort method, options: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING |
| `after` | string | No | Pagination parameter for fetching next page |
| `need_format` | boolean | No | Whether to clean and format the data |
| `filter_posts` | array | No | List of post IDs to filter out |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "subredditV3": {
    "elements": {
      "edges": [
        {
          "__typename": "FeedElementEdge",
          "node": {
            "__typename": "CellGroup",
            "id": "c29ydGNlbGw="
          }
        }
      ]
    }
  }
}
```

### Notes

- Specify `subreddit_name` without the 'r/' prefix (e.g., 'technology').
- Supported `sort` values include BEST, HOT, NEW, TOP, CONTROVERSIAL, and RISING.
- Use `after` to retrieve the next page of feed results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/subreddit-feed.json`](../../../../catalog/models/reddit/app/subreddit-feed.json) · Store page: https://www.sandbase.ai/model/reddit/app/subreddit-feed
