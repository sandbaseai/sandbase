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

Access subreddit channel metadata and flair templates using `subreddit_name`, with options for `sort` and `range` filtering.

### Use cases

- Retrieve post channel and flair templates for a community.
- Inspect subreddit channel settings sorted by hot or top activity.
- Extract flair identifiers to categorize community posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/subreddit-post-channels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sort` | string | No | Sort method, supports HOT, NEW, TOP, CONTROVERSIAL, RISING |
| `range` | string | No | Time range, supports HOUR, DAY, WEEK, MONTH, YEAR, ALL |
| `need_format` | boolean | No | Whether to clean and format the data |
| `subreddit_name` | string | No | Subreddit name |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "subredditInfoByName": {
    "postFlairTemplates": [
      {
        "id": "f988392c-41f4-11ea-856e-0e3f43166111",
        "text": "Arts/Crafts"
      }
    ]
  }
}
```

### Notes

- Supported `sort` values include HOT, NEW, TOP, CONTROVERSIAL, and RISING.
- Supported `range` values include HOUR, DAY, WEEK, MONTH, YEAR, and ALL.
- Set `need_format` to true to return cleaned and formatted data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/subreddit-post-channels.json`](../../../../catalog/models/reddit/app/subreddit-post-channels.json) · Store page: https://www.sandbase.ai/model/reddit/app/subreddit-post-channels
