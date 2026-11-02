# Douyin Hot Challenge List API: pricing, parameters and code examples

`douyin/billboard/hot-challenge-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns trending Douyin challenge leaderboard entries with rank, hot score, and video counts. Supports filtering by keyword and page-based pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-challenge-list", "page": 1, "page_size": 10}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-challenge-list', {'page': 1, 'page_size': 10})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-challenge-list", {
  "page": 1,
  "page_size": 10
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-challenge-list", sandbase.Params{
	"page": 1,
	"page_size": 10,
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-challenge-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer | yes | Page number  |
| `keyword` | string |  | Hot search term default `""` |
| `page_size` | integer | yes | Number of items per page  |

## Details

Retrieve trending challenge rankings on Douyin using `page` and `page_size`, with optional keyword filtering via `keyword`.

### Use cases

- Track top-performing challenge topics on Douyin.
- Analyze challenge popularity through hot scores and video counts.
- Search for specific challenge themes using keyword filters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-challenge-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"page": 1, "page_size": 10}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | Yes | Page number |
| `page_size` | integer | Yes | Number of items per page |
| `keyword` | string | No | Hot search term |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "objs": [
      {
        "SnapshotSubType": "hotspot_challenge",
        "SnapshotType": 2,
        "hot_score": 8870294,
        "label": 0,
        "rank": 1,
        "sentence_id": 2683588,
        "sentence_tag": 1001,
        "video_count": 10
      }
    ]
  }
}
```

### Notes

- Pagination is controlled using the required `page` and `page_size` parameters.
- Use `keyword` to filter challenge results by a specific search term.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/model/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/model/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-challenge-list.json`](../../../../catalog/models/douyin/billboard/hot-challenge-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-challenge-list
