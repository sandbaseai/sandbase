# Weibo User Profile API: pricing, parameters and code examples

`weibo/user-detail` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get a Weibo user profile identified by UID. Use it to look up a known account for creator research, profile review, or subsequent retrieval of that user's posts and videos.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/user-detail", "uid": "2803301701"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/user-detail', {'uid': '2803301701'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/user-detail", {
  "uid": "2803301701"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/user-detail", sandbase.Params{
	"uid": "2803301701",
})
```

Same call via the path form: `POST /v1/api/weibo/user-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Weibo User ID (UID).  |

## Details

Returns the public profile of one Weibo account, including name, bio, follower and post counts, verification status and avatar URLs. It needs the numeric Weibo user ID in `uid`.

### Use cases

- Check follower count and verification status of a known account before a creator partnership.
- Pull the bio, location and verification reason of an account for profile review.
- Track changes in `followers_count` and `statuses_count` for an account over time.
- Confirm a UID maps to the expected `screen_name` before fetching that user's posts or videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/user-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "2803301701"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | Weibo User ID (UID). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "blockText": "",
    "tabList": [
      {
        "name": "home",
        "tabName": "精选"
      }
    ],
    "user": {
      "avatar_hd": "https://tvax4.sinaimg.cn/crop.0.0.1018.1018.1024/0033ImPzly8h8vgemh8kxj60sa0sadg…",
      "avatar_large": "https://tvax4.sinaimg.cn/crop.0.0.1018.1018.180/0033ImPzly8h8vgemh8kxj60sa0sadgw…",
      "cover_image_phone": "https://wx1.sinaimg.cn/crop.0.0.640.640.640/0033ImPzly1gs64jwa7uyj60v90v9n1r02.j…",
      "description": "人民日报法人微博。参与、沟通、记录时代。",
      "domain": "rmrb",
      "follow_me": false,
      "followers_count": 158132190,
      "followers_count_str": "1.58亿",
      "following": false,
      "friends_count": 3096,
      "gender": "m",
      "icon_list": [
        {
          "data": {
            "mbrank": 4,
            "mbtype": 12,
            "svip": 1,
            "vvip": 1
          },
          "type": "vip"
        }
      ]
    }
  },
  "ok": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.user.screen_name` | Display name of the account. |
| `data.user.idstr / data.user.id` | The user ID as a string and as a number. The string matches the `uid` you sent. |
| `data.user.description` | Bio text written by the account owner. |
| `data.user.followers_count / data.user.followers_count_str` | Follower count as a number, and the same count in a short display form such as `1.58亿`. |
| `data.user.friends_count / data.user.statuses_count` | Number of accounts this user follows, and number of posts the user has published. |
| `data.user.verified / data.user.verified_reason` | Whether the account is verified, and the verification text shown on the profile. |
| `data.user.location / data.user.gender` | Location text from the profile, and gender code (`m` in this response). |
| `data.user.status_total_counter` | Totals across the user's posts: `comment_cnt`, `like_cnt`, `repost_cnt` and `total_cnt`. Values are formatted strings, and `total_cnt_format` gives a short form. |
| `data.user.avatar_hd / data.user.avatar_large / data.user.profile_image_url` | Avatar image URLs in different sizes. Each URL carries an `Expires` parameter. |
| `data.user.domain / data.user.profile_url` | The custom domain name of the account and the relative profile path, such as `/u/2803301701`. |

### Notes

- Pass the numeric Weibo user ID as `uid`, as a string. The same ID appears in `data.user.idstr` and in `data.user.profile_url`.
- `data.tabList[]` lists the profile tabs (`home`, `feed`, `newVideo`) shown for the account.
- To read this user's posts, call [Weibo User Published Posts](/apis/weibo/user-post). For videos, call [Weibo User Video List](/apis/weibo/user-video-list).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/weibo/user-detail.json`](../../../catalog/models/weibo/user-detail.json) · Store page: https://www.sandbase.ai/model/weibo/user-detail
