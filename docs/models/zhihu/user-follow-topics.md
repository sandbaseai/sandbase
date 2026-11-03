# Zhihu User Follow Topics API: pricing, parameters and code examples

`zhihu/user-follow-topics` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get Zhihu topics followed by a user, with offset pagination. Use it to browse the topics associated with a known account's follow activity.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/user-follow-topics", "userUrlToken": "excited-vczh"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/user-follow-topics', {'userUrlToken': 'excited-vczh'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/user-follow-topics", {
  "userUrlToken": "excited-vczh"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/user-follow-topics", sandbase.Params{
	"userUrlToken": "excited-vczh",
})
```

Same call via the path form: `POST /v1/api/zhihu/user-follow-topics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Start offset, begins with 0. default `0` |
| `userUrlToken` | string | yes | Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.  |

## Details

Returns the Zhihu topics a user follows, 20 per page by default. It needs the user's `userUrlToken`, the value in `zhihu.com/people/{userUrlToken}`. Each item includes the topic's name data such as description, follower count and discussion count.

### Use cases

- List the topics a known Zhihu account follows to see what subjects it cares about.
- Compare follower and discussion counts across followed topics to find the busiest communities.
- Collect topic IDs from a user's follow list to feed topic research or tracking.
- Group a user's followed topics by `category` to see how their interests split.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/user-follow-topics" \
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
      "contributions_count": 0,
      "topic": {
        "avatar_url": "https://pic1.zhimg.com/v2-40e779d5c5e6bcebda41e92d50594618.jpg?source=57bbeac9",
        "category": "basic",
        "discuss_count": "12858",
        "excerpt": "天体生物学，是一门研究在宇宙中生命起源、生物演化、分布和未来发展的交叉学科，并不只限于地外生物，或包括对地球生物的研究。在天体物理学上，指研究天体上存在生物的条…",
        "followers_count": 2065,
        "foot_line": {
          "content": "2065 关注 · 1.2 万讨论"
        },
        "id": "20015598",
        "introduction": "天体生物学，是一门研究在宇宙中生命起源、生物演化、分布和未来发展的交叉学科，并不只限于地外生物，或包括对地球生物的研究。在天体物理学上，指研究天体上存在生物的条…"
      }
    }
  ],
  "paging": {
    "is_end": false,
    "is_start": true,
    "next": "https://www.zhihu.com/api/v5.1/topics/excited-vczh/following_topics_contribution…",
    "previous": "https://www.zhihu.com/api/v5.1/topics/excited-vczh/following_topics_contribution…",
    "totals": 50
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].topic.id` | Topic ID as a string. |
| `data[].topic.category` | Topic category label, such as `basic` or `n_game`. |
| `data[].topic.excerpt / data[].topic.introduction` | Short text describing the topic. Both can be empty for some topics. |
| `data[].topic.followers_count` | Number of followers of the topic, as an integer. |
| `data[].topic.discuss_count` | Number of discussions on the topic, returned as a string. |
| `data[].topic.foot_line.content` | Display text that combines the follower and discussion counts, for example `2065 关注 · 1.2 万讨论`. |
| `data[].topic.avatar_url` | Image URL for the topic avatar. |
| `data[].contributions_count` | Contribution count attached to each followed topic. It is `0` in all items shown. |
| `paging.totals` | Total number of followed topics for this user. |
| `paging.is_end / paging.is_start` | Flags that show whether this page is the last or the first page. |

### Notes

- Take `userUrlToken` from the profile URL, as in `zhihu.com/people/excited-vczh`.
- Page through results with `offset`, which starts at 0. The `paging.next` URL shows the next page uses `offset=20` with `limit=20`.
- Stop paging when `paging.is_end` is `true`.
- To look up the account itself, call [Zhihu User Info](/apis/zhihu/user-info).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/zhihu/user-follow-topics.json`](../../../catalog/models/zhihu/user-follow-topics.json) · Store page: https://www.sandbase.ai/model/zhihu/user-follow-topics
