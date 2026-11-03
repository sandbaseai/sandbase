# DataForSEO Backlinks Bulk Ranks API: pricing, parameters and code examples

`dataforseo/v3/backlinks/bulk_ranks/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024072 per call · **Modes:** sync

Returns rank metrics for multiple domains or pages in bulk. Evaluates backlink authority and score indicators across a list of target URLs.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024072**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/bulk_ranks/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/bulk_ranks/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/bulk_ranks/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/bulk_ranks/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/bulk_ranks/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `targets` | array |  | Target domains or pages.  |

## Details

Returns a `rank` value for each domain or page in a list of targets. Send a `targets` array of domains or URLs, and the response lists one item per target.

### Use cases

- Compare the backlink rank of your domain against a list of competitor domains in one call.
- Sort a list of prospective link partners by `rank` to decide which sites to contact first.
- Check the rank of several pages on your own site to see which ones carry the most backlink authority.
- Track a set of domains over time by saving the `rank` values from repeated calls.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/bulk_ranks/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"targets": ["nike.com", "adidas.com"]}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `targets` | array | No | Target domains or pages. |

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
        "function": "bulk_ranks",
        "targets": [
          "nike.com"
        ]
      },
      "id": "11030828-2190-0347-0000-8a5f0260698d",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "rank": 604,
              "target": "nike.com"
            }
          ],
          "items_count": 2
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0471 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0539 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].target` | The domain or page that the rank belongs to. It matches one of the values you sent in `targets`. |
| `tasks[].result[].items[].rank` | The rank value for the target. A higher number means a higher rank in this response, for example `604` for `nike.com` and `596` for `adidas.com`. |
| `tasks[].result[].items_count` | The number of items returned in the result. |
| `tasks[].result_count` | The number of result objects in the task. |
| `tasks[].data.targets` | The list of targets the task ran on, echoed from your request. |
| `tasks[].id` | The unique ID of the task. |
| `tasks[].status_code / tasks[].status_message` | The status of the task. `20000` with `Ok.` means the task succeeded. |
| `tasks_count / tasks_error` | The number of tasks in the response and how many of them returned an error. |

### Notes

- Pass domains such as `nike.com` or full page URLs in the `targets` array. Each target returns one row in `items`.
- Match rows to your input by reading `target` in each item, not by position.
- For counts instead of rank, call [DataForSEO Backlinks Bulk Backlink Counts](/apis/dataforseo/v3/backlinks/bulk_backlinks/live) or [DataForSEO Backlinks Bulk Referring Domain Counts](/apis/dataforseo/v3/backlinks/bulk_referring_domains/live).
- For a full profile of one target, call [DataForSEO Backlinks Summary](/apis/dataforseo/v3/backlinks/summary/live).

### Pricing

Billed at the actual cost of each call, about $0.024072 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Competitors](/apis/dataforseo/v3/backlinks/competitors/live): Returns domains that compete for similar backlink profiles.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/bulk_ranks/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/bulk_ranks/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/bulk_ranks/live
