# DataForSEO Backlinks New and Lost Over Time API: pricing, parameters and code examples

`dataforseo/v3/backlinks/timeseries_new_lost_summary/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024144 per call · **Modes:** sync

New and lost backlinks and referring domains for a domain, grouped by day, week, month or year.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024144**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/timeseries_new_lost_summary/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/timeseries_new_lost_summary/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/timeseries_new_lost_summary/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/timeseries_new_lost_summary/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/timeseries_new_lost_summary/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | string |  | Domain, e.g. "nike.com".  |
| `date_to` | string |  | End date, "yyyy-mm-dd".  |
| `date_from` | string |  | Start date, "yyyy-mm-dd".  |
| `group_range` | string |  | "day", "week", "month" or "year".  |

## Details

Returns the number of new and lost backlinks and referring domains for a domain, grouped into day, week, month or year buckets. It needs a `target` domain, a date range and a `group_range` value.

### Use cases

- Track whether a brand domain is gaining or losing links month over month.
- Spot a month with a large spike in lost backlinks and investigate the cause.
- Compare link growth for a domain before and after a site migration or campaign.
- Build a monthly link churn chart for an SEO report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/timeseries_new_lost_summary/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "date_from": "2026-07-01", "date_to": "2026-10-01", "group_range": "month"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date_from` | string | No | Start date, "yyyy-mm-dd". |
| `date_to` | string | No | End date, "yyyy-mm-dd". |
| `group_range` | string | No | "day", "week", "month" or "year". |
| `target` | string | No | Domain, e.g. "nike.com". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "backlinks",
        "date_from": "2026-07-01",
        "date_to": "2026-10-01",
        "function": "timeseries_new_lost_summary",
        "group_range": "month",
        "target": "nike.com"
      },
      "id": "11030828-2190-0460-0000-b953ac10804f",
      "path": [
        "v3"
      ],
      "result": [
        {
          "date_from": "2026-07-01",
          "date_to": "2026-10-01",
          "group_range": "month",
          "items": [
            {
              "date": "2026-07-31 00:00:00 +00:00",
              "lost_backlinks": 1501962,
              "lost_referring_domains": 4175,
              "lost_referring_main_domains": 3639,
              "new_backlinks": 662450,
              "new_referring_domains": 2097,
              "new_referring_main_domains": 1725,
              "type": "backlinks_timeseries_new_lost_summary"
            }
          ],
          "items_count": 4,
          "target": "nike.com"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0076 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0148 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].target` | The domain the numbers describe. |
| `tasks[].result[].group_range` | The bucket size used for the rows, such as `month`. |
| `tasks[].result[].items[].date` | End date of the bucket, as a timestamp like `2026-07-31 00:00:00 +00:00`. |
| `tasks[].result[].items[].new_backlinks / lost_backlinks` | Count of backlinks gained and lost by the target in that bucket. |
| `tasks[].result[].items[].new_referring_domains / lost_referring_domains` | Count of referring domains gained and lost in that bucket. |
| `tasks[].result[].items[].new_referring_main_domains / lost_referring_main_domains` | Count of referring main domains gained and lost in that bucket. |
| `tasks[].result[].items_count` | Number of rows reported for the result. |
| `tasks[].result_count` | Number of result objects in the task. |

### Notes

- Set `group_range` to `day`, `week`, `month` or `year`. Send dates as `yyyy-mm-dd`.
- Each `items[]` row has a bucket end date. In the sample, the monthly rows are dated `2026-07-31`, `2026-08-31` and `2026-09-30`.
- For total backlink counts over time rather than new and lost, call [DataForSEO Backlinks Totals Over Time](/apis/dataforseo/v3/backlinks/timeseries_summary/live).
- For a single snapshot of a domain's link profile, call [DataForSEO Backlinks Summary](/apis/dataforseo/v3/backlinks/summary/live).

### Pricing

Billed at the actual cost of each call, about $0.024144 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/timeseries_new_lost_summary/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/timeseries_new_lost_summary/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/timeseries_new_lost_summary/live
