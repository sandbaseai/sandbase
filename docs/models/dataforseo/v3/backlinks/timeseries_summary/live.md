# DataForSEO Backlinks Totals Over Time API: pricing, parameters and code examples

`dataforseo/v3/backlinks/timeseries_summary/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024144 per call · **Modes:** sync

Backlink and referring domain totals for a domain over time, grouped by day, week, month or year.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024144**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/timeseries_summary/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/timeseries_summary/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/timeseries_summary/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/timeseries_summary/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/timeseries_summary/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | string |  | Domain, e.g. "nike.com".  |
| `date_to` | string |  | End date, "yyyy-mm-dd".  |
| `date_from` | string |  | Start date, "yyyy-mm-dd".  |
| `group_range` | string |  | "day", "week", "month" or "year".  |

## Details

This API returns backlink and referring domain totals for a domain, one row per day, week, month or year. It needs a `target` domain, a date range and a `group_range` value.

### Use cases

- Chart how many backlinks nike.com gained or lost month by month.
- Track the drop or growth in referring domains after a site migration or link cleanup.
- Compare the `rank` trend of a domain against its backlink totals over a quarter.
- Check how the share of nofollow links changes over time for a domain.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/timeseries_summary/live" \
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
        "function": "timeseries_summary",
        "group_range": "month",
        "target": "nike.com"
      },
      "id": "11030828-2190-0459-0000-d67dbdbc4499",
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
              "backlinks": 20107378,
              "backlinks_nofollow": 3643045,
              "date": "2026-07-31 00:00:00 +00:00",
              "rank": 607,
              "referring_domains": 175657,
              "referring_domains_nofollow": 19300,
              "referring_ips": 64636,
              "referring_main_domains": 162842
            }
          ],
          "items_count": 4,
          "target": "nike.com"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0218 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0296 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].date` | End date of the period for this row, as a timestamp such as `2026-07-31 00:00:00 +00:00`. |
| `tasks[].result[].items[].backlinks / tasks[].result[].items[].backlinks_nofollow` | Total backlinks pointing to the target in that period, and how many of them are nofollow. |
| `tasks[].result[].items[].referring_domains / tasks[].result[].items[].referring_domains_nofollow` | Number of referring domains linking to the target, and how many of them link with nofollow. |
| `tasks[].result[].items[].referring_main_domains` | Number of referring main domains linking to the target. |
| `tasks[].result[].items[].referring_ips` | Number of IP addresses that host the referring domains. |
| `tasks[].result[].items[].rank` | Rank value for the target in that period. A lower number in this response goes with a smaller list of figures, so compare it only between rows of the same call. |
| `tasks[].result[].target` | The domain the totals describe. |
| `tasks[].result[].items_count` | Count of rows reported for the result. |

### Notes

- Set `group_range` to `day`, `week`, `month` or `year` to change the size of each period. Dates use the `yyyy-mm-dd` format.
- Each call is one task. Read the rows from `tasks[].result[].items[]`.
- For a single current snapshot of a domain, call [DataForSEO Backlinks Summary](/apis/dataforseo/v3/backlinks/summary/live). For gained and lost links per period, call [DataForSEO Backlinks New and Lost Over Time](/apis/dataforseo/v3/backlinks/timeseries_new_lost_summary/live).

### Pricing

Billed at the actual cost of each call, about $0.024144 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/timeseries_summary/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/timeseries_summary/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/timeseries_summary/live
