# DataForSEO Labs Domain Metrics by Categories API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.132 per call · **Modes:** sync

Top domains in product or service categories with organic traffic and keyword metrics on two dates.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of domains to return.  |
| `first_date` | string |  | First comparison date, "yyyy-mm-dd".  |
| `second_date` | string |  | Second comparison date, "yyyy-mm-dd".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |
| `category_codes` | array |  | Array of category codes.  |

## Details

This API returns the top domains in one or more Google product or service categories. Each domain has organic and paid traffic and keyword metrics on two dates that you choose. It needs `category_codes`, `location_code`, `language_code`, `first_date` and `second_date`.

### Use cases

- Rank the biggest competitors in a retail category, such as auto parts, by estimated organic traffic.
- Track which domains gained or lost organic keywords and traffic between two dates.
- Compare organic and paid footprints of category leaders to see who relies on paid search.
- Build a shortlist of domains to study further for a market entry report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_codes": [10994], "location_code": 2840, "language_code": "en", "first_date": "2026-01-01", "second_date": "2026-06-01", "limit": 10}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_codes` | array | No | Array of category codes. |
| `first_date` | string | No | First comparison date, "yyyy-mm-dd". |
| `language_code` | string | No | Language code, e.g. "en". |
| `limit` | integer | No | Maximum number of domains to return. |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |
| `second_date` | string | No | Second comparison date, "yyyy-mm-dd". |

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
        "category_codes": [
          10994
        ],
        "first_date": "2026-01-01",
        "function": "domain_metrics_by_categories",
        "language_code": "en",
        "limit": 10,
        "location_code": 2840,
        "se_type": "google"
      },
      "id": "11030829-1614-0403-0000-ce7e1395549b",
      "path": [
        "v3"
      ],
      "result": [
        {
          "categories": [
            10994
          ],
          "items": [
            {
              "domain": "www.autozone.com",
              "main_domain": "autozone.com",
              "metrics_difference": {
                "featured_snippet": null,
                "local_pack": null,
                "organic": {
                  "clickstream_age_distribution": null,
                  "clickstream_etv": null,
                  "clickstream_gender_distribution": null,
                  "count": -643695,
                  "estimated_paid_traffic_cost": 1291032.503690768,
                  "etv": 385656.67153696716,
                  "is_down": -306867,
                  "is_lost": 2310
                },
                "paid": {
                  "clickstream_age_distribution": null,
                  "clickstream_etv": null,
                  "clickstream_gender_distribution": null,
                  "count": 6,
                  "estimated_paid_traffic_cost": 7.220676726405776,
                  "etv": 121.67557410694808,
                  "is_down": 0,
                  "is_lost": 6
                }
              },
              "metrics_history": {
                "202601": {
                  "featured_snippet": null,
                  "local_pack": null,
                  "organic": {
                    "clickstream_age_distribution": null,
                    "clickstream_etv": null,
                    "clickstream_gender_distribution": null,
                    "count": 2046519,
                    "estimated_paid_traffic_cost": 8323463.158129627,
                    "etv": 14160725.027441023,
                    "is_down": 581165,
                    "is_lost": 700996
                  },
                  "paid": {
                    "clickstream_age_distribution": null,
                    "clickstream_etv": null,
                    "clickstream_gender_distribution": null,
                    "count": 6,
                    "estimated_paid_traffic_cost": 9.662051890147202,
                    "etv": 81.6208776187808,
                    "is_down": 0,
                    "is_lost": 4
                  }
                },
                "202606": {
                  "featured_snippet": null,
                  "local_pack": null,
                  "organic": {
                    "clickstream_age_distribution": null,
                    "clickstream_etv": null,
                    "clickstream_gender_distribution": null,
                    "count": 1402824,
                    "estimated_paid_traffic_cost": 9614495.661820395,
                    "etv": 14546381.69897799,
                    "is_down": 274298,
                    "is_lost": 703306
                  },
                  "paid": {
                    "clickstream_age_distribution": null,
                    "clickstream_etv": null,
                    "clickstream_gender_distribution": null,
                    "count": 12,
                    "estimated_paid_traffic_cost": 16.882728616552978,
                    "etv": 203.29645172572887,
                    "is_down": 0,
                    "is_lost": 10
                  }
                }
              },
              "organic_count": 1219065,
              "organic_etv": 11797831.982971847,
              "organic_is_lost": 655901,
              "organic_is_new": 544016
            }
          ],
          "items_count": 10,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google",
          "total_count": 56783
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "14.3335 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "14.3857 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].domain / tasks[].result[].items[].main_domain` | The domain as ranked, and its root domain without the subdomain. |
| `tasks[].result[].items[].organic_etv` | Estimated organic traffic value (`etv`) for the domain in this category. |
| `tasks[].result[].items[].organic_count` | Number of organic keywords the domain ranks for in this category. |
| `tasks[].result[].items[].organic_is_new / tasks[].result[].items[].organic_is_lost` | Count of organic keywords that are new or lost for the domain. |
| `tasks[].result[].items[].metrics_history.202601.organic.etv / tasks[].result[].items[].metrics_history.202606.organic.etv` | Organic traffic estimate for the domain in each monthly snapshot. The keys `202601` and `202606` match `first_date` and `second_date` in this example. |
| `tasks[].result[].items[].metrics_history.202601.organic.count / tasks[].result[].items[].metrics_history.202606.organic.count` | Organic keyword count for the domain in each monthly snapshot. |
| `tasks[].result[].items[].metrics_history.202601.paid.etv / tasks[].result[].items[].metrics_history.202606.paid.etv` | Paid traffic estimate for the domain in each monthly snapshot. |
| `tasks[].result[].items[].metrics_difference.organic.etv / tasks[].result[].items[].metrics_difference.organic.count` | Change in organic traffic estimate and keyword count between the two dates. Negative values mean a drop. |
| `tasks[].result[].total_count / tasks[].result[].items_count` | Total domains matching the category and the number returned in this response. |

### Notes

- Set `limit` to control how many domains come back. This response returned 10 items, and `total_count` was 56783.
- The keys under `metrics_history` combine the year and month of `first_date` and `second_date`. For example, `2026-01-01` gives `202601`.
- `location_code` 2840 is the United States and `language_code` `en` is English.
- Fields such as `featured_snippet`, `local_pack` and the `clickstream_*` values can be `null`.

### Pricing

Billed at the actual cost of each call, about $0.132 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live
