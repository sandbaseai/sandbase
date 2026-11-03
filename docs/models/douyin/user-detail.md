# Douyin User Profile API: pricing, parameters and code examples

`douyin/user-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get a Douyin (TikTok China) user profile by secUid. Use it to review a known creator or account before monitoring related content or conducting account research.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/user-detail", "secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/user-detail', {'secUid': 'MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/user-detail", {
  "secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/user-detail", sandbase.Params{
	"secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24",
})
```

Same call via the path form: `POST /v1/api/douyin/user-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `secUid` | string | yes | The unique user ID (sec_uid) on Douyin.  |

## Details

This API returns the public profile of a Douyin (TikTok China) user. It needs one input, the user's `secUid`. The response includes the account's avatar images, cover images, video count and shop window entry.

### Use cases

- Check a known creator's profile and video count before you add the account to a monitoring list.
- Pull avatar and profile cover image URLs to show a creator card in an internal dashboard.
- Check whether an account has a product window and how many items it lists before you start commerce research.
- Confirm that a stored `secUid` still returns a valid user.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/user-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | Yes | The unique user ID (sec_uid) on Douyin. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": null,
    "logid": "2026110315322248F17F939EC10D294C67",
    "now": 1793691142000,
    "search_request_id": null
  },
  "log_pb": {
    "impr_id": "2026110315322248F17F939EC10D294C67"
  },
  "status_code": 0,
  "status_msg": null,
  "user": {
    "account_cert_info": "{}",
    "apple_account": 0,
    "avatar_168x168": {
      "height": 720,
      "uri": "aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16e8aca2a0bd",
      "url_list": [
        "https://p11.douyinpic.com/aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16e8a…"
      ],
      "width": 720
    },
    "avatar_300x300": {
      "height": 720,
      "uri": "aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16e8aca2a0bd",
      "url_list": [
        "https://p11.douyinpic.com/aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16e8a…"
      ],
      "width": 720
    },
    "avatar_is_digged": false,
    "avatar_larger": {
      "height": 720,
      "uri": "aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16e8aca2a0bd",
      "url_list": [
        "https://p11.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_1fcfb510b…"
      ],
      "width": 720
    },
    "avatar_medium": {
      "height": 720,
      "uri": "aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16e8aca2a0bd",
      "url_list": [
        "https://p11.douyinpic.com/aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16e8a…"
      ],
      "width": 720
    },
    "avatar_thumb": {
      "height": 720,
      "uri": "aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16e8aca2a0bd",
      "url_list": [
        "https://p11.douyinpic.com/aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16e8a…"
      ],
      "width": 720
    },
    "aweme_count": 2655,
    "aweme_count_correction_threshold": -1,
    "birthday": "",
    "birthday_hide_level": 0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `status_code` | Result code of the request. The sample response returns `0`. |
| `user.aweme_count` | Number of videos on the account. The sample shows `2655`. |
| `user.avatar_larger.url_list[] / user.avatar_medium.url_list[] / user.avatar_thumb.url_list[]` | Avatar image URLs in different sizes. Each list holds several URLs for the same image. |
| `user.cover_url[].url_list[]` | Profile cover image URLs. These links carry `x-expires` and `x-signature` parameters in the query string. |
| `user.cover_and_head_image_info.profile_cover_list[].cover_url.url_list[]` | Profile cover image URLs with dark and light cover colors in `dark_cover_color` and `light_cover_color`. |
| `user.card_entries[].title / user.card_entries[].sub_title` | Label of a card on the profile. The sample shows a shop window card (`商品橱窗`) with the subtitle `57件好物`. |
| `user.card_entries[].goto_url` | App deep link for the card. It contains the numeric `uid` and the `sec_uid` of the account. |
| `user.commerce_user_info.has_ads_entry` | Shows whether the account has an ads entry. The sample returns `true`. |
| `user.follow_status / user.favorite_permission` | Flags for the relationship to the viewer and for the favorites setting. The sample returns `0` and `1`. |

### Notes

- Send the account's `secUid` as the only required parameter. It is a string that starts with `MS4w`.
- Image links in the response are signed and include an `x-expires` value, so store the image itself if you need it later.
- To list the account's videos, call [Douyin User Videos](/apis/douyin/app-v3/user-post-videos). For another profile format, call [Douyin User Profile (App V3)](/apis/douyin/app-v3/user-profile).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/douyin/user-detail.json`](../../../catalog/models/douyin/user-detail.json) · Store page: https://www.sandbase.ai/model/douyin/user-detail
