# Douyin Series Video List API: pricing, parameters and code examples

`douyin/app-v3/series-video-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the list of videos included in a specific Douyin series or playlet using a series identifier and cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/series-video-list", "cursor": 0, "series_id": "7592054624643713067"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/series-video-list', {'cursor': 0, 'series_id': '7592054624643713067'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/series-video-list", {
  "cursor": 0,
  "series_id": "7592054624643713067"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/series-video-list", sandbase.Params{
	"cursor": 0,
	"series_id": "7592054624643713067",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/series-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is usually the value of count (e.g., 15).  |
| `series_id` | string | yes | Series id  |

## Details

Fetch video lists from Douyin series and playlets by supplying the `series_id` and optional `cursor` parameters.

### Use cases

- Retrieve all episodes within a Douyin drama or playlet series.
- Track video metadata across serialized short video content.
- Index playlet episode releases in chronological viewing sequence.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/series-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_id": "7585746250092251178"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `series_id` | string | Yes | Series id |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is usually the value of count (e.g., 15). |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_list": [
    {
      "activity_video_type": -1,
      "author_user_id": 2740414975578590,
      "aweme_id": "7529494667390586171",
      "aweme_type": 0,
      "bodydance_score": 0,
      "boost_status": 0,
      "caption": "盘点科普一些蝉的种类，你看你认识几种！#盘点#科普#分享#蝉",
      "cf_assets_type": 0,
      "create_time": 1753097092,
      "desc": "盘点科普一些蝉的种类，你看你认识几种！#盘点#科普#分享#蝉",
      "author": {
        "apple_account": 0,
        "authority_status": 0,
        "aweme_count": 0,
        "close_friend_type": 0,
        "comment_filter_status": 0,
        "contacts_status": 2
      },
      "comment_permission_info": {
        "comment_permission_status": 0
      },
      "commerce_info": {
        "ad_type": 0
      },
      "distribute_circle": {
        "distribute_type": 0
      }
    }
  ]
}
```

### Notes

- Set `cursor` to 0 for the initial page, then pass the offset value for subsequent pages.
- Requires a valid `series_id` string to identify the target series.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/series-video-list.json`](../../../../catalog/models/douyin/app-v3/series-video-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/series-video-list
