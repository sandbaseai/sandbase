# Xiaohongshu (RED) PGY Blogger Details API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-detail` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID. Returns creator metrics and account details.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-detail", "user_id": "60b137080000000001000301"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-detail', {'user_id': '60b137080000000001000301'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-detail", {
  "user_id": "60b137080000000001000301"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-detail", sandbase.Params{
	"user_id": "60b137080000000001000301",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Blogger user ID, obtainable from blogger list results or PGY blogger page URL  |

## Details

Retrieve detailed profile information for a PGY blogger on Xiaohongshu (RED). Supply the target creator's identifier via `user_id` to query their profile data.

### Use cases

- Inspect creator profiles on the PGY platform.
- Evaluate potential influencer partnerships.
- Analyze blogger metrics for campaign selection.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "60b137080000000001000301"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Blogger user ID, obtainable from blogger list results or PGY blogger page URL |

### Notes

- `user_id` is obtainable from blogger list results or the PGY blogger page URL.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/apis/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Data Summary](/apis/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Fan History](/apis/xiaohongshu/pgy/blogger-fans-history): Returns historical follower growth counts for a Xiaohongshu Pugongying blogger over time based on user ID and a selected date range.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-detail.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-detail
