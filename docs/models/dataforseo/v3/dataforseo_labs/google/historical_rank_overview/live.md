# DataForSEO Labs Historical Rank Overview API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/historical_rank_overview/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.1272 per call · **Modes:** sync

Monthly history of a domain's Google ranking positions and estimated traffic.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.1272**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/historical_rank_overview/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/historical_rank_overview/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/historical_rank_overview/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/historical_rank_overview/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/historical_rank_overview/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | string |  | Domain, e.g. "nike.com".  |
| `date_from` | string |  | Optional start date, "yyyy-mm-dd".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns a month-by-month history of how a domain ranks in Google organic and paid results. Each month includes the number of ranking keywords and estimated traffic. It needs a `target` domain, a `location_code` and a `language_code`.

### Use cases

- Plot a competitor's organic traffic trend over several months to spot growth or decline.
- Check whether a drop in rankings matches a drop in estimated traffic after a site change.
- Compare the size of organic and paid search presence for a brand in one market.
- Track how many keywords a domain gains or loses from month to month.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/historical_rank_overview/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date_from` | string | No | Optional start date, "yyyy-mm-dd". |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |
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
        "api": "dataforseo_labs",
        "function": "historical_rank_overview",
        "language_code": "en",
        "location_code": 2840,
        "se_type": "google",
        "target": "nike.com"
      },
      "id": "11030828-2190-0406-0000-a7b402597022",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "metrics": {
                "organic": {
                  "clickstream_age_distribution": null,
                  "clickstream_etv": null,
                  "clickstream_gender_distribution": null,
                  "count": 708684,
                  "estimated_paid_traffic_cost": 6718776.3187612,
                  "etv": 9311637.584005594,
                  "is_down": 134128,
                  "is_lost": 391386
                },
                "paid": {
                  "clickstream_age_distribution": null,
                  "clickstream_etv": null,
                  "clickstream_gender_distribution": null,
                  "count": 9,
                  "estimated_paid_traffic_cost": 104.72895193099976,
                  "etv": 207.44792461395264,
                  "is_down": 1,
                  "is_lost": 19
                }
              },
              "month": 10,
              "se_type": "google",
              "year": 2026
            }
          ],
          "items_count": 6,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google",
          "target": "nike.com",
          "total_count": 6
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.8074 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.8159 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[]` | One entry per month of history for the target domain. |
| `tasks[].result[].items[].year / month` | Calendar year and month number (1 to 12) for the entry. |
| `tasks[].result[].items[].metrics.organic.count` | Number of keywords the domain ranks for in Google organic results that month. |
| `tasks[].result[].items[].metrics.organic.etv` | Estimated traffic volume from organic results for that month. |
| `tasks[].result[].items[].metrics.organic.estimated_paid_traffic_cost` | Estimated cost of buying the same organic traffic through paid ads. |
| `tasks[].result[].items[].metrics.organic.is_down / is_lost` | Number of organic keywords that dropped in rank (`is_down`) and keywords that fell out of the results (`is_lost`) compared with the prior period. |
| `tasks[].result[].items[].metrics.paid.count` | Number of keywords the domain has paid ads for that month. |
| `tasks[].result[].items[].metrics.paid.etv / estimated_paid_traffic_cost` | Estimated traffic and estimated cost for the domain's paid results. |
| `tasks[].result[].items_count / total_count` | Number of monthly entries returned and the total available. |
| `tasks[].result[].target` | The domain the history belongs to. |

### Notes

- Pass the bare domain in `target`, for example `nike.com`, without a path.
- Use `date_from` in `yyyy-mm-dd` format to set the first month of the history.
- The `clickstream_*` fields were `null` in this response, so do not rely on them.
- Results sit in `tasks[].result`, and items appear with the newest month first.

### Pricing

Billed at the actual cost of each call, about $0.1272 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/historical_rank_overview/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/historical_rank_overview/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/historical_rank_overview/live
