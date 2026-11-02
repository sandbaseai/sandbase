# Douyin Creator Search Suggestions API: pricing, parameters and code examples

`douyin/index/daren-sug-great-user-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns creator suggestions on Douyin matching a query nickname. Includes profile details, content category tags, follower totals, and item counts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/daren-sug-great-user-list", "keyword": "人工智能", "total": "20"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/daren-sug-great-user-list', {'keyword': '人工智能', 'total': '20'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/daren-sug-great-user-list", {
  "keyword": "人工智能",
  "total": "20"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/daren-sug-great-user-list", sandbase.Params{
	"keyword": "人工智能",
	"total": "20",
})
```

Same call via the path form: `POST /v1/api/douyin/index/daren-sug-great-user-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `total` | string |  | Return count, default 20 default `"20"` |
| `keyword` | string | yes | Daren nickname keyword  |

## Details

Look up suggested Douyin creators by specifying a nickname search term in `keyword`. Adjust the number of returned creator profiles with `total`.

### Use cases

- Discover relevant creators based on partial nickname queries.
- Inspect creator category tags, follower totals, and like counts.
- Provide autocomplete suggestions in creator discovery interfaces.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/daren-sug-great-user-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Daren nickname keyword |
| `total` | string | No | Return count, default 20 |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "userlist": [
    {
      "aweme_id": "CAAI_Douyin",
      "aweme_url": "https://www.douyin.com/user/MS4wLjABAAAAAVx--1Dtm9rEs1BP83SAx5nqlIMoryL9UWIzb0d8YRw",
      "first_tag_name": "科技",
      "follow_count": "731284",
      "item_count": "253",
      "like_count": "7548",
      "second_tag_name": "科技科普",
      "user_id": "<user>",
      "user_name": "<user>"
    }
  ]
}
```

### Notes

- Set `total` to adjust the number of returned creators, which defaults to 20.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/daren-sug-great-user-list.json`](../../../../catalog/models/douyin/index/daren-sug-great-user-list.json) · Store page: https://www.sandbase.ai/model/douyin/index/daren-sug-great-user-list
