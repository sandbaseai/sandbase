# Zhihu User Followees API: pricing, parameters and code examples

`zhihu/user-followees` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get accounts followed by a Zhihu user, with offset pagination. Use it to explore the outgoing connections of a known account.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/user-followees", "userUrlToken": "excited-vczh"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/user-followees', {'userUrlToken': 'excited-vczh'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/user-followees", {
  "userUrlToken": "excited-vczh"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/user-followees", sandbase.Params{
	"userUrlToken": "excited-vczh",
})
```

Same call via the path form: `POST /v1/api/zhihu/user-followees` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Start offset, begins with 0. default `0` |
| `userUrlToken` | string | yes | Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.  |

## Details

Returns the list of accounts that a Zhihu user follows. It needs the user's `userUrlToken` and returns one page of followees with profile counts, plus paging details and the total followee count.

### Use cases

- Map who a known Zhihu account follows to find its interests and peer accounts.
- Find organization accounts among a user's followees by checking `is_org` or `user_type`.
- Rank a user's followees by `follower_count` to spot the most influential accounts they follow.
- Collect `url_token` values from followees to feed into other user-level lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/user-followees" \
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
      "answer_count": 449,
      "articles_count": 10,
      "available_medals_count": 0,
      "avatar_url": "https://picx.zhimg.com/v2-5788e1427561fa3733669a902a7e333a_l.jpg?source=32738c0c",
      "avatar_url_template": "https://picx.zhimg.com/v2-5788e1427561fa3733669a902a7e333a.jpg?source=32738c0c",
      "badge": [],
      "badge_v2": {
        "detail_badges": [],
        "icon": "",
        "merged_badges": [],
        "night_icon": "",
        "title": ""
      },
      "follower_count": 6846,
      "follower_count_num": "6846",
      "follower_count_text": "6846",
      "follower_count_unit": "",
      "gender": 1
    }
  ],
  "paging": {
    "is_end": false,
    "is_start": true,
    "next": "https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B%2A%5…",
    "previous": "https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B%2A%5…",
    "totals": 3288
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].name` | Display name of the followed account. |
| `data[].url_token` | Short token of the followed account. It is the value used in `zhihu.com/people/{url_token}`. |
| `data[].headline` | Short profile tagline of the followed account. It can be an empty string. |
| `data[].user_type / data[].is_org` | Account kind. `user_type` is `people` or `organization` in this response, and `is_org` is `true` for organizations. |
| `data[].follower_count / data[].answer_count / data[].articles_count` | Number of followers, answers and articles for the followed account. |
| `data[].gender` | Numeric gender code. The response shows `1` and `-1`; the meaning of each code is not documented. |
| `data[].is_realname` | Whether the followed account is flagged as real-name verified. |
| `data[].id` | Internal hash ID of the followed account. |
| `paging.totals` | Total number of accounts the user follows. |
| `paging.is_end` | `true` when there are no more pages after this one. |

### Notes

- Take `userUrlToken` from a profile URL: in `zhihu.com/people/{userUrlToken}` it is the last part.
- Page through results with `offset`, starting at `0`. Stop when `paging.is_end` is `true`.
- Use `paging.totals` to see how many followees exist before you page through them.
- To see the accounts that follow this user instead, call [Zhihu User Followers](/apis/zhihu/user-followers). For a profile of one account, call [Zhihu User Info](/apis/zhihu/user-info).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/zhihu/user-followees.json`](../../../catalog/models/zhihu/user-followees.json) · Store page: https://www.sandbase.ai/model/zhihu/user-followees
