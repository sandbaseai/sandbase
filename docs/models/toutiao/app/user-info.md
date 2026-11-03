# Toutiao User Profile API: pricing, parameters and code examples

`toutiao/app/user-info` · data API · Toutiao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get a Toutiao (Jinri Toutiao) user profile by user ID: name, bio, avatar, follower, following and like counts, and content tabs.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/app/user-info", "user_id": "1352838578180211"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('toutiao/app/user-info', {'user_id': '1352838578180211'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("toutiao/app/user-info", {
  "user_id": "1352838578180211"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "toutiao/app/user-info", sandbase.Params{
	"user_id": "1352838578180211",
})
```

Same call via the path form: `POST /v1/api/toutiao/app/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User ID, can be obtained from the following API: `toutiao/app/user-id`  |

## Details

Returns the public profile of a Toutiao (Jinri Toutiao) account: name, bio, avatar and background image URLs, follower, following and like counts, and the content tabs. It needs one input, the numeric `user_id` of the account.

### Use cases

- Check whether a Toutiao account exists and read its name and bio before you add it to a monitoring list.
- Record `followers_count` and `followings_count` on a schedule to compare accounts.
- Find which content tabs an account has, such as short video, and the URL path that loads each tab.
- Detect accounts that link to a Douyin profile through the `external_info` block.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/toutiao/app/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "1352838578180211"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID, can be obtained from the following API: `toutiao/app/user-id` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "avatar_url": "",
    "bg_image": {
      "status": 0,
      "url": "https://p11-sign.toutiaoimg.com/tos-cn-i-tt/d74fb91f2825491584acf1afb99c8a2d~tpl…"
    },
    "big_avatar_url": "",
    "description": "",
    "digg_count": 0,
    "external_info": {
      "app_icon_url": "https://p26.toutiaoimg.com/obj/ies.fe.effect/a752e3bd176b10ea340c65db16e7c91c",
      "app_name": "aweme",
      "app_schema": "snssdk1128://user/profile/1352838578180211",
      "appstore_app_id": 1142110895,
      "button_name": "打开抖音关注作者",
      "download_url": "https://d.douyin.com/eXBJ/",
      "icon_title": "来源于抖音",
      "icon_url": "https://p26.toutiaoimg.com/obj/motor-img/9fd81928b2576d559b363fcf77681f5c",
      "name": "抖音",
      "package_name": "com.ss.android.ugc.aweme"
    },
    "external_media_type": 0,
    "followers_count": 0,
    "followings_count": 0,
    "gender": 0,
    "is_gov_media": false,
    "name": ""
  },
  "errno": 0,
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.user_id` | Numeric ID of the account, the same value you sent in the request. |
| `data.name / data.description` | Display name and bio text of the account. Both can be empty strings, as in the sample response. |
| `data.avatar_url / data.big_avatar_url / data.bg_image.url` | Links to the avatar, a larger avatar and the profile background image. The avatar fields can be empty strings. |
| `data.followers_count / data.followings_count` | Number of followers the account has and number of accounts it follows. |
| `data.digg_count` | Number of likes the account has received. |
| `data.publish_count` | Number of items the account has published. |
| `data.is_gov_media` | Boolean flag that is `true` when the account is marked as a government media account. |
| `data.top_tab[].show_name / data.top_tab[].type` | Label and internal type of each content tab on the profile. The sample shows a short video tab with type `external_ies_video`. |
| `data.top_tab[].url / data.top_tab[].load_count / data.top_tab[].total_count` | Relative feed path for the tab, the number of items loaded per page, and the total item count of the tab. |
| `data.external_info.name / data.external_info.app_schema / data.external_info.download_url` | Shows that the account's content comes from another app (here Douyin), with a deep link into that app and its download link. |

### Notes

- Get `user_id` from the [Toutiao Profile User ID](/apis/toutiao/app/user-id) API, which takes a profile link.
- `data.user_id` comes back as a number, while the request sends `user_id` as a string.
- A profile can return zero counts and empty text fields. Check `data.name` and `data.followers_count` before you treat the account as populated.
- To read the content of an account, call the feed path in `data.top_tab[].url`. For single posts, use [Toutiao Article Details (App)](/apis/toutiao/app/article-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Get information of specified article](/apis/toutiao/app/article-info): Get information of specified post.
- [Get comments of specified post](/apis/toutiao/app/comments): Get comments of specified post.
- [Get user_id from user profile](/apis/toutiao/app/user-id): Get user_id from user profile.

---
Machine-readable: [`catalog/models/toutiao/app/user-info.json`](../../../../catalog/models/toutiao/app/user-info.json) · Store page: https://www.sandbase.ai/model/toutiao/app/user-info
