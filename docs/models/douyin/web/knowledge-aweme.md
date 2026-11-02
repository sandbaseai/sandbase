# Douyin Web Knowledge Videos API: pricing, parameters and code examples

`douyin/web/knowledge-aweme` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves a feed of knowledge-focused videos from Douyin Web. Supports pagination controls using item count and refresh index parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/knowledge-aweme", "count": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/knowledge-aweme', {'count': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/knowledge-aweme", {
  "count": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/knowledge-aweme", sandbase.Params{
	"count": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/web/knowledge-aweme` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer | yes | Number per page, default is 16  |
| `refresh_index` | integer |  | Paging index, default is 1  |

## Details

Access knowledge-oriented video feeds on Douyin Web by specifying `count` and pagination `refresh_index`.

### Use cases

- Browse educational and knowledge-based video feeds on Douyin.
- Collect knowledge video listings for content discovery platforms.
- Paginate through educational content streams programmatically.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/knowledge-aweme" \
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

- `count` defines the number of items per page, defaulting to 16.
- `refresh_index` serves as the paging index and defaults to 1.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/knowledge-aweme.json`](../../../../catalog/models/douyin/web/knowledge-aweme.json) · Store page: https://www.sandbase.ai/model/douyin/web/knowledge-aweme
