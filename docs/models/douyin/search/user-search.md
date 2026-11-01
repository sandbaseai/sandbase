# Douyin User Search (Search)

`douyin/search/user-search` · api · Douyin

Returns a list of Douyin users matching search keywords. Supports filtering by fan count and user type with cursor-based pagination.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/user-search", "cursor": 0, "douyin_user_fans": "", "douyin_user_type": "", "keyword": "猫咪", "search_id": ""}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/user-search', {'cursor': 0, 'douyin_user_fans': '', 'douyin_user_type': '', 'keyword': '猫咪', 'search_id': ''})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/user-search", {
  "cursor": 0,
  "douyin_user_fans": "",
  "douyin_user_type": "",
  "keyword": "猫咪",
  "search_id": ""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/user-search", sandbase.Params{
	"cursor": 0,
	"douyin_user_fans": "",
	"douyin_user_type": "",
	"keyword": "猫咪",
	"search_id": "",
})
```

Same call via the path form: `POST /v1/api/douyin/search/user-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first page) default `0` |
| `keyword` | string |  | Search keyword, e.g., "AI" default `"猫咪"` |
| `search_id` | string |  | Search session ID for pagination default `""` |
| `douyin_user_fans` | string |  | Fan count filter default `""` |
| `douyin_user_type` | string |  | User type filter default `""` |

## Details

Search for Douyin accounts by entering a query term in `keyword`. Results can be refined using `douyin_user_fans` and `douyin_user_type`.

### Use cases

- Discover Douyin creators by niche keywords.
- Filter account search results by fan count brackets.
- Identify verified or specific categories of Douyin users.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/user-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor (0 for first page) |
| `keyword` | string | No | Search keyword, e.g., "AI" |
| `search_id` | string | No | Search session ID for pagination |
| `douyin_user_fans` | string | No | Fan count filter |
| `douyin_user_type` | string | No | User type filter |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "user_list": [
    {
      "dynamic_patch": {
        "origin_type": 4
      }
    }
  ]
}
```

### Notes

- Use `cursor` starting at 0 for the first page of results.
- Pass `search_id` to maintain the search session across paginated requests.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Challenge Search](/model/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/model/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/model/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/user-search.json`](../../../../catalog/models/douyin/search/user-search.json) · Store page: https://www.sandbase.ai/model/douyin/search/user-search
