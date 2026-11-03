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

Returns fan growth statistics for a Douyin Xingtu creator over a date range. It needs the creator's `kolId`, a `startDate` and an `endDate` in `yyyy-MM-dd` format.

### Use cases

- Check the net fan change of a creator between two dates before booking a campaign.
- Compare the fan growth rate of several creators over the same period.
- Spot creators who lost fans in a given month using the negative growth values.
- Feed daily fan data into a dashboard that tracks creator audience size.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-daily-fans-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"endDate": "2025-01-01", "kolId": "7048929565493690398", "startDate": "2024-12-01"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `endDate` | string | Yes | End date, format: yyyy-MM-dd |
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id` |
| `startDate` | string | Yes | Start date, format: yyyy-MM-dd |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "daily": [],
  "delta": [],
  "description": "",
  "fans_advice": "",
  "fans_growth": "0",
  "fans_growth_rate": 0,
  "fans_growth_rate_v2": {
    "value": -22
  },
  "fans_growth_v2": {
    "value": -256
  },
  "raw_play_rate": {}
}
```

### Response fields

| Field | Meaning |
|---|---|
| `fans_growth_v2.value` | Net fan change over the requested date range. A negative number means the creator lost fans. |
| `fans_growth_rate_v2.value` | Fan growth rate over the requested date range. A negative number means a decline. |
| `fans_growth` | Older fan growth value, returned as a string. It can be `"0"` even when `fans_growth_v2.value` is not zero. |
| `fans_growth_rate` | Older fan growth rate, returned as a number. It can be `0` even when `fans_growth_rate_v2.value` is not zero. |
| `daily[]` | List of per-day fan entries. It was empty in this response. |
| `delta[]` | List of fan change entries. It was empty in this response. |
| `fans_advice / description` | Text fields for advice and a description. Both were empty strings in this response. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. `status_code` is `0` and `status_message` is empty in this response. |

### Notes

- Get `kolId` from [Douyin XingTu KOL ID by User ID](/apis/douyin/xingtu/xingtu-kolid-by-uid), [Douyin XingTu kolId Lookup](/apis/douyin/xingtu/xingtu-kolid-by-sec-user-id) or [Douyin XingTu KOL ID by Unique ID](/apis/douyin/xingtu/xingtu-kolid-by-unique-id).
- Send `startDate` and `endDate` as `yyyy-MM-dd`, for example `2024-12-01`.
- The `daily` and `delta` lists can come back empty while the `_v2` growth fields still hold values, so read `fans_growth_v2.value` and `fans_growth_rate_v2.value` first.

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/apis/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/apis/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/apis/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-daily-fans-v1.json`](../../../../catalog/models/douyin/xingtu/kol-daily-fans-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-daily-fans-v1
