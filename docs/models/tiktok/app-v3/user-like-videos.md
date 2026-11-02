# TikTok User Liked Videos API: pricing, parameters and code examples

`tiktok/app-v3/user-like-videos` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns liked videos for a specific user using their secure user ID. Supports cursor-based pagination and page size configuration.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-like-videos", "sec_user_id": "1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-like-videos', {'sec_user_id': '1'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-like-videos", {
  "sec_user_id": "1"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-like-videos", sandbase.Params{
	"sec_user_id": "1",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-like-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `counts` | integer |  | Number per page  |
| `max_cursor` | integer |  | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response.  |
| `sec_user_id` | string | yes | User sec_user_id  |

## Details

Retrieve liked video data for a TikTok user identified by `sec_user_id`. Supports pagination via `max_cursor` and page limits using `counts`.

### Use cases

- Inspect videos liked by a specific TikTok account.
- Analyze user content preferences and engagement trends.
- Paginate through an account's public like history.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-like-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | Yes | User sec_user_id |
| `counts` | integer | No | Number per page |
| `max_cursor` | integer | No | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. |

### Notes

- Requires `sec_user_id` to identify the target profile.
- Set `max_cursor` to 0 for the first page, then pass the returned cursor value for subsequent pages.
- `counts` controls the number of items returned per page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-like-videos.json`](../../../../catalog/models/tiktok/app-v3/user-like-videos.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-like-videos
