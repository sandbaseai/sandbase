# Zhihu Recommended Followees API: pricing, parameters and code examples

`zhihu/web/recommend-followees` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of recommended users to follow on Zhihu. Access personalized author and contributor suggestions directly from Zhihu web.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/recommend-followees"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/recommend-followees', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/recommend-followees", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/recommend-followees", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/zhihu/web/recommend-followees` with the body above minus `model`.

## Details

Returns a list of Zhihu users that Zhihu recommends the current account to follow. It needs no input: send an empty JSON object `{}`.

### Use cases

- Show a list of suggested Zhihu accounts in an onboarding or discovery screen.
- Collect creators tagged with a topic area, such as AI or technology, using the `reason` text.
- Find verified and official accounts by reading the badge fields.
- Build a seed list of user IDs to look up in more detail.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/recommend-followees" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "actor": {
        "avatar_url": "https://picx.zhimg.com/v2-e8a4e76a1420ca566c932936ad0f04d6_l.jpg?source=a0c391dc",
        "badge": [],
        "badge_v2": {
          "detail_badges": null,
          "merged_badges": [],
          "title": ""
        },
        "description": "",
        "exposed_medal": {
          "avatar_url": "https://pic1.zhimg.com/v2-340c50d93c8821c172477e82f0f4e08e_720w.jpg?source=a0c39…",
          "medal_avatar_frame": "",
          "medal_id": "972473506181627904"
        },
        "gender": -1,
        "headline": "靠谱科普 就看果壳",
        "id": "486e2e8a3d77380f1607d6de0fd27c10"
      },
      "attached_info": "",
      "personal_desc": "靠谱科普 就看果壳",
      "reason": "「人工智能」领域答主"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One recommended user. Each item holds the user details in `actor` and the reason for the suggestion. |
| `data[].actor.id` | The user's ID, a 32-character hex string. Use it to look up the user in other Zhihu APIs. |
| `data[].actor.headline` | The short tagline shown under the user's name. |
| `data[].actor.description` | The user's profile description. It can be an empty string. |
| `data[].actor.avatar_url` | Link to the user's avatar image. |
| `data[].reason` | Why Zhihu suggests this user, for example a topic area the user answers in or `你可能感兴趣` (you may be interested). |
| `data[].personal_desc` | A short description of the user. It often matches the headline or the badge text. |
| `data[].actor.badge[].description / data[].actor.badge_v2.title` | The verified identity text of the user, such as an official account or a job title. Both are empty when the user has no badge. |
| `data[].actor.badge_v2.merged_badges[].badge_status` | Verification status of the badge. The sample shows `passed`. |
| `data[].actor.is_followed` | Whether the current account already follows this user. It does not appear on every item. |

### Notes

- The request takes no parameters, so send `{}` as the body.
- The sample response has no pagination fields.
- Take `data[].actor.id` and pass it to [Zhihu Web User Profile](/apis/zhihu/web/user-info) for the full profile.
- Use [Zhihu User Answers](/apis/zhihu/web/user-answers) to read what a recommended user has written.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/recommend-followees.json`](../../../../catalog/models/zhihu/web/recommend-followees.json) · Store page: https://www.sandbase.ai/model/zhihu/web/recommend-followees
