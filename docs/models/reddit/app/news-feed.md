# Reddit App News Feed API: pricing, parameters and code examples

`reddit/app/news-feed` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns news-related recommended content from the Reddit app, including current affairs discussions, with optional subtopic filtering and formatting.

## Pricing

- **$0.001 per call** (USD)
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

Returns a page of news-related recommended posts from the Reddit app feed. Each item is a group of cells holding the subreddit, author, title, linked article and comment count. All inputs are optional: `subtopic_ids` filters by news category, `after` pages through results, and `need_format` cleans the data.

### Use cases

- Track which news articles are being shared and discussed on Reddit right now.
- Collect the source domain and link of each news post to see which outlets get traction.
- Compare comment counts across posts to find the most debated current events stories.
- Separate sponsored cells from organic posts when analysing a news feed.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/news-feed" \
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
| `subtopic_ids` | array | No | List of subtopic IDs, default ["all"] means all news categories |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "newsV3": {
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
                "__typename": "MetadataCell",
                "authorName": "u/southpawFA",
                "color": {
                  "__typename": "CustomCellColor",
                  "rgbaColor": "#205493FF"
                },
                "createdAt": "2026-11-02T22:38:45.943000+0000",
                "detailsLink": "politics",
                "detailsString": "r/politics",
                "iconPath": "https://styles.redditmedia.com/t5_2cneq/styles/communityIcon_fy84mdgh75201.jpg?w…",
                "iconShape": "ROUND"
              }
            ],
            "crosspostCells": [
              {
                "__typename": "MetadataCell"
              }
            ],
            "groupId": "t3_1xmbvk3",
            "groupRecommendationContext": null,
            "id": "dDNfMXhtYnZrMw==",
            "payload": null
          }
        }
      ],
      "pageInfo": {
        "endCursor": "dDNfMXhtZXRkeQ=="
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `newsV3.elements.dist` | Number of elements in this page of the feed. |
| `newsV3.elements.edges[].node.groupId` | Post ID of the feed item, for example `t3_1xmbvk3`. |
| `newsV3.elements.edges[].node.cells[].authorName` | Username of the poster, prefixed with `u/`. |
| `newsV3.elements.edges[].node.cells[].detailsString / newsV3.elements.edges[].node.cells[].detailsLink` | Subreddit the post belongs to. `detailsString` is the display form such as `r/politics`, and `detailsLink` is the bare name. |
| `newsV3.elements.edges[].node.cells[].createdAt` | ISO 8601 timestamp of when the post was created. |
| `newsV3.elements.edges[].node.cells[].titleCell.title` | Title of the post. |
| `newsV3.elements.edges[].node.cells[].thumbnail.path` | URL of the news article the post links to. |
| `newsV3.elements.edges[].node.cells[].thumbnail.domain` | Domain of the linked article, such as `lgbtqnation.com`. |
| `newsV3.elements.edges[].node.cells[].commentCount` | Number of comments on the post. It appears in the `ActionCell`. |
| `newsV3.elements.edges[].node.adPayload` | Set to an object when the item is a sponsored ad, and `null` for regular posts. Ad items include fields like `adLinkUrl` and a gallery of products. |

### Notes

- Send `{}` to get the default feed. `subtopic_ids` defaults to `["all"]`.
- Pass the `after` value to request the next page.
- Check `adPayload` and each cell's `__typename` (such as `MetadataCell`, `TitleWithThumbnailCell`, `ActionCell`, `AdGalleryCell`) to tell post cells from ad cells.
- For other feeds, see [Reddit App Popular Feed](/apis/reddit/app/popular-feed) or [Reddit App Home Feed](/apis/reddit/app/home-feed).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/news-feed.json`](../../../../catalog/models/reddit/app/news-feed.json) · Store page: https://www.sandbase.ai/model/reddit/app/news-feed
