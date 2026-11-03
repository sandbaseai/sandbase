# Twitter (X) User Profile API: pricing, parameters and code examples

`twitter/web/user-profile` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get a Twitter / X user profile by screen name or user ID: name, bio, follower and following counts, post and media counts, verification and creation date.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-profile"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-profile', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-profile", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-profile", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/twitter/web/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `rest_id` | integer |  | User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected.  |
| `screen_name` | string |  | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk  |

## Details

Pass an X screen name (or numeric user ID) and get the account's public profile and counts.

### Use cases

- Vet influencers and partners.
- Track follower growth.
- Resolve handles to stable user IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"screen_name": "NASA"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `rest_id` | integer | No | User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. |
| `screen_name` | string | No | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twi… |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "blue_verified": true,
  "desc": "Making the seemingly impossible, possible. ✨",
  "id": "11348282",
  "media_count": 28179,
  "name": "NASA",
  "rest_id": "11348282",
  "status": "active",
  "statuses_count": 74382,
  "sub_count": 92374842,
  "verification_type": "Government"
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Twitter (X) Search](/apis/twitter/web/search-timeline): Search Twitter / X posts by keyword and get tweets with text, author, time and engagement counts (likes, retweets, replies, views).
- [Twitter (X) Trending Topics](/apis/twitter/web/trending): Get trending topics on Twitter / X by country: trend names with their category context, for the United States, Japan, India, the UK and other markets.
- [Twitter Tweet Detail](/apis/twitter/web/tweet-detail): Get a single tweet (X post) by ID: full text, author, media, and like, retweet, reply, quote, bookmark and view counts.

---
Machine-readable: [`catalog/models/twitter/web/user-profile.json`](../../../../catalog/models/twitter/web/user-profile.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-profile
