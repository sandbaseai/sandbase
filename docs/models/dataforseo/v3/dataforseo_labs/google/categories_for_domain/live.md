# DataForSEO Google Categories for Domain API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/categories_for_domain/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0132 per call · **Modes:** sync

See which Google product and service categories a domain ranks for, with keyword counts and estimated traffic per category.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/categories_for_domain/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/categories_for_domain/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/categories_for_domain/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/categories_for_domain/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/categories_for_domain/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  |   |
| `target` | string |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

This API returns the Google product and service categories a domain ranks for in a given country and language. Each category row includes keyword counts and estimated traffic for organic and paid results. It needs a `target` domain, a `location_code` and a `language_code`.

### Use cases

- Check which topic categories drive the most organic traffic for a competitor domain.
- Compare the category mix of two sites to find topics where a rival ranks and you do not.
- Spot categories where a domain has paid keywords to see where it buys ads.
- Pick the categories to focus on when planning content for a new site section.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/categories_for_domain/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "openai.com", "location_code": 2840, "language_code": "en", "limit": 10}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No |  |
| `limit` | integer | No |  |
| `location_code` | integer | No |  |
| `target` | string | No |  |

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
        "function": "categories_for_domain",
        "language_code": "en",
        "limit": 10,
        "location_code": 2840,
        "se_type": "google",
        "target": "openai.com"
      },
      "id": "11030828-2190-0402-0000-25be71529d55",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "categories": [
                10013
              ],
              "metrics": {
                "featured_snippet": null,
                "local_pack": null,
                "organic": {
                  "clickstream_age_distribution": null,
                  "clickstream_etv": null,
                  "clickstream_gender_distribution": null,
                  "count": 44924,
                  "estimated_paid_traffic_cost": 37659.30839930046,
                  "etv": 21447.406957434636,
                  "is_down": 699,
                  "is_lost": 0
                },
                "paid": {
                  "clickstream_age_distribution": null,
                  "clickstream_etv": null,
                  "clickstream_gender_distribution": null,
                  "count": 0,
                  "estimated_paid_traffic_cost": 0,
                  "etv": 0,
                  "is_down": 0,
                  "is_lost": 0
                }
              },
              "se_type": "google"
            }
          ],
          "items_count": 10,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google",
          "target": "openai.com",
          "total_count": 2932
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.6141 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.6222 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].target` | The domain that was analyzed. |
| `tasks[].result[].total_count` | Total number of categories found for the domain. Compare it with `items_count` to see how many rows were returned. |
| `tasks[].result[].items_count` | Number of category rows in this response. It follows the `limit` you set. |
| `tasks[].result[].items[].categories` | List of Google category IDs for the row. The response gives IDs only, not names. |
| `tasks[].result[].items[].metrics.organic.count` | Number of organic keywords the domain ranks for in this category. |
| `tasks[].result[].items[].metrics.organic.etv` | Estimated organic traffic value for the category, a modeled traffic figure. |
| `tasks[].result[].items[].metrics.organic.estimated_paid_traffic_cost` | Estimated cost of buying the same organic traffic through ads. |
| `tasks[].result[].items[].metrics.organic.is_down / tasks[].result[].items[].metrics.organic.is_lost` | Counts of organic keywords whose ranking dropped (`is_down`) or disappeared (`is_lost`). |
| `tasks[].result[].items[].metrics.paid.count / tasks[].result[].items[].metrics.paid.etv` | Number of paid keywords in the category and their estimated traffic. Both are 0 when the domain has no paid keywords there. |

### Notes

- Pass `location_code` as a number, for example `2840`, and `language_code` as a short code such as `en`.
- Use `limit` to control how many category rows come back. Compare `total_count` with `items_count` to see if more categories exist.
- Fields such as `featured_snippet`, `local_pack` and the clickstream values can be `null` when no data exists for a category.
- Category IDs such as `10013` appear in `categories` as integers, so keep a lookup of category names to read them.

### Pricing

Billed at the actual cost of each call, about $0.0132 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/categories_for_domain/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/categories_for_domain/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/categories_for_domain/live
