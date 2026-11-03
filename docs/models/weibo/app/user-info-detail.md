# Weibo User Profile Details (App) API: pricing, parameters and code examples

`weibo/app/user-info-detail` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comprehensive profile information for a Weibo user, including verification status, account level, and tags based on the specified user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-info-detail", "uid": "8431518763"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-info-detail', {'uid': '8431518763'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-info-detail", {
  "uid": "8431518763"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-info-detail", sandbase.Params{
	"uid": "8431518763",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-info-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |

## Details

Returns a Weibo user's profile detail page for one user ID. The response has the account record (`userInfo`) and the app's display layout (`items`) for fields such as nickname, bio and gender. It needs one input, `uid`.

### Use cases

- Check the account creation time and credit score of a Weibo user before you trust the account.
- Read follower, favourite and block counts for a user and store them in a creator database.
- Check the verification fields (`auth_status`, `auth_career`, `auth_realname`) and the `badge` flags for an account.
- Pull the nickname, bio and gender text shown on the app's detail page for a given user.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-info-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "8431518763"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "flowConfig": {
    "background": "https://h5.sinaimg.cn/upload/100/1734/2023/02/14/information_bg.png",
    "backgroundDark": "https://h5.sinaimg.cn/upload/100/1734/2023/02/14/information_bg_dark.png",
    "titleRightActionlog": {
      "act_code": 7292,
      "cardid": "qrcode",
      "ext": "type:qrcode",
      "fid": "",
      "uicode": "10001487"
    },
    "titleRightIcon": "https://h5.sinaimg.cn/upload/100/1734/2023/02/16/icon_code.png",
    "titleRightIconDark": "https://h5.sinaimg.cn/upload/100/1734/2023/02/16/icon_code_dark.png",
    "titleRightScheme": "sinaweibo://wbaction_qrshare?uid=8431518763"
  },
  "items": [
    {
      "category": "group",
      "header": {
        "avatar": {
          "avatarUrl": "https://tvax1.sinaimg.cn/default/images/default_avatar_female_180.gif?KID=imgbed…",
          "badgeUrl": "",
          "itemId": "profileme_head_avatar",
          "mask_type": 0,
          "pendantUrl": "",
          "pendantUrl_v3": "",
          "style": {
            "height": 77,
            "margin": [
              0
            ],
            "mask_type": 0,
            "pendantGifLoopCount": 1,
            "pendantGifScrollNotNeedRePlay": true,
            "pendantHeight": 89,
            "pendantHiddenInDark": true,
            "pendantOffsetX": 0
          },
          "type": "avatar"
        },
        "category": "cell",
        "itemId": "profileme_mine_head",
        "type": "avatarInfo"
      },
      "itemId": "profileme_mine",
      "items": [
        {
          "category": "userinfo",
          "itemId": "mainnums_statuses",
          "style": {
            "background": {
              "color": "#ffffff",
              "colorKey": "CommonCardBackground",
              "corners": [
                7
              ],
              "type": "color"
            },
            "grid": true,
            "height": 0,
            "margin": [
              0
            ]
          },
          "type": "userInfoDetailRichText"
        }
      ],
      "style": {
        "column": 2,
        "padding": [
          10
        ]
      },
      "type": "grid"
    }
  ],
  "pageData": "{}",
  "userInfo": {
    "allow_all_act_msg": false,
    "allow_all_comment": true,
    "audio_ability": 0,
    "auth_career": null,
    "auth_career_name": null,
    "auth_realname": null,
    "auth_status": 1,
    "avatar_hd": "https://tvax1.sinaimg.cn/default/images/default_avatar_female_180.gif?KID=imgbed…",
    "avatar_large": "https://tvax1.sinaimg.cn/default/images/default_avatar_female_180.gif?KID=imgbed…",
    "avatar_type": 0,
    "badge": {
      "acg_2024": 0,
      "aizi_2020": 0,
      "anniversary": 0,
      "ant_2019": 0,
      "aoyun_2021": 0,
      "aoyun_2024": 0,
      "article_visible": 0,
      "asiad_2018": 0,
      "avengers_2019": 0,
      "baokemeng_2022": 0,
      "baokemeng_2023": 0,
      "baoshilong_1": 0
    },
    "badge_top": ""
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `userInfo.created_at` | Account creation time as a text date, for example `Thu Sep 04 14:17:15 +0800 2025`. |
| `userInfo.followers_count / userInfo.bi_followers_count` | Number of followers, and the second count the API reports as `bi_followers_count`. The example account has 1 follower. |
| `userInfo.favourites_count` | Count of favourites reported for the user. |
| `userInfo.credit_score` | Numeric credit score of the account. The example value is 80. |
| `userInfo.class` | Account level value. The example value is 1. |
| `userInfo.auth_status / userInfo.auth_career / userInfo.auth_realname` | Verification-related fields. `auth_career` and `auth_realname` are `null` when the account has no such data. |
| `userInfo.avatar_hd / userInfo.avatar_large` | Avatar image URLs. The example account shows a default avatar. |
| `userInfo.badge` | Object of badge flags, one key per badge. A value of `0` means the user does not have that badge. |
| `userInfo.description / userInfo.birthday / userInfo.constellation` | Profile text fields. They are empty strings when the user has not filled them in. |
| `items[].items[].rightTextIconView.text.content` | Display value of one profile row, such as nickname, bio or gender. The matching label is in `leftTextIconView.text.content`. |

### Notes

- Pass the numeric user ID as a string in `uid`, for example `8431518763`.
- `items` and `flowConfig` hold layout and style data for the app screen. Use `userInfo` for structured values.
- `userInfo.city` returned `1000` for the example user. The response does not show what this code maps to.
- For another profile view, see [Weibo User Profile Information](/apis/weibo/app/user-info). For the user's posts, see [Weibo User Timeline](/apis/weibo/app/user-timeline).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/user-info-detail.json`](../../../../catalog/models/weibo/app/user-info-detail.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-info-detail
