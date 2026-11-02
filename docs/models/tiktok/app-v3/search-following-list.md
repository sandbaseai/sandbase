# TikTok Following List Search API: pricing, parameters and code examples

`tiktok/app-v3/search-following-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Searches the following list of a specified TikTok account by nickname keyword. Returns matching accounts along with the match count for the query.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/search-following-list", "keyword": "openai", "user_id": "107955"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/search-following-list', {'keyword': 'openai', 'user_id': '107955'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/search-following-list", {
  "keyword": "openai",
  "user_id": "107955"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/search-following-list", sandbase.Params{
	"keyword": "openai",
	"user_id": "107955",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/search-following-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword, the user's nickname contains the keyword to match.  |
| `user_id` | string | yes | User ID, this is a pure numeric version of the user ID, which can be obtained through the get user info API.  |

## Details

Query a target TikTok account's following list using `user_id` and filter results by nickname via `keyword`.

### Use cases

- Check if a target user follows a specific account or brand.
- Filter a user's followed accounts by nickname keyword.
- Inspect network connections and relationship graphs between profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/search-following-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai", "user_id": "107955"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword, the user's nickname contains the keyword to match. |
| `user_id` | string | Yes | User ID, this is a pure numeric version of the user ID, which can be obtained through the get user info API. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "keyword": "openai",
  "result_count": 0,
  "user_id": "<user>"
}
```

### Notes

- `user_id` must be a numeric ID obtained from user info endpoints.
- `keyword` matches against user nicknames in the following list.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/search-following-list.json`](../../../../catalog/models/tiktok/app-v3/search-following-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/search-following-list
