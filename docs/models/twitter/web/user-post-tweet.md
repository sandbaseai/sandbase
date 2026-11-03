# Twitter (X) User Posts API: pricing, parameters and code examples

`twitter/web/user-post-tweet` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns posts and tweets from a specified Twitter (X) user timeline. Users can be identified by either their screen name or numeric user ID, with cursor pagination supported.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-post-tweet", "screen_name": "sandbaseai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-post-tweet', {'screen_name': 'sandbaseai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-post-tweet", {
  "screen_name": "sandbaseai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-post-tweet", sandbase.Params{
	"screen_name": "sandbaseai",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-post-tweet` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the JSON in the last request.  |
| `rest_id` | integer |  | User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected.  |
| `screen_name` | string |  | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk  |

## Details

Retrieve a user's timeline posts using either their `screen_name` or numeric `rest_id`. You can paginate through older posts using the `cursor` parameter.

### Use cases

- Archive public tweets and posts from a specific profile.
- Monitor recent timeline activity for designated accounts.
- Analyze posting frequency and timeline history for public figures.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-post-tweet" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"screen_name": "elonmusk", "rest_id": 44196397}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Cursor, default is None, used for paging, obtained from the JSON in the last request. |
| `rest_id` | integer | No | User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. |
| `screen_name` | string | No | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk |

### Notes

- Provide either `rest_id` or `screen_name`; if `rest_id` is specified, `screen_name` is ignored.
- Pass `cursor` from the previous response payload to page through timeline results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Twitter (X) Latest Tweet Comments](/apis/twitter/web/latest-post-comments): Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.
- [Twitter (X) Tweet Comments](/apis/twitter/web/post-comments): Returns comment threads and replies under a specified tweet.
- [Twitter (X) Retweet User List](/apis/twitter/web/retweet-user-list): Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.

---
Machine-readable: [`catalog/models/twitter/web/user-post-tweet.json`](../../../../catalog/models/twitter/web/user-post-tweet.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-post-tweet
