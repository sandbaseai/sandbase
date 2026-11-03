# Xiaohongshu (RED) User Information API: pricing, parameters and code examples

`xiaohongshu/app-v2/user-info` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns detailed profile data for a Xiaohongshu user. Look up accounts by providing either a specific user identifier or a profile share link.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/user-info", "user_id": "5c668b3e0000000012021605"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/user-info', {'user_id': '5c668b3e0000000012021605'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/user-info", {
  "user_id": "5c668b3e0000000012021605"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/user-info", sandbase.Params{
	"user_id": "5c668b3e0000000012021605",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User ID, e.g. "61b46d790000000010008153" default `""` |
| `share_text` | string |  | Xiaohongshu sharing link (support APP and Web sharing link) default `""` |

## Details

Returns the public profile of a Xiaohongshu (RED) user, including nickname, bio, follower and following counts, like and save totals, avatar images and IP location. Pass either a `user_id` or a Xiaohongshu share link in `share_text`.

### Use cases

- Pull a creator's follower count and total likes to compare accounts before a partnership.
- Resolve a shared `xhslink.com` link into a user profile with a nickname and bio.
- Track a creator's `fans` and `liked` values over time by calling the API on a schedule.
- Collect avatar and banner image URLs to build creator cards in a dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "61b46d790000000010008153", "share_text": "https://xhslink.com/m/3ZSCJZAMz0a"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_text` | string | No | Xiaohongshu sharing link (support APP and Web sharing link) |
| `user_id` | string | No | User ID, e.g. "61b46d790000000010008153" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "avatar_handle_entry_list": [],
    "avatar_like_status": false,
    "avatar_pendant": {
      "current_user_pendant": false,
      "current_user_pet": false
    },
    "banner_info": {
      "bg_color": "c7e6fa",
      "image": "http://sns-avatar-qc.rednotecdn.com/user_banner/default/h240-b100.png?imageView2…",
      "like_status": false
    },
    "block_view_from_user": false,
    "block_view_to_user": false,
    "blocked": false,
    "blocking": false,
    "collected": 48646,
    "collected_book_num": 0,
    "collected_brand_num": 0,
    "collected_movie_num": 0
  },
  "debug_id": "898018b4",
  "debug_info": "gAAAAABq6ZFv5BtK4dso-3h-ngz1foB6gdA6F2YCQNeRx4m40l-FFNMQ02-TZHGXND36iDpfo2CDnftS…",
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.nickname` | Display name of the user. |
| `data.desc` | Bio text the user wrote for their profile. |
| `data.fans / data.follows` | Number of followers and number of accounts the user follows. |
| `data.liked / data.collected` | Total likes and total saves the user's content has received. |
| `data.interactions[]` | Summary counters for the profile header. Each row has `type`, a display `name`, a `count` and an `is_private` flag. The `interaction` row (`Likes & Collects`) gives the combined total. |
| `data.ip_location` | IP-based location label shown on the profile, such as `Beijing`. |
| `data.ndiscovery` | Count of discovery items on the profile. Its exact meaning is not documented, and it is likely the number of published notes. |
| `data.images / data.imageb` | Avatar image URLs. `images` is the smaller version and `imageb` is the larger one. |
| `data.banner_info.image` | URL of the profile banner image. `bg_color` holds its background color. |
| `data.hula_tabs.all_show_tab_config[]` | Tabs shown on the profile page, with `tab_id` and `tab_name`, for example Notes and Saves. |

### Notes

- Send either `user_id` or `share_text`. The example sends both, and `user_id` is a 24-character hex string such as `61b46d790000000010008153`.
- `share_text` accepts a Xiaohongshu app or web share link, for example `https://xhslink.com/m/3ZSCJZAMz0a`.
- A successful call returns `code` `0` and `success` `true`. The profile sits under `data`.
- To list the user's notes, call [Xiaohongshu (RED) User Posted Notes](/apis/xiaohongshu/app-v2/user-posted-notes). For saved notes, call [Xiaohongshu (RED) User Favorited Notes](/apis/xiaohongshu/app-v2/user-faved-notes).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/user-info.json`](../../../../catalog/models/xiaohongshu/app-v2/user-info.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/user-info
