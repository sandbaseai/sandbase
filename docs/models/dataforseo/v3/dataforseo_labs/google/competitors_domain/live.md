# DataForSEO Google Competitors Domain API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/competitors_domain/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0126 per call · **Modes:** sync

Returns Google organic search competitor domains and comparative ranking metrics for a specified domain, enabling competitive research and market analysis.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0126**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/competitors_domain/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/competitors_domain/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/competitors_domain/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/competitors_domain/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/competitors_domain/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `target` | string |  | Target domain or page, e.g. "nike.com".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns Google organic and paid search competitors for a target domain, with keyword overlap and traffic metrics for each competitor. It needs a `target` domain, and you can set `location_code`, `language_code` and `limit`.

### Use cases

- Find which domains rank for the same Google keywords as your site and sort them by overlap.
- Compare the estimated organic traffic value of a brand against its closest search rivals.
- Check how many of a competitor's keywords are shared with your domain before planning content.
- Spot large general sites such as video or marketplace domains that compete for the same queries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/competitors_domain/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "limit": 5, "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No | Language code, e.g. "en". |
| `limit` | integer | No | Maximum number of results (up to 100). |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |
| `target` | string | No | Target domain or page, e.g. "nike.com". |

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
        "function": "competitors_domain",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "se_type": "google",
        "target": "nike.com"
      },
      "id": "11030829-1614-0386-0000-2ae0341339fd",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "avg_position": 13.995931809376211,
              "competitor_metrics": {
                "featured_snippet": null,
                "local_pack": null,
                "organic": {
                  "clickstream_age_distribution": null,
                  "clickstream_etv": null,
                  "clickstream_gender_distribution": null,
                  "count": 665888,
                  "estimated_paid_traffic_cost": 5818161.501292778,
                  "etv": 8815052.876410568,
                  "is_down": 124703,
                  "is_lost": 0
                },
                "paid": {
                  "clickstream_age_distribution": null,
                  "clickstream_etv": null,
                  "clickstream_gender_distribution": null,
                  "count": 10,
                  "estimated_paid_traffic_cost": 155.61605195701122,
                  "etv": 196.75402009487152,
                  "is_down": 1,
                  "is_lost": 0
                }
              },
              "domain": "nike.com",
              "full_domain_metrics": {
                "featured_snippet": null,
                "local_pack": null,
                "organic": {
                  "clickstream_age_distribution": null,
                  "clickstream_etv": null,
                  "clickstream_gender_distribution": null,
                  "count": 665888,
                  "estimated_paid_traffic_cost": 5818161.501292776,
                  "etv": 8815052.876410566,
                  "is_down": 124703,
                  "is_lost": 386977
                },
                "paid": {
                  "clickstream_age_distribution": null,
                  "clickstream_etv": null,
                  "clickstream_gender_distribution": null,
                  "count": 10,
                  "estimated_paid_traffic_cost": 155.61605195701122,
                  "etv": 196.75402009487152,
                  "is_down": 1,
                  "is_lost": 17
                }
              },
              "intersections": 665898,
              "metrics": {
                "featured_snippet": null,
                "local_pack": null,
                "organic": {
                  "clickstream_age_distribution": null,
                  "clickstream_etv": null,
                  "clickstream_gender_distribution": null,
                  "count": 665888,
                  "estimated_paid_traffic_cost": 5818161.501292778,
                  "etv": 8815052.876410568,
                  "is_down": 124703,
                  "is_lost": 0
                },
                "paid": {
                  "clickstream_age_distribution": null,
                  "clickstream_etv": null,
                  "clickstream_gender_distribution": null,
                  "count": 10,
                  "estimated_paid_traffic_cost": 155.61605195701122,
                  "etv": 196.75402009487152,
                  "is_down": 1,
                  "is_lost": 0
                }
              },
              "se_type": "google",
              "sum_position": 9319863
            }
          ],
          "items_count": 5,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google",
          "target": "nike.com",
          "total_count": 617048
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "19.7067 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "19.7647 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].domain` | The competitor domain found for the target. |
| `tasks[].result[].items[].avg_position` | Average Google ranking position of the competitor across the shared keywords. |
| `tasks[].result[].items[].intersections` | Number of keywords where both the target and this competitor rank. |
| `tasks[].result[].items[].sum_position` | Sum of the competitor's ranking positions across the shared keywords. Dividing it by `intersections` gives `avg_position`. |
| `tasks[].result[].items[].metrics.organic.count / tasks[].result[].items[].metrics.organic.etv` | Number of organic keywords and estimated traffic value (`etv`) for the competitor, counted only over the shared keyword set. |
| `tasks[].result[].items[].full_domain_metrics.organic.count / tasks[].result[].items[].full_domain_metrics.organic.etv` | Organic keyword count and estimated traffic value for the competitor's whole domain, not only the shared keywords. |
| `tasks[].result[].items[].metrics.organic.estimated_paid_traffic_cost` | Estimated cost of buying the same organic traffic through paid ads. |
| `tasks[].result[].items[].full_domain_metrics.organic.is_down / tasks[].result[].items[].full_domain_metrics.organic.is_lost` | Counts of organic rankings that moved down and rankings that were lost for the whole domain. |
| `tasks[].result[].total_count` | Total number of competitor domains found for the target. |
| `tasks[].result[].items_count` | Number of competitor items returned in this response. |

### Notes

- Set `limit` to control how many competitors come back, up to 100.
- `location_code` 2840 is the United States and `language_code` `en` is English.
- Fields such as `clickstream_etv` and `featured_snippet` can be `null` when no data exists for that domain.
- The first item can be the target domain itself, as `nike.com` is in the sample response.

### Pricing

Billed at the actual cost of each call, about $0.0126 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/competitors_domain/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/competitors_domain/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/competitors_domain/live
