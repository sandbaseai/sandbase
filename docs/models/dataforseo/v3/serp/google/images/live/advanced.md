# DataForSEO Google Images SERP API: pricing, parameters and code examples

`dataforseo/v3/serp/google/images/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Returns Google Images search engine results pages with detailed image metadata. Provides real-time SERP data for visual search queries across Google Images.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/images/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/images/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/images/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/images/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/images/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns Google Images search results for a keyword, with the rank, title, source site and image links for each result. It needs a `keyword`, and you can set `location_code` and `language_code` to choose the market.

### Use cases

- Track which pages and brands appear in Google Images for a product keyword in a given country.
- Compare the `source_url` domains of the top image results to see which sites win visual search.
- Collect image titles and alt text to review how competitors describe their product images.
- Check the related carousel topics Google shows for a query, such as brand names, to find new keyword ideas.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/images/live/advanced" \
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
        "se": "google"
      },
      "id": "11030829-1614-0139-0000-2f06afcc5851",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://www.google.com/search?q=running%20shoes&udm=2&hl=en&gl=US&gws_rd=cr&ie=U…",
          "datetime": "2026-11-03 08:29:38 +00:00",
          "item_types": [
            "images_search"
          ],
          "items": [
            {
              "items": [
                {
                  "image_url": "https://api.dataforseo.com/cdn/i/11030829-1614-0139-0000-2f06afcc5851:0",
                  "subtitle": null,
                  "title": "Nike",
                  "type": "carousel_element"
                }
              ],
              "page": 1,
              "position": "left",
              "rank_absolute": 1,
              "rank_group": 1,
              "rectangle": null,
              "title": null,
              "type": "carousel"
            }
          ],
          "items_count": 105,
          "keyword": "running shoes",
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "8.7524 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "8.8263 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[]` | One block on the results page. The `type` value tells you what it is, such as `images_search` for an image result or `carousel` for a row of related topics. |
| `tasks[].result[].items[].rank_absolute / rank_group` | `rank_absolute` is the position of the block among all blocks on the page. `rank_group` is the position among blocks of the same `type`. |
| `tasks[].result[].items[].title / alt` | The title and alt text of an image result. |
| `tasks[].result[].items[].subtitle` | The site or brand name shown under the image, for example `Runner's World`. |
| `tasks[].result[].items[].source_url` | The address of the image file on the site that hosts it. |
| `tasks[].result[].items[].encoded_url` | A Google-hosted thumbnail address for the image. |
| `tasks[].result[].items[].items[].title / image_url` | The label and image link of each entry inside a `carousel` block. |
| `tasks[].result[].item_types` | The block types found on this results page, such as `images_search`, `related_searches` and `carousel`. |
| `tasks[].result[].items_count` | The number of items found for the query. |
| `tasks[].result[].check_url` | The Google Images search address that matches this request. |

### Notes

- The `type` field changes which keys an item has. `images_search` items have `source_url` and `encoded_url`, while `carousel` items hold their entries in a nested `items` list.
- Results are nested under `tasks[].result[]`. A single call returns one task, and `tasks[].id` is the ID of that task.
- `datetime` on each result is formatted like `2026-11-03 08:29:38 +00:00`.
- Use `location_code` 2840 for the United States and `language_code` `en` for English.

### Pricing

Billed at the actual cost of each call, about $0.002 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/images/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/images/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/images/live/advanced
