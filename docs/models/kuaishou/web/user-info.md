# Kuaishou Web User Info API: pricing, parameters and code examples

`kuaishou/web/user-info` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns public profile information for a specified Kuaishou web user. Supply the target user identifier to retrieve account metadata.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/user-info", "user_id": "3xz63mn6fngqtiq"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/user-info', {'user_id': '3xz63mn6fngqtiq'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/user-info", {
  "user_id": "3xz63mn6fngqtiq"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/user-info", sandbase.Params{
	"user_id": "3xz63mn6fngqtiq",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | 用户 ID (eid)/User ID (eid)  |

## Details

Returns the public profile of a Kuaishou web user, including name, avatar, bio, gender, and follower, following, like and public post counts. It needs one input, the user's `user_id` (eid).

### Use cases

- Show a Kuaishou creator's name, avatar and bio in an internal dashboard.
- Record `ownerCount.fan` and `ownerCount.like` on a schedule to chart a creator's growth.
- Check whether a creator is live right now using `userProfile.livingInfo.living`.
- Match a creator's custom handle in `userDefineId` to their `user_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3xz63mn6fngqtiq"}'
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
  "host-name": "public-bjy-c34-kce-node3594.idchb1az2.hb1.kwaidc.com",
  "result": 1,
  "userProfile": {
    "gender": "M",
    "isFollowing": false,
    "isUserIsolated": false,
    "livingInfo": {
      "iconType": 0,
      "living": false,
      "livingId": null
    },
    "ownerCount": {
      "fan": 4177857,
      "follow": 210,
      "like": 38618671,
      "photo_public": 257
    },
    "profile": {
      "headurl": "https://p66.a.kwimgs.com/uhead/AB/2025/08/11/21/BMjAyNTA4MTEyMTEyNDlfMjI4OTA1ODA…",
      "user_id": "3xz63mn6fngqtiq",
      "user_name": "权少爱吃小汉堡🍔",
      "user_profile_bg_url": "//s2-10623.kwimgs.com/kos/nlav10623/vision_images/profile_background.5bc08b1bf4f…",
      "user_text": "感谢你的关注木木哒 我玩得游戏叫:Gmod\n\n禁止冒充搬运视频 违者必究"
    },
    "showCollectTab": false,
    "userDefineId": "quanshaogmod"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `userProfile.profile.user_name` | Display name of the user. It can contain emoji. |
| `userProfile.profile.user_id` | The user ID (eid). It matches the `user_id` you sent. |
| `userProfile.profile.user_text` | The bio text on the profile. It can contain line breaks. |
| `userProfile.profile.headurl / userProfile.profile.user_profile_bg_url` | Image URLs for the avatar and the profile background. The background URL starts with `//`, so add a scheme before use. |
| `userProfile.ownerCount.fan / userProfile.ownerCount.follow` | Number of followers and number of accounts this user follows. |
| `userProfile.ownerCount.like / userProfile.ownerCount.photo_public` | Total likes counted for the user and the number of public posts. |
| `userProfile.gender` | Gender code of the user. The sample value is `M`. |
| `userProfile.userDefineId` | Custom handle set by the user, such as `quanshaogmod`. |
| `userProfile.livingInfo.living` | Boolean that shows whether the user is live now. `livingInfo.livingId` is `null` when the user is not live. |
| `userProfile.isFollowing / userProfile.showCollectTab` | Booleans for the follow state in the request context and for whether the favorites tab is shown on the profile. |

### Notes

- Pass the ID in `user_id`. It is a string such as `3xz63mn6fngqtiq`.
- If you only have a user share link, call [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id) first to get the ID.
- To list a user's favorites, call [Kuaishou User Favorites](/apis/kuaishou/web/user-collect). To see broadcast replays, call [Kuaishou User Broadcast Replay](/apis/kuaishou/web/user-live-replay).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Web Share Short URL](/apis/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/apis/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/user-info.json`](../../../../catalog/models/kuaishou/web/user-info.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/user-info
