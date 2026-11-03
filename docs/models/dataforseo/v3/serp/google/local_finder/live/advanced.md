# DataForSEO Google Local Finder Advanced API: pricing, parameters and code examples

`dataforseo/v3/serp/google/local_finder/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Returns real-time Google Local Finder search engine results page data. Retrieves local business listings, map results, and advanced SERP elements based on search queries.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/local_finder/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/local_finder/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/local_finder/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/local_finder/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/local_finder/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_coordinate` | string |  | Coordinates as "latitude,longitude,zoom", e.g. "40.7128,-74.0060,14z".  |

## Details

Returns Google Local Finder results for a search query at a map location. Each call needs a `keyword`, a `location_coordinate` in `latitude,longitude,zoom` form, and a `language_code`.

### Use cases

- Check which businesses appear for a query such as `coffee shop` around a given street corner.
- Collect `cid` values for local businesses to look up their full profiles.
- Compare the listings returned for the same keyword at different coordinates to see how local results shift.
- Read the address and review snippet in each listing's `description` to build a list of nearby competitors.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/local_finder/live/advanced" \
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
      "id": "11030829-1614-0139-0000-8b50a676e6cc",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://www.google.com/search?q=coffee+shop&uule=j+WzEsMTIsMTc5MzY5NDU1NzA3ODAwM…",
          "datetime": "2026-11-03 08:29:29 +00:00",
          "item_types": [
            "local_pack"
          ],
          "items": [
            {
              "booking_url": null,
              "cid": "9407787749561276587",
              "description": "93 Worth St \nClosed · Opens 7 AM \n\"The whiskey and rum infused coffee options ma…",
              "domain": null,
              "is_paid": false,
              "page": 1,
              "phone": null,
              "position": "left"
            }
          ],
          "items_count": 20,
          "keyword": "coffee shop",
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "3.2541 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "3.3437 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[]` | The local business listings found for the query. The sample call has `items_count` of 20, and only a few listings are shown in the trimmed response. |
| `tasks[].result[].items[].cid` | Google's customer ID for the business listing, as a numeric string. |
| `tasks[].result[].items[].description` | Text block for the listing. It holds the street address, the open or closed status with opening time, and a review snippet. |
| `tasks[].result[].items[].position` | Where the listing sits on the page. The sample shows `left`. |
| `tasks[].result[].items[].page` | The result page the listing came from. |
| `tasks[].result[].items[].is_paid` | Shows whether the listing is a paid placement. |
| `tasks[].result[].items[].phone / domain / booking_url` | Phone number, website domain and booking link of the listing. These are `null` when Google shows none, as in the sample. |
| `tasks[].result[].items_count` | Number of items in the result. |
| `tasks[].result[].check_url` | The Google search URL that matches this query and location. |
| `tasks[].result[].location_code` | Numeric code of the location used for the search. The sample shows `2840`. |

### Notes

- Take `location_coordinate` from the latitude and longitude of the area you want, then add a zoom level such as `14z`.
- The sample response lists `datetime` in the form `2026-11-03 08:29:29 +00:00`.
- `item_types` shows the kinds of elements in the result. The sample contains only `local_pack`.
- Use `cid` to identify a business, then call [DataForSEO Google Business Listing Info](/apis/dataforseo/v3/business_data/google/my_business_info/live/advanced) for more detail on it.

### Pricing

Billed at the actual cost of each call, about $0.002 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/local_finder/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/local_finder/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/local_finder/live/advanced
