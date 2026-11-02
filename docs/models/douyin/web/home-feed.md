# Douyin Web Home Feed API: pricing, parameters and code examples

`douyin/web/home-feed` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves the Douyin web home feed containing video listings and media metadata. Supports setting the item count and pagination index.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/home-feed", "count": 10, "refresh_index": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/home-feed', {'count': 10, 'refresh_index': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/home-feed", {
  "count": 10,
  "refresh_index": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/home-feed", sandbase.Params{
	"count": 10,
	"refresh_index": 0,
})
```

Same call via the path form: `POST /v1/api/douyin/web/home-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number, default is 10, it is recommended to keep it unchanged.  |
| `refresh_index` | integer |  | Refresh/paging index, start at 0 and +1 per page.  |

## Details

Retrieve video items from the Douyin web home feed using `refresh_index` for pagination and `count` for the batch size.

### Use cases

- Retrieve recommended videos from the Douyin home feed.
- Paginate through web feed items for content discovery.
- Inspect video bitrate and stream quality options for feed media.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/home-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number, default is 10, it is recommended to keep it unchanged. |
| `refresh_index` | integer | No | Refresh/paging index, start at 0 and +1 per page. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_list": [
    {
      "video": {
        "bit_rate": [
          {
            "bit_rate": 808807,
            "gear_name": "normal_1080_0",
            "quality_type": 1
          }
        ]
      }
    }
  ]
}
```

### Notes

- `refresh_index` starts at 0 and increments by 1 for each page.
- `count` defaults to 10 and is recommended to remain unchanged.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/home-feed.json`](../../../../catalog/models/douyin/web/home-feed.json) · Store page: https://www.sandbase.ai/model/douyin/web/home-feed
