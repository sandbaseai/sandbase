# AutoZone Category Listings API: pricing, parameters and code examples

`autozone/scrape/category` · data API · AutoZone · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** async

Extract product listings from an AutoZone category page URL with pagination and preferred-store pricing.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "autozone/scrape/category", "url": "https://www.autozone.com/batteries-starting-and-charging/battery"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('autozone/scrape/category', {'url': 'https://www.autozone.com/batteries-starting-and-charging/battery'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("autozone/scrape/category", {
  "url": "https://www.autozone.com/batteries-starting-and-charging/battery"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "autozone/scrape/category", sandbase.Params{
	"url": "https://www.autozone.com/batteries-starting-and-charging/battery",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/autozone/scrape/category` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full AutoZone page URL, e.g. https://www.autozone.com/batteries-starting-and-charging/battery  |
| `page` | integer |  | Results page number (1-indexed; default 1). range 1–9007199254740991 |
| `preferedstore` | string |  | Preferred AutoZone store ID for local availability and pricing (the parameter name is spelled this way).  |

## Details

Returns the product listings for an AutoZone category page, plus the category path, filter options, and paging counts. It needs the full category page `url`. You can add `page` and `preferedstore` to change the results.

### Use cases

- Build a catalog of battery SKUs with part numbers, brands, and specs such as `CCA`.
- Compare how many products each brand has in a category using the brand facet counts.
- Collect product page URLs and image URLs for a list of parts.
- Walk through every page of a category to count and export all of its products.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/autozone/scrape/category" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.autozone.com/batteries-starting-and-charging/battery"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full AutoZone page URL, e.g. https://www.autozone.com/batteries-starting-and-charging/battery |
| `page` | integer | No | Results page number (1-indexed; default 1). |
| `preferedstore` | string | No | Preferred AutoZone store ID for local availability and pricing (the parameter name is spelled this way). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attributionToken": "",
  "filter": "NOT attributes.stores_ss: ANY(\"*\", \"5414\") AND availability: ANY(\"IN_STOCK\") AND…",
  "interchangeSearchFlag": false,
  "productShelfResults": {
    "breadCrumbs": [
      {
        "canonicalUrl": "/batteries-starting-and-charging",
        "categoryIdPath": "/a34cb75b-abb6-47f8-a63c-df61277f",
        "categoryName": "Batteries & Chargers",
        "pageType": "TopLevel",
        "taxonomyPath": "/batteries-chargers"
      }
    ],
    "categoryIdPath": "/a34cb75b-abb6-47f8-a63c-df61277f/c398b9c5-a12d-45ba-86bf-27235a82/433b0182-6f87…",
    "componentLocations": null,
    "facets": [
      {
        "facetDisplayName": "Pick Up Today",
        "facetInternalName": "available_stores_ss",
        "facetValues": [
          {
            "botEnabledFacetPath": "/b/near-me",
            "botSeoUrl": "/batteries-starting-and-charging/battery/b/near-me",
            "facetValueDisplayName": "Pick Up In Store",
            "facetValueInternalName": "5414",
            "itemCount": 156,
            "selectedFlag": false,
            "seoUrl": "/batteries-starting-and-charging/battery/b/near-me"
          }
        ],
        "isOneClickFilter": false,
        "multiSelectFlag": false
      }
    ],
    "firstRecordNumber": 1,
    "installationInstructions": null,
    "lastRecordNumber": 24,
    "makeId": 0,
    "makeModelYearPath": null,
    "makeName": null,
    "modelId": 0,
    "modelName": null
  },
  "redirectUrl": null,
  "xfusionQueryId": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `productShelfResults.skuRecords[].itemDescription` | Full product name, including brand, type, and group size. |
| `productShelfResults.skuRecords[].partNumber / alternatePartNumber` | The main part number and an alternate part number. The alternate value can have trailing spaces. |
| `productShelfResults.skuRecords[].itemId` | AutoZone item ID for the product. It also appears at the end of the product page path. |
| `productShelfResults.skuRecords[].brandName` | Brand name of the product, such as `Duralast`. |
| `productShelfResults.skuRecords[].productAttributes` | Key and value pairs of product specs, such as `Battery Technology`, `Battery Type` and `CCA`. |
| `productShelfResults.skuRecords[].productDetailsPageUrl / productImageUrl` | Relative path to the product detail page and the full URL of the product image. |
| `productShelfResults.totalNumberOfRecords` | Total number of products in the category. |
| `productShelfResults.firstRecordNumber / lastRecordNumber / recordsPerPage` | Position of the first and last record on this page, and the page size. |
| `productShelfResults.facets[].facetValues[]` | Filter options for the category. Each has a display name, an internal name, an `itemCount`, and a `seoUrl` path. |
| `productShelfResults.breadCrumbs[].categoryName` | Category names from the top level down to the leaf category, with `canonicalUrl` for each. |

### Notes

- Send the full AutoZone category page URL in `url`, for example `https://www.autozone.com/batteries-starting-and-charging/battery`.
- Use `page` (1-indexed) to move through results. Compare `lastRecordNumber` with `totalNumberOfRecords` to see if more pages remain.
- Pass a store ID in `preferedstore` for local results. The facet value `5414` under `Pick Up Today` is an example of a store ID in the response.
- Paths such as `productDetailsPageUrl` are relative. Add `https://www.autozone.com` in front to get a full link.

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/autozone/scrape/category.json`](../../../../catalog/models/autozone/scrape/category.json) · Store page: https://www.sandbase.ai/model/autozone/scrape/category
