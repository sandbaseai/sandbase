# Reddit App Popular Feed API: pricing, parameters and code examples

`reddit/app/popular-feed` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns trending and popular posts across Reddit with engagement metrics, subreddit details, and media metadata. Supports sorting and time filters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/popular-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/popular-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/popular-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/popular-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/reddit/app/popular-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort method, options: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING default `"BEST"` |
| `time` | string |  | Time range, options: ALL, HOUR, DAY, WEEK, MONTH, YEAR default `"ALL"` |
| `after` | string |  | Pagination parameter for fetching next page default `""` |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `filter_posts` | array |  | List of post IDs to filter out, used to avoid duplicate fetches default `[]` |

## Details

Returns popular and trending post listings from the Reddit app, customizable using `sort` and `time` parameters.

### Use cases

- Monitor trending posts and viral topics across Reddit communities.
- Track engagement metrics like comment counts and scores on popular submissions.
- Collect popular media links and subreddit highlights for social listening.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/popular-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sort` | string | No | Sort method, options: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING |
| `time` | string | No | Time range, options: ALL, HOUR, DAY, WEEK, MONTH, YEAR |
| `after` | string | No | Pagination parameter for fetching next page |
| `need_format` | boolean | No | Whether to clean and format the data |
| `filter_posts` | array | No | List of post IDs to filter out, used to avoid duplicate fetches |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "popularfeed": {
    "postsInfoByIds": [
      {
        "__typename": "SubredditPost",
        "commentCount": 754,
        "id": "t3_1wyjtbt",
        "isAuthorBlocked": false,
        "isScoreHidden": false,
        "permalink": "/r/mildlyinfuriating/comments/1wyjtbt/supreme_we_do_not_allow_cancellations_supreme_six/",
        "postTitle": "Supreme: “We do not allow cancellations.” Supreme six hours after I mention PayPal:",
        "score": 18775,
        "url": "https://i.redd.it/j59df1dynpth1.jpeg",
        "authorInfo": {
          "__typename": "Redditor",
          "accountType": "USER",
          "id": "t2_1n6lhgykn9",
          "name": "Alert-Lavishness-99"
        },
        "flair": {
          "__typename": "PostFlair",
          "richtext": "[{\"e\":\"text\",\"t\":\"Winter is Coming\"}]",
          "text": "Winter is Coming",
          "type": "richtext"
        },
        "media": {
          "__typename": "Media",
          "typeHint": "IMAGE"
        },
        "outboundLink": {
          "url": "https://i.redd.it/j59df1dynpth1.jpeg"
        },
        "subreddit": {
          "__typename": "Subreddit",
          "id": "t5_2ubgg",
          "isTitleSafe": true,
          "name": "mildlyinfuriating",
          "prefixedName": "r/mildlyinfuriating",
          "subscribersCount": 12622421.0
        }
      }
    ]
  }
}
```

### Notes

- Supported `sort` options include BEST, HOT, NEW, TOP, CONTROVERSIAL, and RISING.
- Supported `time` options include ALL, HOUR, DAY, WEEK, MONTH, and YEAR.
- Use `after` for pagination and `filter_posts` with post IDs to exclude previously viewed items.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/popular-feed.json`](../../../../catalog/models/reddit/app/popular-feed.json) · Store page: https://www.sandbase.ai/model/reddit/app/popular-feed
