# Instagram User Reels (V1) API: pricing, parameters and code examples

`instagram/v1/user-reels` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a paginated list of Instagram Reels associated with a specific user account. Supports custom page sizes and cursor-based navigation.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-reels", "user_id": "25025320"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-reels', {'user_id': '25025320'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-reels", {
  "user_id": "25025320"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-reels", sandbase.Params{
	"user_id": "25025320",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-reels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Count per page, default 12 default `12`; range 1–50 |
| `max_id` | string |  | Pagination cursor, omit for first request  |
| `user_id` | string | yes | Instagram user ID  |

## Details

Returns a paginated list of Reels for one Instagram account. You pass the numeric Instagram `user_id`, and each item in `items` holds a `media` object for one Reel.

### Use cases

- Pull the latest Reels from a creator profile to review their recent video output.
- Build a posting timeline for an account from the caption `created_at` values.
- Page through an account's full Reels history with `max_id` and store the media IDs.
- Check which Reels allow resharing or saving by reading the `can_viewer_reshare` and `can_viewer_save` flags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-reels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Instagram user ID |
| `count` | integer | No | Count per page, default 12 |
| `max_id` | string | No | Pagination cursor, omit for first request |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attempts": "0",
  "items": [
    {
      "media": {
        "are_remixes_crosspostable": true,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": [],
        "can_see_insights_as_brand": false,
        "can_viewer_reshare": true,
        "can_viewer_save": true,
        "caption": {
          "bit_flags": 0,
          "content_type": "comment",
          "created_at": 1793647551,
          "created_at_utc": 1793647551,
          "did_report_as_spam": false,
          "is_covered": false,
          "is_ranked_comment": false,
          "media_id": 4021726163100932870
        }
      }
    }
  ],
  "paging_info": {
    "max_id": "QVFESzFzMkVFcTJZS0NNa3ZiMGktQ2NMaS01N0k2VmlRcTNncm1iZW5DaUlmQ3NNVi1hX0kwc0pFa19W…",
    "more_available": true
  },
  "status": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].media` | One Reel. All other per-Reel fields sit inside this object. |
| `items[].media.caption.media_id` | Numeric ID of the Reel that the caption belongs to. |
| `items[].media.caption.created_at / items[].media.caption.created_at_utc` | Time the caption was created, as a Unix timestamp in seconds. Both fields hold the same value in this response. |
| `items[].media.caption.content_type` | Type of the caption object. It shows `comment` in this response. |
| `items[].media.can_viewer_reshare / items[].media.can_viewer_save` | Booleans that show whether the viewer can reshare or save the Reel. |
| `items[].media.are_remixes_crosspostable` | Boolean that shows whether remixes of the Reel can be crossposted. |
| `paging_info.max_id` | Cursor for the next page. Send it as `max_id` in the next request. |
| `paging_info.more_available` | Boolean that is `true` when more Reels can be fetched with the cursor. |
| `status` | Request status. The value is `ok` on success. |

### Notes

- Omit `max_id` on the first request. For the next page, send the value of `paging_info.max_id`.
- Keep paging while `paging_info.more_available` is `true`.
- `count` sets the page size from 1 to 50 and defaults to 12.
- To find a `user_id` from a username, call [Instagram User Info by Username](/apis/instagram/v1/user-info-by-username).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-reels.json`](../../../../catalog/models/instagram/v1/user-reels.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-reels
