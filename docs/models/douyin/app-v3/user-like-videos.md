# Douyin User Liked Videos (App V3) API: pricing, parameters and code examples

`douyin/app-v3/user-like-videos` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of videos liked by a specific Douyin user. Supports cursor-based pagination and custom item counts per page.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/user-like-videos", "sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/user-like-videos', {'sec_user_id': 'MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/user-like-videos", {
  "sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/user-like-videos", sandbase.Params{
	"sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/user-like-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `counts` | integer |  | Number per page  |
| `max_cursor` | integer |  | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response.  |
| `sec_user_id` | string | yes | User sec_user_id  |

## Details

Look up videos liked by a Douyin user using their `sec_user_id`. Supports cursor-based pagination with `max_cursor` and results sizing via `counts`.

### Use cases

- Inspect videos liked by a specific Douyin profile.
- Analyze content preferences and audience interests from liked feeds.
- Track historical video likes for research and monitoring.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/user-like-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | Yes | User sec_user_id |
| `counts` | integer | No | Number per page |
| `max_cursor` | integer | No | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. |

### Notes

- Requires `sec_user_id` to identify the Douyin user.
- For pagination, pass 0 to `max_cursor` on the first call, then use the returned `max_cursor` value on subsequent calls.
- Use `counts` to set the number of items returned per page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/user-like-videos.json`](../../../../catalog/models/douyin/app-v3/user-like-videos.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/user-like-videos
