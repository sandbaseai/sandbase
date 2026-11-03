# TikTok User Follower Search API: pricing, parameters and code examples

`tiktok/app-v3/search-follower-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches a specific TikTok user's follower list for accounts matching a nickname keyword. Returns matching follower results and a count based on the provided user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/search-follower-list", "keyword": ".v7.v7.v7", "user_id": "7455877271699113003"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/search-follower-list', {'keyword': '.v7.v7.v7', 'user_id': '7455877271699113003'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/search-follower-list", {
  "keyword": ".v7.v7.v7",
  "user_id": "7455877271699113003"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/search-follower-list", sandbase.Params{
	"keyword": ".v7.v7.v7",
	"user_id": "7455877271699113003",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/search-follower-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword, the user's nickname contains the keyword to match.  |
| `user_id` | string | yes | User ID, this is a pure numeric version of the user ID, which can be obtained through the get user info API.  |

## Details

Searches one TikTok account's followers for nicknames that contain a keyword. It needs a numeric `user_id` and a `keyword`, and returns the matching followers with a count.

### Use cases

- Check whether an account with a brand name in its nickname follows a target account.
- Find followers of an influencer whose nicknames contain a given word.
- Spot-check a creator's audience for accounts tied to a partner or competitor.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/search-follower-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai", "user_id": "107955"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword, the user's nickname contains the keyword to match. |
| `user_id` | string | Yes | User ID, this is a pure numeric version of the user ID, which can be obtained through the get user info API. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "keyword": "openai",
  "result_count": 0,
  "results": [],
  "user_id": "107955"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `keyword` | The search keyword from the request. The API matches it against follower nicknames. |
| `user_id` | The numeric ID of the account whose followers were searched. |
| `result_count` | The number of followers that matched the keyword. It is `0` when nothing matched. |
| `results[]` | The list of matching followers. It is an empty list when `result_count` is `0`, as in this example. |

### Notes

- Pass the pure numeric `user_id`. Get it from [TikTok User Profile Details](/apis/tiktok/app-v3/user-profile) or [TikTok User ID by Username](/apis/tiktok/app-v3/user-id-and-sec-user-id-by-username).
- A search with no matches returns `result_count` of `0` and an empty `results` list, not an error.
- To browse followers without a keyword, use [TikTok User Follower List](/apis/tiktok/app-v3/user-follower-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/search-follower-list.json`](../../../../catalog/models/tiktok/app-v3/search-follower-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/search-follower-list
