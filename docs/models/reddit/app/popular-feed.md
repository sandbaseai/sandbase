# Reddit App Popular Feed API: pricing, parameters and code examples

`reddit/app/popular-feed` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending and popular posts across Reddit with engagement metrics, subreddit details, and media metadata. Supports sorting and time filters.

## Pricing

- **$0.001 per call** (USD)
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

Returns a page of posts from the Reddit popular feed, with author details, post content, and flags such as locked or NSFW. It needs no input. You can set `sort`, `time`, and `after` to change the order, the time window, and the page.

### Use cases

- Pull the current popular posts to see which topics are trending on Reddit.
- Track `commentCount` on popular posts to find the threads with the most discussion.
- Collect the posts that carry ads or app download links by checking `__typename` and `callToAction`.
- Page through the feed with `after` and skip known posts with `filter_posts` to build a deduplicated list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/popular-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `after` | string | No | Pagination parameter for fetching next page |
| `filter_posts` | array | No | List of post IDs to filter out, used to avoid duplicate fetches |
| `need_format` | boolean | No | Whether to clean and format the data |
| `sort` | string | No | Sort method, options: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING |
| `time` | string | No | Time range, options: ALL, HOUR, DAY, WEEK, MONTH, YEAR |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "after": "dDNfMXhseWMwcg==",
  "popularfeed": {
    "postsInfoByIds": [
      {
        "__typename": "SubredditPost",
        "attributionInfo": null,
        "authorCommunityBadge": null,
        "authorFlair": null,
        "authorInfo": {
          "__typename": "Redditor",
          "accountType": "USER",
          "iconSmall": {
            "__typename": "MediaSource",
            "dimensions": {
              "height": 256,
              "width": 256
            },
            "url": "https://www.redditstatic.com/avatars/defaults/v2/avatar_default_1.png"
          },
          "id": "t2_2pw0aoobrt",
          "isBlocked": false,
          "isCakeDayNow": false,
          "name": "TrainingThink9747",
          "newIcon": {
            "__typename": "MediaSource",
            "dimensions": {
              "height": 256,
              "width": 256
            },
            "url": "https://www.redditstatic.com/avatars/defaults/v2/avatar_default_1.png"
          }
        },
        "awardings": [],
        "awardingsInfo": {
          "promos": null
        },
        "commentCount": 405,
        "content": {
          "html": "I 26M recently started hooking up with an older coworker 56F \nWe work for a real…",
          "markdown": "I 26M recently started hooking up with an older coworker 56F \n\nWe work for a rea…",
          "preview": "I 26M recently started hooking up with an older coworker 56F We work for a reall…",
          "richtext": "{\"document\":[{\"c\":[{\"e\":\"text\",\"t\":\"I 26M recently started hooking up with an ol…",
          "richtextMedia": []
        },
        "createdAt": "2026-11-02T18:57:40.939000+0000",
        "crosspostRoot": null,
        "crowdControlLevel": "OFF"
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `after` | Cursor for the next page. Send it back as the `after` parameter. |
| `popularfeed.postsInfoByIds[]` | List of posts in the feed. Each item is one post object. |
| `popularfeed.postsInfoByIds[].__typename` | Post type. The response shows `SubredditPost` for normal posts and `ProfilePost` for posts made from a user profile. |
| `popularfeed.postsInfoByIds[].id` | Post ID with the `t3_` prefix, for example `t3_1xm61yj`. |
| `popularfeed.postsInfoByIds[].commentCount` | Number of comments on the post. |
| `popularfeed.postsInfoByIds[].createdAt` | Creation time of the post as an ISO 8601 timestamp with a `+0000` offset. |
| `popularfeed.postsInfoByIds[].authorInfo.name / authorInfo.id` | Username of the author and their ID with the `t2_` prefix. |
| `popularfeed.postsInfoByIds[].content.markdown / content.preview` | Post body as markdown and as a short plain-text preview. `content` is `null` for link posts such as ads. |
| `popularfeed.postsInfoByIds[].domain` | Domain the post points to. Self posts show values like `self.confession`, and image posts show `i.redd.it`. |
| `popularfeed.postsInfoByIds[].isLocked / isNsfw / isSelfPost` | Flags that show if the post is locked, marked NSFW, or a text post. |

### Notes

- Send an empty body `{}` to get the default feed, which uses `sort` of `BEST` and `time` of `ALL`.
- For the next page, pass the top-level `after` value as the `after` parameter.
- Pass IDs you have already seen in `filter_posts` to leave them out of the results.
- To read the comments of a post, call [Reddit App Post Comments](/apis/reddit/app/post-comments). For full post data, call [Reddit Post Details](/apis/reddit/app/post-details).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/popular-feed.json`](../../../../catalog/models/reddit/app/popular-feed.json) · Store page: https://www.sandbase.ai/model/reddit/app/popular-feed
