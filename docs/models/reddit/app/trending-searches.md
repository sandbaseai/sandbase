# Reddit App Trending Searches API: pricing, parameters and code examples

`reddit/app/trending-searches` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns currently trending search queries and topics from the Reddit mobile application, with an option to clean and format the output data.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/trending-searches", "need_format": true}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/trending-searches', {'need_format': True})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/trending-searches", {
  "need_format": true
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/trending-searches", sandbase.Params{
	"need_format": true,
})
```

Same call via the path form: `POST /v1/api/reddit/app/trending-searches` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | Whether to clean and format the data default `false` |

## Details

Retrieve real-time trending search queries from the Reddit app. Use `need_format` to specify whether the response data should be cleaned and formatted.

### Use cases

- Monitor popular and emerging search queries across Reddit.
- Power search recommendation interfaces with real-time platform trends.
- Track shifts in user interest and breaking discussion topics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/trending-searches" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `need_format` | boolean | No | Whether to clean and format the data |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "trendingQueries": [
    {
      "displayQuery": "Administrative Petition for Correction Automated System",
      "id": "Administrative Petition for Correction Automated System",
      "rawQuery": "Administrative Petition for Correction Automated System"
    }
  ]
}
```

### Notes

- Use `need_format` to control whether the query data is cleaned and formatted.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/trending-searches.json`](../../../../catalog/models/reddit/app/trending-searches.json) · Store page: https://www.sandbase.ai/model/reddit/app/trending-searches
