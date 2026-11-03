# Zhihu User Followers API: pricing, parameters and code examples

`zhihu/user-followers` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get accounts that follow a Zhihu user, with offset pagination. Use it to explore the audience connections of a known account.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/user-followers", "userUrlToken": "excited-vczh"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/user-followers', {'userUrlToken': 'excited-vczh'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/user-followers", {
  "userUrlToken": "excited-vczh"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/user-followers", sandbase.Params{
	"userUrlToken": "excited-vczh",
})
```

Same call via the path form: `POST /v1/api/zhihu/user-followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Start offset, begins with 0. default `0` |
| `userUrlToken` | string | yes | Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.  |

## Details

Returns a page of Zhihu accounts that follow a given user. Each row has profile basics such as name, headline, follower count and URL token. The input is the user's `userUrlToken`, with an optional `offset`.

### Use cases

- Build a list of the accounts that follow a known Zhihu creator.
- Find high-reach followers by sorting rows on `follower_count`.
- Check how many followers an account has through `paging.totals`.
- Collect `url_token` values to pull full profiles for each follower.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/user-followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userUrlToken": "excited-vczh"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userUrlToken` | string | Yes | Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`. |
| `offset` | integer | No | Start offset, begins with 0. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "answer_count": 2,
      "articles_count": 0,
      "available_medals_count": 0,
      "avatar_url": "https://pic1.zhimg.com/v2-70abac091e46d958e71b20a984d98016_l.jpg?source=32738c0c",
      "avatar_url_template": "https://picx.zhimg.com/v2-70abac091e46d958e71b20a984d98016.jpg?source=32738c0c",
      "badge": [],
      "badge_v2": {
        "detail_badges": [],
        "icon": "",
        "merged_badges": [],
        "night_icon": "",
        "title": ""
      },
      "follower_count": 29,
      "follower_count_num": "29",
      "follower_count_text": "29",
      "follower_count_unit": "",
      "gender": 1
    }
  ],
  "paging": {
    "is_end": false,
    "is_start": true,
    "next": "https://www.zhihu.com/api/v4/members/excited-vczh/followers?include=data%5B%2A%5…",
    "previous": "https://www.zhihu.com/api/v4/members/excited-vczh/followers?include=data%5B%2A%5…",
    "totals": 834484
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].name` | Display name of the follower. |
| `data[].url_token` | The follower's URL token. Use it as `userUrlToken` in other Zhihu user APIs. |
| `data[].headline` | Short bio line the follower shows on their profile. |
| `data[].follower_count` | Number of followers the follower has. |
| `data[].answer_count / articles_count` | Number of answers and articles the follower has published. |
| `data[].is_org / is_realname / is_advertiser` | Flags for organization accounts, real-name verified accounts and advertiser accounts. |
| `data[].vip_info.is_vip` | Whether the follower has a VIP membership. |
| `data[].gender` | Numeric gender code. The sample shows `1` and `0`; the response does not explain the values. |
| `paging.totals` | Total number of followers of the requested user. |
| `paging.is_end` | `true` when there are no more pages. |

### Notes

- Take `userUrlToken` from the profile URL: in `zhihu.com/people/{userUrlToken}` it is the last part.
- Pass `offset` starting at `0` to page through results. Keep going until `paging.is_end` is `true`.
- `paging.next` holds the link to the next page of the platform's own API. Use `offset` to page here.
- To see who the user follows instead, call [Zhihu User Followees](/apis/zhihu/user-followees). For one follower's full profile, call [Zhihu User Info](/apis/zhihu/user-info).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/zhihu/user-followers.json`](../../../catalog/models/zhihu/user-followers.json) · Store page: https://www.sandbase.ai/model/zhihu/user-followers
