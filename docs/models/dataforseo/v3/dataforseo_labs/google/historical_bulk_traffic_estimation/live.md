# DataForSEO Labs Historical Bulk Traffic Estimation API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.1224 per call · **Modes:** sync

Monthly estimated organic and paid traffic history for up to 1,000 domains.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.1224**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `targets` | array |  | Array of domains (up to 1,000).  |
| `date_from` | string |  | Optional start date, "yyyy-mm-dd".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns monthly estimated organic and paid Google search traffic history for each domain in a list. Send up to 1,000 domains in `targets`, plus a `location_code` and `language_code`.

### Use cases

- Compare the organic traffic trend of two competing retail sites over recent months.
- Spot a sudden drop or rise in a domain's estimated search traffic.
- Track how much a competitor relies on paid search versus organic search.
- Rank a large list of prospect domains by estimated traffic value.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"targets": ["nike.com", "adidas.com"], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date_from` | string | No | Optional start date, "yyyy-mm-dd". |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |
| `targets` | array | No | Array of domains (up to 1,000). |

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
        "function": "historical_bulk_traffic_estimation",
        "language_code": "en",
        "location_code": 2840,
        "se_type": "google",
        "targets": [
          "nike.com"
        ]
      },
      "id": "11030828-2190-0563-0000-31023f757648",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "metrics": {
                "featured_snippet": null,
                "local_pack": null,
                "organic": [
                  {
                    "count": 421526,
                    "etv": 4397718.960320013,
                    "month": 10,
                    "year": 2026
                  }
                ],
                "paid": [
                  {
                    "count": 1,
                    "etv": 6.212034702301025,
                    "month": 10,
                    "year": 2026
                  }
                ]
              },
              "se_type": "google",
              "target": "adidas.com"
            }
          ],
          "items_count": 2,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google",
          "total_count": 2
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.1797 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.1870 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].target` | The domain the metrics belong to. Each domain in `targets` gets one item. |
| `tasks[].result[].items[].metrics.organic[]` | Monthly history of organic search traffic for the domain. Each entry is one month, with the newest month first. |
| `tasks[].result[].items[].metrics.paid[]` | Monthly history of paid search traffic for the domain, in the same entry format as `organic`. |
| `tasks[].result[].items[].metrics.organic[].count / tasks[].result[].items[].metrics.paid[].count` | Number of ranking keywords counted for that month. For `paid`, it is the number of keywords with paid results. |
| `tasks[].result[].items[].metrics.organic[].etv / tasks[].result[].items[].metrics.paid[].etv` | Estimated traffic value for that month. Treat it as a relative figure for comparing months and domains. |
| `tasks[].result[].items[].metrics.organic[].year / tasks[].result[].items[].metrics.organic[].month` | Calendar year and month number (1 to 12) of the entry. The `paid` entries use the same keys. |
| `tasks[].result[].items[].metrics.featured_snippet / tasks[].result[].items[].metrics.local_pack` | Metrics for featured snippets and local packs. Both are `null` in this response. |
| `tasks[].result[].total_count` | Number of domain items in the result. Compare it with `items_count` to check the item count. |

### Notes

- Pass domains without a protocol, for example `nike.com`.
- Set `date_from` in `yyyy-mm-dd` format to choose the start of the history.
- Items do not follow the order of `targets`. Match each item by its `target` value.
- Read results from `tasks[].result[]`. The `tasks[].id` value identifies the task.

### Pricing

Billed at the actual cost of each call, about $0.1224 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live
