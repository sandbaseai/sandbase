# DataForSEO Backlinks Domain Intersection API: pricing, parameters and code examples

`dataforseo/v3/backlinks/domain_intersection/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02436 per call · **Modes:** sync

Referring domains that link to all (or some) of up to 20 target domains, for link-gap analysis.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02436**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/domain_intersection/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/domain_intersection/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/domain_intersection/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/domain_intersection/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/domain_intersection/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of referring domains to return.  |
| `targets` | object |  | Object of up to 20 targets keyed "1", "2", ... (domains or subdomains).  |
| `exclude_targets` | string |  | Optional array of domains whose referrers are excluded.  |

## Details

This API returns referring domains that link to several target domains at once. It needs a `targets` object with up to 20 domains or subdomains, and it reports link stats per target for each referring domain.

### Use cases

- Find sites that link to both `nike.com` and `adidas.com` but not to your own site.
- Build an outreach list from domains that link to many of your competitors.
- Rank link-gap candidates by the `rank` and `backlinks_spam_score` of each referring domain.
- Check how long a referring domain has linked to each competitor using `first_seen`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/domain_intersection/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"targets": {"1": "nike.com", "2": "adidas.com"}, "limit": 10}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `exclude_targets` | string | No | Optional array of domains whose referrers are excluded. |
| `limit` | integer | No | Maximum number of referring domains to return. |
| `targets` | object | No | Object of up to 20 targets keyed "1", "2", ... (domains or subdomains). |

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
        "function": "domain_intersection",
        "limit": 10,
        "targets": {
          "1": "nike.com",
          "2": "adidas.com"
        }
      },
      "id": "11030828-2190-0268-0000-9d9add018aa7",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "domain_intersection": {
                "1": {
                  "backlinks": 22221,
                  "backlinks_spam_score": 0,
                  "broken_backlinks": 719,
                  "broken_pages": 715,
                  "first_seen": "2019-01-22 20:39:27 +00:00",
                  "lost_date": null,
                  "rank": 312,
                  "referring_domains": 1
                },
                "2": {
                  "backlinks": 4,
                  "backlinks_spam_score": 0,
                  "broken_backlinks": 2,
                  "broken_pages": 2,
                  "first_seen": "2021-12-04 09:36:33 +00:00",
                  "lost_date": null,
                  "rank": 0,
                  "referring_domains": 1
                }
              },
              "summary": {
                "intersections_count": 2
              }
            }
          ],
          "items_count": 10,
          "targets": {
            "1": "nike.com",
            "2": "adidas.com"
          },
          "total_count": 3807
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "1.7381 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "1.7502 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Total number of referring domains that match the intersection. Use it to see how many rows exist beyond your `limit`. |
| `tasks[].result[].items_count` | Number of referring domains returned in this response. |
| `tasks[].result[].items[].domain_intersection` | Object keyed by the same `"1"`, `"2"` keys you used in `targets`. Each entry holds the link stats between one referring domain and that target. |
| `tasks[].result[].items[].domain_intersection.1.backlinks / tasks[].result[].items[].domain_intersection.2.backlinks` | Number of backlinks from this referring domain to the target with that key. |
| `tasks[].result[].items[].domain_intersection.1.broken_backlinks / tasks[].result[].items[].domain_intersection.1.broken_pages` | Count of broken backlinks and broken pages for this referring domain and target. Broken links can point to reclaim opportunities. |
| `tasks[].result[].items[].domain_intersection.1.rank` | Rank value of the referring domain for that target. Higher values appear on stronger domains in this sample. |
| `tasks[].result[].items[].domain_intersection.1.backlinks_spam_score` | Spam score for the backlinks from this domain to that target. `0` is the lowest value in the sample. |
| `tasks[].result[].items[].domain_intersection.1.first_seen / tasks[].result[].items[].domain_intersection.1.lost_date` | When the link was first seen, as a UTC timestamp like `2019-01-22 20:39:27 +00:00`. `lost_date` is `null` when the link has not been marked lost. |
| `tasks[].result[].items[].summary.intersections_count` | Number of targets this referring domain links to. |

### Notes

- Key each target as `"1"`, `"2"`, and so on. The same keys label the per-target stats in `domain_intersection`.
- Use `limit` to set how many referring domains come back. Compare it with `total_count` to see how many matches exist.
- Use `exclude_targets` to drop referring domains that already link to your own site.
- To see the individual links from one referring domain, call [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live).

### Pricing

Billed at the actual cost of each call, about $0.02436 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/domain_intersection/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/domain_intersection/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/domain_intersection/live
