# TikTok User Profile Details API: pricing, parameters and code examples

`tiktok/app-v3/user-profile` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns profile information for a specified TikTok user. Lookups can be performed using a numeric user ID, username, or sec_user_id.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-profile", "unique_id": "srlechuza2.0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-profile', {'unique_id': 'srlechuza2.0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-profile", {
  "unique_id": "srlechuza2.0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-profile", sandbase.Params{
	"unique_id": "srlechuza2.0",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User uid, optional parameter, pure number, if used, please keep sec_user_id and unique_id empty. default `""` |
| `unique_id` | string |  | User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user information, unique_id is also the user's username, if used, please keep sec_user_id and user_id empty. default `""` |
| `sec_user_id` | string |  | User sec_user_id default `""` |

## Details

Returns the public profile of one TikTok account, including nickname, follower and following counts, video count, verification label and avatar image URLs. You pass one identifier: `sec_user_id`, `unique_id` (the username) or `user_id`.

### Use cases

- Track the `follower_count` and `aweme_count` of a creator or brand account over time.
- Check whether an account is verified and which category label it carries before a partnership.
- Download avatar images and the bio link of an account for a profile card or a CRM record.
- Confirm that a `sec_user_id` belongs to the expected account by checking its `nickname`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | No | User sec_user_id |
| `unique_id` | string | No | User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user information, unique_id is also the user's username, if used, please keep sec_user_id and user_id empty. |
| `user_id` | string | No | User uid, optional parameter, pure number, if used, please keep sec_user_id and unique_id empty. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "2026110307440258124FAE33158303128D",
    "now": 1793691843000
  },
  "log_pb": {
    "impr_id": "2026110307440258124FAE33158303128D"
  },
  "status_code": 0,
  "status_msg": "",
  "user": {
    "account_labels": [
      {
        "content": "Artist",
        "label_type": 3
      }
    ],
    "account_type": 3,
    "ad_virtual": false,
    "avatar_168x168": {
      "uri": "tos-useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a",
      "url_list": [
        "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691…"
      ],
      "url_prefix": null
    },
    "avatar_300x300": {
      "uri": "tos-useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a",
      "url_list": [
        "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691…"
      ],
      "url_prefix": null
    },
    "avatar_larger": {
      "uri": "tos-useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a",
      "url_list": [
        "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691…"
      ],
      "url_prefix": null
    },
    "avatar_medium": {
      "uri": "tos-useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a",
      "url_list": [
        "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691…"
      ],
      "url_prefix": null
    },
    "avatar_thumb": {
      "uri": "tos-useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a",
      "url_list": [
        "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691…"
      ],
      "url_prefix": null
    },
    "aweme_count": 1601,
    "bio_secure_url": "https://www.tiktoklinksafety.us/link/v2?aid=1233&lang=en&scene=bio_url&target=ti…",
    "bio_url": "tiktok.com/discovermore",
    "biz_account_info": {
      "added_contact_and_link_list": null,
      "android_download_app_link": "",
      "coupon_list": null,
      "ios_download_app_link": "",
      "leads_gen": {
        "action_name": "",
        "business_data": "",
        "has_leads_gen": false,
        "page_id": 0,
        "schema_url": ""
      },
      "permission_list": [
        "017002"
      ],
      "rba_user_info": {
        "company_name": "TikTok"
      }
    }
  },
  "version": "v2"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user.nickname` | Display name of the account. |
| `user.follower_count / user.following_count` | Number of followers the account has and number of accounts it follows. |
| `user.aweme_count` | Number of videos posted by the account. |
| `user.enterprise_verify_reason` | Verification text shown on the account, for example `Verified account`. |
| `user.account_labels[].content` | Label shown on the account, for example `Artist`. |
| `user.category` | Category of the account, for example `Others`. |
| `user.bio_url` | Link shown in the profile bio. `user.bio_secure_url` holds the same link wrapped in a TikTok link safety redirect. |
| `user.avatar_larger.url_list[] / user.avatar_medium.url_list[] / user.avatar_thumb.url_list[]` | Avatar image URLs in large, medium and thumbnail sizes. Each list has several URLs for the same image. |
| `user.original_musician.music_count` | Number of original sounds credited to the account. |
| `user.privacy_setting.following_visibility` | Setting that controls who can see the account's following list. The response shows only the value `1`. |

### Notes

- Send only one of `sec_user_id`, `unique_id` or `user_id`. Leave the other two empty.
- `unique_id` is the username, for example `tiktok`. If you only have a username and need the IDs, call [TikTok User ID by Username](/apis/tiktok/app-v3/user-id-and-sec-user-id-by-username).
- To list the videos of the account, call [TikTok User Videos (App V3)](/apis/tiktok/app-v3/user-post-videos) with the same `sec_user_id`.
- `status_code` is `0` when the lookup works. The profile data sits under `user`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-profile.json`](../../../../catalog/models/tiktok/app-v3/user-profile.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-profile
