# Douyin User Profile by Unique ID API: pricing, parameters and code examples

`douyin/web/user-profile-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns profile details and compilation information for a specified Douyin user account based on their unique identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-profile-v2", "unique_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-profile-v2', {'unique_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-profile-v2", {
  "unique_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-profile-v2", sandbase.Params{
	"unique_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-profile-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `unique_id` | string | yes | User unique_id  |

## Details

Returns the public profile of a Douyin account, including nickname, `sec_uid`, follower-style counts and avatar URLs. It needs one input, the account `unique_id` (the Douyin ID handle).

### Use cases

- Look up the `sec_uid` for a Douyin handle so you can call other user endpoints.
- Check an account's nickname, signature and post count from its `unique_id`.
- Download avatar images for a creator directory.
- Compare `total_favorited` and `following_count` across several accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-profile-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"unique_id": "TheChief"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `unique_id` | string | Yes | User unique_id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "logid": "20261103153238A5DEF746CA9D67CB166D",
    "now": 1793691159083
  },
  "is_oversea": 0,
  "status_code": 0,
  "user_info": {
    "account_cert_info": "{}",
    "avatar_medium": {
      "uri": "aweme-avatar/tos-cn-avt-0015_b864d4d80c09ad5b48591f6e8ebe4732",
      "url_list": [
        "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_b864d4d80c09…"
      ]
    },
    "avatar_thumb": {
      "uri": "aweme-avatar/tos-cn-avt-0015_b864d4d80c09ad5b48591f6e8ebe4732",
      "url_list": [
        "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_b864d4d80c09…"
      ]
    },
    "aweme_count": 6,
    "card_entries": [],
    "custom_verify": "",
    "enterprise_verify_reason": "",
    "favoriting_count": 57000,
    "follow_status": 0,
    "followers_detail": null,
    "following_count": 400,
    "geofencing": null
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user_info.nickname` | Display name of the account. |
| `user_info.unique_id` | The Douyin ID handle you searched for. |
| `user_info.sec_uid` | Encrypted user ID that starts with `MS4w`. Other Douyin user APIs use it to identify the account. |
| `user_info.signature` | Profile bio text. In this response the value is Base64 text with a `B64: ` prefix, so decode it to read the bio. |
| `user_info.aweme_count` | Number of videos posted by the account. |
| `user_info.total_favorited` | Total likes the account has received. It comes back as a string. |
| `user_info.following_count / user_info.favoriting_count` | Number of accounts this user follows and number of videos this user has liked. |
| `user_info.mplatform_followers_count` | Follower count reported under this key name. |
| `user_info.avatar_medium.url_list[] / user_info.avatar_thumb.url_list[]` | Image URLs for the medium and thumbnail avatar. Each list has several mirror URLs for the same image. |
| `status_code` | `0` when the request succeeded. |

### Notes

- Pass the account handle as `unique_id`, for example `TheChief`.
- Use `user_info.sec_uid` from this response as input to [Douyin User Video Posts](/apis/douyin/web/user-post-videos).
- If you only have a profile URL, use [Douyin sec_user_id from URL](/apis/douyin/web/sec-user-id) to get the `sec_user_id`.
- `user_info.mix_info` is `null` in this response, so the account has no compilation data here.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-profile-v2.json`](../../../../catalog/models/douyin/web/user-profile-v2.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-profile-v2
