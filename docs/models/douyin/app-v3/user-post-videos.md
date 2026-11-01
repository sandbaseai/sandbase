# Douyin User Videos

`douyin/app-v3/user-post-videos` · api · Douyin

Get the videos on a Douyin user's profile with descriptions, publish time and play, like, comment and share counts. Sort by latest or most popular, with cursor pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/user-post-videos", "sec_user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/user-post-videos', {'sec_user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/user-post-videos", {
  "sec_user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/user-post-videos", sandbase.Params{
	"sec_user_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/user-post-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Maximum count number, do not exceed 20, it is recommended to keep it unchanged.  |
| `sort_type` | integer |  | Sort type, optional values are as follows: `0`: Latest sorting - default; `1`: Hottest sorting  |
| `max_cursor` | integer |  | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response.  |
| `sec_user_id` | string | yes | User sec_user_id  |

## Details

Pass a Douyin `sec_user_id` and get the videos on that user's homepage, newest first or most popular first, with full statistics.

### Use cases

- Track a creator's posting cadence and performance.
- Audit an influencer's recent content before a campaign.
- Collect a brand account's videos for analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/user-post-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAKzTVRAaDq7fTxkJteVYjRsyVPxxofLDAyViyWT43BNRdTjgmqCcolsU_UqRgbzBU", "count": 5}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | Yes | User sec_user_id |
| `count` | integer | No | Maximum count number, do not exceed 20, it is recommended to keep it unchanged. |
| `sort_type` | integer | No | Sort type, optional values are as follows: `0`: Latest sorting - default; `1`: Hottest sorting |
| `max_cursor` | integer | No | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "has_more": 1,
  "max_cursor": "<next max_cursor>",
  "aweme_list": [
    {
      "aweme_id": "7657847286442471077",
      "create_time": 1782981514,
      "duration": 6014,
      "author": {
        "nickname": "<user>",
        "sec_uid": "<sec_uid>"
      },
      "statistics": {
        "play_count": 0,
        "digg_count": 8,
        "comment_count": 0,
        "share_count": 0,
        "collect_count": 2
      },
      "share_url": "https://www.iesdouyin.com/share/video/7657847286442471077/?…"
    }
  ]
}
```

### Notes

- `sort_type`: 0 = latest (default), 1 = most popular.
- Paginate with `max_cursor` from the previous response.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Hot Search List](/model/douyin/app-v3/hot-search-list): Get the Douyin hot search list and other boards (seeding, entertainment, social and challenge lists): trending words with heat values and video counts.
- [Douyin Video Statistics (Batch)](/model/douyin/app-v3/multi-video-statistics): Get play, like, share and download counts for up to 50 Douyin videos in one request by passing comma-separated video IDs.
- [Get Douyin brand hot search list data](/model/douyin/app-v3/brand-hot-search-list): Get Douyin brand hot search category data.

---
Machine-readable: [`catalog/models/douyin/app-v3/user-post-videos.json`](../../../../catalog/models/douyin/app-v3/user-post-videos.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/user-post-videos
