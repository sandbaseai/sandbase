# Douyin Batch User Profile API: pricing, parameters and code examples

`douyin/web/batch-user-profile-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieves public profile information for multiple Douyin accounts in a single request. Specify up to 10 user IDs to return user details in batch.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/batch-user-profile-v1", "sec_user_ids": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/batch-user-profile-v1', {'sec_user_ids': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/batch-user-profile-v1", {
  "sec_user_ids": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/batch-user-profile-v1", sandbase.Params{
	"sec_user_ids": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/batch-user-profile-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_user_ids` | string | yes | User sec_user_id list, separated by commas, up to 10  |

## Details

Returns public profile details for up to 10 Douyin accounts in one call. The input is a comma-separated string of `sec_user_ids`. The response is a list with one object per account.

### Use cases

- Fill a creator database with nicknames, bios and avatars for a list of Douyin accounts.
- Check whether a set of accounts has changed its `nickname`, `signature` or `unique_id`.
- Match accounts across systems using `uid`, `short_id` and `sec_uid`.
- Screen a list of accounts for verification or commerce status before outreach.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/batch-user-profile-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_ids": "MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE,MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_ids` | string | Yes | User sec_user_id list, separated by commas, up to 10 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "account_cert_info": "{}",
    "avatar_signature": "",
    "avatar_small": {
      "uri": "168x168/aweme-avatar/tos-cn-avt-0015_d8306450a4b1f0a9992ce420b7468b0b",
      "url_list": [
        "https://p11.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_d8306450a4b1f0a9992ce…"
      ]
    },
    "avatar_thumb": {
      "uri": "100x100/aweme-avatar/tos-cn-avt-0015_d8306450a4b1f0a9992ce420b7468b0b",
      "url_list": [
        "https://p11.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_d8306450a4b…"
      ]
    },
    "birthday_hide_level": 1,
    "commerce_user_level": 0,
    "custom_verify": "",
    "enterprise_verify_reason": "",
    "follow_status": 0,
    "follower_status": 0,
    "has_e_account_role": false,
    "im_activeness": 1
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `nickname` | Display name of the account. |
| `signature` | Bio text written by the user. It can be an empty string. |
| `sec_uid` | Encrypted user ID. It matches the value you sent in `sec_user_ids`. |
| `uid / short_id / unique_id` | Other identifiers for the account. `uid` is the numeric user ID. `unique_id` is the public Douyin ID, and it can equal `short_id` when the user has not set a custom one. |
| `avatar_thumb.url_list[] / avatar_small.url_list[]` | Avatar image URLs at 100x100 and 168x168 sizes. Each list holds several mirror URLs for the same image. |
| `store_region` | Region code stored for the account, such as `cn-hn` or `cn-zj`. |
| `verification_type / custom_verify / enterprise_verify_reason` | Verification state and any verification text. In this response they are `0` and empty strings. |
| `commerce_user_level / with_commerce_entry` | Commerce level of the account and whether it shows a commerce entry. |
| `follow_status / follower_status / is_block` | Relationship flags between the account and the calling session. They are `0` or `false` in this response. |

### Notes

- Pass `sec_user_ids` as one string with IDs separated by commas. The limit is 10 IDs per request.
- If you only have profile URLs, get the IDs first with [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id).
- If you only have a numeric `uid`, convert it with [Douyin UID to Sec User ID](/apis/douyin/web/encrypt-uid-to-sec-user-id).
- This response has no follower counts or video counts. Use [Douyin User Profile (Web)](/apis/douyin/web/user-profile) for a single account in more detail.

### Pricing

$0.03 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/batch-user-profile-v1.json`](../../../../catalog/models/douyin/web/batch-user-profile-v1.json) · Store page: https://www.sandbase.ai/model/douyin/web/batch-user-profile-v1
