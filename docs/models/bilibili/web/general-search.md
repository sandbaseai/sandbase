# Bilibili Web General Search API: pricing, parameters and code examples

`bilibili/web/general-search` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns search results from Bilibili based on a search keyword, with sorting options and filters for duration and publication date range.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/general-search", "duration": 0, "keyword": "OpenAI", "order": "totalrank", "page": 1, "page_size": 20, "pubtime_begin_s": 0, "pubtime_end_s": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/general-search', {'duration': 0, 'keyword': 'OpenAI', 'order': 'totalrank', 'page': 1, 'page_size': 20, 'pubtime_begin_s': 0, 'pubtime_end_s': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/general-search", {
  "duration": 0,
  "keyword": "OpenAI",
  "order": "totalrank",
  "page": 1,
  "page_size": 20,
  "pubtime_begin_s": 0,
  "pubtime_end_s": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/general-search", sandbase.Params{
	"duration": 0,
	"keyword": "OpenAI",
	"order": "totalrank",
	"page": 1,
	"page_size": 20,
	"pubtime_begin_s": 0,
	"pubtime_end_s": 0,
})
```

Same call via the path form: `POST /v1/api/bilibili/web/general-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer | yes | Page number  |
| `order` | string | yes | Order method  |
| `keyword` | string | yes | Search keyword  |
| `duration` | integer |  | Duration filter default `0` |
| `page_size` | integer | yes | Number per page  |
| `pubtime_end_s` | integer |  | End date, 10-digit timestamp, must be greater than start date default `0` |
| `pubtime_begin_s` | integer |  | Start date, 10-digit timestamp, must be less than end date default `0` |

## Details

Query video search results across Bilibili by specifying a `keyword` along with pagination and sorting criteria.

### Use cases

- Search for videos matching specific query terms across Bilibili.
- Filter search results by video duration and publication date timestamps.
- Sort keyword search listings by criteria such as overall ranking.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/general-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI", "order": "totalrank", "page": 1, "page_size": 20}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | Yes | Page number |
| `order` | string | Yes | Order method |
| `keyword` | string | Yes | Search keyword |
| `page_size` | integer | Yes | Number per page |
| `duration` | integer | No | Duration filter |
| `pubtime_end_s` | integer | No | End date, 10-digit timestamp, must be greater than start date |
| `pubtime_begin_s` | integer | No | Start date, 10-digit timestamp, must be less than end date |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "result": [
      {
        "author": "AI大圆镜",
        "card_status": 0,
        "description": "9月22号，越狱圈名人老普林尼把GPT-6 Sol Codex全套系统提示词传上GitHub，超29万字符，连禁AI味都写进了家规。",
        "duration": "1:0",
        "id": 117385952495187,
        "like": 399,
        "live_status": 0,
        "parent_area_id": 0,
        "pubdate": 1791167590,
        "rank_index": 1
      }
    ]
  }
}
```

### Notes

- `pubtime_begin_s` and `pubtime_end_s` accept 10-digit timestamps, where the start date must be earlier than the end date.
- Results can be paginated using `page` and `page_size`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/general-search.json`](../../../../catalog/models/bilibili/web/general-search.json) · Store page: https://www.sandbase.ai/model/bilibili/web/general-search
