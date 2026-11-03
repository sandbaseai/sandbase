# Zhihu Web User Profile API: pricing, parameters and code examples

`zhihu/web/user-info` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves public profile metrics and details for a Zhihu user. Returns article counts, answer counts, follower totals, and user account metadata.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/user-info", "user_url_token": "ming-he-43-93"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/user-info', {'user_url_token': 'ming-he-43-93'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/user-info", {
  "user_url_token": "ming-he-43-93"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/user-info", sandbase.Params{
	"user_url_token": "ming-he-43-93",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_url_token` | string | yes | User ID  |

## Details

Returns the public profile of a Zhihu user, including display name, headline, answer and article counts, and follower count. It needs one input, the user's `user_url_token`, which is the slug in the profile URL.

### Use cases

- Track a Zhihu author's follower count and content totals over time.
- Check whether an account is a real-name verified personal account or an organization before outreach.
- Show a creator's name, headline, and avatar on an external dashboard.
- Build a profile record from a known `url_token` before pulling that user's answers or articles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_url_token": "ming-he-43-93"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_url_token` | string | Yes | User ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ai_assistant_info": null,
  "allow_message": true,
  "answer_count": 9,
  "articles_count": 87,
  "available_medals_count": 0,
  "avatar_url": "https://pic1.zhimg.com/v2-60386d319ef90da6904da4fe604bc48f_xl.jpg?source=32738c0…",
  "avatar_url_template": "https://picx.zhimg.com/v2-60386d319ef90da6904da4fe604bc48f_l.jpg?source=32738c0c…",
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
  "follower_count": 2830
}
```

### Response fields

| Field | Meaning |
|---|---|
| `name / headline` | Display name and short self-description of the user. |
| `url_token` | The user's profile slug. It matches the `user_url_token` you sent. |
| `id` | Internal hash ID of the user account. |
| `follower_count` | Number of followers as an integer. `follower_count_text` and `follower_count_num` give the same value as strings. |
| `answer_count / articles_count` | Number of answers and number of articles the user has published. |
| `project_count / available_medals_count` | Count of the user's projects and of medals available on the account. |
| `is_realname / is_org / is_advertiser` | Flags that show whether the account is real-name verified, an organization, or an advertiser. |
| `vip_info.is_vip / kvip_info.is_vip` | Flags that show whether the user holds a VIP membership. |
| `gender` | Numeric gender code. This example returns `1`. |
| `avatar_url / url` | Link to the avatar image and to the user's profile API URL. |

### Notes

- Take `user_url_token` from the end of a Zhihu profile URL, such as `ming-he-43-93` in `zhihu.com/people/ming-he-43-93`.
- `ip_info` can return a placeholder text when the location is not known.
- To list this user's content, call [Zhihu User Answers](/apis/zhihu/web/user-answers) or [Zhihu User Articles](/apis/zhihu/web/user-articles) with the same token.
- To see who this user follows or who follows them, use [Zhihu User Followees](/apis/zhihu/web/user-followees).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/user-info.json`](../../../../catalog/models/zhihu/web/user-info.json) · Store page: https://www.sandbase.ai/model/zhihu/web/user-info
