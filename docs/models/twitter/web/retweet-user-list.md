# Twitter (X) Retweet User List API: pricing, parameters and code examples

`twitter/web/retweet-user-list` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/retweet-user-list", "tweet_id": "2107237881668313108"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/retweet-user-list', {'tweet_id': '2107237881668313108'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/retweet-user-list", {
  "tweet_id": "2107237881668313108"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/retweet-user-list", sandbase.Params{
	"tweet_id": "2107237881668313108",
})
```

Same call via the path form: `POST /v1/api/twitter/web/retweet-user-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the last request  |
| `tweet_id` | string | yes | Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in https://x.com/elonmusk/status/1808168603721650364  |

## Details

Fetch the accounts that reposted a post by supplying its `tweet_id`. Use the optional `cursor` parameter to navigate through paginated results.

### Use cases

- Analyze audience reach and engagement for specific posts.
- Identify influencers and active followers who amplify content.
- Monitor distribution networks and sharing patterns across the platform.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/retweet-user-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tweet_id": "2107237881668313108"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tweet_id` | string | Yes | Tweet ID, can be obtained from the tweet link. |
| `cursor` | string | No | Cursor, default is None, used for paging, obtained from the last request |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "retweets": [
    {
      "followers_count": 1076,
      "friends_count": 1708,
      "media_count": 3809,
      "name": "Francisco Javier",
      "screen_name": "<user>",
      "statuses_count": 80694,
      "user_id": "<user>"
    }
  ]
}
```

### Notes

- Find the `tweet_id` directly inside the URL of the post status.
- Use `cursor` from the previous response to paginate through subsequent user records.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Twitter (X) Latest Tweet Comments](/apis/twitter/web/latest-post-comments): Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.
- [Twitter (X) Tweet Comments](/apis/twitter/web/post-comments): Returns comment threads and replies under a specified tweet.
- [Twitter (X) Search](/apis/twitter/web/search-timeline): Search Twitter / X posts by keyword and get tweets with text, author, time and engagement counts (likes, retweets, replies, views).

---
Machine-readable: [`catalog/models/twitter/web/retweet-user-list.json`](../../../../catalog/models/twitter/web/retweet-user-list.json) · Store page: https://www.sandbase.ai/model/twitter/web/retweet-user-list
