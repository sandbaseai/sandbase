# TikTok Music Search API: pricing, parameters and code examples

`tiktok/app-v3/music-search-result` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns TikTok music search results matching specified keywords, with options to filter by title or author and sort by usage or duration.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/music-search-result", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/music-search-result', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/music-search-result", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/music-search-result", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/music-search-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number, do not exceed 20 default `20` |
| `offset` | integer |  | Offset, starting from 0, the second page gets the cursor value from the response as the offset to continue the request. default `0` |
| `region` | string |  | Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. default `"US"` |
| `keyword` | string | yes | Keyword  |
| `filter_by` | integer |  | Filter type, 0-All, 1-Title, 2-Author, default is 0-All default `0` |
| `sort_type` | integer |  | Sort type, 0-Relatedness, 1-Most used, 2-Latest, 3-Shortest duration, 4-Longest duration, default is 0-Relatedness default `0` |

## Details

Search for TikTok music tracks using a specified `keyword`. Filter by title or artist and sort results by relevance, usage, or duration.

### Use cases

- Search TikTok tracks by keyword, title, or artist name.
- Filter music track results for specific target regions.
- Discover popular audio tracks sorted by usage count or duration.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/music-search-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `count` | integer | No | Number, do not exceed 20 |
| `offset` | integer | No | Offset, starting from 0, the second page gets the cursor value from the response as the offset to continue the request. |
| `region` | string | No | Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. |
| `filter_by` | integer | No | Filter type, 0-All, 1-Title, 2-Author, default is 0-All |
| `sort_type` | integer | No | Sort type, 0-Relatedness, 1-Most used, 2-Latest, 3-Shortest duration, 4-Longest duration, default is 0-Relatedness |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "music": [
    {
      "audition_duration": 60,
      "author": "OpenAI",
      "author_deleted": false,
      "binded_challenge_id": 0,
      "commercial_right_type": 1,
      "create_time": 1676501099,
      "duration": 60,
      "id": 7200517085770811393,
      "music_group_use_count": 0,
      "music_ugid_use_count": 0,
      "duration_high_precision": {
        "audition_duration_precision": 60,
        "duration_precision": 60,
        "shoot_duration_precision": 60,
        "video_duration_precision": 60
      },
      "matched_song": {
        "author": "OpenAI",
        "full_duration": 275100,
        "id": "7200516864395462658",
        "title": "Chatbot"
      },
      "music_release_info": {
        "group_release_date": 0
      }
    }
  ]
}
```

### Notes

- `filter_by` supports `0` (All), `1` (Title), and `2` (Author).
- `sort_type` supports `0` (Relatedness), `1` (Most used), `2` (Latest), `3` (Shortest duration), and `4` (Longest duration).
- `count` must not exceed 20, with subsequent pages using the response cursor as the `offset`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/music-search-result.json`](../../../../catalog/models/tiktok/app-v3/music-search-result.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/music-search-result
