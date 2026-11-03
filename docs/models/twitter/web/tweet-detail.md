# Twitter Tweet Detail API: pricing, parameters and code examples

`twitter/web/tweet-detail` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get a single tweet (X post) by ID: full text, author, media, and like, retweet, reply, quote, bookmark and view counts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/tweet-detail", "tweet_id": "1808168603721650364"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/tweet-detail', {'tweet_id': '1808168603721650364'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/tweet-detail", {
  "tweet_id": "1808168603721650364"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/tweet-detail", sandbase.Params{
	"tweet_id": "1808168603721650364",
})
```

Same call via the path form: `POST /v1/api/twitter/web/tweet-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tweet_id` | string | yes | Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in https://x.com/elonmusk/status/1808168603721650364  |

## Details

Pass a tweet ID and get the full post as JSON, including author details, media attachments and engagement metrics.

### Use cases

- Track engagement on specific posts over time.
- Enrich tweet IDs from search results with full details.
- Archive posts referenced in reports.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/tweet-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tweet_id": "1808168603721650364"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tweet_id` | string | Yes | Tweet ID, can be obtained from the tweet link. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "id": "1808168603721650364",
  "created_at": "Tue Jul 02 15:59:23 +0000 2024",
  "lang": "en",
  "likes": 282804,
  "retweets": 52252,
  "replies": 18666,
  "quotes": 3899,
  "bookmarks": 6568,
  "views": "53721665",
  "text": "<tweet text>",
  "author": {
    "screen_name": "<user>",
    "rest_id": "<user id>"
  },
  "media": [
    "…"
  ]
}
```

### Notes

- The tweet ID is the number after `/status/` in the post URL.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Twitter (X) Search](/apis/twitter/web/search-timeline): Search Twitter / X posts by keyword and get tweets with text, author, time and engagement counts (likes, retweets, replies, views).
- [Twitter (X) Trending Topics](/apis/twitter/web/trending): Get trending topics on Twitter / X by country: trend names with their category context, for the United States, Japan, India, the UK and other markets.
- [Twitter (X) User Profile](/apis/twitter/web/user-profile): Get a Twitter / X user profile by screen name or user ID: name, bio, follower and following counts, post and media counts, verification and creation date.

---
Machine-readable: [`catalog/models/twitter/web/tweet-detail.json`](../../../../catalog/models/twitter/web/tweet-detail.json) · Store page: https://www.sandbase.ai/model/twitter/web/tweet-detail
