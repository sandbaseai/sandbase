# Douyin User Published Videos API: pricing, parameters and code examples

`douyin/user-video-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get videos published by a Douyin (TikTok China) user, with cursor pagination and newest or most-popular sorting. Use it to browse or monitor a creator's public video output.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/user-video-list", "secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/user-video-list', {'secUid': 'MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/user-video-list", {
  "secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/user-video-list", sandbase.Params{
	"secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24",
})
```

Same call via the path form: `POST /v1/api/douyin/user-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `secUid` | string | yes | The unique user ID (sec_user_id) on Douyin.  |
| `sortType` | string |  | Sort order: `LATEST` for newest first (default), or `MOST_POPULAR` for most popular first. one of: `LATEST`, `MOST_POPULAR`; default `"LATEST"` |
| `maxCursor` | string |  | Pagination cursor; use 0 for the first page, and the `max_cursor` from the previous response for subsequent pages. default `"0"` |

## Details

Get videos published by a Douyin (TikTok China) user, with cursor pagination and newest or most-popular sorting. Use it to browse or monitor a creator's public video output.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/user-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | Yes | The unique user ID (sec_user_id) on Douyin. |
| `maxCursor` | string | No | Pagination cursor; use 0 for the first page, and the `max_cursor` from the previous response for subsequent pages. |
| `sortType` | string | No | Sort order: `LATEST` for newest first (default), or `MOST_POPULAR` for most popular first. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/user-video-list.json`](../../../catalog/models/douyin/user-video-list.json) · Store page: https://www.sandbase.ai/model/douyin/user-video-list
