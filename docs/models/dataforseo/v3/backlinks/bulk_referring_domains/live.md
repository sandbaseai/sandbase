# DataForSEO Backlinks Bulk Referring Domain Counts API: pricing, parameters and code examples

`dataforseo/v3/backlinks/bulk_referring_domains/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024072 per call · **Modes:** sync

Referring domain counts for up to 1,000 domains, subdomains or pages in one request.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024072**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/bulk_referring_domains/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/bulk_referring_domains/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/bulk_referring_domains/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/bulk_referring_domains/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/bulk_referring_domains/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `targets` | array |  | Array of domains, subdomains or page URLs (up to 1,000).  |

## Details

This API returns referring domain counts for each target you send. Send up to 1,000 domains, subdomains or page URLs in `targets`, and get one row per target.

### Use cases

- Compare the referring domain counts of several competitor sites in one call.
- Rank a list of prospect domains by how many sites link to them.
- Check how many referring domains are nofollow versus all referring domains for a set of pages.
- Add referring domain counts to a spreadsheet of hundreds of URLs without sending one request per URL.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/bulk_referring_domains/live" \
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
        "function": "bulk_referring_domains",
        "targets": [
          "nike.com"
        ]
      },
      "id": "11030828-2190-0351-0000-78537a6dd681",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "referring_domains": 173751,
              "referring_domains_nofollow": 21984,
              "referring_main_domains": 160551,
              "referring_main_domains_nofollow": 17377,
              "target": "nike.com"
            }
          ],
          "items_count": 2
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.6460 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.6542 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].target` | The domain, subdomain or page URL this row describes. It matches a value you sent in `targets`. |
| `tasks[].result[].items[].referring_domains` | Total number of referring domains that link to the target. |
| `tasks[].result[].items[].referring_domains_nofollow` | Number of referring domains that link to the target with nofollow links. |
| `tasks[].result[].items[].referring_main_domains` | Number of referring main domains that link to the target. A main domain is the root domain without subdomains, so this count is lower than `referring_domains`. |
| `tasks[].result[].items[].referring_main_domains_nofollow` | Number of referring main domains that link to the target with nofollow links. |
| `tasks[].result[].items_count` | Number of rows in `items` for this result. |
| `tasks[].data.targets` | The list of targets the task received. |
| `tasks[].id` | The task ID for this call. |

### Notes

- Pass every target in the `targets` array of one request. The limit is 1,000 targets.
- The response uses the original task structure. Read the rows from `tasks[].result[].items[]`.
- Use [Backlinks Bulk Backlink Counts](/apis/dataforseo/v3/backlinks/bulk_backlinks/live) to get backlink counts for the same targets.
- Use [Backlinks Referring Domains](/apis/dataforseo/v3/backlinks/referring_domains/live) to list the actual referring domains for one target.

### Pricing

Billed at the actual cost of each call, about $0.024072 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/bulk_referring_domains/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/bulk_referring_domains/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/bulk_referring_domains/live
