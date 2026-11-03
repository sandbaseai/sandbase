# Threads Post Detail (V2) API: pricing, parameters and code examples

`threads/web/post-detail-v2` · data API · Threads · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specific Threads post. Queries can be performed using either a full post link or a post short code as input.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/post-detail-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/post-detail-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/post-detail-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/post-detail-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/threads/web/post-detail-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | Full post URL (optional), for example: https://www.threads.com/@taylorswift/post/DPVUglOjOUu  |
| `post_id` | string |  | Post short code (optional), for example: DPVUglOjOUu, can be extracted from post URL, e.g., DPVUglOjOUu in https://www.threads.com/@taylorswift/post/DPVUglOjOUu  |

## Details

Returns the details of one Threads post, including its caption, media, engagement counts, author, and a list of replies. It needs either a full post link in `url` or the post short code in `post_id`.

### Use cases

- Track the like, reply, and repost counts of a single announcement post over time.
- Download the image URLs from a carousel post for archiving or review.
- Read the top replies to a post to see how an audience reacts.
- Check the author's username and verification status from a shared post link.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/post-detail-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_id": "DPVUglOjOUu", "url": "https://www.threads.com/@taylorswift/post/DPVUglOjOUu"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_id` | string | No | Post short code (optional), for example: DPVUglOjOUu, can be extracted from post URL, e.g., DPVUglOjOUu in https://www.threads.com/@taylorswift/post/DPVUglOjOUu |
| `url` | string | No | Full post URL (optional), for example: https://www.threads.com/@taylorswift/post/DPVUglOjOUu |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "author_thread": [],
  "parent_thread": [],
  "pinned_replies": [],
  "post": {
    "accessibility_caption": null,
    "can_inline_expand_below": false,
    "caption": "I can’t tell you how proud I am to share this with you, an album that just feels…",
    "caption_is_edited": false,
    "carousel_media": [
      {
        "accessibility_caption": null,
        "id": "3734981661403426835_66109110437",
        "image_versions2": {
          "candidates": [
            {
              "height": 1440,
              "url": "https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/558969126_17913678132206…",
              "width": 2159
            }
          ]
        },
        "media_type": 1,
        "original_height": 1440,
        "original_width": 2159,
        "pk": "3734981661403426835",
        "video_versions": []
      }
    ],
    "code": "DPVUglOjOUu",
    "direct_reply_count": 10079,
    "image_versions2": {
      "candidates": [
        {
          "height": 1440,
          "url": "https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/558969126_17913678132206…",
          "width": 2159
        }
      ]
    },
    "is_pinned_to_profile": false,
    "is_post_unavailable": false,
    "is_reply": false,
    "like_count": 139993
  },
  "raw_json_size": 611771,
  "replies": [
    {
      "accessibility_caption": null,
      "can_inline_expand_below": false,
      "caption": "I LOVE YOU SO MUCH TAYLOR!!! THIS ALBUM ASWELL AS ALL YOUR OTHER ALBUMS IS AMAZI…",
      "caption_is_edited": false,
      "carousel_media": [],
      "code": "DPXoFfxjQUQ",
      "direct_reply_count": 0,
      "image_versions2": {
        "candidates": []
      },
      "is_pinned_to_profile": false,
      "is_post_unavailable": false,
      "is_reply": true,
      "like_count": 1
    }
  ],
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `post.caption` | The text of the post. `post.caption_is_edited` shows whether the author edited it. |
| `post.code / post.post_id` | `code` is the short code used in the post link. `post_id` is the long numeric ID of the same post. |
| `post.like_count / post.direct_reply_count / post.quote_count / post.repost_count / post.reshare_count` | Engagement counts for the post: likes, direct replies, quotes, reposts, and reshares. |
| `post.taken_at` | Time the post was published, as a Unix timestamp in seconds. |
| `post.user.username / post.user.full_name / post.user.is_verified` | The author's handle, display name, and verification flag. |
| `post.carousel_media[].image_versions2.candidates[]` | Image files for each carousel item. Each entry has `url`, `width`, and `height`, with several sizes per image. |
| `post.media_type` | A numeric code for the post format. This post has `8` and a `carousel_media` list with 3 images. |
| `replies[]` | Replies to the post. Each item uses the same structure as `post`, with its own `caption`, `like_count`, `code`, and `user`. |
| `replies[].is_reply` | Is `true` for items in the reply list. |
| `author_thread[] / parent_thread[] / pinned_replies[]` | Related thread lists. They are empty in this response. |

### Notes

- Send `post_id` or `url`. The short code is the last part of a post link, for example `DPVUglOjOUu` in `https://www.threads.com/@taylorswift/post/DPVUglOjOUu`.
- The long numeric `post.post_id` differs from the short `post.code`. To look up a post by its numeric ID, use [Threads Post Detail](/apis/threads/web/post-detail).
- To list more posts from the author, call [Threads User Posts](/apis/threads/web/user-posts). For their replies, call [Threads User Replies](/apis/threads/web/user-replies).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Threads Post Detail](/apis/threads/web/post-detail): Returns detailed information for a specific Threads post using its numeric ID.
- [Threads Profile Search](/apis/threads/web/search-profiles): Searches Threads user profiles based on a specified text query string.
- [Threads Recent Content Search](/apis/threads/web/search-recent): Searches recent Threads content matching a specified keyword query.

---
Machine-readable: [`catalog/models/threads/web/post-detail-v2.json`](../../../../catalog/models/threads/web/post-detail-v2.json) · Store page: https://www.sandbase.ai/model/threads/web/post-detail-v2
