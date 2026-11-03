# DataForSEO Google Bulk Traffic Estimation API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/bulk_traffic_estimation/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01224 per call · **Modes:** sync

Estimate monthly organic and paid traffic for up to 100 domains, subdomains or URLs in Google by location and language.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01224**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/bulk_traffic_estimation/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/bulk_traffic_estimation/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/bulk_traffic_estimation/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/bulk_traffic_estimation/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/bulk_traffic_estimation/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `targets` | array |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

Returns estimated monthly organic and paid search traffic for a list of domains, subdomains or URLs on Google. Send up to 100 `targets` with a `location_code` and a `language_code`.

### Use cases

- Compare the estimated organic traffic of several competitor domains in one call.
- Check whether a domain buys paid search traffic by reading its paid keyword count and traffic value.
- Rank a list of prospect sites by estimated search traffic before outreach.
- Track how a set of domains differs between locations by repeating the call with another `location_code`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/bulk_traffic_estimation/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"targets": ["openai.com", "anthropic.com"], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No |  |
| `location_code` | integer | No |  |
| `targets` | array | No |  |

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
        "function": "bulk_traffic_estimation",
        "language_code": "en",
        "location_code": 2840,
        "se_type": "google",
        "targets": [
          "openai.com"
        ]
      },
      "id": "11030828-2190-0391-0000-28e0759fdf73",
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
                  "count": 322762,
                  "etv": 18608008.67582856
                },
                "paid": {
                  "count": 40,
                  "etv": 422.7895669937134
                }
              },
              "se_type": "google",
              "target": "openai.com"
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
      "time": "0.2070 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.2155 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].target` | The domain, subdomain or URL that the metrics describe. Match it to the value you sent in `targets`. |
| `tasks[].result[].items[].metrics.organic.count` | Number of organic results counted for the target, such as `322762` for `openai.com`. |
| `tasks[].result[].items[].metrics.organic.etv` | Estimated traffic value (`etv`) of the target's organic results. Use it to compare targets with each other. |
| `tasks[].result[].items[].metrics.paid.count` | Number of paid results counted for the target. A value of `0` means no paid results were found. |
| `tasks[].result[].items[].metrics.paid.etv` | Estimated traffic value (`etv`) of the target's paid results. |
| `tasks[].result[].items[].metrics.featured_snippet / tasks[].result[].items[].metrics.local_pack` | Metrics for featured snippet and local pack results. They are `null` when none apply to the target. |
| `tasks[].result[].items_count / tasks[].result[].total_count` | Number of items in the result and total number of items available. Both are `2` for the two targets in this request. |
| `tasks[].result[].location_code / tasks[].result[].language_code` | The location and language the estimate was calculated for. |

### Notes

- Pass `targets` as an array of up to 100 strings. Each string can be a domain, a subdomain or a URL.
- Use `location_code` `2840` with `language_code` `en` for the example request. Other location codes select other markets.
- Results come back in `tasks[].result[].items[]`, one item per target. Read `tasks[].status_code` to confirm the task succeeded (`20000` means OK).

### Pricing

Billed at the actual cost of each call, about $0.01224 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/bulk_traffic_estimation/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/bulk_traffic_estimation/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/bulk_traffic_estimation/live
