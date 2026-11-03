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

Returns a page of posts from the Reddit mobile app home feed. Each post includes author details, comment count, flair, awards, and link domain. All inputs are optional, so an empty request returns a default feed.

### Use cases

- Pull a page of home feed posts and track which subreddits and domains show up most.
- Page through the feed with the `after` cursor and store each post by its `id`.
- Skip posts you already saved by passing their IDs in `filter_posts`.
- Find promoted or app-install posts by checking `callToAction` and `domain`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/home-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `after` | string | No | Pagination parameter for fetching the next page |
| `filter_posts` | array | No | List of post IDs to filter out, used to exclude already fetched posts |
| `need_format` | boolean | No | Whether to clean and format the data |
| `sort` | string | No | Sort method, supports HOT, NEW, TOP, BEST, CONTROVERSIAL |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "after": "dDNfMXhrOXRmbA==",
  "homefeed": {
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
            "url": "https://www.redditstatic.com/avatars/defaults/v2/avatar_default_7.png"
          },
          "id": "t2_ne49b",
          "isBlocked": false,
          "isCakeDayNow": false,
          "name": "brainland",
          "newIcon": {
            "__typename": "MediaSource",
            "dimensions": {
              "height": 256,
              "width": 256
            },
            "url": "https://www.redditstatic.com/avatars/defaults/v2/avatar_default_7.png"
          }
        },
        "awardings": [
          {
            "__typename": "AwardingTotal",
            "award": {
              "__typename": "Award",
              "id": "award_free_bravo",
              "name": "Bravo",
              "static_icon_16": {
                "__typename": "MediaSource",
                "dimensions": {
                  "height": 16,
                  "width": 16
                },
                "url": "https://i.redd.it/snoovatar/snoo_assets/marketing/bravo_16.png"
              },
              "static_icon_24": {
                "__typename": "MediaSource",
                "dimensions": {
                  "height": 24,
                  "width": 24
                },
                "url": "https://i.redd.it/snoovatar/snoo_assets/marketing/bravo_24.png"
              },
              "static_icon_32": {
                "__typename": "MediaSource",
                "dimensions": {
                  "height": 32,
                  "width": 32
                },
                "url": "https://i.redd.it/snoovatar/snoo_assets/marketing/bravo_32.png"
              },
              "static_icon_48": {
                "__typename": "MediaSource",
                "dimensions": {
                  "height": 48,
                  "width": 48
                },
                "url": "https://i.redd.it/snoovatar/snoo_assets/marketing/bravo_48.png"
              },
              "static_icon_64": {
                "__typename": "MediaSource",
                "dimensions": {
                  "height": 64,
                  "width": 64
                },
                "url": "https://i.redd.it/snoovatar/snoo_assets/marketing/bravo_64.png"
              }
            },
            "total": 8
          }
        ],
        "awardingsInfo": {
          "promos": null
        },
        "commentCount": 5447,
        "content": null,
        "createdAt": "2026-10-29T16:30:44.831000+0000",
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
| `after` | Cursor token for the next page. Pass it back as the `after` request parameter. |
| `homefeed.postsInfoByIds[]` | List of posts in the feed. Each item has a `__typename` such as `SubredditPost` or `ProfilePost`. |
| `homefeed.postsInfoByIds[].id` | Post ID in the form `t3_...`. Use it with `filter_posts` or in post lookups. |
| `homefeed.postsInfoByIds[].createdAt` | Time the post was created, as an ISO 8601 timestamp with a UTC offset. |
| `homefeed.postsInfoByIds[].commentCount` | Number of comments on the post. |
| `homefeed.postsInfoByIds[].authorInfo.name / homefeed.postsInfoByIds[].authorInfo.id` | Username of the author and the author ID in the form `t2_...`. |
| `homefeed.postsInfoByIds[].domain` | Domain the post links to, such as `v.redd.it` for Reddit video or `apps.apple.com` for an app link. |
| `homefeed.postsInfoByIds[].flair.text` | Text of the post flair, such as `Fear Factor`. The value is `null` when the post has no flair. |
| `homefeed.postsInfoByIds[].awardings[].award.name / homefeed.postsInfoByIds[].awardings[].total` | Name of an award on the post and how many times it was given. |
| `homefeed.postsInfoByIds[].isNsfw / homefeed.postsInfoByIds[].isLocked / homefeed.postsInfoByIds[].isScoreHidden` | Flags for adult content, a locked post, and a hidden score. |

### Notes

- Set `sort` to `HOT`, `NEW`, `TOP`, `BEST`, or `CONTROVERSIAL`.
- Copy the top-level `after` value into the next request to get the following page.
- To read a post in full, call [Reddit Post Details](/apis/reddit/app/post-details) with its ID. To read its comments, call [Reddit App Post Comments](/apis/reddit/app/post-comments).
- For the site-wide popular feed instead of the home feed, use [Reddit App Popular Feed](/apis/reddit/app/popular-feed).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/home-feed.json`](../../../../catalog/models/reddit/app/home-feed.json) · Store page: https://www.sandbase.ai/model/reddit/app/home-feed
