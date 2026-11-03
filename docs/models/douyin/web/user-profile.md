# Douyin User Profile (Web) API: pricing, parameters and code examples

`douyin/web/user-profile` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns profile details for a specified Douyin user using their secure user identifier. Retrieve account information such as user cover URLs by providing a sec_user_id.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-profile", "sec_user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-profile', {'sec_user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-profile", {
  "sec_user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-profile", sandbase.Params{
	"sec_user_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_user_id` | string | yes | User sec_user_id  |

## Details

Returns the public profile of one Douyin account, including avatar images, cover images, video count and follower count. It needs one input, the account's `sec_user_id`.

### Use cases

- Show a Douyin creator's follower count and video count in a dashboard.
- Download a creator's avatar and profile cover images for a report or media kit.
- Check whether a creator appears in a Douyin ranking by reading the `user.dog_card_info` block.
- Track how `user.follower_count` changes for an account over time by calling the API on a schedule.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | Yes | User sec_user_id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153241C7B606B0314B371AFCD7",
    "now": 1793691161000
  },
  "log_pb": {
    "impr_id": "20261103153241C7B606B0314B371AFCD7"
  },
  "status_code": 0,
  "status_msg": null,
  "user": {
    "account_cert_info": "{}",
    "apple_account": 0,
    "avatar_168x168": {
      "height": 720,
      "uri": "aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c745843",
      "url_list": [
        "https://p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd…"
      ],
      "width": 720
    },
    "avatar_300x300": {
      "height": 720,
      "uri": "aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c745843",
      "url_list": [
        "https://p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd…"
      ],
      "width": 720
    },
    "avatar_larger": {
      "height": 720,
      "uri": "aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c745843",
      "url_list": [
        "https://p3-pc.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_9186d2f…"
      ],
      "width": 720
    },
    "avatar_medium": {
      "height": 720,
      "uri": "aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c745843",
      "url_list": [
        "https://p3-pc.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_9186d2f6f…"
      ],
      "width": 720
    },
    "avatar_thumb": {
      "height": 720,
      "uri": "aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c745843",
      "url_list": [
        "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_9186d2f6f…"
      ],
      "width": 720
    },
    "aweme_count": 91,
    "aweme_count_correction_threshold": -1,
    "birthday_hide_level": 0,
    "can_set_item_cover": false,
    "can_show_group_card": 1
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user.follower_count` | Number of followers the account has. |
| `user.aweme_count` | Number of videos the account has posted. |
| `user.avatar_thumb / user.avatar_168x168 / user.avatar_300x300 / user.avatar_medium / user.avatar_larger` | Avatar image in different sizes. Each has `url_list` with image links, plus `width`, `height` and `uri`. |
| `user.cover_url[].url_list` | Links to the profile cover images. Each entry in `cover_url` has its own `uri` and `url_list`. |
| `user.cover_and_head_image_info.profile_cover_list[].cover_url.url_list` | Links to the profile cover image, repeated inside the cover info block. |
| `user.cover_and_head_image_info.profile_cover_list[].dark_cover_color / user.cover_and_head_image_info.profile_cover_list[].light_cover_color` | Color codes for the cover, written as hex strings. |
| `user.dog_card_info.dog_card_text / user.dog_card_info.rank / user.dog_card_info.rank_type` | Ranking label shown on the profile, with the rank number and rank type. In the example the text is `短剧最热榜`, the rank is `11` and the type is `hot`. |
| `user.follow_status` | Follow state value for the account. The example returns `0`. |
| `status_code` | Result code for the call. `0` appears in the example response. |

### Notes

- Pass `sec_user_id` as a string. It starts with `MS4wLjABAAAA` in the example.
- Image links in `cover_url` carry `x-expires` and `x-signature` query values, so download them soon after you call the API.
- If you only have a profile page link, call [Douyin sec_user_id from URL](/apis/douyin/web/sec-user-id) first to get the `sec_user_id`.
- To profile many accounts in one call, use [Douyin Batch User Profile](/apis/douyin/web/batch-user-profile-v1).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-profile.json`](../../../../catalog/models/douyin/web/user-profile.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-profile
