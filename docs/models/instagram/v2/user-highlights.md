# Instagram User Highlights (V2) API: pricing, parameters and code examples

`instagram/v2/user-highlights` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns an Instagram user's list of highlights and saved story collections. Query using either a target user ID or account username.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/user-highlights", "user_id": "18527", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/user-highlights', {'user_id': '18527', 'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/user-highlights", {
  "user_id": "18527",
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/user-highlights", sandbase.Params{
	"user_id": "18527",
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/user-highlights` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User ID (either username or user_id required)  |
| `username` | string |  | Username (either username or user_id required)  |

## Details

Returns the list of story highlights on a public Instagram profile, with title, cover image, item count and timestamps for each one. Send either `username` or `user_id`.

### Use cases

- List every highlight title and cover image to show a profile's highlight row in a custom viewer.
- Compare `media_count` across highlights to see which collections hold the most stories.
- Track `updated_timestamp` over time to detect when an account adds to or edits a highlight.
- Collect highlight IDs for an account, then fetch the stories inside each one.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/user-highlights" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram", "user_id": "18527"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | No | User ID (either username or user_id required) |
| `username` | string | No | Username (either username or user_id required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "count": 7,
    "highlights_tray_type": "DEFAULT",
    "items": [
      {
        "can_gif_quick_reply": true,
        "can_react_with_avatar": false,
        "can_reply": false,
        "can_reshare": true,
        "contains_stitched_media_blocked_by_rm": false,
        "cover_media": {
          "crop_rect": null,
          "cropped_image_version": {
            "height": 150,
            "url": "https://scontent-iad3-1.cdninstagram.com/v/t51.71878-15/756700225_16539857623317…",
            "width": 150
          },
          "full_image_version": {
            "height": 1080,
            "url": "https://scontent-iad3-1.cdninstagram.com/v/t51.71878-15/756700225_16539857623317…",
            "width": 1080
          },
          "id": "None",
          "upload_id": null
        },
        "created_at": 1719606671,
        "highlight_pog_unseen": null,
        "highlight_reel_type": "DEFAULT",
        "id": "highlight:18223279177302854",
        "is_archived": false,
        "is_converted_to_clips": false
      }
    ]
  },
  "pagination_token": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of highlights returned for the account. |
| `data.items[].id` | Highlight ID in the form `highlight:<number>`. |
| `data.items[].title` | Name of the highlight as shown under the profile. |
| `data.items[].media_count` | Number of stories inside the highlight. |
| `data.items[].cover_media.cropped_image_version.url / data.items[].cover_media.full_image_version.url` | Cover image URLs. The cropped version is 150 by 150 pixels and the full version is 1080 by 1080 pixels. |
| `data.items[].created_at / data.items[].updated_timestamp / data.items[].latest_reel_media` | Unix timestamps in seconds. They mark when the highlight was created, when it was last updated, and its latest story media. |
| `data.items[].is_pinned_highlight` | Whether the highlight is pinned on the profile. |
| `data.items[].user.id / data.items[].user.full_name` | ID and display name of the account that owns the highlight. |
| `data.items[].user.is_verified / data.items[].user.is_private` | Whether the owner account is verified and whether it is private. |

### Notes

- Pass `username` or `user_id`. The request needs at least one of them.
- The response has a `pagination_token` field, and it is `null` in this example.
- Highlight IDs look like `highlight:18223279177302854`. Use them with [Instagram Highlight Stories](/apis/instagram/v2/highlight-stories) to get the stories inside a highlight.
- To find a `user_id` from a name, call [Instagram User Profile](/apis/instagram/v2/user-info).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/user-highlights.json`](../../../../catalog/models/instagram/v2/user-highlights.json) · Store page: https://www.sandbase.ai/model/instagram/v2/user-highlights
