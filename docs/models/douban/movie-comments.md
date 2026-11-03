# Douban Movie Short Comments API: pricing, parameters and code examples

`douban/movie-comments` · data API · Douban · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Short comments (one-line reviews) on a Douban movie or TV subject with rating, user and location, sorted by time or score.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douban/movie-comments", "subjectId": "1292052"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douban/movie-comments', {'subjectId': '1292052'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douban/movie-comments", {
  "subjectId": "1292052"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douban/movie-comments", sandbase.Params{
	"subjectId": "1292052",
})
```

Same call via the path form: `POST /v1/api/douban/movie-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `sort` | string |  | Sort order for the result set. one of: `time`, `new_score`; default `"time"` |
| `subjectId` | string | yes | The unique ID for a movie or TV subject on Douban.  |

## Details

Returns short one-line comments for a Douban movie or TV subject. Each comment includes the text, the user's rating label, the user name and a location. The API needs the Douban `subjectId`.

### Use cases

- Collect audience reactions to a film such as the one with `subjectId` `1292052` for sentiment analysis.
- Compare the newest comments against the top-scored comments by switching `sort` between `time` and `new_score`.
- Count how many commenters give each rating label to gauge how a title is received.
- Group comments by `location` to see which Chinese regions discuss a title.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douban/movie-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"subjectId": "1292052"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subjectId` | string | Yes | The unique ID for a movie or TV subject on Douban. |
| `page` | integer | No | Page number for pagination. |
| `sort` | string | No | Sort order for the result set. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comments": [
    {
      "avatar": "https://img3.doubanio.com/icon/u210199036-3.webp",
      "cid": "4980937286",
      "content": "牢狱困得住躯体，困不住希望。安迪以漫长时光守住内心，告诉我们自由从不在高墙之外，而永不熄灭的信念本身就是救赎。",
      "location": "安徽",
      "rating": "推荐",
      "time": "",
      "username": "大喊一声啦啦啦",
      "vote_count": 0
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[]` | List of short comments on the subject. Each item is one comment. |
| `comments[].cid` | ID of the comment, returned as a string. |
| `comments[].content` | Text of the short comment. |
| `comments[].rating` | Rating label the user gave, such as `推荐` or `力荐`. It is a text label, not a number. |
| `comments[].username` | Display name of the user who wrote the comment. |
| `comments[].avatar` | URL of the user's avatar image. |
| `comments[].location` | Location shown for the user, such as a province name. |
| `comments[].vote_count` | Number of votes the comment received. |
| `comments[].time` | Time field of the comment. It was an empty string in the sample response. |

### Notes

- Find the `subjectId` with [Douban Recent Hot Movie](/apis/douban/recent-hot-movie) or [Douban Recent Hot Tv](/apis/douban/recent-hot-tv). Use [Douban Subject Details](/apis/douban/subject-detail) for the title's own data.
- `sort` accepts `time` (default) or `new_score`. Use `page` to get more comments, starting at `1`.
- For longer reviews, call [Douban Movie Reviews](/apis/douban/movie-reviews).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/douban/movie-comments.json`](../../../catalog/models/douban/movie-comments.json) · Store page: https://www.sandbase.ai/model/douban/movie-comments
