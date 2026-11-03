# Instagram User Reposts API: pricing, parameters and code examples

`instagram/v1/user-reposts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a paginated list of reposts and shared media for a specified Instagram account. Includes engagement metrics, captions, and original owner details.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-reposts", "user_id": "25025320"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-reposts', {'user_id': '25025320'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-reposts", {
  "user_id": "25025320"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-reposts", sandbase.Params{
	"user_id": "25025320",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-reposts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `max_id` | string |  | Pagination cursor, omit for first request  |
| `user_id` | string | yes | Instagram user ID  |

## Details

Returns a paginated list of reposted and shared Instagram media for one account. The only required input is the numeric Instagram `user_id`.

### Use cases

- Build a history of the posts and reels an account has reposted.
- Find which creators an account reposts most by reading the co-author entries on each item.
- Compare comment counts across reposted items to see which shared content drew the most discussion.
- Page through an account's full repost list by passing the returned cursor back as `max_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-reposts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Instagram user ID |
| `max_id` | string | No | Pagination cursor, omit for first request |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attempts": "95",
  "items": [
    {
      "accessibility_caption": null,
      "all_previous_submitters": null,
      "are_remixes_crosspostable": true,
      "attribution_content_url": null,
      "audience": null,
      "autodub_status": null,
      "boost_unavailable_identifier": null,
      "boost_unavailable_reason": null,
      "boost_upsell_banner_payload": null,
      "boosted_post_id": null,
      "boosted_status": null,
      "byoa_langs": null
    }
  ],
  "more_available": true,
  "next_max_id": "QVFETDlKMWlrSktSYWhtUVNvMXVKaWtyVFlpNEJ2dUNlcWkya2J6RXdtNzlWSE5vX1lybVlWalg3Q0dV…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[]` | One reposted or shared media item. Each entry is a post, reel, or carousel. |
| `items[].code` | Short code of the post. It is the identifier used in Instagram post URLs. |
| `items[].client_cache_key` | Cache key string for the item. Use it to tell items apart. |
| `items[].comment_count` | Number of comments on the item. |
| `items[].caption.created_at / items[].caption.created_at_utc` | Unix timestamp for the caption. Both fields carry the same value in this response. |
| `items[].caption_is_edited` | Whether the caption was edited after posting. |
| `items[].carousel_media[]` | Slides of a carousel post. Each slide has an `id` and `image_versions2.candidates[]` with image `url`, `width` and `height`. |
| `items[].carousel_media_count` | Total number of slides in a carousel post. It is `null` for non-carousel items. |
| `items[].clips_metadata.audio_type` | Type of audio on a reel, for example `original_sounds`. It is `null` when the item is not a reel. |
| `items[].coauthor_producers[]` | Co-authors of the item. Each entry has `id`, `full_name`, `is_verified`, `is_private` and `profile_pic_url`. |
| `more_available` | `true` when more reposts can be fetched. |
| `next_max_id` | Cursor for the next page. Send it as `max_id` in the next request. |

### Notes

- To get `user_id`, call [Instagram User Info by Username](/apis/instagram/v1/user-info-by-username) with a handle and read the account ID from the result.
- Omit `max_id` on the first call. While `more_available` is `true`, pass `next_max_id` as `max_id` to get the next page.
- Use the `code` value with [Instagram Post Details by ID](/apis/instagram/v1/post-by-id) or the post-by-URL APIs to look up a single item in more detail.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-reposts.json`](../../../../catalog/models/instagram/v1/user-reposts.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-reposts
