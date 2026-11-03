# Zhihu User Follow Collections API: pricing, parameters and code examples

`zhihu/user-follow-collections` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get Zhihu collections followed by a user, with offset pagination. Use it to browse the collections associated with a known account's follow activity.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/user-follow-collections", "userUrlToken": "excited-vczh"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/user-follow-collections', {'userUrlToken': 'excited-vczh'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/user-follow-collections", {
  "userUrlToken": "excited-vczh"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/user-follow-collections", sandbase.Params{
	"userUrlToken": "excited-vczh",
})
```

Same call via the path form: `POST /v1/api/zhihu/user-follow-collections` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Start offset, begins with 0. default `0` |
| `userUrlToken` | string | yes | Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.  |

## Details

Returns the Zhihu collections that a given user follows. Each item includes the collection's title, description, counts, and creator. The only required input is the user's `userUrlToken`.

### Use cases

- List the collections a known Zhihu account follows to see which topics and curators they pay attention to.
- Rank followed collections by `follower_count` to find the most popular ones in a user's list.
- Collect creator IDs and headlines from followed collections to find curators in a niche.
- Page through a user's full follow list with `offset` and store the collection IDs for later tracking.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/user-follow-collections" \
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
      "answer_count": 1050,
      "comment_count": 215,
      "created_time": 1505443114,
      "creator": {
        "avatar_url": "https://pic1.zhimg.com/v2-6cb9ef28ccf4f0c49024521f2aacef50_l.jpg?source=b1748391",
        "avatar_url_template": "https://pic1.zhimg.com/v2-6cb9ef28ccf4f0c49024521f2aacef50.jpg?source=b1748391",
        "badge": [
          {
            "description": "优秀回答者",
            "type": "best_answerer"
          }
        ],
        "gender": 1,
        "headline": "总有一天，我要把中国大好河山看遍，然后从地球科学视角讲给你听",
        "id": "c39f4121c89698006dd97f020769c19b",
        "is_advertiser": false,
        "is_org": false
      },
      "description": "致力于收藏违背事实证据的、缺乏科学证据的、违反科学方法的、声称推翻教材的、声称推翻某学科大厦的内容。不收迷信和宗教，欢迎带着简单的依据艾特我。",
      "follower_count": 17273,
      "id": 186197750,
      "is_following": false,
      "is_public": true,
      "title": "存在科学错误系列——地科主场及其他",
      "type": "collection",
      "updated_time": 1727150595
    }
  ],
  "paging": {
    "is_end": true,
    "is_start": true,
    "next": "http://www.zhihu.com/api/v4/members/excited-vczh/following-favlists?include=data…",
    "previous": "http://www.zhihu.com/api/v4/members/excited-vczh/following-favlists?include=data…",
    "totals": 9
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].id` | Numeric ID of the collection. It is also the last part of the collection `url`. |
| `data[].title / data[].description` | Name of the collection and the text its creator wrote about it. `description` can be an empty string. |
| `data[].answer_count / data[].comment_count` | Number of answers saved in the collection and number of comments on it. |
| `data[].follower_count` | Number of users who follow the collection. |
| `data[].created_time / data[].updated_time` | Unix timestamps in seconds for when the collection was created and last updated. |
| `data[].is_public / data[].is_following` | Whether the collection is public, and whether the current viewer follows it. |
| `data[].creator.id / data[].creator.headline` | ID and profile headline of the user who owns the collection. |
| `data[].creator.badge[].description` | Badge text shown on the creator, such as `优秀回答者`. The list is empty when the creator has no badge. |
| `data[].creator.is_org / data[].creator.is_advertiser` | Flags that show whether the creator is an organization account or an advertiser account. |
| `paging.totals` | Total number of followed collections for this user. |

### Notes

- Take `userUrlToken` from a profile URL: it is the part after `zhihu.com/people/`. You can also look it up with [Zhihu User Info](/apis/zhihu/user-info).
- Pass `offset` starting at `0` to page through results. `paging.is_end` is `true` when there are no more pages.
- `paging.next` and `paging.previous` hold the platform's own page URLs. Use `offset` in your request instead.
- To list collections the user created rather than followed, call [Zhihu User Collections](/apis/zhihu/web/user-collections).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/zhihu/user-follow-collections.json`](../../../catalog/models/zhihu/user-follow-collections.json) · Store page: https://www.sandbase.ai/model/zhihu/user-follow-collections
