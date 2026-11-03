# DataForSEO Whois Overview with Site Metrics API: pricing, parameters and code examples

`dataforseo/v3/domain_analytics/whois/overview/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.1212 per call · **Modes:** sync

Whois records for domains matching filters, enriched with backlink and organic traffic metrics.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.1212**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/domain_analytics/whois/overview/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/domain_analytics/whois/overview/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/domain_analytics/whois/overview/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/domain_analytics/whois/overview/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/domain_analytics/whois/overview/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of domains to return.  |
| `filters` | array |  | Filter array, e.g. [["domain", "=", "nike.com"]].  |

## Details

Returns Whois records for domains that match a filter, plus backlink totals and organic and paid search metrics for each domain. The request needs a `filters` array such as `[["domain", "=", "nike.com"]]` and an optional `limit`.

### Use cases

- Check when a competitor's domain was registered and when it expires.
- Screen a list of domains by Whois dates and by backlink or organic traffic size.
- Compare the search footprint of a domain with its registration age before a purchase or partnership.
- Spot domains with transfer or delete locks by reading the EPP status codes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/domain_analytics/whois/overview/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"filters": [["domain", "=", "nike.com"]], "limit": 1}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `filters` | array | No | Filter array, e.g. [["domain", "=", "nike.com"]]. |
| `limit` | integer | No | Maximum number of domains to return. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "domain_analytics",
        "filters": [
          [
            "domain"
          ]
        ],
        "function": "overview",
        "limit": 1,
        "se": "whois"
      },
      "id": "11030829-1614-0481-0000-88656c257a38",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "backlinks_info": {
                "backlinks": 17551828,
                "dofollow": 11095498,
                "referring_domains": 172279,
                "referring_main_domains": 159301,
                "referring_pages": 15013843,
                "time_update": "2026-10-15 15:39:19 +00:00"
              },
              "changed_datetime": "2026-02-01 09:27:27 +00:00",
              "created_datetime": "1995-03-04 05:00:00 +00:00",
              "domain": "nike.com",
              "epp_status_codes": [
                "client_delete_prohibited"
              ],
              "expiration_datetime": "2028-03-05 05:00:00 +00:00",
              "first_seen": "2020-10-07 00:00:00 +00:00",
              "metrics": {
                "organic": {
                  "count": 1746902,
                  "estimated_paid_traffic_cost": 82053343.65460545,
                  "etv": 152122024.95863244,
                  "pos_1": 459240,
                  "pos_11_20": 283431,
                  "pos_21_30": 190044,
                  "pos_2_3": 194687,
                  "pos_31_40": 118887
                },
                "paid": {
                  "count": 134,
                  "estimated_paid_traffic_cost": 4578.252756208181,
                  "etv": 10641.983788073063,
                  "pos_1": 127,
                  "pos_11_20": 0,
                  "pos_21_30": 0,
                  "pos_2_3": 7,
                  "pos_31_40": 0
                }
              }
            }
          ],
          "items_count": 1,
          "offset": 0,
          "offset_token": "eyJDdXJy…",
          "total_count": 1
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "2.6555 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "2.6705 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].domain` | Domain name that the record describes. |
| `tasks[].result[].items[].created_datetime / changed_datetime / expiration_datetime` | Dates from the Whois record when the domain was registered, last changed, and will expire. |
| `tasks[].result[].items[].first_seen` | Date when the domain first appeared in the dataset. |
| `tasks[].result[].items[].epp_status_codes[]` | EPP status codes on the domain, such as `client_delete_prohibited` and `client_transfer_prohibited`. |
| `tasks[].result[].items[].backlinks_info.backlinks / dofollow` | Total backlinks pointing to the domain and how many of them are dofollow. |
| `tasks[].result[].items[].backlinks_info.referring_domains / referring_main_domains / referring_pages` | Counts of referring domains, referring main domains, and referring pages. |
| `tasks[].result[].items[].backlinks_info.time_update` | Timestamp of the backlink data for this record. |
| `tasks[].result[].items[].metrics.organic.count` | Number of keywords for which the domain ranks in organic results. |
| `tasks[].result[].items[].metrics.organic.etv / estimated_paid_traffic_cost` | `etv` is the estimated traffic volume. `estimated_paid_traffic_cost` is the estimated cost of buying that traffic through ads. |
| `tasks[].result[].items[].metrics.organic.pos_1 / pos_2_3 / pos_11_20` | Number of organic keywords ranking in each position bucket. The same position buckets exist under `metrics.paid`. |

### Notes

- Set `filters` to `[["domain", "=", "example.com"]]` to look up one domain. Use `limit` to cap the number of domains returned.
- Read results from `tasks[].result[].items[]`. `total_count` gives the number of matching domains and `items_count` gives the number returned.
- For more rows, pass the `offset_token` from the response. The response also shows an `offset` value.
- Dates use the format `YYYY-MM-DD HH:MM:SS +00:00`.

### Pricing

Billed at the actual cost of each call, about $0.1212 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/domain_analytics/whois/overview/live.json`](../../../../../../../catalog/models/dataforseo/v3/domain_analytics/whois/overview/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/domain_analytics/whois/overview/live
