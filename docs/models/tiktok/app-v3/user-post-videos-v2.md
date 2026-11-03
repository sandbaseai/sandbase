# TikTok User Videos (App V3, V2) API: pricing, parameters and code examples

`tiktok/app-v3/user-post-videos-v2` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns video data from a TikTok user homepage based on their profile identifier or username, with options for sorting and pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-post-videos-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-post-videos-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-post-videos-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-post-videos-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-post-videos-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Maximum count number default `20` |
| `sort_type` | integer |  | Sort type, 0-Latest, 1-Hot default `0` |
| `unique_id` | string |  | User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username. default `""` |
| `max_cursor` | integer |  | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. default `0` |
| `sec_user_id` | string |  | User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data. default `""` |

## Details

Retrieve homepage videos for a specific creator using `sec_user_id` or `unique_id`. Results can be sorted by latest or popular posts.

### Use cases

- Display a creator's video feed directly inside an external dashboard.
- Monitor recently posted video performance metrics for a specific account.
- Retrieve top-performing videos from a creator's public profile.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-post-videos-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Maximum count number |
| `sort_type` | integer | No | Sort type, 0-Latest, 1-Hot |
| `unique_id` | string | No | User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username. |
| `max_cursor` | integer | No | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. |
| `sec_user_id` | string | No | User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data. |

### Notes

- Provide `sec_user_id` first; if it is unavailable, supply `unique_id` instead.
- Set `sort_type` to `0` for the latest videos or `1` for hot videos.
- For pagination, set `max_cursor` to `0` for the initial request, then pass the previous response cursor value for subsequent pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-post-videos-v2.json`](../../../../catalog/models/tiktok/app-v3/user-post-videos-v2.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-post-videos-v2
