# Instagram Hashtag Posts (V1) API: pricing, parameters and code examples

`instagram/v1/hashtag-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns public Instagram posts associated with a specific hashtag. Filter by hashtag name and paginate through media results using a cursor.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/hashtag-posts", "hashtag": "veganrecipes"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/hashtag-posts', {'hashtag': 'veganrecipes'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/hashtag-posts", {
  "hashtag": "veganrecipes"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/hashtag-posts", sandbase.Params{
	"hashtag": "veganrecipes",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/hashtag-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `hashtag` | string | yes | Hashtag name (without #)  |
| `end_cursor` | string |  | Pagination cursor, omit for first request  |

## Details

Returns public Instagram posts tagged with a given hashtag, plus basic details about the hashtag itself. It needs one input: the hashtag name without the `#`.

### Use cases

- Pull recent posts under a brand or product hashtag to see how people write about it.
- Collect image URLs and captions from an event hashtag for a content review.
- Read the total post count for a hashtag to compare how widely different topics are used.
- Page through a hashtag feed to build a dataset of captions for text analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/hashtag-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashtag": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag` | string | Yes | Hashtag name (without #) |
| `end_cursor` | string | No | Pagination cursor, omit for first request |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attempts": "70",
  "data": {
    "hashtag": {
      "allow_following": false,
      "edge_hashtag_to_content_advisory": {
        "count": 0,
        "edges": []
      },
      "edge_hashtag_to_media": {
        "count": 2360486,
        "edges": [
          {
            "node": {
              "__typename": "GraphSidecar",
              "accessibility_caption": "Photo by Snap & Hiro on November 02, 2026. May be a meme of gas mask, costume, g…",
              "comments_disabled": false,
              "dimensions": {
                "height": 1080,
                "width": 1080
              },
              "display_url": "https://scontent-cdg4-2.cdninstagram.com/v/t51.82787-15/884791041_18031929077885…",
              "edge_liked_by": {
                "count": 0
              },
              "edge_media_preview_like": {
                "count": 0
              },
              "edge_media_to_caption": {
                "edges": [
                  {
                    "node": {
                      "text": "Too bad for him 👀\n\n(A better version of my previous take)\n\n#openai #ramshortage …"
                    }
                  }
                ]
              }
            }
          }
        ],
        "page_info": {
          "end_cursor": "QVFBeEF1N1otVlBLRElnT3ZuSk1EZnV6NEZUQkY3Rk94VU1lejA2OHljSkFaaFZ5S3owd0cwQVZ4U2hf…",
          "has_next_page": true
        }
      },
      "edge_hashtag_to_null_state": {
        "edges": []
      },
      "edge_hashtag_to_top_posts": {
        "edges": []
      },
      "id": "17841553213093056",
      "is_following": false,
      "is_top_media_only": false,
      "name": "openai",
      "profile_pic_url": "https://scontent-cdg4-2.cdninstagram.com/v/t51.82787-15/882860819_18630928774013…"
    }
  },
  "status": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.hashtag.name / data.hashtag.id` | The hashtag name and its numeric ID. |
| `data.hashtag.edge_hashtag_to_media.count` | Total number of posts that use this hashtag. |
| `data.hashtag.edge_hashtag_to_media.edges[].node.__typename` | Post type. The response shows `GraphImage` for a single image and `GraphSidecar` for a multi-item post. |
| `data.hashtag.edge_hashtag_to_media.edges[].node.edge_media_to_caption.edges[].node.text` | Caption text of the post, including its hashtags. |
| `data.hashtag.edge_hashtag_to_media.edges[].node.accessibility_caption` | Auto-generated text description of the post, with the author name and date. |
| `data.hashtag.edge_hashtag_to_media.edges[].node.display_url` | URL of the post image. |
| `data.hashtag.edge_hashtag_to_media.edges[].node.dimensions.height / data.hashtag.edge_hashtag_to_media.edges[].node.dimensions.width` | Size of the displayed media. |
| `data.hashtag.edge_hashtag_to_media.edges[].node.comments_disabled` | `true` when the author turned off comments on the post. |
| `data.hashtag.edge_hashtag_to_media.page_info.end_cursor` | Cursor to pass as `end_cursor` to get the next page. |
| `data.hashtag.edge_hashtag_to_media.page_info.has_next_page` | `true` when more posts are available. |

### Notes

- Send the hashtag without the leading `#`, for example `openai`.
- Omit `end_cursor` on the first request. For the next page, pass the value of `data.hashtag.edge_hashtag_to_media.page_info.end_cursor`.
- Stop paging when `has_next_page` is `false`.
- In this response, the like counts in `edge_liked_by.count` and `edge_media_preview_like.count` are `0`, so do not rely on them for engagement.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.
- [Instagram Location Posts (V1)](/apis/instagram/v1/location-posts): Returns posts tagged at a designated location.

---
Machine-readable: [`catalog/models/instagram/v1/hashtag-posts.json`](../../../../catalog/models/instagram/v1/hashtag-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v1/hashtag-posts
