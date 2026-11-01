# Instagram Location Posts (V2)

`instagram/v2/location-posts` · api · Instagram

Returns public Instagram posts tagged at a designated location. Requires a location ID and supports pagination tokens for browsing subsequent results.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/location-posts", "location_id": "331004901"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/location-posts', {'location_id': '331004901'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/location-posts", {
  "location_id": "331004901"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/location-posts", sandbase.Params{
	"location_id": "331004901",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/location-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `location_id` | string | yes | Location ID  |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Retrieve public Instagram posts associated with a specific location by passing `location_id`.

### Use cases

- Discover content tagged at specific venues or geographical spots.
- Track social activity and media from specific locations.
- Monitor visitor media and public posts from travel destinations.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/location-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"location_id": "331004901"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location_id` | string | Yes | Location ID |
| `pagination_token` | string | No | Pagination token from previous response |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "items": [
      {
        "caption_is_edited": false,
        "coauthor_producer_can_see_organic_insights": false,
        "comment_count": 1,
        "device_timestamp": 1791288704181305,
        "disable_caption_and_comment": false,
        "feed_type": "media",
        "filter_type": 0,
        "id": "4001942187585855200",
        "ig_play_count": 90,
        "layout_type": "media_grid",
        "caption": {
          "id": "4001942187585855200",
          "private_reply_status": 0,
          "text": "Вот такая осень в Париже🍂✨",
          "type": 1,
          "user_id": "<user>"
        },
        "clips_metadata": {
          "audio_type": "licensed_music",
          "professional_clips_upsell_type": 0
        },
        "location": {
          "facebook_places_id": 509413279115937,
          "id": "331004901",
          "name": "Paris , Eiffel Tower",
          "short_name": "Paris"
        },
        "user": {
          "account_type": 3,
          "eligible_for_text_app_activation_badge": false,
          "full_name": "Raya",
          "id": "1496267232",
          "profile_pic_id": "3994684519919488052",
          "profile_pic_url": "https://scontent-arn2-1.cdninstagram.com/v/t51.82787-19/825325846_18629745385011…"
        }
      }
    ]
  }
}
```

### Notes

- Obtain `location_id` from location search endpoints.
- Pass `pagination_token` from a previous response to fetch subsequent pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/location-posts.json`](../../../../catalog/models/instagram/v2/location-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v2/location-posts
