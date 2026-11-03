# DataForSEO Backlinks Summary API: pricing, parameters and code examples

`dataforseo/v3/backlinks/summary/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024036 per call · **Modes:** sync

Returns high-level backlink profile metrics and overview data for a target domain or URL. Helps evaluate link authority and overall link counts for SEO analysis.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024036**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/summary/live", "backlinks_status_type": "all", "internal_list_limit": 5, "target": "dataforseo.com"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/summary/live', {'backlinks_status_type': 'all', 'internal_list_limit': 5, 'target': 'dataforseo.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/summary/live", {
  "backlinks_status_type": "all",
  "internal_list_limit": 5,
  "target": "dataforseo.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/summary/live", sandbase.Params{
	"backlinks_status_type": "all",
	"internal_list_limit": 5,
	"target": "dataforseo.com",
})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/summary/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | string |  | Target domain or page, e.g. "nike.com".  |

## Details

Returns a backlink profile summary for one domain or page. It gives counts of backlinks, broken links and crawled pages, plus spam scores and basic server details. The only input is `target`, such as `nike.com`.

### Use cases

- Compare the total backlink count of your site with a competitor's domain.
- Check `backlinks_spam_score` and `info.target_spam_score` to flag a domain with a risky link profile.
- Find how many backlinks and pages are broken to plan link reclamation work.
- Look up the country, server and CMS of a target before an SEO audit.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/summary/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `target` | string | No | Target domain or page, e.g. "nike.com". |

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
        "function": "summary",
        "target": "nike.com"
      },
      "id": "11030828-2190-0265-0000-19272d50772c",
      "path": [
        "v3"
      ],
      "result": [
        {
          "backlinks": 17595303,
          "backlinks_spam_score": 10,
          "broken_backlinks": 1739366,
          "broken_pages": 1353132,
          "crawled_pages": 5181466,
          "external_links_count": 41218143,
          "first_seen": "2019-01-15 22:56:16 +00:00",
          "info": {
            "cms": "asciidoc",
            "country": "US",
            "ip_address": "23.52.180.92",
            "is_ip": false,
            "platform_type": null,
            "server": "unified-edge-router",
            "target_spam_score": 1
          }
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0072 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0133 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].backlinks` | Total number of backlinks found pointing to the target. |
| `tasks[].result[].backlinks_spam_score` | Spam score for the target's backlinks. Higher values suggest more spammy links. |
| `tasks[].result[].broken_backlinks / broken_pages` | Count of backlinks that point to broken pages, and count of broken pages on the target. |
| `tasks[].result[].crawled_pages` | Number of pages on the target that were crawled. |
| `tasks[].result[].external_links_count` | Number of external links found on the target's pages. |
| `tasks[].result[].first_seen` | Date and time the target was first seen, in `YYYY-MM-DD HH:MM:SS +00:00` format. |
| `tasks[].result[].info.target_spam_score` | Spam score for the target itself. |
| `tasks[].result[].info.cms / info.server / info.platform_type` | Detected CMS, web server and platform type of the target. Values can be `null`. |
| `tasks[].result[].info.country / info.ip_address / info.is_ip` | Country code and IP address of the target. `is_ip` shows whether the target is an IP address. |
| `tasks[].result_count` | Number of items in `result`. A single-target call returns 1. |

### Notes

- Send the domain or page in `target`, for example `nike.com`. Leave out the protocol and use the bare domain for a domain-level summary.
- The response holds one task in `tasks[]`. Its `id` is a task ID string, and `status_code` of `20000` means the call succeeded.
- For the individual links behind these totals, call [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live). For growth over time, use [DataForSEO Backlinks Totals Over Time](/apis/dataforseo/v3/backlinks/timeseries_summary/live).

### Pricing

Billed at the actual cost of each call, about $0.024036 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/summary/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/summary/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/summary/live
