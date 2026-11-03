# Douyin Music Hot Search List API: pricing, parameters and code examples

`douyin/app-v3/music-hot-search-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves Douyin hot search music rankings, audio details, and artist metadata based on the selected chart category and pagination cursor.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/music-hot-search-list", "chart_type": "hot", "cursor": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/music-hot-search-list', {'chart_type': 'hot', 'cursor': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/music-hot-search-list", {
  "chart_type": "hot",
  "cursor": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/music-hot-search-list", sandbase.Params{
	"chart_type": "hot",
	"cursor": "0",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/music-hot-search-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default value is '0', used for paginating data retrieval. After each request, the next cursor value will be returned, and the `has_more` field indicates whether there is more data available. default `"0"` |
| `chart_type` | string |  | Chart type, default value is 'hot', supports the following values: 'hot': Hot chart; 'trending': Trending chart; 'original': Original chart default `"hot"` |

## Details

Access Douyin trending and popular music rankings by supplying `chart_type` and `cursor`. It returns audio tracks, duration, and artist details across different leaderboard categories.

### Use cases

- Track trending background music across Douyin charts.
- Analyze popular original and rising music tracks.
- Monitor top viral sounds for social media content strategy.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/music-hot-search-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Cursor, default value is '0', used for paginating data retrieval. |
| `chart_type` | string | No | Chart type, default value is 'hot', supports the following values: 'hot': Hot chart; 'trending': Trending chart; 'original': Original chart |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "music_list": [
    {
      "music_info": {
        "audition_duration": 173,
        "author": "好久不见",
        "author_deleted": false,
        "binded_challenge_id": 0,
        "dsp_status": 10,
        "duration": 173
      }
    }
  ]
}
```

### Notes

- Supported `chart_type` values include 'hot' (Hot chart), 'trending' (Trending chart), and 'original' (Original chart).
- Pagination is handled via `cursor`, which defaults to '0', while the response indicates whether more items remain.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/music-hot-search-list.json`](../../../../catalog/models/douyin/app-v3/music-hot-search-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/music-hot-search-list
