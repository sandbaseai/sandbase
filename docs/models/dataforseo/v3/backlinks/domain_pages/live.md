# DataForSEO Backlinks Domain Pages API: pricing, parameters and code examples

`dataforseo/v3/backlinks/domain_pages/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02418 per call · **Modes:** sync

Returns a list of pages on a target domain along with their backlink metrics and link profile statistics.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02418**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/domain_pages/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/domain_pages/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/domain_pages/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/domain_pages/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/domain_pages/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `target` | string |  | Target domain or page, e.g. "nike.com".  |

## Details

Returns a list of pages found on a target domain. Each item holds crawl details such as the page URL, host, IP address and visit dates. It needs a `target` domain or page, and an optional `limit`.

### Use cases

- List the pages crawled on a competitor domain and count how many exist with `total_count`.
- Check when a page was first seen and last fetched using `first_visited` and `fetch_time`.
- Group crawled pages by host or IP address to see how a site is spread across subdomains and servers.
- Build a page list for a domain, then pass chosen URLs to a page-level backlink API.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/domain_pages/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "limit": 5}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of results (up to 100). |
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
        "function": "domain_pages",
        "limit": 5,
        "target": "nike.com"
      },
      "id": "11030828-2190-0270-0000-723612c25a98",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "content_encoding": null,
              "domain": "www.nike.com",
              "encoded_size": 0,
              "fetch_time": "2026-10-23 12:18:38 +00:00",
              "first_visited": "2019-01-15 23:49:04 +00:00",
              "ip": "2.19.216.98",
              "location": "https://www.nike.com/de/",
              "main_domain": "nike.com"
            }
          ],
          "items_count": 5,
          "target": "nike.com",
          "total_count": 5186327
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "2.0646 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "2.0715 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].location` | URL of the page. It can be `null` for some items. |
| `tasks[].result[].items[].domain` | Host name of the page, for example `www.nike.com`. |
| `tasks[].result[].items[].main_domain` | Root domain the page belongs to, for example `nike.com`. |
| `tasks[].result[].items[].first_visited / tasks[].result[].items[].fetch_time` | Timestamps for when the page was first visited and when it was last fetched. Both use the format `YYYY-MM-DD HH:MM:SS +00:00`. |
| `tasks[].result[].items[].ip` | IP address recorded for the page. |
| `tasks[].result[].items[].content_encoding` | Content encoding seen for the page, such as `gzip`. It is `null` when none is recorded. |
| `tasks[].result[].items[].encoded_size` | Encoded size value recorded for the page. It is `0` in the sample items. |
| `tasks[].result[].total_count` | Total number of pages available for the target. It is 5186327 for `nike.com`. |
| `tasks[].result[].items_count` | Number of items returned in this response. |
| `tasks[].result[].target` | The target that was queried. |

### Notes

- Pass a bare domain such as `nike.com` as `target`. The `limit` parameter caps the number of items returned, up to 100.
- Compare `items_count` with `total_count` to see how much of the full page list the response covers.
- For a summary of backlink counts per page, call [DataForSEO Backlinks Domain Pages Summary](/apis/dataforseo/v3/backlinks/domain_pages_summary/live).
- For the links pointing to a target, call [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live).

### Pricing

Billed at the actual cost of each call, about $0.02418 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/domain_pages/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/domain_pages/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/domain_pages/live
