# Douyin User Profile Details API: pricing, parameters and code examples

`douyin/web/user-profile-v3` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns profile information and badges for a specified Douyin user using their account identifier. Query by providing the user's short ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-profile-v3", "uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-profile-v3', {'uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-profile-v3", {
  "uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-profile-v3", sandbase.Params{
	"uid": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-profile-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User uid, which is the short_id of the Douyin number  |

## Details

Returns profile details and badge data for a Douyin account. It needs one input, `uid`, which is the short ID of the Douyin number.

### Use cases

- Check whether a Douyin account carries an enterprise verification label before you work with it.
- Download an account's avatar in 100x100, 720x720 or 1080x1080 size.
- Read the public display ID (`display_id`) for a known short ID.
- Check the honor level badges shown on a creator's account.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-profile-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "92769419069"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User uid, which is the short_id of the Douyin number |

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
    "now": 1793691155539
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.display_id` | The account's public display ID, for example `dyczxzs`. |
| `data.authentication_info.enterprise_verify_reason` | The text of the enterprise verification label. In this response it reads as an official account of the Douyin creator center. |
| `data.authentication_info.authentication_badge.uri` | Path of the verification badge icon. It is not a full URL. |
| `data.avatar_large.url_list[] / data.avatar_medium.url_list[] / data.avatar_thumb.url_list[]` | Image URLs for the avatar in 1080x1080, 720x720 and 100x100 sizes. Each list holds several mirror URLs for the same image. |
| `data.badge_image_list[].content.alternative_text` | Text description of a badge. In this response it describes an honor level 0 badge. |
| `data.badge_image_list[].content.level` | Numeric level of the badge. |
| `data.badge_image_list_v2[]` | A second badge list with the same structure as `badge_image_list`. |
| `data.allow_strange_comment / data.allow_unfollower_comment / data.allow_others_download_video` | Boolean privacy and permission flags for the account. All are `false` in this response. |
| `data.create_time / data.birthday / data.city` | Account creation time, birthday and city. They are `0` or empty in this response, so expect blanks for some accounts. |

### Notes

- Pass the account's short ID as `uid`. It is a string, for example `92769419069`.
- Many profile fields come back as `0`, `false` or an empty string. Check for empty values before you use them.
- To work with a `sec_user_id` instead, call [Douyin UID to Sec User ID](/apis/douyin/web/encrypt-uid-to-sec-user-id).
- To look up several accounts in one call, use [Douyin Batch User Profile](/apis/douyin/web/batch-user-profile-v1).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-profile-v3.json`](../../../../catalog/models/douyin/web/user-profile-v3.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-profile-v3
