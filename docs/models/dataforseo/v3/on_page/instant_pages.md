# DataForSEO OnPage Instant Pages API: pricing, parameters and code examples

`dataforseo/v3/on_page/instant_pages` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00015 per call · **Modes:** sync

Returns instant page-level on-page SEO audit metrics for analyzed web pages. Inspect technical SEO elements and on-page optimization signals for audit workflows.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00015**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/on_page/instant_pages"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/on_page/instant_pages', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/on_page/instant_pages", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/on_page/instant_pages", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/on_page/instant_pages` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | Page URL.  |

## Details

Returns an on-page SEO audit for a single web page, using the page `url` as the only required input. The response lists crawl status, cache settings, and a `checks` object with true/false results for technical SEO items.

### Use cases

- Check whether a page declares a canonical URL and an HTML doctype.
- Flag pages that use deprecated HTML tags, frames, or Flash.
- Detect duplicate title tags or duplicate meta tags on a landing page.
- Run a quick one-page audit before a full site crawl.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/on_page/instant_pages" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.python.org/"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | No | Page URL. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "on_page",
        "function": "instant_pages",
        "url": "https://www.python.org/"
      },
      "id": "11030829-1614-0275-0000-e3413d28ed62",
      "path": [
        "v3"
      ],
      "result": [
        {
          "crawl_gateway_address": "168.119.141.170",
          "crawl_progress": "finished",
          "crawl_status": null,
          "items": [
            {
              "broken_links": false,
              "broken_resources": false,
              "cache_control": {
                "cachable": false,
                "ttl": 0
              },
              "checks": {
                "canonical": true,
                "deprecated_html_tags": false,
                "duplicate_meta_tags": false,
                "duplicate_title_tag": false,
                "flash": false,
                "frame": false,
                "from_sitemap": false,
                "has_html_doctype": true
              },
              "click_depth": 0,
              "content_encoding": "gzip",
              "custom_js_client_exception": null,
              "custom_js_response": null
            }
          ],
          "items_count": 1
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.1056 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.1693 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].crawl_progress` | Crawl state for the page. The sample shows `finished`. |
| `tasks[].result[].items_count` | Number of page items returned in `items`. |
| `tasks[].result[].items[].checks.canonical` | Boolean check for the canonical tag. `true` in the sample for python.org. |
| `tasks[].result[].items[].checks.has_html_doctype` | Boolean check for an HTML doctype declaration. |
| `tasks[].result[].items[].checks.duplicate_title_tag / tasks[].result[].items[].checks.duplicate_meta_tags` | Boolean checks for duplicated title or meta tags on the page. `false` means the check found none. |
| `tasks[].result[].items[].checks.deprecated_html_tags / tasks[].result[].items[].checks.flash / tasks[].result[].items[].checks.frame` | Boolean checks for deprecated tags, Flash content, and frames. |
| `tasks[].result[].items[].broken_links / tasks[].result[].items[].broken_resources` | Boolean flags for broken links and broken resources found on the page. |
| `tasks[].result[].items[].click_depth` | Number of clicks from the start page. `0` in the sample for the home page. |
| `tasks[].result[].items[].cache_control.cachable / tasks[].result[].items[].cache_control.ttl` | Whether the page response is cachable, and the cache time to live value. |
| `tasks[].result[].items[].content_encoding` | Content encoding of the page response, such as `gzip`. |

### Notes

- Pass the full page address in `url`, including the `https://` prefix.
- The audit data sits in `tasks[].result[].items[]`. Each call returns one task.
- The `checks` object in the trimmed sample shows only some of the checks. Read the full response for the rest.
- `tasks[].id` is the task ID string for the call.

### Pricing

Billed at the actual cost of each call, about $0.00015 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/on_page/instant_pages.json`](../../../../../catalog/models/dataforseo/v3/on_page/instant_pages.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/on_page/instant_pages
