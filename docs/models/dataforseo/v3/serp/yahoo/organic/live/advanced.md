# DataForSEO Yahoo Organic SERP API: pricing, parameters and code examples

`dataforseo/v3/serp/yahoo/organic/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Returns real-time organic search engine results pages from Yahoo. Delivers detailed rank positions, titles, URLs, and SERP snippet data for specified search queries.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/yahoo/organic/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/yahoo/organic/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/yahoo/organic/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/yahoo/organic/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/yahoo/organic/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns the live Yahoo search results page for a keyword, location and language. Each result lists the page type, its rank on the page, and the page details such as domain, breadcrumb and description. The request needs a `keyword`, and it also takes `location_code` and `language_code`.

### Use cases

- Check where a domain ranks on Yahoo for a keyword in the United States.
- Collect the snippet text of the top Yahoo results for a keyword to review how competitors describe their pages.
- Detect which SERP blocks appear for a keyword, such as image carousels or People Also Ask.
- Open the `check_url` to see the same Yahoo results page in a browser and compare it with the API output.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/yahoo/organic/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "running shoes", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query. |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "serp",
        "device": "desktop",
        "function": "live",
        "keyword": "running shoes",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "yahoo"
      },
      "id": "11030829-1614-0139-0000-0f2f7a755016",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://us.search.yahoo.com/search?p=running+shoes&vl=lang_en&ei=UTF-8&fl=1&lat=…",
          "datetime": "2026-11-03 08:29:34 +00:00",
          "item_types": [
            "organic"
          ],
          "items": [
            {
              "about_this_result": null,
              "amp_version": false,
              "breadcrumb": "https://www.runnersworld.com › gear › a19663621",
              "cache_url": null,
              "checks": null,
              "description": "Oct 22, 2026 ·  Find the best running shoes of 2026, including Runner’s World–te…",
              "domain": "www.runnersworld.com",
              "extended_people_also_search": null
            }
          ],
          "items_count": 14,
          "keyword": "running shoes",
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "5.3721 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "5.4878 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[]` | One block on the results page. Organic results and other blocks such as images sit in this same list. |
| `tasks[].result[].item_types` | List of block types found on the page, for example `organic`, `images` and `people_also_ask`. |
| `tasks[].result[].items[].rank_group / tasks[].result[].items[].rank_absolute` | Position of the block. `rank_group` counts within blocks of the same type, `rank_absolute` counts across all blocks on the page. |
| `tasks[].result[].items[].domain` | Domain of the organic result, for example `www.runnersworld.com`. |
| `tasks[].result[].items[].breadcrumb` | Displayed URL path of the organic result, with parts separated by `›`. |
| `tasks[].result[].items[].description` | Snippet text shown under the result. It can start with a date. |
| `tasks[].result[].items[].items[].image_url` | Image link inside an `images` block. |
| `tasks[].result[].check_url` | Yahoo search URL that matches this query and location. |
| `tasks[].result[].items_count` | Number of items returned in `items`. |
| `tasks[].result[].datetime` | Date and time of the result, with a UTC offset. |

### Notes

- The response holds one task. Read the results from `tasks[0].result[0]`.
- Use `location_code` `2840` for the United States and `language_code` `en` for English.
- Items are not all organic listings. Check each item's type before you treat it as a ranked page, since blocks like `images` have a `title` and nested `items` instead of `domain` and `description`.
- `tasks[].id` identifies the task, and `status_code` `20000` means the call succeeded.

### Pricing

Billed at the actual cost of each call, about $0.002 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/yahoo/organic/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/yahoo/organic/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/yahoo/organic/live/advanced
