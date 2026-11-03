# DataForSEO Backlinks Bulk New and Lost Backlinks API: pricing, parameters and code examples

`dataforseo/v3/backlinks/bulk_new_lost_backlinks/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024072 per call · **Modes:** sync

New and lost backlink counts since a date for up to 1,000 targets.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024072**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/bulk_new_lost_backlinks/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/bulk_new_lost_backlinks/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/bulk_new_lost_backlinks/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/bulk_new_lost_backlinks/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/bulk_new_lost_backlinks/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `targets` | array |  | Array of domains, subdomains or page URLs (up to 1,000).  |
| `date_from` | string |  | Optional start date, "yyyy-mm-dd".  |

## Details

Returns the number of new and lost backlinks for each target you send. A target can be a domain, a subdomain or a page URL, and one call accepts up to 1,000 targets. Add `date_from` to set the start date of the count.

### Use cases

- Compare link growth between competing domains, such as nike.com and adidas.com, in one call.
- Flag domains in a client portfolio that lost many backlinks in the period.
- Rank a long list of prospect sites by `new_backlinks` to find those gaining links fastest.
- Track link churn for specific pages by passing page URLs as targets.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/bulk_new_lost_backlinks/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"targets": ["nike.com", "adidas.com"]}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date_from` | string | No | Optional start date, "yyyy-mm-dd". |
| `targets` | array | No | Array of domains, subdomains or page URLs (up to 1,000). |

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
        "function": "bulk_new_lost_backlinks",
        "targets": [
          "nike.com"
        ]
      },
      "id": "11030828-2190-0349-0000-7da41015310a",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "lost_backlinks": 536609,
              "new_backlinks": 426575,
              "target": "nike.com"
            }
          ],
          "items_count": 2
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.2283 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.2391 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].target` | The domain, subdomain or page URL that the counts belong to. It matches a value from your `targets` list. |
| `tasks[].result[].items[].new_backlinks` | Number of new backlinks found for the target in the period. |
| `tasks[].result[].items[].lost_backlinks` | Number of backlinks lost by the target in the period. |
| `tasks[].result[].items_count` | Number of target rows returned in this result. |
| `tasks[].data.targets` | The targets the task received, echoed from your request. |
| `tasks[].id` | Unique ID of the task. |
| `tasks[].status_code / tasks[].status_message` | Status of the task. `20000` with `Ok.` means it succeeded. |
| `tasks_count / tasks_error` | Number of tasks in the call and how many of them failed. |

### Notes

- Send the targets in one `targets` array. This is cheaper in calls than one request per domain.
- Use `date_from` in `yyyy-mm-dd` format to set the start date. The request above left it out.
- Each row holds only counts. To see the actual links, call [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live).
- For new and lost referring domains instead of backlinks, use [DataForSEO Backlinks Bulk New and Lost Referring Domains](/apis/dataforseo/v3/backlinks/bulk_new_lost_referring_domains/live).

### Pricing

Billed at the actual cost of each call, about $0.024072 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/bulk_new_lost_backlinks/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/bulk_new_lost_backlinks/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/bulk_new_lost_backlinks/live
