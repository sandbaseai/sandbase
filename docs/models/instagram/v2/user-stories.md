# Instagram User Stories (V2) API: pricing, parameters and code examples

`instagram/v2/user-stories` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns active stories posted by an Instagram user within the last 24 hours. The request accepts either an account username or a user identifier.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/user-stories"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/user-stories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/user-stories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/user-stories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/v2/user-stories` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User ID (either username or user_id required)  |
| `username` | string |  | Username (either username or user_id required)  |

## Details

Returns the active stories an Instagram account posted in the last 24 hours. Each story includes image links, expiry times and sharing flags. The input is a `username` or a `user_id`.

### Use cases

- Show the current stories of a brand account in a dashboard or feed.
- Save story image links before the stories expire.
- Check how many stories an account has live and when the newest one was posted.
- Track which stories a verified account allows others to reshare.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/user-stories" \
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
    "additional_data": {
      "ad_expiry_timestamp_in_millis": null,
      "can_gif_quick_reply": true,
      "can_react_with_avatar": false,
      "can_reply": false,
      "can_reshare": true,
      "disabled_reply_types": [
        "story_remix_reply"
      ],
      "expiring_at": 1793742535,
      "id": "25025320",
      "is_archived": false,
      "latest_reel_media": 1793656135,
      "reel_type": "user_reel",
      "show_expiration_tray_signal": false
    },
    "count": 3,
    "items": [
      {
        "archive_story_deletion_ts": 0,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "can_extend_expiration": null,
        "can_hype": false,
        "can_mention_back": false,
        "can_mention_share": false,
        "can_play_spotify_audio": false,
        "can_reply": false,
        "can_reshare": true,
        "can_reshare_to_story": true
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of stories returned in `data.items`. |
| `data.items[].id / data.items[].code` | Story identifiers. `id` is the numeric story ID and `code` is a short alphanumeric code for the same story. |
| `data.items[].expiring_at` | Unix timestamp in seconds that shows when the story expires. |
| `data.items[].device_timestamp` | Timestamp from the posting device. The value is much larger than `expiring_at`, so it is not in seconds. |
| `data.items[].image_versions.items[].url` | Link to an image of the story. |
| `data.items[].image_versions.items[].width / data.items[].image_versions.items[].height` | Pixel size of each image version, so you can pick the size you need. |
| `data.items[].has_audio` | `true` when the story has audio. The field appears only on some items. |
| `data.items[].can_reshare / data.items[].can_reply` | Flags that show whether the story can be reshared or replied to. |
| `data.additional_data.latest_reel_media` | Unix timestamp in seconds of the newest story in the set. |
| `data.additional_data.user.full_name / data.additional_data.user.is_verified` | Display name of the account and whether it is verified. |

### Notes

- Send either `username` or `user_id`. The example response used both values together.
- `data.additional_data.user.id` holds the account ID. Use it as `user_id` in other calls.
- Story links are image versions in `image_versions.items`. Each story lists several sizes.
- To see saved stories that stay on a profile, call [Instagram User Highlights (V2)](/apis/instagram/v2/user-highlights) or [Instagram Highlight Stories](/apis/instagram/v2/highlight-stories).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/user-stories.json`](../../../../catalog/models/instagram/v2/user-stories.json) · Store page: https://www.sandbase.ai/model/instagram/v2/user-stories
