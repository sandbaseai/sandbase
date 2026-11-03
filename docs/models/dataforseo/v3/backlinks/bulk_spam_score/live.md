# DataForSEO Backlinks Bulk Spam Score API: pricing, parameters and code examples

`dataforseo/v3/backlinks/bulk_spam_score/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024072 per call · **Modes:** sync

Backlink spam scores for up to 1,000 domains, subdomains or pages.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024072**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/bulk_spam_score/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/bulk_spam_score/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/bulk_spam_score/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/bulk_spam_score/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/bulk_spam_score/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `targets` | array |  | Array of domains, subdomains or page URLs (up to 1,000).  |

## Details

This API returns a backlink spam score for each domain, subdomain or page URL you send. It needs a `targets` array with up to 1,000 entries.

### Use cases

- Screen a list of link prospects and drop domains with a high spam score before outreach.
- Compare the spam score of your own site against competitor domains.
- Check a batch of specific page URLs before you accept a guest post or link swap.
- Add a spam score column to a large domain list in one call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/bulk_spam_score/live" \
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
        "function": "bulk_spam_score",
        "targets": [
          "nike.com"
        ]
      },
      "id": "11030828-2190-0482-0000-9450f4d2848b",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "spam_score": 8,
              "target": "nike.com",
              "type": "backlinks_bulk_spam_score"
            }
          ],
          "items_count": 2
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0469 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0546 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].target` | The domain, subdomain or page URL that was scored. It matches an entry from your `targets` array. |
| `tasks[].result[].items[].spam_score` | The spam score for the target as a number. In the example, `nike.com` returns `8` and `adidas.com` returns `22`. |
| `tasks[].result[].items[].type` | The item type. It is `backlinks_bulk_spam_score` for every row. |
| `tasks[].result[].items_count` | The number of scored items in the result. |
| `tasks[].data.targets` | The targets the task received, echoed back from your request. |
| `tasks[].id` | The unique task ID, in UUID-like format. |
| `tasks[].status_code / tasks[].status_message` | The task status. `20000` with `Ok.` means the task succeeded. |
| `tasks_count / tasks_error` | The number of tasks in the response and how many of them failed. |

### Notes

- Send domains such as `nike.com`, subdomains, or full page URLs in `targets`. You can mix them in one call.
- Read results from `tasks[].result[].items[]`. Each target gets one item.
- To see the full backlink profile of a target, call [DataForSEO Backlinks Summary](/apis/dataforseo/v3/backlinks/summary/live). For rank values on many targets, use [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live).

### Pricing

Billed at the actual cost of each call, about $0.024072 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/bulk_spam_score/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/bulk_spam_score/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/bulk_spam_score/live
