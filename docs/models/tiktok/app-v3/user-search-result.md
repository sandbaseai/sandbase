# TikTok User Search Results

`tiktok/app-v3/user-search-result` · api · TikTok

Returns a list of user profiles matching specified keywords, with options to filter by account type, follower count, and preferences.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-search-result", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-search-result', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-search-result", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-search-result", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-search-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `20` |
| `offset` | integer |  | Offset default `0` |
| `keyword` | string | yes | Keyword  |
| `user_search_other_pref` | string |  | Sort by other preferences default `""` |
| `user_search_profile_type` | string |  | Sort by account type default `""` |
| `user_search_follower_count` | string |  | Sort by number of followers default `""` |

## Details

Look up TikTok profiles by query using `keyword`. Supports pagination via `count` and `offset` alongside multiple filtering parameters.

### Use cases

- Find creators and accounts matching target search terms.
- Filter account listings by follower volume and profile type.
- Page through keyword query matches for audience research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-search-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `count` | integer | No | Number |
| `offset` | integer | No | Offset |
| `user_search_other_pref` | string | No | Sort by other preferences |
| `user_search_profile_type` | string | No | Sort by account type |
| `user_search_follower_count` | string | No | Sort by number of followers |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "user_list": [
    {
      "user_info": {
        "authority_status": 0,
        "aweme_count": 542,
        "block_status": 0,
        "comment_filter_status": 0,
        "fb_expire_time": 0,
        "follow_status": 0
      }
    }
  ]
}
```

### Notes

- Control pagination using `count` and `offset`.
- Refine queries using `user_search_follower_count` and `user_search_profile_type`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-search-result.json`](../../../../catalog/models/tiktok/app-v3/user-search-result.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-search-result
