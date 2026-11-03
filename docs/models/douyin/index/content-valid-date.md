# Douyin Content Guide Valid Dates API: pricing, parameters and code examples

`douyin/index/content-valid-date` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the valid date ranges supported by the Douyin content guide index. Helps clients determine allowable date intervals before requesting trend and guide statistics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/content-valid-date"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/content-valid-date', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/content-valid-date", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/content-valid-date", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/content-valid-date` with the body above minus `model`.

## Details

Returns the latest valid dates for the Douyin content guide index. It needs no input. The response gives one date for day, week and month data, plus the earliest week available.

### Use cases

- Set the maximum selectable date in a date picker for a Douyin content guide dashboard.
- Check the latest `day`, `week` or `month` value before you request content trend data.
- Limit weekly queries to the range between `earliest_week` and `week`.
- Pick the most recent valid date for a scheduled report job.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-valid-date" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "day": "20261101",
  "earliest_week": "20260809",
  "month": "20261031",
  "week": "20261101"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `day` | Latest valid date for daily data, as a `YYYYMMDD` string. |
| `week` | Latest valid date for weekly data, as a `YYYYMMDD` string. |
| `earliest_week` | Earliest valid date for weekly data. Use it as the lower bound of a weekly range. |
| `month` | Latest valid date for monthly data, as a `YYYYMMDD` string. The value in the example is the last day of a month. |

### Notes

- Send an empty JSON object `{}`. The API has no request parameters.
- All dates are strings in `YYYYMMDD` format.
- Only the weekly data has an earliest date in this response. The response shows no earliest date for `day` or `month`.
- For valid dates of other Douyin Index data types, call [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-valid-date.json`](../../../../catalog/models/douyin/index/content-valid-date.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-valid-date
