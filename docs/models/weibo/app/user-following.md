# Weibo User following API: pricing, parameters and code examples

`weibo/app/user-following` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get user following on Weibo. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-following", "uid": "1856404484"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-following', {'uid': '1856404484'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-following", {
  "uid": "1856404484"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-following", sandbase.Params{
	"uid": "1856404484",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-following` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Uid  |
| `since_id` | string |  | since_id  |
| `sort_type` | integer |  | Sort Type default `2` |

## Details

Returns the list of accounts a Weibo user follows. Each entry has the followed account's description, avatar URLs and follower count. The API needs the `uid` of the user whose following list you want.

### Use cases

- Map which brands, media accounts and creators a given Weibo user follows.
- Build a list of accounts in one niche by reading the following lists of known accounts in that niche.
- Check whether the followed accounts also follow the queried user, using the `follow_me` flag.
- Rank followed accounts by audience size using `followers_count`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-following" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "1856404484", "sort_type": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes |  |
| `since_id` | string | No |  |
| `sort_type` | integer | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "has_filtered_attentions": false,
    "since_id": "1793691972|20",
    "total_cnt": 1510,
    "uid": 1856404484,
    "users": [
      {
        "flag": 0,
        "itemid": "2310510024_1_ _0_7714083748_81e016ec",
        "user": {
          "avatar_hd": "https://tvax3.sinaimg.cn/crop.0.0.1080.1080.1024/008q3vzCly8ihevz7xuqjj30u00u0t9…",
          "avatar_large": "https://tvax3.sinaimg.cn/crop.0.0.1080.1080.180/008q3vzCly8ihevz7xuqjj30u00u0t92…",
          "descStruct": {
            "labelDesc": [
              {
                "followers_count_str": "69.4万",
                "name": "694402",
                "suffix": "粉丝"
              }
            ],
            "textDesc": "简介：智在随心 奔赴热爱 · 新豪华 阿维塔"
          },
          "description": "智在随心 奔赴热爱 · 新豪华 阿维塔",
          "follow_me": false,
          "followers_count": 694402,
          "followers_count_str": "69.4万",
          "following": false
        }
      }
    ]
  },
  "http_code": 200,
  "ok": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.total_cnt` | Total number of accounts the user follows. |
| `data.uid` | The numeric ID of the user whose following list was requested. |
| `data.since_id` | Cursor value for the next page. It looks like `1793691972/20`. |
| `data.has_filtered_attentions` | Boolean flag on the list. It was `false` in this response. |
| `data.users[].user.description` | Bio text of the followed account. |
| `data.users[].user.followers_count / data.users[].user.followers_count_str` | Follower count of the followed account. The first is a number, the second is a short display string such as `69.4万`. |
| `data.users[].user.follow_me` | Whether the followed account follows back, as a boolean. |
| `data.users[].user.following` | Boolean relation flag for the followed account. It was `false` for every user in this response. |
| `data.users[].user.avatar_hd / data.users[].user.avatar_large` | Image URLs for the account avatar in two sizes. The URLs carry `Expires` and `ssig` query values. |
| `data.users[].user.descStruct.labelDesc[]` | Label chips shown for the account, such as follower count text and topic tags like `科学科普博主`. |

### Notes

- Pass the numeric Weibo user ID as `uid`. You can find it in the response of [Weibo User Profile Information](/apis/weibo/app/user-info).
- For the next page, send the `data.since_id` value from the last response as `since_id`.
- `sort_type` defaults to `2`. The docs do not describe other values.
- Read `data.total_cnt` to see how many accounts the user follows in total.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/weibo/app/user-following.json`](../../../../catalog/models/weibo/app/user-following.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-following
