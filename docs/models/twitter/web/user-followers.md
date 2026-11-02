# Twitter (X) User Followers API: pricing, parameters and code examples

`twitter/web/user-followers` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves follower profiles for a specified Twitter (X) account, including follower counts and verification statuses. Supports pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-followers", "screen_name": "NASA"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-followers', {'screen_name': 'NASA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-followers", {
  "screen_name": "NASA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-followers", sandbase.Params{
	"screen_name": "NASA",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the last request  |
| `screen_name` | string | yes | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk  |

## Details

Retrieve a list of followers for any public account using their `screen_name`. Supports cursor-based pagination via `cursor`.

### Use cases

- Inspect follower profiles and counts for a specific account.
- Track verified accounts following a target profile.
- Page through large follower bases for audience analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-followers" \
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
  "followers": [
    {
      "blue_verified": true,
      "followers_count": 41935094,
      "name": "SpaceX",
      "screen_name": "<user>",
      "user_id": "<user>",
      "verified": false
    }
  ]
}
```

### Notes

- Pass the account handle found in the profile URL as `screen_name`.
- Use `cursor` from the previous response to paginate through results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Twitter (X) Latest Tweet Comments](/model/twitter/web/latest-post-comments): Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.
- [Twitter (X) Tweet Comments](/model/twitter/web/post-comments): Returns comment threads and replies under a specified tweet.
- [Twitter (X) Retweet User List](/model/twitter/web/retweet-user-list): Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.

---
Machine-readable: [`catalog/models/twitter/web/user-followers.json`](../../../../catalog/models/twitter/web/user-followers.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-followers
