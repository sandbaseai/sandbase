# DataForSEO Google Subdomains API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/subdomains/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0132 per call · **Modes:** sync

List the subdomains of a domain with their ranked keyword counts, position distribution and estimated organic traffic in Google.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/subdomains/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/subdomains/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/subdomains/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/subdomains/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/subdomains/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  |   |
| `target` | string |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

Returns the subdomains of a domain that rank in Google, with organic and paid ranking metrics for each one. It needs a `target` domain, plus `location_code` and `language_code` to pick the market.

### Use cases

- List every subdomain of a competitor and see which ones bring in the most estimated organic traffic.
- Compare a docs, help or community subdomain against the main site by ranked keyword count.
- Spot subdomains that have paid keywords and estimate their paid traffic cost.
- Check how many subdomains a domain has before you run deeper keyword research on one of them.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/subdomains/live" \
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
        "function": "subdomains",
        "language_code": "en",
        "limit": 10,
        "location_code": 2840,
        "se_type": "google",
        "target": "openai.com"
      },
      "id": "11030829-1614-0384-0000-24d9323275c3",
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
                  "count": 261396,
                  "estimated_paid_traffic_cost": 5601238.468985448,
                  "etv": 18152867.130501848,
                  "is_down": 4415,
                  "is_lost": 0
                },
                "paid": {
                  "clickstream_age_distribution": null,
                  "clickstream_etv": null,
                  "clickstream_gender_distribution": null,
                  "count": 35,
                  "estimated_paid_traffic_cost": 11261.504961013794,
                  "etv": 384.7928841114044,
                  "is_down": 0,
                  "is_lost": 0
                }
              },
              "se_type": "google",
              "subdomain": "openai.com"
            }
          ],
          "items_count": 10,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google",
          "target": "openai.com",
          "total_count": 29
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.3705 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.3877 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Total number of subdomains found for the target. Compare it with `items_count` to see if more rows exist than were returned. |
| `tasks[].result[].items_count` | Number of subdomain rows returned in this response. |
| `tasks[].result[].items[].subdomain` | The subdomain hostname, for example `help.openai.com`. The root domain also appears as its own row. |
| `tasks[].result[].items[].metrics.organic.count` | Number of keywords this subdomain ranks for in Google organic results. |
| `tasks[].result[].items[].metrics.organic.etv` | Estimated organic traffic value (ETV) for the subdomain. Use it to rank subdomains by traffic. |
| `tasks[].result[].items[].metrics.organic.estimated_paid_traffic_cost` | Estimated cost of buying the same organic traffic through paid ads. |
| `tasks[].result[].items[].metrics.organic.is_down / metrics.organic.is_lost` | Counts of organic keywords that moved down in rank and keywords that were lost. |
| `tasks[].result[].items[].metrics.paid.count` | Number of keywords this subdomain has paid results for. It is `0` when the subdomain has no paid keywords. |
| `tasks[].result[].items[].metrics.paid.etv / metrics.paid.estimated_paid_traffic_cost` | Estimated paid traffic and its estimated cost for the subdomain. |

### Notes

- Set `target` to a bare domain such as `openai.com`, without `https://` or a path.
- Use `limit` to control how many subdomains come back. Compare `items_count` with `total_count` to see if you got them all.
- Fields such as `featured_snippet`, `local_pack` and the `clickstream_*` values can be `null` when no data exists for a subdomain.

### Pricing

Billed at the actual cost of each call, about $0.0132 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/subdomains/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/subdomains/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/subdomains/live
