# Instagram User Reels (V3) API: pricing, parameters and code examples

`instagram/v3/user-reels` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns a list of Reels for a specific Instagram user. Supports cursor-based forward and backward pagination alongside page size limits.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-reels", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-reels', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-reels", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-reels", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-reels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `last` | integer |  | Reels per page for backward pagination, use with `before`  |
| `after` | string |  | Forward pagination cursor, from previous response `data.page_info.end_cursor`  |
| `first` | integer |  | Reels per page for forward pagination (default 12, max 50) default `12`; range 1–50 |
| `before` | string |  | Backward pagination cursor, from previous response `data.page_info.start_cursor`  |
| `username` | string | yes | Instagram username (required)  |
| `page_size` | integer |  | Videos per page (default 12) default `12` |

## Details

Returns a page of Reels for one Instagram account. Each Reel includes its caption, like, comment and view counts, a thumbnail URL and a video URL. The only required input is `username`.

### Use cases

- Compare likes, comments and views across an account's recent Reels to find its best performers.
- Collect Reel captions to check which topics, hashtags and mentions a brand uses.
- Page through a creator's Reel history and save the `video_url` and `thumbnail_url` of each clip.
- Build a list of Reel shortcodes and pass them to a post details API for deeper checks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-reels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username (required) |
| `after` | string | No | Forward pagination cursor, from previous response `data.page_info.end_cursor` |
| `before` | string | No | Backward pagination cursor, from previous response `data.page_info.start_cursor` |
| `first` | integer | No | Reels per page for forward pagination (default 12, max 50) |
| `last` | integer | No | Reels per page for backward pagination, use with `before` |
| `page_size` | integer | No | Videos per page (default 12) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "37c234b2a69a8",
  "count": 12,
  "data": {
    "xdt_api__v1__clips__user__connection_v2": {
      "edges": [
        {
          "node": {
            "caption_text": "@troyesivan's advice? Go make music in your bedroom 🎶\n\n“Making music at home is …",
            "code": "DfQCqMnhpsG",
            "comment_count": 3330,
            "id": "4021726163100932870_25025320",
            "is_video": true,
            "like_count": 145724,
            "media_type": 2,
            "owner": {
              "full_name": "Instagram",
              "is_verified": true,
              "pk": "25025320",
              "username": "instagram"
            }
          }
        }
      ],
      "page_info": {
        "end_cursor": "QVFBU2V5Wm9UcW5ORFZHNkV6QzFtamtwbU9jNjJZRmtlbzR0eFBXVW5DVlZHQmljdTFNR24tNjlUVi1p…",
        "has_next_page": true
      }
    }
  },
  "edges": [
    {
      "node": {
        "caption_text": "@troyesivan's advice? Go make music in your bedroom 🎶\n\n“Making music at home is …",
        "code": "DfQCqMnhpsG",
        "comment_count": 3330,
        "id": "4021726163100932870_25025320",
        "is_video": true,
        "like_count": 145724,
        "media_type": 2,
        "owner": {
          "full_name": "Instagram",
          "is_verified": true,
          "pk": "25025320",
          "username": "instagram"
        }
      }
    }
  ],
  "items": [
    {
      "caption_text": "@troyesivan's advice? Go make music in your bedroom 🎶\n\n“Making music at home is …",
      "code": "DfQCqMnhpsG",
      "comment_count": 3330,
      "id": "4021726163100932870_25025320",
      "is_video": true,
      "like_count": 145724,
      "media_type": 2,
      "owner": {
        "full_name": "Instagram",
        "is_verified": true,
        "pk": "25025320",
        "username": "instagram"
      },
      "pk": "4021726163100932870",
      "shortcode": "DfQCqMnhpsG",
      "taken_at": null,
      "thumbnail_url": "https://scontent-mia5-2.cdninstagram.com/v/t51.82787-15/883416041_18810804649001…"
    }
  ],
  "next_max_id": "QVFBU2V5Wm9UcW5ORFZHNkV6QzFtamtwbU9jNjJZRmtlbzR0eFBXVW5DVlZHQmljdTFNR24tNjlUVi1p…",
  "page_info": {
    "end_cursor": "QVFBU2V5Wm9UcW5ORFZHNkV6QzFtamtwbU9jNjJZRmtlbzR0eFBXVW5DVlZHQmljdTFNR24tNjlUVi1p…",
    "has_next_page": true
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].caption_text` | Caption of the Reel. Long captions are cut in the response. |
| `items[].code / items[].shortcode` | Short code of the Reel. It is the same value in both fields and appears in the Reel's Instagram URL. |
| `items[].id / items[].pk` | `id` is the media ID with the owner's ID added after an underscore. `pk` is the same media ID without that suffix. |
| `items[].like_count / items[].comment_count / items[].view_count` | Number of likes, comments and views on the Reel. |
| `items[].video_url / items[].thumbnail_url` | Links to the video file and to a still image of the Reel. |
| `items[].owner.username / items[].owner.full_name / items[].owner.is_verified` | Username, display name and verified status of the account that posted the Reel. |
| `items[].owner.pk` | Numeric ID of the account that owns the Reel, as a string. |
| `items[].taken_at` | Posting time field. It was `null` in this response, so do not rely on it. |
| `page_info.end_cursor / page_info.has_next_page` | `end_cursor` is the cursor for the next page. `has_next_page` is `true` when more Reels are available. |
| `data.xdt_api__v1__clips__user__connection_v2.edges[].node` | The same Reels in a nested format with fewer fields. The flat `items` list has more fields, such as `view_count` and `video_url`. |

### Notes

- To get the next page, send `page_info.end_cursor` as `after`. The top-level `next_max_id` holds the same value.
- Use `first` to set the page size, from 1 to 50. The default is 12.
- The `data.page_info.start_cursor` mentioned for `before` was not in this response. Backward paging with `before` and `last` needs a `start_cursor` value.
- To look up the account behind a Reel, use [Instagram User Profile (V3)](/apis/instagram/v3/user-profile). For regular posts instead of Reels, use [Instagram User Posts (V3)](/apis/instagram/v3/user-posts).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-reels.json`](../../../../catalog/models/instagram/v3/user-reels.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-reels
