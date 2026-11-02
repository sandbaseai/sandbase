# Reddit App Games Feed API: pricing, parameters and code examples

`reddit/app/games-feed` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns recommended gaming posts from Reddit app feeds. Supports filtering by sorting method and time range, with optional response formatting.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/games-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/games-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/games-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/games-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/reddit/app/games-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort method, options: NEW, HOT, TOP, RISING default `"NEW"` |
| `time` | string |  | Time range, options: ALL, HOUR, DAY, WEEK, MONTH, YEAR default `"ALL"` |
| `after` | string |  | Pagination parameter for fetching next page default `""` |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |

## Details

Look up gaming feed items from the Reddit app using `sort` and `time` filters. Page through additional results using the `after` cursor.

### Use cases

- Track trending gaming discussions and community posts on Reddit.
- Surface popular video game highlights across custom time ranges.
- Collect structured gaming feed entries for community analytics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/games-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sort` | string | No | Sort method, options: NEW, HOT, TOP, RISING |
| `time` | string | No | Time range, options: ALL, HOUR, DAY, WEEK, MONTH, YEAR |
| `after` | string | No | Pagination parameter for fetching next page |
| `need_format` | boolean | No | Whether to clean and format the data |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "gamesFeed": {
    "elements": {
      "edges": [
        {
          "__typename": "FeedElementEdge",
          "node": {
            "__typename": "CellGroup",
            "id": "dDNfMXd5cXAxMw=="
          }
        }
      ]
    }
  }
}
```

### Notes

- `sort` options include `NEW`, `HOT`, `TOP`, and `RISING`.
- `time` options include `ALL`, `HOUR`, `DAY`, `WEEK`, `MONTH`, and `YEAR`.
- Use `after` to paginate through subsequent pages of results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/games-feed.json`](../../../../catalog/models/reddit/app/games-feed.json) · Store page: https://www.sandbase.ai/model/reddit/app/games-feed
