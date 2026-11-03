# Twitter (X) Tweet Comments API: pricing, parameters and code examples

`twitter/web/post-comments` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comment threads and replies under a specified tweet. Provide a tweet ID and paginate through conversations using cursor values.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/post-comments", "tweet_id": "2107237881668313108"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/post-comments', {'tweet_id': '2107237881668313108'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/post-comments", {
  "tweet_id": "2107237881668313108"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/post-comments", sandbase.Params{
	"tweet_id": "2107237881668313108",
})
```

Same call via the path form: `POST /v1/api/twitter/web/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the last request  |
| `tweet_id` | string | yes | Tweet ID  |

## Details

Retrieve discussion threads and replies for a specific post by providing `tweet_id`. Use the optional `cursor` parameter to browse through multiple pages of replies.

### Use cases

- Read public audience replies and conversations under a specific tweet.
- Track engagement metrics such as reply likes and view counts.
- Monitor user interactions and follow-up threads on brand announcements.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tweet_id": "2107237881668313108"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tweet_id` | string | Yes | Tweet ID |
| `cursor` | string | No | Cursor, default is None, used for paging, obtained from the last request |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "thread": [
    {
      "conversation_id": "2107237881668313108",
      "display_text": ".@grok what’s the most important thing that’s ever been discovered on the ISS?",
      "id": "2107269640590070134",
      "likes": 1,
      "status": "active",
      "text": "@NASA @Space_Station @SpaceX .@grok what’s the most important thing that’s ever been disc…",
      "views": "795",
      "author": {
        "blue_verified": true,
        "name": "SavingPrivateBryan",
        "rest_id": "1865856717839339520",
        "screen_name": "<user>"
      }
    }
  ]
}
```

### Notes

- Requires `tweet_id` to identify the post.
- Use `cursor` from the previous response to paginate through additional comments.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Twitter (X) Latest Tweet Comments](/apis/twitter/web/latest-post-comments): Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.
- [Twitter (X) Retweet User List](/apis/twitter/web/retweet-user-list): Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.
- [Twitter (X) Search](/apis/twitter/web/search-timeline): Search Twitter / X posts by keyword and get tweets with text, author, time and engagement counts (likes, retweets, replies, views).

---
Machine-readable: [`catalog/models/twitter/web/post-comments.json`](../../../../catalog/models/twitter/web/post-comments.json) · Store page: https://www.sandbase.ai/model/twitter/web/post-comments
