# Douyin User Profile API: pricing, parameters and code examples

`douyin/user-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get a Douyin (TikTok China) user profile by secUid. Use it to review a known creator or account before monitoring related content or conducting account research.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/user-detail", "secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/user-detail', {'secUid': 'MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/user-detail", {
  "secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/user-detail", sandbase.Params{
	"secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24",
})
```

Same call via the path form: `POST /v1/api/douyin/user-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `secUid` | string | yes | The unique user ID (sec_uid) on Douyin.  |

## Details

Get a Douyin (TikTok China) user profile by secUid. Use it to review a known creator or account before monitoring related content or conducting account research.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/user-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | Yes | The unique user ID (sec_uid) on Douyin. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/user-detail.json`](../../../catalog/models/douyin/user-detail.json) · Store page: https://www.sandbase.ai/model/douyin/user-detail
