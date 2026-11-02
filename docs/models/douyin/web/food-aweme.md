# Douyin Food Videos API: pricing, parameters and code examples

`douyin/web/food-aweme` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a feed of food-related videos from Douyin Web. Results can be paginated using count and refresh index parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/food-aweme", "count": 1, "refresh_index": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/food-aweme', {'count': 1, 'refresh_index': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/food-aweme", {
  "count": 1,
  "refresh_index": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/food-aweme", sandbase.Params{
	"count": 1,
	"refresh_index": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/web/food-aweme` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer | yes | Number per page, default is 16  |
| `refresh_index` | integer |  | Paging index, default is 1  |

## Details

Retrieves food video content from Douyin Web using `count` and `refresh_index` for pagination.

### Use cases

- Discover trending food videos on Douyin Web.
- Collect food video feeds for content analysis.
- Paginate through food-related Douyin posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/food-aweme" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"count": "<count>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | Yes | Number per page, default is 16 |
| `refresh_index` | integer | No | Paging index, default is 1 |

### Notes

- Set `count` to specify the number of items per page, defaulting to 16.
- Use `refresh_index` to control the paging index, defaulting to 1.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/food-aweme.json`](../../../../catalog/models/douyin/web/food-aweme.json) · Store page: https://www.sandbase.ai/model/douyin/web/food-aweme
