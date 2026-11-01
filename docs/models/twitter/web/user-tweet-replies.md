# Twitter (X) User Tweet Replies

`twitter/web/user-tweet-replies` · api · Twitter

Returns a timeline of replies posted by a specific Twitter user. Filter by username and paginate through responses using cursor tokens.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-tweet-replies", "screen_name": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-tweet-replies', {'screen_name': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-tweet-replies", {
  "screen_name": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-tweet-replies", sandbase.Params{
	"screen_name": "example",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-tweet-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the last request  |
| `screen_name` | string | yes | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk  |

## Details

Retrieve reply tweets from a designated account using the `screen_name` parameter. Pass a `cursor` value to paginate through earlier reply history.

### Use cases

- Monitor conversational engagement from a brand or competitor profile.
- Archive customer support responses and thread interactions for a user.
- Analyze communication patterns and reply volume across accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-tweet-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"screen_name": "NASA"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `screen_name` | string | Yes | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk |
| `cursor` | string | No | Cursor, default is None, used for paging, obtained from the last request |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "timeline": [
    {
      "conversation_id": "2107095768821576019",
      "in_reply_to_status_id_str": "2107095768821576019",
      "text": "@NASA I know this is a replay. My brain still does the little 'please work' thing.",
      "tweet_id": "2107144593343189432",
      "views": "4115",
      "author": {
        "blue_verified": true,
        "name": "Mohammed Siddiq",
        "rest_id": "1913390828405628928",
        "screen_name": "<user>"
      }
    }
  ]
}
```

### Notes

- `screen_name` can be extracted directly from a profile URL (for example, elonmusk from https://twitter.com/elonmusk).
- Use the `cursor` returned from the prior response to navigate pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Twitter (X) Latest Tweet Comments](/model/twitter/web/latest-post-comments): Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.
- [Twitter (X) Tweet Comments](/model/twitter/web/post-comments): Returns comment threads and replies under a specified tweet.
- [Twitter (X) Retweet User List](/model/twitter/web/retweet-user-list): Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.

---
Machine-readable: [`catalog/models/twitter/web/user-tweet-replies.json`](../../../../catalog/models/twitter/web/user-tweet-replies.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-tweet-replies
