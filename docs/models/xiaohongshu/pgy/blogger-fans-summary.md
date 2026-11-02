# Xiaohongshu (RED) PGY Blogger Fans Summary API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-fans-summary` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns an overview of a Xiaohongshu blogger audience on PGY, including fan scale and activity metrics. Looks up fan statistics for a specified blogger user ID.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-fans-summary", "user_id": "60b137080000000001000301"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-fans-summary', {'user_id': '60b137080000000001000301'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-fans-summary", {
  "user_id": "60b137080000000001000301"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-fans-summary", sandbase.Params{
	"user_id": "60b137080000000001000301",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-fans-summary` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Blogger user ID  |

## Details

Retrieve audience overview metrics for a PGY blogger by supplying the target `user_id`. It returns fan statistics such as audience scale and activity levels.

### Use cases

- Evaluate blogger audience size and engagement before collaboration.
- Analyze fan scale metrics for targeted influencer campaigns.
- Monitor changes in blogger follower activity over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-fans-summary" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "60b137080000000001000301"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Blogger user ID |

### Notes

- Requires the blogger's `user_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/model/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Data Summary](/model/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Details](/model/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-fans-summary.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-fans-summary.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-fans-summary
