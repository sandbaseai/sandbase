# TikTok User Videos (App V3)

`tiktok/app-v3/user-post-videos` · api · TikTok

Returns videos posted on a TikTok user profile. Filter by account identifier, specify sorting order by latest or popular items, and paginate through results.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-post-videos"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-post-videos', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-post-videos", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-post-videos", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-post-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Maximum count number default `20` |
| `region` | string |  | Region, optional parameter, if not passed, the US region data will be used by default. After passing, the data of the corresponding country and region will be preferred, for example: US, GB, FR, JP, SG, VN, etc. default `""` |
| `sort_type` | integer |  | Sort type, 0-Latest, 1-Hot default `0` |
| `unique_id` | string |  | User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username. default `""` |
| `max_cursor` | integer |  | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. default `0` |
| `sec_user_id` | string |  | User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data. default `""` |

## Details

Retrieve posted video content from a target TikTok profile using either `sec_user_id` or `unique_id`.

### Use cases

- Track video releases and performance from specific creator accounts.
- Retrieve historical video catalogs for public TikTok profiles.
- Sort profile uploads by latest posts or top-performing hot videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-post-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Maximum count number |
| `region` | string | No | Region, optional parameter, if not passed, the US region data will be used by default. |
| `sort_type` | integer | No | Sort type, 0-Latest, 1-Hot |
| `unique_id` | string | No | User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username. |
| `max_cursor` | integer | No | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. |
| `sec_user_id` | string | No | User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data. |

### Notes

- Lookup prioritizes `sec_user_id`; if empty, provide the username via `unique_id`.
- Set `sort_type` to 0 for latest videos or 1 for hot videos.
- Paginate by setting `max_cursor` to 0 on the first call, then pass the returned cursor value on subsequent requests.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-post-videos.json`](../../../../catalog/models/tiktok/app-v3/user-post-videos.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-post-videos
