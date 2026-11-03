# DataForSEO Backlinks Bulk Backlink Counts API: pricing, parameters and code examples

`dataforseo/v3/backlinks/bulk_backlinks/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024072 per call · **Modes:** sync

Backlink counts for up to 1,000 domains, subdomains or pages in one request.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024072**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/bulk_backlinks/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/bulk_backlinks/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/bulk_backlinks/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/bulk_backlinks/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/bulk_backlinks/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `targets` | array |  | Array of domains, subdomains or page URLs (up to 1,000).  |

## Details

Returns the total backlink count for each target you send. The input is a `targets` array of up to 1,000 domains, subdomains or page URLs.

### Use cases

- Compare the backlink totals of several competitor domains in one call.
- Rank a list of prospect sites by backlink count before outreach.
- Track a set of your own pages by logging their backlink counts over time.
- Screen a large list of domains and drop those with very few backlinks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/bulk_backlinks/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"targets": ["nike.com", "adidas.com"]}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
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
        "function": "bulk_backlinks",
        "targets": [
          "nike.com"
        ]
      },
      "id": "11030828-2190-0348-0000-a692ff37ed48",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "backlinks": 17399186,
              "target": "nike.com"
            }
          ],
          "items_count": 2
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0063 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0140 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].target` | The domain, subdomain or page URL that the count belongs to. It matches a value you sent in `targets`. |
| `tasks[].result[].items[].backlinks` | The number of backlinks found for that target. |
| `tasks[].result[].items_count` | The number of rows in `items` for this result. |
| `tasks[].result_count` | The number of result objects in the task. |
| `tasks[].data.targets` | The list of targets the task received, echoed back from your request. |
| `tasks[].id` | The task ID, a string made of hex groups separated by dashes. |
| `tasks[].status_code / tasks[].status_message` | The status of the task. `20000` with `Ok.` means it succeeded. |
| `tasks_count / tasks_error` | The number of tasks in the response and the number of those that returned an error. |

### Notes

- Send all targets in one `targets` array instead of making one call per target.
- Read the counts from `tasks[].result[].items[]`. Match each row to your input by `target`.
- For referring domain counts instead of backlink counts, call [DataForSEO Backlinks Bulk Referring Domain Counts](/apis/dataforseo/v3/backlinks/bulk_referring_domains/live).
- For rank values or spam scores on the same targets, use [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live) or [DataForSEO Backlinks Bulk Spam Score](/apis/dataforseo/v3/backlinks/bulk_spam_score/live).

### Pricing

Billed at the actual cost of each call, about $0.024072 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/bulk_backlinks/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/bulk_backlinks/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/bulk_backlinks/live
