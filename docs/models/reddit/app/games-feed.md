# Reddit App Games Feed API: pricing, parameters and code examples

`reddit/app/games-feed` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended gaming posts from Reddit app feeds. Supports filtering by sorting method and time range, with optional response formatting.

## Pricing

- **$0.001 per call** (USD)
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

Returns a page of recommended gaming posts from the Reddit app games feed. Each item is a cell group with the post title, the subreddit it came from, and a creation time. No input is required, and `sort`, `time`, and `after` are optional.

### Use cases

- Collect post titles and source subreddits from the Reddit games feed for community research.
- Find small or new subreddits that Reddit recommends in the gaming feed, using the subreddit name and icon.
- Page through the feed with `after` to build a dataset of suggested gaming posts.
- Compare feed results across `sort` and `time` values to see which posts appear for each setting.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/games-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `after` | string | No | Pagination parameter for fetching next page |
| `need_format` | boolean | No | Whether to clean and format the data |
| `sort` | string | No | Sort method, options: NEW, HOT, TOP, RISING |
| `time` | string | No | Time range, options: ALL, HOUR, DAY, WEEK, MONTH, YEAR |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "gamesFeed": {
    "elements": {
      "dist": 7,
      "edges": [
        {
          "__typename": "FeedElementEdge",
          "node": {
            "__typename": "CellGroup",
            "adPayload": null,
            "cells": [
              {
                "__typename": "RichtextRecommendationContextCell",
                "id": "UmljaFRleHRSZWNvbW1lbmRhdGlvbkNvbnRleHRDZWxsLXQzXzF4bWMyOTg=",
                "rtJsonText": "{\"document\":[{\"c\":[{\"e\":\"text\",\"t\":\"Suggested\"}],\"e\":\"par\"}]}"
              }
            ],
            "crosspostCells": [
              {
                "__typename": "RichtextRecommendationContextCell"
              }
            ],
            "groupId": "t3_1xmc298",
            "groupRecommendationContext": {
              "__typename": "RecommendationContext",
              "isContextHidden": true,
              "name": null,
              "richText": "{\"document\":[{\"c\":[{\"e\":\"text\",\"t\":\"Suggested\"}],\"e\":\"par\"}]}",
              "sourceId": null,
              "typeIdentifier": "dev_platform"
            },
            "id": "dDNfMXhtYzI5OA==",
            "payload": null
          }
        }
      ],
      "pageInfo": {
        "endCursor": "dDNfMXhtZWh0eQ=="
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `gamesFeed.elements.edges[].node.groupId` | Post ID in `t3_` format, for example `t3_1xmc298`. Use it to identify the post in other Reddit calls. |
| `gamesFeed.elements.edges[].node.cells[].title` | Post title. This field sits in the cell with `__typename` set to `TitleCell`. |
| `gamesFeed.elements.edges[].node.cells[].detailsString / gamesFeed.elements.edges[].node.cells[].detailsLink` | Subreddit label such as `r/BunnyTrials`, and the same subreddit name without the `r/` prefix. Both sit in the `MetadataCell`. |
| `gamesFeed.elements.edges[].node.cells[].createdAt` | Creation time of the post as an ISO 8601 timestamp with a `+0000` offset. |
| `gamesFeed.elements.edges[].node.cells[].iconPath` | URL of the subreddit icon image. |
| `gamesFeed.elements.edges[].node.cells[].authorName` | Author name in the `MetadataCell`. It is `null` in the sample response. |
| `gamesFeed.elements.edges[].node.groupRecommendationContext.typeIdentifier` | Label for why the post was recommended, such as `dev_platform` or `dev_platform_diversity`. |
| `gamesFeed.elements.edges[].node.adPayload` | Ad data for the item. It is `null` when the item is not an ad. |
| `gamesFeed.elements.dist` | Number of items in the current page. |
| `gamesFeed.elements.pageInfo.endCursor` | Cursor for the end of this page. Pass it as `after` to request the next page. |

### Notes

- Pass `pageInfo.endCursor` from the last response as `after` to get the next page.
- Each edge holds a list of `cells`. Find the title, subreddit, and timestamp by checking each cell's `__typename`: `TitleCell` or `MetadataCell`.
- `sort` accepts `NEW`, `HOT`, `TOP`, or `RISING`. `time` accepts `ALL`, `HOUR`, `DAY`, `WEEK`, `MONTH`, or `YEAR`.
- To get full post data for a `groupId`, call [Reddit Post Details](/apis/reddit/app/post-details).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/games-feed.json`](../../../../catalog/models/reddit/app/games-feed.json) · Store page: https://www.sandbase.ai/model/reddit/app/games-feed
