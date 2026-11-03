# Kuaishou Single User Data (V2) API: pricing, parameters and code examples

`kuaishou/app/one-user-v2` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns profile details and personal entrance configurations for a specific Kuaishou account using the target user identifier.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/one-user-v2", "user_id": "3795214411"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/one-user-v2', {'user_id': '3795214411'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/one-user-v2", {
  "user_id": "3795214411"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/one-user-v2", sandbase.Params{
	"user_id": "3795214411",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/one-user-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | 用户ID/User ID  |

## Details

Returns the profile page data for one Kuaishou account: name, bio, avatar, follower and post counts, IP location, shop links and the entrance buttons shown on the profile. It needs the numeric `user_id` of the account.

### Use cases

- Read the follower count, post count and total likes of a Kuaishou creator before you decide to track them.
- Check whether an account runs a Kuaishou shop and read the shop link and product count.
- Save the display name, bio and avatar URLs of an account for a creator database.
- Read the IP location shown on a profile for audience or account research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/one-user-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3795214411"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "adImBusinessInfo": {
    "adImEntranceStyle": "DEFAULT"
  },
  "adProfileExtInfo": {
    "hasMagnetic": true,
    "pageId": 100022410,
    "posId": 20905,
    "subPageId": 100024409
  },
  "authorInfo": {
    "isAdBusinessUser": false,
    "isVerifiedUser": false
  },
  "clientLog": {
    "userStatus": "NORMAL"
  },
  "debug_id": "8ce99695",
  "debug_info": "gAAAAABq6Y7r1P_y-S7GJrTF1G8HSuPD_HX4C0lU5lmua-IPSxq0kCMZ9VP9hbBbSvW65aHshkuowMt6…",
  "host-name": "public-bjmt-c56-kce-node279.idchb1az4.hb1.kwaidc.com",
  "profileTemplateCardInfo": {
    "enableMiddleCardManagement": false,
    "enableSubManagePanel": false,
    "profileTemplateCardShowType": 1,
    "profileTemplateCards": [
      {
        "bizType": 1,
        "cardType": 1,
        "cardTypeName": "MERCHANT_SHOP",
        "cardViewStyle": 0,
        "darkIconUrl": "http://p1-ec.ecukwai.com/kos/nlav12333/trade-assets/mp3bbfap5o.d1f073b3f413828d.…",
        "darkIconUrls": [
          {
            "cdn": "p1-ec.ecukwai.com",
            "url": "http://p1-ec.ecukwai.com/kos/nlav12333/trade-assets/mp3bbfap5o.d1f073b3f413828d.…"
          }
        ],
        "disableManagement": true,
        "enableIconPlayLoop": true,
        "extra": {
          "is_sales_tag": "true",
          "selling_points_type": "2",
          "subTitleType": "2"
        },
        "iconUrl": "http://p1-ec.ecukwai.com/kos/nlav12333/trade-assets/fuhiss96tc.1243ad193de71988.…",
        "iconUrls": [
          {
            "cdn": "p1-ec.ecukwai.com",
            "url": "http://p1-ec.ecukwai.com/kos/nlav12333/trade-assets/fuhiss96tc.1243ad193de71988.…"
          }
        ],
        "ksOrderId": "guest_profile_my_shop_1cards_1"
      }
    ],
    "promptCount": 1,
    "redDotRules": {
      "exitRule": {
        "exitDays": 3,
        "exposureThreshold": 5,
        "permanentExitTimes": 4
      },
      "maxShowCountEveryType": 1
    }
  },
  "recommendUserShowStyle": 0,
  "result": 1,
  "tips": {},
  "totalPhotoLike": {
    "linkUrl": "kwai://krn?bundleId=KwaiPostLikeList&componentName=LikeList&ownerId=3795214411&g…",
    "showRedDot": false,
    "urls": [
      {
        "cdn": "tx2.a.kwimgs.com",
        "url": "https://tx2.a.kwimgs.com/udata/pkg/KS-PROFILE/light_like.05cc35bb8f13018c.jpg"
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `userProfile.profile.user_id / userProfile.profile.user_name` | Numeric ID and display name of the account. |
| `userProfile.profile.user_text` | Bio text shown on the profile. |
| `userProfile.profile.headurl / userProfile.profile.bigHeadUrls[].url` | Avatar image URL, plus a list of larger avatar URLs on different CDN hosts. |
| `userProfile.profile.user_profile_bg_url` | URL of the profile background image. |
| `userProfile.ownerCount.fan / userProfile.ownerCount.follow` | Number of followers and number of accounts this user follows. |
| `userProfile.ownerCount.photo / userProfile.ownerCount.photo_public / userProfile.ownerCount.photo_private` | Count of all posts, public posts and private posts. |
| `userProfile.ownerCount.total_photo_like` | Total likes received across the account's posts. |
| `userProfile.ipLocation.ipLocationName` | Region name shown as the account's IP location, such as `Hunan`. |
| `userProfile.extraLinks[].entranceTitle / userProfile.extraLinks[].subTitle / userProfile.extraLinks[].link` | Name, short subtitle and link of the shop entrance shown on the profile. |
| `userProfile.personalEntrances[].entrances[].entranceName / userProfile.personalEntrances[].entrances[].entranceType` | Label and type code of each action button on the profile, such as `chat` or `shareProfile`. |

### Notes

- `user_id` is a numeric string such as `3795214411`. The same value comes back as `userProfile.profile.user_id`.
- Some text fields are in Chinese and some in English, for example the shop title and `entrances[].detail`.
- Fields like `debug_id`, `debug_info` and `host-name` are request diagnostics, not profile data.
- To list the account's videos, call [Kuaishou User Video List (V2)](/apis/kuaishou/app/user-post-v2). To check for a live stream, call [Kuaishou User Broadcast Details](/apis/kuaishou/app/user-live-info).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/one-user-v2.json`](../../../../catalog/models/kuaishou/app/one-user-v2.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/one-user-v2
