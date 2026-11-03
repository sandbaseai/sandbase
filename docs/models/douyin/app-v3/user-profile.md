# Douyin User Profile (App V3) API: pricing, parameters and code examples

`douyin/app-v3/user-profile` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns profile information and follower statistics for a specified Douyin user based on their unique secure user identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/user-profile", "sec_user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/user-profile', {'sec_user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/user-profile", {
  "sec_user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/user-profile", sandbase.Params{
	"sec_user_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_user_id` | string | yes | User sec_user_id  |

## Details

Returns profile data for one Douyin user, including avatar images, cover images, video count and follower count. It needs the user's `sec_user_id`.

### Use cases

- Track the `follower_count` of a creator over time to measure audience growth.
- Check how many videos an account has published with `aweme_count` before pulling its video list.
- Download avatar and profile cover images for a creator database or review dashboard.
- Check whether an account has an ads entry in its commerce settings.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/user-profile" \
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
    "fatal_item_ids": null,
    "logid": "202611031531419AC4E1CB78CA9D11D6BF",
    "now": 1793691101000,
    "search_request_id": null
  },
  "log_pb": {
    "impr_id": "202611031531419AC4E1CB78CA9D11D6BF"
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
        "https://p3.douyinpic.com/aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c…"
      ],
      "width": 720
    },
    "avatar_300x300": {
      "height": 720,
      "uri": "aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c745843",
      "url_list": [
        "https://p3.douyinpic.com/aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c…"
      ],
      "width": 720
    },
    "avatar_is_digged": false,
    "avatar_larger": {
      "height": 720,
      "uri": "aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c745843",
      "url_list": [
        "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_9186d2f6f9…"
      ],
      "width": 720
    },
    "avatar_medium": {
      "height": 720,
      "uri": "aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c745843",
      "url_list": [
        "https://p3.douyinpic.com/aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c…"
      ],
      "width": 720
    },
    "avatar_thumb": {
      "height": 720,
      "uri": "aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c745843",
      "url_list": [
        "https://p3.douyinpic.com/aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c…"
      ],
      "width": 720
    },
    "aweme_count": 92,
    "aweme_count_correction_threshold": -1,
    "birthday": "",
    "birthday_hide_level": 0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user.follower_count` | Number of followers of the account. |
| `user.aweme_count` | Number of videos (works) on the account. |
| `user.dongtai_count / user.favoriting_count / user.evaluation_count` | Other count values on the profile. In this sample all three are `0`. |
| `user.avatar_larger / user.avatar_medium / user.avatar_thumb` | Avatar image objects in different sizes. Each has `uri`, `width`, `height` and a `url_list` of image links. |
| `user.avatar_larger.url_list[]` | Image links for the avatar. Several links with different formats (`heic`, `jpeg`) can appear in one list. |
| `user.cover_url[].url_list[]` | Links to the profile cover images of the account. These links contain `x-expires` and `x-signature` query values. |
| `user.cover_and_head_image_info.profile_cover_list[]` | Profile cover entries with `cover_url`, `dark_cover_color` and `light_cover_color`. |
| `user.commerce_user_info.has_ads_entry` | `true` when the account has an ads entry in its commerce info. |
| `user.follow_status` | Follow relationship value for this user. It is `0` in this sample. |
| `status_code` | `0` in this response, which is the success value seen here. |

### Notes

- Pass `sec_user_id` exactly as given. It is a long string that starts with `MS4wLjABAAAA`.
- Many fields, such as `city`, `country` and `birthday`, can be empty strings.
- To list this user's videos, pass the same `sec_user_id` to [Douyin User Videos](/apis/douyin/app-v3/user-post-videos).
- To list videos this user liked, use [Douyin User Liked Videos (App V3)](/apis/douyin/app-v3/user-like-videos).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/user-profile.json`](../../../../catalog/models/douyin/app-v3/user-profile.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/user-profile
