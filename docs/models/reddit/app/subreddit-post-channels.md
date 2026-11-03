# Reddit App Subreddit Post Channels API: pricing, parameters and code examples

`reddit/app/subreddit-post-channels` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns post channel and flair details for a target subreddit. Supports custom sort methods and time range filters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/subreddit-post-channels", "need_format": false, "range": "DAY", "sort": "HOT", "subreddit_name": "pics"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/subreddit-post-channels', {'need_format': False, 'range': 'DAY', 'sort': 'HOT', 'subreddit_name': 'pics'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/subreddit-post-channels", {
  "need_format": false,
  "range": "DAY",
  "sort": "HOT",
  "subreddit_name": "pics"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/subreddit-post-channels", sandbase.Params{
	"need_format": false,
	"range": "DAY",
	"sort": "HOT",
	"subreddit_name": "pics",
})
```

Same call via the path form: `POST /v1/api/reddit/app/subreddit-post-channels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort method, supports HOT, NEW, TOP, CONTROVERSIAL, RISING default `"HOT"` |
| `range` | string |  | Time range, supports HOUR, DAY, WEEK, MONTH, YEAR, ALL default `"DAY"` |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `subreddit_name` | string |  | Subreddit name default `"pics"` |

## Details

Returns the post flair templates for a subreddit. You send the subreddit name in `subreddit_name`. The request also accepts `sort`, `range` and `need_format`.

### Use cases

- List every flair a subreddit offers so a posting tool can show a flair picker.
- Find which flairs are restricted to moderators before you submit a post.
- Map flair `id` values to their `text` labels when you group posts by category.
- Compare the flair sets of several communities to see how each one organizes its posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/subreddit-post-channels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `need_format` | boolean | No | Whether to clean and format the data |
| `range` | string | No | Time range, supports HOUR, DAY, WEEK, MONTH, YEAR, ALL |
| `sort` | string | No | Sort method, supports HOT, NEW, TOP, CONTROVERSIAL, RISING |
| `subreddit_name` | string | No | Subreddit name |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "subredditInfoByName": {
    "__typename": "Subreddit",
    "postFlairTemplates": [
      {
        "id": "260873e0-c9b8-11e5-be06-0ecbb6f4dd8d",
        "isModOnly": false,
        "richtext": null,
        "text": "Politics"
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `subredditInfoByName` | Top-level object for the requested subreddit. |
| `subredditInfoByName.__typename` | Object type. The value is `Subreddit`. |
| `subredditInfoByName.postFlairTemplates[]` | List of post flair templates that the subreddit defines. |
| `subredditInfoByName.postFlairTemplates[].id` | Unique ID of the flair template, in UUID format. |
| `subredditInfoByName.postFlairTemplates[].text` | Display label of the flair, such as `Politics` or `Backstory`. |
| `subredditInfoByName.postFlairTemplates[].isModOnly` | Boolean. When `true`, only moderators can use this flair. In the sample it is `false` for every flair. |
| `subredditInfoByName.postFlairTemplates[].richtext` | Rich text version of the flair label. It is `null` in the sample, so the plain `text` field holds the label. |

### Notes

- The sample request sent an empty body, so the defaults applied: `subreddit_name` is `pics`, `sort` is `HOT`, `range` is `DAY` and `need_format` is `false`.
- `sort` accepts `HOT`, `NEW`, `TOP`, `CONTROVERSIAL` and `RISING`. `range` accepts `HOUR`, `DAY`, `WEEK`, `MONTH`, `YEAR` and `ALL`.
- To read the posts in a subreddit, call [Reddit Subreddit Feed](/apis/reddit/app/subreddit-feed). For general community details, use [Reddit App Subreddit Info](/apis/reddit/app/subreddit-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/subreddit-post-channels.json`](../../../../catalog/models/reddit/app/subreddit-post-channels.json) · Store page: https://www.sandbase.ai/model/reddit/app/subreddit-post-channels
