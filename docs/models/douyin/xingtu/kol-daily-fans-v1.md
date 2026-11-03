# Douyin Xingtu KOL Daily Fans API: pricing, parameters and code examples

`douyin/xingtu/kol-daily-fans-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns daily fan statistics for a Douyin Xingtu creator over a specified date range. Requires the creator ID alongside the start and end dates formatted as yyyy-MM-dd.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-daily-fans-v1", "endDate": "2026-09-28", "kolId": "6677767167234015243", "startDate": "2026-09-01"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-daily-fans-v1', {'endDate': '2026-09-28', 'kolId': '6677767167234015243', 'startDate': '2026-09-01'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-daily-fans-v1", {
  "endDate": "2026-09-28",
  "kolId": "6677767167234015243",
  "startDate": "2026-09-01"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-daily-fans-v1", sandbase.Params{
	"endDate": "2026-09-28",
	"kolId": "6677767167234015243",
	"startDate": "2026-09-01",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-daily-fans-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |
| `endDate` | string | yes | End date, format: yyyy-MM-dd  |
| `startDate` | string | yes | Start date, format: yyyy-MM-dd  |

## Details

Retrieve daily fan counts for a specified Douyin creator by providing `kolId`, `startDate`, and `endDate`.

### Use cases

- Track daily follower growth trends for specific Douyin creators.
- Evaluate creator audience changes over selected date intervals.
- Monitor audience retention and acquisition fluctuations across specific ranges.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-daily-fans-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"endDate": "2025-01-01", "kolId": "7048929565493690398", "startDate": "2024-12-01"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xin… |
| `endDate` | string | Yes | End date, format: yyyy-MM-dd |
| `startDate` | string | Yes | Start date, format: yyyy-MM-dd |

### Notes

- `kolId` can be obtained from the corresponding Xingtu KOL ID lookup endpoints using UID, sec_user_id, or unique ID.
- `startDate` and `endDate` must be formatted as yyyy-MM-dd.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/apis/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/apis/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/apis/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-daily-fans-v1.json`](../../../../catalog/models/douyin/xingtu/kol-daily-fans-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-daily-fans-v1
