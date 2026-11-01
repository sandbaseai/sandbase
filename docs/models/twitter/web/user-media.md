# Twitter (X) User Media

`twitter/web/user-media` · api · Twitter

Returns media posts and timeline items for a specified user profile, queried by screen name or user ID. Supports cursor-based pagination for browsing past media posts.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-media", "screen_name": "NASA"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-media', {'screen_name': 'NASA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-media", {
  "screen_name": "NASA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-media", sandbase.Params{
	"screen_name": "NASA",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-media` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the `next_cursor` in the last request  |
| `rest_id` | integer |  | User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected.  |
| `screen_name` | string | yes | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk  |

## Details

Retrieve a user's media timeline using their `screen_name` or `rest_id`. Page through additional media results with the `cursor` parameter.

### Use cases

- Browse photos and videos shared by a specific account.
- Archive media posts from a public profile timeline.
- Track recent multimedia assets shared by organizations or creators.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-media" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"screen_name": "NASA"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `screen_name` | string | Yes | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk |
| `cursor` | string | No | Cursor, default is None, used for paging, obtained from the `next_cursor` in the last request |
| `rest_id` | integer | No | User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "timeline": [
    {
      "conversation_id": "2107237881668313108",
      "text": "Time to bring them home 🌎  After nearly eight months aboard the @Space_Station, the four …",
      "tweet_id": "2107237881668313108",
      "views": "1979091",
      "author": {
        "blue_verified": true,
        "name": "NASA",
        "rest_id": "11348282",
        "screen_name": "<user>"
      }
    }
  ]
}
```

### Notes

- If `rest_id` is supplied, `screen_name` is ignored.
- Pass `cursor` using the next cursor value from a previous response to page through results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Twitter (X) Latest Tweet Comments](/model/twitter/web/latest-post-comments): Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.
- [Twitter (X) Tweet Comments](/model/twitter/web/post-comments): Returns comment threads and replies under a specified tweet.
- [Twitter (X) Retweet User List](/model/twitter/web/retweet-user-list): Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.

---
Machine-readable: [`catalog/models/twitter/web/user-media.json`](../../../../catalog/models/twitter/web/user-media.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-media
