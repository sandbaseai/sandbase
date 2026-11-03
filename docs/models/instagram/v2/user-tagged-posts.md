# Instagram User Tagged Posts (V2) API: pricing, parameters and code examples

`instagram/v2/user-tagged-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns posts where a specified Instagram account has been tagged by other users. Supports looking up accounts by identifier or username, with pagination handling.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/user-tagged-posts"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/user-tagged-posts', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/user-tagged-posts", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/user-tagged-posts", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/v2/user-tagged-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User ID (either username or user_id required)  |
| `username` | string |  | Username (either username or user_id required)  |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Returns a page of Instagram posts where a given account is tagged. You pass either a `username` or a `user_id`. The response includes post details, a `total` count, and a `pagination_token` for the next page.

### Use cases

- Find user-generated posts that tag a brand account.
- Rank tagged posts by `comment_count` to spot the ones that drew the most discussion.
- Pull the `caption.hashtags` from tagged posts to see which hashtags people use with a brand.
- Download image URLs from tagged posts for a content review.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/user-tagged-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram", "user_id": "18527"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `pagination_token` | string | No | Pagination token from previous response |
| `user_id` | string | No | User ID (either username or user_id required) |
| `username` | string | No | Username (either username or user_id required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "count": 21,
    "items": [
      {
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "can_reshare": true,
        "can_save": true,
        "can_viewer_add_media_to_grid": false,
        "caption": {
          "content_type": "comment",
          "created_at": 1582576667,
          "created_at_utc": 1582576667,
          "did_report_as_spam": false,
          "has_translation": true,
          "hashtags": [],
          "id": "2251138696266127152",
          "is_covered": false
        },
        "caption_is_edited": false,
        "coauthor_producer_can_see_organic_insights": false,
        "coauthor_producers": [],
        "code": "B89prebFBcw",
        "collaborator_edit_eligibility": false
      }
    ],
    "total": 130
  },
  "pagination_token": "Ck1JBBkp…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.total` | Total number of tagged posts reported for the account. |
| `data.count` | Number of posts returned in this page. |
| `data.items[].id` | Numeric ID of the post. |
| `data.items[].code` | Short code of the post. It is the same kind of value used in Instagram post URLs. |
| `data.items[].caption.created_at` | Unix timestamp for when the caption was created. `created_at_utc` holds the same value in the sample. |
| `data.items[].caption.hashtags` | List of hashtags in the caption, with the `#` sign. |
| `data.items[].comment_count` | Number of comments on the post. |
| `data.items[].image_versions.items[].url / width / height` | URL and pixel size of each image version of the post. |
| `data.items[].can_reshare / can_save` | Flags for whether the post can be reshared or saved. |
| `pagination_token` | Token to send in the next request to get the next page. |

### Notes

- Send either `username` or `user_id`. The example request sends both.
- To get the next page, send the returned `pagination_token` with the same account value.
- Captions are returned as a nested object, so read the text and timestamps from `caption`.
- To open one post in full, call [Instagram Post Details (V2)](/apis/instagram/v2/post-info). For the comments on a post, use [Instagram Post Comments (V2)](/apis/instagram/v2/post-comments).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/user-tagged-posts.json`](../../../../catalog/models/instagram/v2/user-tagged-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v2/user-tagged-posts
