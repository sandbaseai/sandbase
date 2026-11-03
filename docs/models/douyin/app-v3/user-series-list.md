# Douyin User Series List API: pricing, parameters and code examples

`douyin/app-v3/user-series-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of video series or playlet collections for a specific Douyin user. Query by user ID or encrypted user ID, with pagination supported via a cursor.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/user-series-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/user-series-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/user-series-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/user-series-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/user-series-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.  |
| `user_id` | string |  | User id  |
| `sec_user_id` | string |  | User encrypted id  |

## Details

Retrieve playlet and series collections associated with an account by providing `user_id` or `sec_user_id`. Pagination is handled through the `cursor` parameter.

### Use cases

- Browse playlet collections hosted by a specific Douyin creator.
- Track episodic video series released across user profiles.
- Paginate through cataloged video compilations for content discovery.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/user-series-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |
| `user_id` | string | No | User id |
| `sec_user_id` | string | No | User encrypted id |

### Notes

- Set `cursor` to 0 for the first page, then pass the cursor value from the previous response for subsequent pages.
- Identify target accounts using either `user_id` or `sec_user_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/user-series-list.json`](../../../../catalog/models/douyin/app-v3/user-series-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/user-series-list
