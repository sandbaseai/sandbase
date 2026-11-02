# Douyin User Search API: pricing, parameters and code examples

`douyin/search-user` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search Douyin (TikTok China) users by keyword with page-based pagination and optional account-type filtering. Use it to discover creators, brands, or verified accounts for research.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search-user", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search-user', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search-user", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search-user", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/douyin/search-user` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (starting from 1). default `1` |
| `keyword` | string | yes | The search keyword.  |
| `userType` | string |  | Filter by user type. one of: `common_user`, `enterprise_user`, `personal_user` |

## Details

Search Douyin (TikTok China) users by keyword with page-based pagination and optional account-type filtering. Use it to discover creators, brands, or verified accounts for research.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search-user" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "美食"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | The search keyword. |
| `page` | integer | No | Page number (starting from 1). |
| `userType` | string | No | Filter by user type. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/search-user.json`](../../../catalog/models/douyin/search-user.json) · Store page: https://www.sandbase.ai/model/douyin/search-user
