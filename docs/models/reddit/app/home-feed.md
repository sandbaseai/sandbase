# Reddit App Home Feed API: pricing, parameters and code examples

`reddit/app/home-feed` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Reddit mobile app home feed content including post metadata, author details, scores, and media links. Supports sorting methods, pagination tokens, and post exclusion lists.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/home-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/home-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/home-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/home-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/reddit/app/home-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort method, supports HOT, NEW, TOP, BEST, CONTROVERSIAL  |
| `after` | string |  | Pagination parameter for fetching the next page  |
| `need_format` | boolean |  | Whether to clean and format the data  |
| `filter_posts` | array |  | List of post IDs to filter out, used to exclude already fetched posts  |

## Details

Retrieves the Reddit app home feed using optional parameters such as `sort`, `after`, and `filter_posts` to paginate and filter content.

### Use cases

- Display trending or top posts from the Reddit home feed.
- Paginate through mobile feed posts using cursor tokens.
- Exclude previously viewed post IDs from feed responses.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/home-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sort` | string | No | Sort method, supports HOT, NEW, TOP, BEST, CONTROVERSIAL |
| `after` | string | No | Pagination parameter for fetching the next page |
| `need_format` | boolean | No | Whether to clean and format the data |
| `filter_posts` | array | No | List of post IDs to filter out, used to exclude already fetched posts |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "homefeed": {
    "postsInfoByIds": [
      {
        "__typename": "SubredditPost",
        "commentCount": 489,
        "id": "t3_1ww2n4p",
        "isAuthorBlocked": false,
        "isScoreHidden": false,
        "permalink": "/r/teenagers/comments/1ww2n4p/whats_a_crazy_rumour_from_your_school_that_turned/",
        "postTitle": "Whats a crazy rumour from your school that turned out to be true?",
        "score": 389,
        "url": "https://i.redd.it/956mpuopt3th1.jpeg",
        "authorFlair": {
          "__typename": "AuthorFlair",
          "richtext": "[{\"e\":\"text\",\"t\":\"Teenager\"}]",
          "text": "Teenager"
        },
        "authorInfo": {
          "__typename": "Redditor",
          "accountType": "USER",
          "id": "t2_25tl8ckdgd",
          "name": "Crimsonrainflower33"
        },
        "flair": {
          "__typename": "PostFlair",
          "richtext": "[{\"e\":\"text\",\"t\":\"Discussion\"}]",
          "text": "Discussion",
          "type": "richtext"
        },
        "media": {
          "__typename": "Media",
          "typeHint": "IMAGE"
        },
        "outboundLink": {
          "url": "https://i.redd.it/956mpuopt3th1.jpeg"
        }
      }
    ]
  }
}
```

### Notes

- `sort` supports HOT, NEW, TOP, BEST, and CONTROVERSIAL.
- Use `after` to fetch the next page of feed items.
- Pass an array of post IDs into `filter_posts` to exclude already viewed items.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/home-feed.json`](../../../../catalog/models/reddit/app/home-feed.json) · Store page: https://www.sandbase.ai/model/reddit/app/home-feed
