# Instagram Hashtag Posts (V3) API: pricing, parameters and code examples

`instagram/v3/hashtag-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Retrieves public posts associated with a specified hashtag. Supports pagination cursors to browse through historical content feeds.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/hashtag-posts", "tag": "veganrecipes"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/hashtag-posts', {'tag': 'veganrecipes'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/hashtag-posts", {
  "tag": "veganrecipes"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/hashtag-posts", sandbase.Params{
	"tag": "veganrecipes",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/hashtag-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tag` | string | yes | Hashtag keyword (without #)  |
| `max_id` | string |  | Pagination cursor from previous response, omit for first request  |

## Details

Returns a page of public Instagram posts that use a given hashtag. Each post includes its caption, like and comment counts, media type, thumbnail, and owner details. The only required input is `tag`, the hashtag without the `#`.

### Use cases

- Collect captions and engagement counts for posts under a branded hashtag campaign.
- List the accounts that post most often under a topic hashtag, using `owner.username`.
- Page through a hashtag feed with `next_max_id` to build a sample of posts on one topic.
- Gather post shortcodes for a hashtag and send them to a post detail API for deeper data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/hashtag-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tag": "cat"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag` | string | Yes | Hashtag keyword (without #) |
| `max_id` | string | No | Pagination cursor from previous response, omit for first request |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 21,
  "items": [
    {
      "caption_text": "#igcats #meow #cat #Catsofinstagram\n#貓",
      "code": "DfRWVkaSnmE",
      "comment_count": 0,
      "id": "4022094181446613380_562740540",
      "is_video": false,
      "like_count": 2,
      "media_type": 1,
      "owner": {
        "full_name": "Takano",
        "is_verified": false,
        "pk": "562740540",
        "username": "takano.snapshot"
      },
      "pk": "4022094181446613380",
      "shortcode": "DfRWVkaSnmE",
      "taken_at": null,
      "thumbnail_url": "https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/888724102_18641860837052…"
    }
  ],
  "more_available": true,
  "next_max_id": "WyJRVkZCVjFkVkxXVXpiemR1Wm1jNFR6UkZZMUU0V0dFMFIwTmtWSE5uUm5NMVdXRkhiVGxVUWpWeFpU…",
  "status": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[]` | List of posts returned for the hashtag on this page. |
| `items[].caption_text` | Caption of the post, including its hashtags and mentions. |
| `items[].code / items[].shortcode` | Short code of the post. Both keys hold the same value in the sample, for example `DfRWVkaSnmE`. |
| `items[].id / items[].pk` | Identifiers of the post. `id` joins the post `pk` and the owner `pk` with an underscore. |
| `items[].like_count / items[].comment_count / items[].view_count` | Number of likes, comments and views on the post. |
| `items[].media_type / items[].is_video` | `is_video` tells you if the post is a video. `media_type` is a numeric type code; the sample shows `1` and `8`. |
| `items[].thumbnail_url / items[].video_url` | URL of the thumbnail image and of the video file. Either one can be `null`. |
| `items[].owner.username / items[].owner.full_name` | Username and display name of the account that posted. |
| `items[].owner.pk / items[].owner.is_verified` | Numeric ID of the account as a string, and whether the account is verified. |
| `more_available / next_max_id` | `more_available` says if more results exist. `next_max_id` is the cursor for the next page. |

### Notes

- Send `tag` without the `#` symbol, for example `cat`.
- For the next page, pass the `next_max_id` value from the response as `max_id`. Omit `max_id` on the first request.
- `taken_at` was `null` in the sample, so do not rely on it for post dates.
- To get more detail on a post, pass its shortcode to [Instagram Post Info by Shortcode](/apis/instagram/v3/post-info-by-code), or read its comments with [Instagram Post Comments (V3)](/apis/instagram/v3/post-comments).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/hashtag-posts.json`](../../../../catalog/models/instagram/v3/hashtag-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v3/hashtag-posts
