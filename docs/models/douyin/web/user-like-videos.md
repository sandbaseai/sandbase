# Douyin User Liked Videos (Web)

`douyin/web/user-like-videos` · api · Douyin

Returns videos liked by a specific Douyin web user. Filter results using the user security ID with pagination support via cursor and page size.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-like-videos", "sec_user_id": "<sec_user_id>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-like-videos', {'sec_user_id': '<sec_user_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-like-videos", {
  "sec_user_id": "<sec_user_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-like-videos", sandbase.Params{
	"sec_user_id": "<sec_user_id>",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-like-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `counts` | integer |  | Number per page  |
| `max_cursor` | integer |  | Maximum cursor  |
| `sec_user_id` | string | yes | User sec_user_id  |

## Details

Retrieve a Douyin user's liked video list by providing `sec_user_id`. Supports cursor-based pagination with `max_cursor` and page size controls via `counts`.

### Use cases

- Inspect public video favorites for a specific Douyin account.
- Analyze user content preferences based on liked videos.
- Paginate through liked video feeds for user profile insights.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-like-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "<sec_user_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | Yes | User sec_user_id |
| `counts` | integer | No | Number per page |
| `max_cursor` | integer | No | Maximum cursor |

### Notes

- Requires `sec_user_id` to identify the user.
- Supports pagination using `max_cursor` and `counts`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-like-videos.json`](../../../../catalog/models/douyin/web/user-like-videos.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-like-videos
