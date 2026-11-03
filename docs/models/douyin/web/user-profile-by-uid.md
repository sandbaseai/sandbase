# Douyin User Profile by UID API: pricing, parameters and code examples

`douyin/web/user-profile-by-uid` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns public profile details, badge lists, and account metadata for a Douyin web user by querying their unique identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-profile-by-uid", "uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-profile-by-uid', {'uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-profile-by-uid", {
  "uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-profile-by-uid", sandbase.Params{
	"uid": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-profile-by-uid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User UID  |

## Details

Returns public profile details for a Douyin user, including avatar images, verification info, badge lists, and account settings flags. It needs one input, the numeric `uid` of the user.

### Use cases

- Fetch the avatar image URLs and `display_id` of a Douyin account to show it in a dashboard.
- Check the verification text in `authentication_info.enterprise_verify_reason` to see whether an account is marked as an official account.
- Read the badge lists to see which honor level badge a Douyin user shows.
- Check the privacy and permission flags, such as whether others can download the user's videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-profile-by-uid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "92769419069"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User UID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "adversary_authorization_info": 1,
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
    "now": 1793691154704
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.display_id` | Public display ID of the account, such as `dyczxzs` in the example. |
| `data.authentication_info.enterprise_verify_reason` | Verification text shown for the account. In the example it reads as an official account of the Douyin creator center. |
| `data.authentication_info.custom_verify / data.authentication_info.account_cert_info` | Other verification text fields. They are empty strings in the example. |
| `data.avatar_large.url_list[] / data.avatar_medium.url_list[] / data.avatar_thumb.url_list[]` | Avatar image URLs at 1080x1080, 720x720 and 100x100 sizes. Each list holds several mirror URLs for the same image. |
| `data.badge_image_list[].content.alternative_text` | Text description of a badge. The example reads as an honor level 0 badge. |
| `data.badge_image_list[].content.level` | Level number of the badge. |
| `data.badge_image_list_v2[]` | Second badge list with the same structure as `badge_image_list`. |
| `data.allow_others_download_video / data.allow_strange_comment / data.allow_unfollower_comment` | Boolean flags for what other users may do with this account, such as downloading videos or commenting. |
| `data.city / data.constellation / data.birthday_description` | Location and personal text fields. They are empty in the example, so expect blanks when the user has not set them. |
| `extra.now` | Numeric timestamp of the response. The example value looks like Unix time in milliseconds. |

### Notes

- Pass the numeric `uid` as a string, for example `92769419069`.
- If you only have a `sec_user_id`, or need to convert between ID types, use [Douyin UID to Sec User ID](/apis/douyin/web/encrypt-uid-to-sec-user-id).
- To look up several users in one call, use [Douyin Batch User Profile](/apis/douyin/web/batch-user-profile-v1).
- `status_code` is `0` in a successful response.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-profile-by-uid.json`](../../../../catalog/models/douyin/web/user-profile-by-uid.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-profile-by-uid
