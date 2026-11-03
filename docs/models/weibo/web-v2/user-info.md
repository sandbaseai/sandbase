# Weibo User Profile Details (Web V2) API: pricing, parameters and code examples

`weibo/web-v2/user-info` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed Weibo user profile information including nickname, avatar, bio, following count, and followers count by user ID or custom username.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-info", "uid": "2062052743"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-info', {'uid': '2062052743'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-info", {
  "uid": "2062052743"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-info", sandbase.Params{
	"uid": "2062052743",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` |  |  | User ID (optional, choose one with custom)  |
| `custom` |  |  | Custom username (optional, choose one with uid)  |

## Details

Returns the public profile of a Weibo account, including nickname, avatar URLs, bio, follower and following counts, verification status, and total post engagement. Send either `uid` (the numeric user ID) or `custom` (the custom username in the profile URL).

### Use cases

- Show a creator's nickname, avatar, and bio on a dashboard using `user.screen_name`, `user.avatar_hd`, and `user.description`.
- Track the follower count of a celebrity or brand account with `user.followers_count`.
- Check whether an account is verified and read its verification label before listing it as an official source.
- Convert a custom username such as `shuqi` into the numeric `user.idstr` for other Weibo calls.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "1722594714", "custom": "shuqi"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `custom` | string | No | Custom username (optional, choose one with uid) |
| `uid` | string | No | User ID (optional, choose one with custom) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "blockText": "",
  "tabList": [
    {
      "name": "feed",
      "tabName": "微博"
    }
  ],
  "user": {
    "avatar_hd": "https://tvax2.sinaimg.cn/crop.0.0.1080.1080.1024/001SzPzIly8glt0lw5p9tj60u00u0js…",
    "avatar_large": "https://tvax2.sinaimg.cn/crop.0.0.1080.1080.180/001SzPzIly8glt0lw5p9tj60u00u0jsn…",
    "cover_image_phone": "https://ww1.sinaimg.cn/crop.0.0.640.640.640/9d44112bjw1f1xl1c10tuj20hs0hs0tw.jpg",
    "description": "心存善念惜福喔(o^,^o)~~",
    "domain": "shuqi",
    "follow_me": false,
    "followers_count": 40414299,
    "followers_count_str": "4041.4万",
    "following": false,
    "friends_count": 540,
    "gender": "f",
    "icon_list": [
      {
        "data": {
          "mbrank": 9,
          "mbtype": 12,
          "svip": 1,
          "vvip": 0
        },
        "type": "vip"
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user.id / user.idstr` | Numeric user ID, returned as a number and as a string. |
| `user.screen_name` | Display nickname of the account. |
| `user.domain` | Custom username of the account. It is `shuqi` in this example. |
| `user.description` | Bio text written by the user. |
| `user.followers_count / user.followers_count_str` | Follower count as a number, and the same count in a short display form such as `4041.4万`. |
| `user.friends_count / user.statuses_count` | Number of accounts the user follows, and number of posts the user has published. |
| `user.avatar_hd / user.avatar_large / user.profile_image_url` | Avatar image URLs in decreasing size. The URLs contain `Expires` and `ssig` query parameters. |
| `user.verified / user.verified_reason` | Whether the account is verified, and the verification label, such as `演员` (actor). |
| `user.status_total_counter.like_cnt / comment_cnt / repost_cnt / total_cnt` | Total likes, comments, reposts, and their sum across the user's posts. The first four are strings with thousands separators. |
| `user.gender / user.location` | Gender code (`f` here) and the location text from the profile. |

### Notes

- Send `uid` or `custom`. The schema marks both as optional and says to choose one.
- Use `user.profile_url` (for example `/u/1722594714`) as the relative path of the profile page.
- To read the account's posts next, call [Weibo User Posts](/apis/weibo/web-v2/user-posts) or [Weibo User Original Posts](/apis/weibo/web-v2/user-original-posts).
- For a lighter profile lookup, call [Weibo User Basic Information](/apis/weibo/web-v2/user-basic-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-info.json`](../../../../catalog/models/weibo/web-v2/user-info.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-info
