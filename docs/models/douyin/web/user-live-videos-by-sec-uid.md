# Douyin User Broadcast Videos API: pricing, parameters and code examples

`douyin/web/user-live-videos-by-sec-uid` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns broadcast video data for a specified Douyin user using their security identifier. Provide the account identifier to inspect streaming content and badge details.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-live-videos-by-sec-uid", "sec_uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-live-videos-by-sec-uid', {'sec_uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-live-videos-by-sec-uid", {
  "sec_uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-live-videos-by-sec-uid", sandbase.Params{
	"sec_uid": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-live-videos-by-sec-uid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_uid` | string | yes | User sec_uid, also called sec_user_id, can be found in the user's homepage link.  |

## Details

Returns a Douyin user's live-streaming profile record for a given `sec_uid`. The response holds the account's display ID, avatar images, live privacy flags, and honor level badges. It needs only the `sec_uid` from the user's homepage link.

### Use cases

- Read the honor level badge of a Douyin account from `badge_image_list` and its `level` value.
- Fetch avatar image URLs in three sizes for a user whose `sec_uid` you already have.
- Check the `display_id` of an account to match a `sec_uid` to its visible Douyin ID.
- Read the live-related permission flags, such as `allow_use_linkmic`, for a streamer account.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-live-videos-by-sec-uid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_uid, also called sec_user_id, can be found in the user's homepage link. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "adversary_authorization_info": 3,
    "adversary_user_status": 1,
    "age_range": 0,
    "allow_be_located": false,
    "allow_find_by_contacts": false,
    "allow_others_download_video": false,
    "allow_others_download_when_sharing_video": false,
    "allow_share_show_profile": false,
    "allow_show_in_gossip": false,
    "allow_show_my_action": false,
    "allow_strange_comment": false,
    "allow_unfollower_comment": false
  },
  "extra": {
    "now": 1793691153681
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.display_id` | The public display ID of the account, for example `Wuf666`. |
| `data.badge_image_list[].content.level` | The honor level shown on the badge. The example value is `21`. |
| `data.badge_image_list[].content.alternative_text` | Text description of the badge. The example reads as an honor level 21 badge. |
| `data.badge_image_list[].url_list` | Image URLs for the badge. Each item in the list points to the same badge image on a different host. |
| `data.badge_image_list_v2` | A second badge list with the same structure as `badge_image_list`. |
| `data.avatar_large.url_list / data.avatar_medium.url_list / data.avatar_thumb.url_list` | Avatar image URLs. The `uri` values show sizes of 1080x1080, 720x720 and 100x100. |
| `data.allow_use_linkmic / data.allow_be_located / data.allow_find_by_contacts` | Boolean privacy and live settings of the account. All are `false` in the example. |
| `data.fans_club.data` | Fans club details for the account, including `club_name` and `level`. The example values are empty or `0`. |
| `data.bottom_entry.schema` | An in-app link for the honor level page in the live room toolbar. |
| `status_code` | Status of the call. `0` in the example response. |

### Notes

- Find `sec_uid` in the user's homepage link. To pull it out of a link, use [Douyin sec_user_id from URL](/apis/douyin/web/sec-user-id).
- Many fields come back empty or as `0` in the example, such as `city`, `birthday` and `create_time`. Treat these as not set.
- For a full account profile, call [Douyin User Profile (Web)](/apis/douyin/web/user-profile).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-live-videos-by-sec-uid.json`](../../../../catalog/models/douyin/web/user-live-videos-by-sec-uid.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-live-videos-by-sec-uid
