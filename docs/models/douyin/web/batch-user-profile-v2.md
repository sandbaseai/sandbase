# Douyin Batch User Profile (V2) API: pricing, parameters and code examples

`douyin/web/batch-user-profile-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.15 per call · **Modes:** sync

Retrieves user profile details in batches for up to 50 Douyin accounts at once. Pass comma-separated secure user identifiers to return account data.

## Pricing

- **$0.15 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/batch-user-profile-v2", "sec_user_ids": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/batch-user-profile-v2', {'sec_user_ids': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/batch-user-profile-v2", {
  "sec_user_ids": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/batch-user-profile-v2", sandbase.Params{
	"sec_user_ids": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/batch-user-profile-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_user_ids` | string | yes | User sec_user_id list, separated by commas, up to 50  |

## Details

Returns a list of Douyin account profiles, one object per account. The input is `sec_user_ids`, a comma-separated string of up to 50 `sec_user_id` values.

### Use cases

- Pull nicknames, handles and bios for a roster of Douyin creators in one call.
- Check which accounts in a list still use the default avatar or an empty `signature`.
- Map `sec_uid` values to the numeric `uid` and `short_id` of each account.
- Group a list of accounts by `store_region` to see where each one is registered.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/batch-user-profile-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_ids": "MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE,MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_ids` | string | Yes | User sec_user_id list, separated by commas, up to 50 |

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
| `[].sec_uid` | The secure user ID of the account. It matches the value you sent in `sec_user_ids`, so you can join results back to your input. |
| `[].uid / [].short_id` | The numeric user ID and the short ID of the account, both returned as strings. |
| `[].unique_id` | The public Douyin handle of the account. When the owner has not set a custom one, it equals `short_id`. |
| `[].nickname` | The display name of the account. |
| `[].signature` | The bio text of the account. It can be an empty string and can contain line breaks. |
| `[].avatar_thumb.url_list / [].avatar_small.url_list` | Image URLs for the 100x100 and 168x168 avatars. Each list holds several mirror URLs for the same image. |
| `[].store_region` | A region code for the account, such as `cn-hn` or `cn-zj`. |
| `[].verification_type / [].custom_verify / [].enterprise_verify_reason` | Verification data for the account. In this sample the type is `0` and both text fields are empty. |
| `[].follow_status / [].follower_status / [].is_block` | The relation between the calling session and the account. In this sample all are `0` or `false`. |
| `[].with_commerce_entry / [].commerce_user_level` | Commerce flags for the account. In this sample the entry is `false` and the level is `0`. |

### Notes

- The response is a JSON array, not an object. Each item is one account.
- Send up to 50 comma-separated values in `sec_user_ids`. A `sec_user_id` starts with `MS4wLjAB`.
- To get a `sec_user_id` from a homepage link, call [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id). To convert a numeric `uid`, call [Douyin UID to Sec User ID](/apis/douyin/web/encrypt-uid-to-sec-user-id).
- Some fields appear only on some accounts. For example, `bless_end_time`, `im_bubble_id` and `im_bubble_exp` are present for one account and missing for the other.

### Pricing

$0.15 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/batch-user-profile-v2.json`](../../../../catalog/models/douyin/web/batch-user-profile-v2.json) · Store page: https://www.sandbase.ai/model/douyin/web/batch-user-profile-v2
