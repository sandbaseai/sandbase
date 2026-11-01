# Twitter (X) Latest Tweet Comments

`twitter/web/latest-post-comments` · api · Twitter

Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/latest-post-comments", "tweet_id": "2107237881668313108"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/latest-post-comments', {'tweet_id': '2107237881668313108'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/latest-post-comments", {
  "tweet_id": "2107237881668313108"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/latest-post-comments", sandbase.Params{
	"tweet_id": "2107237881668313108",
})
```

Same call via the path form: `POST /v1/api/twitter/web/latest-post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the last request  |
| `tweet_id` | string | yes | Tweet ID  |

## Details

Retrieve recent replies for a target post by providing `tweet_id`. Use the optional `cursor` parameter to step through paginated comment timelines.

### Use cases

- Monitor audience discussions and replies on specific posts.
- Track recent public reactions to announcements or news.
- Gather reply threads for sentiment analysis workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/latest-post-comments" \
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
  "timeline": [
    {
      "conversation_id": "2107237881668313108",
      "in_reply_to_screen_name": "NASA",
      "in_reply_to_status_id_str": "2107237881668313108",
      "in_reply_to_user_id_str": "11348282",
      "screen_name": "<user>",
      "text": "@NASA @Space_Station @SpaceX Nearly eight months in space and they're finally coming home…",
      "tweet_id": "2107450375645351938",
      "type": "tweet",
      "views": "6",
      "user_info": {
        "favorites_count": 1948,
        "followers_count": 157,
        "name": "Anup",
        "rest_id": "1695754196",
        "screen_name": "<user>",
        "verified": true
      }
    }
  ]
}
```

### Notes

- Supply `cursor` from the prior response to page through additional comments.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Twitter (X) Tweet Comments](/model/twitter/web/post-comments): Returns comment threads and replies under a specified tweet.
- [Twitter (X) Retweet User List](/model/twitter/web/retweet-user-list): Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.
- [Twitter (X) Search](/model/twitter/web/search-timeline): Search Twitter / X posts by keyword and get tweets with text, author, time and engagement counts (likes, retweets, replies, views).

---
Machine-readable: [`catalog/models/twitter/web/latest-post-comments.json`](../../../../catalog/models/twitter/web/latest-post-comments.json) · Store page: https://www.sandbase.ai/model/twitter/web/latest-post-comments
