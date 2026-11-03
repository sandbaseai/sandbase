# Zhihu User Info API: pricing, parameters and code examples

`zhihu/user-info` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get the public profile for a Zhihu user identified by URL token. Use it to inspect an account found through Zhihu content or relationship data.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/user-info", "userUrlToken": "excited-vczh"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/user-info', {'userUrlToken': 'excited-vczh'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/user-info", {
  "userUrlToken": "excited-vczh"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/user-info", sandbase.Params{
	"userUrlToken": "excited-vczh",
})
```

Same call via the path form: `POST /v1/api/zhihu/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userUrlToken` | string | yes | Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.  |

## Details

Returns the public profile of one Zhihu user, including name, follower count, answer and article counts, verification flags and IP location. It needs the user's `userUrlToken`, the last part of a `zhihu.com/people/{userUrlToken}` link.

### Use cases

- Check follower count and `is_realname` status of a Zhihu author before you work with them.
- Resolve a `url_token` found in answer or follower lists into a name, avatar and profile summary.
- Track how an account's `answer_count` and `articles_count` change by calling the API on a schedule.
- Separate personal accounts from organization accounts using `is_org` and `type`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userUrlToken": "excited-vczh"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userUrlToken` | string | Yes | Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ai_assistant_info": null,
  "allow_message": true,
  "answer_count": 7,
  "articles_count": 147,
  "available_medals_count": 0,
  "avatar_url": "https://picx.zhimg.com/v2-ada18a9354a3831171306f2c7ce20aaf_xl.jpg?source=32738c0…",
  "avatar_url_template": "https://picx.zhimg.com/v2-ada18a9354a3831171306f2c7ce20aaf_l.jpg?source=32738c0c…",
  "badge": [],
  "badge_v2": {
    "detail_badges": [],
    "icon": "",
    "merged_badges": [],
    "night_icon": "",
    "title": ""
  },
  "employments": [],
  "extra": null,
  "follower_count": 834484
}
```

### Response fields

| Field | Meaning |
|---|---|
| `name` | Display name of the user. |
| `url_token` | The user's URL token. It matches the `userUrlToken` you sent. |
| `id` | Zhihu's internal ID for the user, a 32-character hex string. |
| `follower_count` | Number of followers as an integer. |
| `follower_count_text` | Follower count in a short display form, for example `83.4 万`. Use `follower_count` when you need the exact number. |
| `answer_count / articles_count` | Number of answers and number of articles the user has published. |
| `headline` | Short profile tagline. It can be an empty string. |
| `ip_info` | IP location label shown on the profile, for example `IP 属地美国`. |
| `is_realname / is_org / is_advertiser` | Flags for a real-name verified account, an organization account, and an advertiser account. |
| `avatar_url` | Link to the user's avatar image. |
| `vip_info.is_vip / kvip_info.is_vip` | Whether the account has a VIP membership of each kind. |

### Notes

- Take `userUrlToken` from a profile link, `zhihu.com/people/{userUrlToken}`, or from the `url_token` field in other Zhihu user results.
- `gender` is `-1` in this response. Do not assume other values from this one example.
- Next, call [Zhihu User Articles](/apis/zhihu/user-articles) for this user's articles, or [Zhihu User Followers](/apis/zhihu/user-followers) to list who follows them.
- [Zhihu Web User Profile](/apis/zhihu/web/user-info) is a separate profile API in the same Zhihu family.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/zhihu/user-info.json`](../../../catalog/models/zhihu/user-info.json) · Store page: https://www.sandbase.ai/model/zhihu/user-info
