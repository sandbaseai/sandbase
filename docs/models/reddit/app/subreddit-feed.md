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

Returns the post feed of one subreddit as a list of cell groups, each holding the cells that make up a post (author, title, flair, media). It needs a `subreddit_name` without the `r/` prefix, and you can set the sort order.

### Use cases

- Pull the newest posts from r/technology with `sort` set to `NEW` to track breaking tech news.
- Collect post titles, linked article URLs and flairs to build a link digest for one community.
- Read the `flair` text on each post to count how many posts fall into topics such as Business.
- Page through a subreddit feed with `after` to build a dataset of posts for later analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/subreddit-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"subreddit_name": "technology"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subreddit_name` | string | Yes | Subreddit name (without r/ prefix), e.g., "pics", "funny" |
| `after` | string | No | Pagination parameter for fetching next page |
| `filter_posts` | array | No | List of post IDs to filter out |
| `need_format` | boolean | No | Whether to clean and format the data |
| `sort` | string | No | Sort method, options: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "subredditV3": {
    "elements": {
      "dist": 6,
      "edges": [
        {
          "__typename": "FeedElementEdge",
          "node": {
            "__typename": "CellGroup",
            "adPayload": null,
            "cells": [
              {
                "__typename": "SortCell",
                "isModerator": false,
                "layoutOptions": [
                  "CARD"
                ]
              }
            ],
            "crosspostCells": [
              {
                "__typename": "SortCell"
              }
            ],
            "groupId": "sortcell",
            "groupRecommendationContext": null,
            "id": "c29ydGNlbGw=",
            "payload": null
          }
        }
      ],
      "pageInfo": {
        "endCursor": "dDNfMXhtNnRmMg=="
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `subredditV3.elements.edges[].node.groupId` | Identifier of the feed item. Post items use a `t3_` prefix followed by the post ID, such as `t3_1xm9jey`. The first item has the value `sortcell` and is the sort control, not a post. |
| `subredditV3.elements.edges[].node.cells[].__typename` | Type of each cell, such as `MetadataCell`, `TitleWithThumbnailCell`, `FlairCell`, `TitleCell` or `ImageCell`. Use it to find the cell you need inside a post. |
| `subredditV3.elements.edges[].node.cells[].authorName` | Author of the post, written as `u/name`. It appears in the metadata cell. |
| `subredditV3.elements.edges[].node.cells[].createdAt` | Creation time of the post as an ISO 8601 string with a UTC offset. |
| `subredditV3.elements.edges[].node.cells[].titleCell.title` | Post title. It appears in the `TitleWithThumbnailCell`. Cells of type `TitleCell` hold it in `title`. |
| `subredditV3.elements.edges[].node.cells[].thumbnail.path` | URL of the page the post links to. The `thumbnail.domain` field gives its domain, and `thumbnail.media.path` gives a preview image. |
| `subredditV3.elements.edges[].node.cells[].flair.text` | Flair label of the post, such as `Business`. |
| `subredditV3.elements.edges[].node.adPayload` | Set to an object when the item is an ad. It holds fields like `adLinkUrl`. It is `null` for normal posts. |
| `subredditV3.elements.pageInfo.endCursor` | Cursor that points to the end of this page. Use it to request the next page. |
| `subredditV3.elements.dist` | Number of items in this response. |

### Notes

- Pass `subreddit_name` without the `r/` prefix, for example `technology`.
- For the next page, send the value of `subredditV3.elements.pageInfo.endCursor` as `after`.
- Skip items with a non-null `adPayload` if you only want organic posts. The first edge, with `groupId` of `sortcell`, is not a post either.
- To get the full content and comments of a post, take the ID from `groupId` and call [Reddit Post Details](/apis/reddit/app/post-details) or [Reddit App Post Comments](/apis/reddit/app/post-comments).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/subreddit-feed.json`](../../../../catalog/models/reddit/app/subreddit-feed.json) · Store page: https://www.sandbase.ai/model/reddit/app/subreddit-feed
