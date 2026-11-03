# DataForSEO Google Maps Local SERP API: pricing, parameters and code examples

`dataforseo/v3/serp/google/maps/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Returns real-time Google Maps search engine results pages and local business listings. Supports local SEO monitoring and geographical business discovery directly from Google Maps.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/maps/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/maps/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/maps/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/maps/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/maps/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_coordinate` | string |  | Coordinates as "latitude,longitude,zoom", e.g. "40.7128,-74.0060,14z".  |

## Details

Returns Google Maps search results for a keyword at a given map position. Each result is a local business listing with its address, category and Google place ID. Send a `keyword`, a `location_coordinate` in `latitude,longitude,zoom` format and a `language_code`.

### Use cases

- Check which coffee shops, dentists or other businesses show up on Google Maps around a specific street corner.
- Build a list of local businesses in a neighborhood with their addresses and categories.
- Compare the listings returned for the same keyword at different coordinates to see how local results shift.
- Collect `cid` values to look up each business in a detail API.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/maps/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "coffee shop", "location_coordinate": "40.7128,-74.0060,14z", "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query. |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_coordinate` | string | No | Coordinates as "latitude,longitude,zoom", e.g. "40.7128,-74.0060,14z". |

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
        "keyword": "coffee shop",
        "language_code": "en",
        "location_coordinate": "40.7128,-74.0060,14z",
        "os": "windows",
        "se": "google"
      },
      "id": "11030829-1614-0139-0000-334d806f6706",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://google.com/maps/search/coffee+shop/@40.7128,-74.006,14z?hl=en&gl=US&uule…",
          "datetime": "2026-11-03 08:29:30 +00:00",
          "item_types": [
            "maps_search"
          ],
          "items": [
            {
              "additional_categories": null,
              "address": "140 Nassau St, New York, NY 10038",
              "address_info": {
                "address": "140 Nassau St",
                "borough": "Manhattan",
                "city": "New York",
                "country_code": "US",
                "region": "New York",
                "zip": "10038"
              },
              "book_online_url": null,
              "category": "Coffee shop",
              "category_ids": null,
              "cid": "15667002398697190332",
              "contact_url": null
            }
          ],
          "items_count": 100,
          "keyword": "coffee shop",
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "4.0392 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "4.2000 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[]` | One Google Maps listing per entry, in the order Google returned them. |
| `tasks[].result[].items_count` | Number of items reported for the result. |
| `tasks[].result[].items[].address` | Full street address of the business as a single string. |
| `tasks[].result[].items[].address_info.city / address_info.region / address_info.zip / address_info.country_code` | The address split into parts: city, region, ZIP code and country code. |
| `tasks[].result[].items[].address_info.borough` | Borough name when the address has one, such as `Manhattan`. |
| `tasks[].result[].items[].category` | Main Google Maps category of the business, such as `Coffee shop`. |
| `tasks[].result[].items[].additional_categories` | List of extra categories for the business, or `null` when none are listed. |
| `tasks[].result[].items[].cid` | Google customer ID of the business listing, as a string of digits. |
| `tasks[].result[].items[].book_online_url / contact_url` | Links for booking online or contacting the business. They are `null` when the listing has none. |
| `tasks[].result[].check_url` | Google Maps URL that matches the search, so you can open the same results in a browser. |

### Notes

- Pass the map center in `location_coordinate` as `latitude,longitude,zoom`, for example `40.7128,-74.0060,14z`.
- The response echoes the search in `tasks[].data` and `tasks[].result[]`, including `keyword`, `language_code` and a numeric `location_code`.
- `tasks[].result[].datetime` is a UTC timestamp such as `2026-11-03 08:29:30 +00:00`.
- Use the `cid` of a listing with [DataForSEO Google Business Listing Info](/apis/dataforseo/v3/business_data/google/my_business_info/live/advanced) to get more detail on one business.

### Pricing

Billed at the actual cost of each call, about $0.002 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/maps/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/maps/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/maps/live/advanced
