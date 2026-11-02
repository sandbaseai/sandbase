# Reddit App News Feed API: pricing, parameters and code examples

`reddit/app/news-feed` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns news-related recommended content from the Reddit app, including current affairs discussions, with optional subtopic filtering and formatting.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/news-feed", "after": "", "need_format": false, "subtopic_ids": ["all"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/news-feed', {'after': '', 'need_format': False, 'subtopic_ids': ['all']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/news-feed", {
  "after": "",
  "need_format": false,
  "subtopic_ids": [
    "all"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/news-feed", sandbase.Params{
	"after": "",
	"need_format": false,
	"subtopic_ids": []any{"all"},
})
```

Same call via the path form: `POST /v1/api/reddit/app/news-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `after` | string |  | Pagination parameter for fetching next page default `""` |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `subtopic_ids` | array |  | List of subtopic IDs, default ["all"] means all news categories default `["all"]` |

## Details

Retrieve trending news recommendations from the Reddit app feed, filtered by `subtopic_ids` and paginated via `after`.

### Use cases

- Monitor trending news topics and discussions across Reddit communities.
- Filter Reddit app news streams by specific category identifiers.
- Ingest curated news feed items into custom aggregators and dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/news-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `after` | string | No | Pagination parameter for fetching next page |
| `need_format` | boolean | No | Whether to clean and format the data |
| `subtopic_ids` | array | No | List of subtopic IDs, default ["all"] means all news categories |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "newsV3": {
    "elements": {
      "edges": [
        {
          "__typename": "FeedElementEdge",
          "node": {
            "__typename": "CellGroup",
            "id": "dDNfMXd5em03bA=="
          }
        }
      ]
    }
  }
}
```

### Notes

- Use `after` for cursor-based pagination across news feed pages.
- The `subtopic_ids` parameter defaults to ["all"] to cover all news categories.
- Set `need_format` to true to clean and format the returned data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/news-feed.json`](../../../../catalog/models/reddit/app/news-feed.json) · Store page: https://www.sandbase.ai/model/reddit/app/news-feed
