# Instagram User Stories (V3) API: pricing, parameters and code examples

`instagram/v3/user-stories` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns active Instagram stories posted by a user within the last 24 hours. Queries data using the target profile username.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-stories", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-stories', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-stories", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-stories", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-stories` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Instagram username (required)  |

## Details

Returns the active Instagram stories a user posted in the last 24 hours. It needs one input, the profile `username`. Each story item includes its type, shortcode, thumbnail and, for videos, a video URL.

### Use cases

- Archive the photo and video URLs of a brand account's current stories before they expire.
- Check whether a profile has posted any story today by reading `count`.
- Separate photo stories from video stories using `story_type` or `is_video` to route media to different processing steps.
- Collect story shortcodes and IDs for a watchlist of accounts and log them over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-stories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username (required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "35c9da38f3372",
  "count": 3,
  "items": [
    {
      "caption_text": null,
      "code": "DfPRX4yNRpE",
      "comment_count": null,
      "expiring_at": null,
      "id": "4021509400575679044_25025320",
      "is_video": false,
      "like_count": null,
      "media_type": 1,
      "owner": {
        "full_name": "Instagram",
        "is_verified": true,
        "pk": "25025320",
        "username": "instagram"
      },
      "pk": "4021509400575679044",
      "shortcode": "DfPRX4yNRpE",
      "story_type": "photo"
    }
  ],
  "reels": {
    "25025320": {
      "items": [
        {
          "caption_text": null,
          "code": "DfPRX4yNRpE",
          "comment_count": null,
          "expiring_at": null,
          "id": "4021509400575679044_25025320",
          "is_video": false,
          "like_count": null,
          "media_type": 1
        }
      ]
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Number of story items returned for the user. |
| `items[].id` | Story ID in the form `<media pk>_<owner pk>`. |
| `items[].pk` | Numeric ID of the story media, as a string. |
| `items[].code / items[].shortcode` | Short code of the story media. Both fields hold the same value in this response. |
| `items[].story_type / items[].is_video / items[].media_type` | Type of the story. `story_type` is `photo` or `video`, `is_video` is a boolean, and `media_type` is `1` for the photo and `2` for the videos in this response. |
| `items[].thumbnail_url` | URL of the preview image for the story. |
| `items[].video_url` | URL of the video file. It is `null` for photo stories. |
| `items[].owner.username / items[].owner.full_name / items[].owner.is_verified` | Username, display name and verified status of the account that posted the story. |
| `items[].owner.pk` | Numeric ID of the account that posted the story. |
| `reels` | Object keyed by the owner's numeric ID, such as `25025320`. Each entry holds an `items` list with the same stories in a shorter form, without media URLs. |

### Notes

- Pass the profile name as `username`, for example `instagram`.
- Fields such as `taken_at`, `expiring_at`, `like_count`, `comment_count` and `view_count` came back as `null` for these stories, so do not rely on them.
- Use [Instagram User Highlights (V3)](/apis/instagram/v3/user-highlights) to get the profile's highlights.
- To get the numeric account ID from a username, call [Instagram User ID Lookup](/apis/instagram/v3/user-id-by-username).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-stories.json`](../../../../catalog/models/instagram/v3/user-stories.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-stories
