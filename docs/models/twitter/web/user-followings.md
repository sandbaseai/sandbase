# Twitter (X) User Followings

`twitter/web/user-followings` · api · Twitter

Returns a list of accounts followed by a specified Twitter (X) user. Results provide follower counts, friend counts, media statistics, and profile details.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-followings", "screen_name": "NASA"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-followings', {'screen_name': 'NASA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-followings", {
  "screen_name": "NASA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-followings", sandbase.Params{
	"screen_name": "NASA",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-followings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the last request  |
| `screen_name` | string | yes | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk  |

## Details

Retrieve the list of accounts that a user follows using their `screen_name`. Paginate through extended results by passing the `cursor` from previous responses.

### Use cases

- Audit the public accounts followed by a specific profile.
- Track network connections and interest graphs across Twitter (X).
- Collect profile statistics for accounts in a user following list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-followings" \
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
  "following": [
    {
      "description": "The official X account for the NASA Hubble Space Telescope, managed and operated by NASA'…",
      "followers_count": 8900825,
      "friends_count": 44,
      "media_count": 3138,
      "name": "Hubble",
      "screen_name": "<user>",
      "statuses_count": 8467,
      "user_id": "<user>"
    }
  ]
}
```

### Notes

- `screen_name` corresponds to the handle found in the user profile URL.
- Pass `cursor` from the previous response to paginate through followings.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Twitter (X) Latest Tweet Comments](/model/twitter/web/latest-post-comments): Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.
- [Twitter (X) Tweet Comments](/model/twitter/web/post-comments): Returns comment threads and replies under a specified tweet.
- [Twitter (X) Retweet User List](/model/twitter/web/retweet-user-list): Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.

---
Machine-readable: [`catalog/models/twitter/web/user-followings.json`](../../../../catalog/models/twitter/web/user-followings.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-followings
