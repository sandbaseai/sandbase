# Reddit Search API: pricing, parameters and code examples

`reddit/app/dynamic-search` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Search Reddit posts, communities, comments, media and users with the Reddit app search. Sort by relevance, hot, top, new or comments and filter by time range, with NSFW and safe-search controls.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/dynamic-search", "after": "", "allow_nsfw": "0", "need_format": false, "query": "OpenAI", "safe_search": "unset", "search_type": "post"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/dynamic-search', {'after': '', 'allow_nsfw': '0', 'need_format': False, 'query': 'OpenAI', 'safe_search': 'unset', 'search_type': 'post'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/dynamic-search", {
  "after": "",
  "allow_nsfw": "0",
  "need_format": false,
  "query": "OpenAI",
  "safe_search": "unset",
  "search_type": "post"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/dynamic-search", sandbase.Params{
	"after": "",
	"allow_nsfw": "0",
	"need_format": false,
	"query": "OpenAI",
	"safe_search": "unset",
	"search_type": "post",
})
```

Same call via the path form: `POST /v1/api/reddit/app/dynamic-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort method (only for post/comment/media): RELEVANCE, HOT, TOP, NEW, COMMENTS  |
| `after` | string |  | Pagination parameter for fetching next page default `""` |
| `query` | string | yes | Search keyword  |
| `allow_nsfw` | string |  | Allow NSFW content, "0" or "1" default `"0"` |
| `time_range` | string |  | Time range (only for post/media): all, year, month, week, day, hour  |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `safe_search` | string |  | Safe search setting, "unset" or "strict" default `"unset"` |
| `search_type` | string |  | Search type: post, community, comment, media, people default `"post"` |

## Details

Search Reddit for a keyword across posts, communities, comments, media or people. Choose sort and time range, and paginate with `after`.

### Use cases

- Monitor discussions about a brand or product.
- Find active subreddits for a topic.
- Collect posts and comments for sentiment analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/dynamic-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword |
| `sort` | string | No | Sort method (only for post/comment/media): RELEVANCE, HOT, TOP, NEW, COMMENTS |
| `after` | string | No | Pagination parameter for fetching next page |
| `allow_nsfw` | string | No | Allow NSFW content, "0" or "1" |
| `time_range` | string | No | Time range (only for post/media): all, year, month, week, day, hour |
| `need_format` | boolean | No | Whether to clean and format the data |
| `safe_search` | string | No | Safe search setting, "unset" or "strict" |
| `search_type` | string | No | Search type: post, community, comment, media, people |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "search": {
    "dynamic": {
      "components": {
        "main": {
          "edges": [
            {
              "node": {
                "__typename": "SearchListComponent",
                "children": [
                  {
                    "__typename": "SearchPost",
                    "post": {
                      "id": "t3_1wsu05i",
                      "title": "Post by Altman pretty much confirms direction from OpenAI",
                      "type": "TEXT",
                      "isNsfw": false
                    },
                    "community": "codex"
                  }
                ]
              }
            }
          ],
          "pageInfo": {
            "hasNextPage": true,
            "endCursor": "<after>"
          }
        }
      }
    }
  }
}
```

### Notes

- `search_type`: post, community, comment, media or people.
- Set `need_format` to `true` for a cleaned, flatter response.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Check if Subreddit is Muted](/model/reddit/app/check-subreddit-muted): Check if a specified Reddit subreddit is muted by the current user.
- [Fetch Reddit APP Comment Replies (Sub-comments)](/model/reddit/app/comment-replies): Fetch replies (sub-comments/second-level comments) under a specified Reddit APP comment Use this endpoint when a comment node has more.cursor field to get its …
- [Fetch Reddit APP Community Highlights](/model/reddit/app/community-highlights): Fetch featured highlight content of a specified Reddit APP community, including popular posts and important announcements.

---
Machine-readable: [`catalog/models/reddit/app/dynamic-search.json`](../../../../catalog/models/reddit/app/dynamic-search.json) · Store page: https://www.sandbase.ai/model/reddit/app/dynamic-search
