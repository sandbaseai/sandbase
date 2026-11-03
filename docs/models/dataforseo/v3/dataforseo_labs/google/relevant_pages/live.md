# DataForSEO Google Relevant Pages API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/relevant_pages/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0132 per call · **Modes:** sync

List a domain's pages that rank in Google, with the keywords, positions, estimated traffic and SERP features each page earns.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/relevant_pages/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/relevant_pages/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/relevant_pages/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/relevant_pages/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/relevant_pages/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  |   |
| `target` | string |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

This API lists pages of a domain that rank in Google for a chosen country and language. For each page it returns the number of ranking keywords and the estimated traffic from organic and paid results. It needs a `target` domain, a `location_code` and a `language_code`.

### Use cases

- Find which pages on your site bring in the most estimated organic traffic.
- Compare the top ranking pages of a competitor domain with your own.
- Spot pages that have lost rankings by checking the `is_lost` and `is_down` counts.
- Build a content audit list of every page that ranks in Google for a given market.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/relevant_pages/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "sandbase.ai", "location_code": 2840, "language_code": "en", "limit": 10}'
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
        "function": "relevant_pages",
        "language_code": "en",
        "limit": 10,
        "location_code": 2840,
        "se_type": "google",
        "target": "sandbase.ai"
      },
      "id": "11030828-2190-0385-0000-b1f9f1f92114",
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
                "organic": {
                  "clickstream_age_distribution": null,
                  "clickstream_etv": null,
                  "clickstream_gender_distribution": null,
                  "count": 7,
                  "estimated_paid_traffic_cost": 4.855564475059509,
                  "etv": 3.6234274385496974,
                  "is_down": 0,
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
              "page_address": "https://www.sandbase.ai/model/instagram/v3/user-id-by-username",
              "se_type": "google"
            }
          ],
          "items_count": 10,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google",
          "target": "sandbase.ai",
          "total_count": 101
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.3039 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.3130 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].page_address` | Full URL of a page on the target domain that ranks in Google. |
| `tasks[].result[].items[].metrics.organic.count` | Number of organic results the page has in this location and language. |
| `tasks[].result[].items[].metrics.organic.etv` | Estimated traffic value of the page from organic results. |
| `tasks[].result[].items[].metrics.organic.estimated_paid_traffic_cost` | Estimated cost to buy the same organic traffic through paid ads. |
| `tasks[].result[].items[].metrics.organic.is_down / tasks[].result[].items[].metrics.organic.is_lost` | Counts of organic results that moved down or dropped out of the rankings. |
| `tasks[].result[].items[].metrics.paid.count / tasks[].result[].items[].metrics.paid.etv` | Same measures for paid results. They are `0` for the pages in this sample. |
| `tasks[].result[].items[].metrics.featured_snippet / tasks[].result[].items[].metrics.local_pack` | Metrics for these SERP features. The value is `null` when the page has none. |
| `tasks[].result[].total_count` | Total number of ranking pages found for the target. |
| `tasks[].result[].items_count` | Number of pages returned in this response. |

### Notes

- Pass the domain in `target` without a path. Set `location_code` (for example `2840`) and `language_code` (for example `en`) to choose the market.
- Use `limit` to set how many pages come back. Compare `items_count` with `total_count` to see whether more pages exist.
- The `clickstream_*` fields are `null` in this response.

### Pricing

Billed at the actual cost of each call, about $0.0132 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/relevant_pages/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/relevant_pages/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/relevant_pages/live
