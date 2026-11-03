# DataForSEO Backlinks History API: pricing, parameters and code examples

`dataforseo/v3/backlinks/history/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024324 per call · **Modes:** sync

Monthly history of backlinks, referring domains and rank for a domain since 2019.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024324**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/history/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/history/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/history/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/history/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/history/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | string |  | Domain, e.g. "nike.com".  |
| `date_to` | string |  | Optional end date, "yyyy-mm-dd".  |
| `date_from` | string |  | Optional start date, "yyyy-mm-dd".  |

## Details

Returns a monthly history of backlink and link counts for a domain. You send a `target` domain and an optional `date_from` and `date_to`, and get one row per month.

### Use cases

- Chart how the backlink count of a competitor domain changes month by month.
- Spot a sudden drop in backlinks or crawled pages after a site migration.
- Track the growth of broken backlinks to decide when to run a link reclamation campaign.
- Compare the internal and external link counts of a domain over a set date range.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/history/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "date_from": "2026-01-01"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date_from` | string | No | Optional start date, "yyyy-mm-dd". |
| `date_to` | string | No | Optional end date, "yyyy-mm-dd". |
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
        "date_from": "2026-01-01",
        "function": "history",
        "target": "nike.com"
      },
      "id": "11030828-2190-0266-0000-b4472b165650",
      "path": [
        "v3"
      ],
      "result": [
        {
          "date_from": "2026-01-01",
          "date_to": null,
          "items": [
            {
              "backlinks": 30543076,
              "broken_backlinks": 1739678,
              "broken_pages": 1312614,
              "crawled_pages": 4448802,
              "date": "2026-01-31 00:00:00 +00:00",
              "external_links_count": 33620799,
              "info": {
                "cms": "asciidoc",
                "country": null,
                "ip_address": "69.192.162.70",
                "is_ip": false,
                "platform_type": null,
                "server": "unified-edge-router",
                "target_spam_score": 0
              },
              "internal_links_count": 281032106
            }
          ],
          "items_count": 9,
          "target": "nike.com"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.1114 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.1620 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].target` | The domain the history belongs to. |
| `tasks[].result[].items_count` | Number of monthly rows in `items`. |
| `tasks[].result[].items[].date` | Date of the monthly snapshot, for example `2026-01-31 00:00:00 +00:00`. |
| `tasks[].result[].items[].backlinks` | Total number of backlinks pointing to the target in that month. |
| `tasks[].result[].items[].broken_backlinks / tasks[].result[].items[].broken_pages` | Count of broken backlinks and count of broken pages for the target in that month. |
| `tasks[].result[].items[].crawled_pages` | Number of pages of the target that were crawled in that month. |
| `tasks[].result[].items[].external_links_count / tasks[].result[].items[].internal_links_count` | Number of external links and internal links found on the target in that month. |
| `tasks[].result[].items[].info.target_spam_score` | Spam score of the target for that month. |
| `tasks[].result[].items[].info.cms / tasks[].result[].items[].info.server / tasks[].result[].items[].info.ip_address` | The CMS, server name and IP address detected for the target in that month. These values can change between months. |

### Notes

- Pass a bare domain such as `nike.com` as `target`.
- Use `date_from` and `date_to` in `yyyy-mm-dd` format to limit the range. `date_to` is `null` in the result when you do not send it.
- Each row in `items` is dated with the last day of a month.
- For current totals, call [DataForSEO Backlinks Summary](/apis/dataforseo/v3/backlinks/summary/live). For individual links, call [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live).

### Pricing

Billed at the actual cost of each call, about $0.024324 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/history/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/history/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/history/live
