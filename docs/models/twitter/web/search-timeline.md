# Twitter (X) Search API: pricing, parameters and code examples

`twitter/web/search-timeline` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Search Twitter / X posts by keyword and get tweets with text, author, time and engagement counts (likes, retweets, replies, views). Supports Top, Latest, Media, People and Lists results.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/search-timeline", "keyword": "AI agents", "search_type": "Top"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/search-timeline', {'keyword': 'AI agents', 'search_type': 'Top'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/search-timeline", {
  "keyword": "AI agents",
  "search_type": "Top"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/search-timeline", sandbase.Params{
	"keyword": "AI agents",
	"search_type": "Top",
})
```

Same call via the path form: `POST /v1/api/twitter/web/search-timeline` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the last request  |
| `keyword` | string | yes | Search keyword  |
| `search_type` | string |  | Search type, default is Top, other optional values are Latest, Media, People, Lists default `"Top"` |

## Details

Search X (Twitter) for a keyword or query and get matching tweets with author, text, timestamps and engagement metrics. Switch between Top, Latest, Media, People and Lists tabs.

### Use cases

- Monitor brand, product or competitor mentions on X.
- Collect the latest tweets about an event with `search_type=Latest`.
- Find influential accounts discussing a topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/search-timeline" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `cursor` | string | No | Cursor, default is None, used for paging, obtained from the last request |
| `search_type` | string | No | Search type, default is Top, other optional values are Latest, Media, People, Lists |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "status": "ok",
  "next_cursor": "<cursor>",
  "timeline": [
    {
      "tweet_id": "2104987422308335828",
      "screen_name": "OpenAI",
      "created_at": "Tue Sep 29 17:31:24 +0000 2026",
      "lang": "en",
      "favorites": 4456,
      "retweets": 315,
      "replies": 256,
      "quotes": 131,
      "bookmarks": 1224,
      "views": "570812",
      "text": "Codex Security Cloud is getting a major upgrade, with access to cyber-capable models thro…"
    }
  ]
}
```

### Notes

- Paginate with `cursor` from the previous response (`next_cursor`).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Get the latest tweet comments](/model/twitter/web/latest-post-comments): Get the latest tweet comments.
- [Get comments](/model/twitter/web/post-comments): Get comments under the tweet.
- [ReTweet User list](/model/twitter/web/retweet-user-list): Get ReTweet User list.

---
Machine-readable: [`catalog/models/twitter/web/search-timeline.json`](../../../../catalog/models/twitter/web/search-timeline.json) · Store page: https://www.sandbase.ai/model/twitter/web/search-timeline
