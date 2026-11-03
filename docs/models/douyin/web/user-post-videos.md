# Douyin User Video Posts API: pricing, parameters and code examples

`douyin/web/user-post-videos` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns video data posted on a Douyin user homepage. Query by user identifier with support for pagination and sorting by popularity or default order.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-post-videos", "count": 20, "filter_type": "0", "max_cursor": "0", "sec_user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-post-videos', {'count': 20, 'filter_type': '0', 'max_cursor': '0', 'sec_user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-post-videos", {
  "count": 20,
  "filter_type": "0",
  "max_cursor": "0",
  "sec_user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-post-videos", sandbase.Params{
	"count": 20,
	"filter_type": "0",
	"max_cursor": "0",
	"sec_user_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-post-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Maximum count number, it is recommended not to exceed 20  |
| `max_cursor` | string |  | Paging cursor, pass 0 for the first request, and then pass the max_cursor returned by the previous request for paging each time.  |
| `filter_type` | string |  | Filter type, optional parameters are as follows: 0: Default sorting; 3: Sort by popularity  |
| `sec_user_id` | string | yes | User sec_user_id  |

## Details

Retrieve a list of posted videos from a specific Douyin user profile using `sec_user_id`. Supports cursor-based pagination and popularity sorting.

### Use cases

- Inspect video uploads from specific Douyin creator profiles.
- Track newly posted content across creator homepages.
- Analyze popular video listings for creator performance benchmarking.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-post-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | Yes | User sec_user_id |
| `count` | integer | No | Maximum count number, it is recommended not to exceed 20 |
| `max_cursor` | string | No | Paging cursor, pass 0 for the first request, and then pass the max_cursor returned by the previous request for paging each time. |
| `filter_type` | string | No | Filter type, optional parameters are as follows: 0: Default sorting; 3: Sort by popularity |

### Notes

- Pass `0` to `max_cursor` for the initial call, then provide the returned cursor value for subsequent pages.
- Set `filter_type` to `0` for default sorting or `3` to sort by popularity.
- It is recommended to keep `count` at 20 or fewer.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-post-videos.json`](../../../../catalog/models/douyin/web/user-post-videos.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-post-videos
