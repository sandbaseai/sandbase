# GetApp Category Leaders API: pricing, parameters and code examples

`getapp/category-leaders` · data API · GetApp · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retrieve the category page data including top-ranked software products, buyers guide content, facets, and pagination for a given category.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "getapp/category-leaders", "category_slug": "customer-management-software/crm"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('getapp/category-leaders', {'category_slug': 'customer-management-software/crm'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("getapp/category-leaders", {
  "category_slug": "customer-management-software/crm"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "getapp/category-leaders", sandbase.Params{
	"category_slug": "customer-management-software/crm",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/getapp/category-leaders` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `category_slug` | string | yes | Category URL path segment without leading/trailing slashes (e.g. 'customer-management-software/crm'). Same format as list_software_by_category.  |

## Details

Returns the GetApp category page for one software category as JSON. It includes the buyers guide text, comparison pairs, filter facets, and page metadata. The only input is `category_slug`, for example `customer-management-software/crm`.

### Use cases

- Pull the buyers guide text for a category to summarize what the software type does.
- Collect the filter options for a category, such as pricing types, operating systems, and customer types, to build a category profile.
- Find popular product pairs in a category from the comparison list and open their compare pages.
- Map a category's breadcrumb and tab links to build a category tree of GetApp pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/getapp/category-leaders" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_slug": "customer-management-software/crm"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_slug` | string | Yes | Category URL path segment without leading/trailing slashes (e.g. 'customer-management-software/crm'). Same format as list_software_by_category. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "appData": {
      "_vercelExperimentsGa4": {},
      "_vercelFlags": {
        "getapp-ai-assistant": 1,
        "getapp-osano-cmp-primary": -1
      },
      "canShowLiveChat": true,
      "categories": [],
      "category": {
        "cta_urls": {
          "detail": "/customer-management-software/crm/"
        },
        "definition": null,
        "directoryH1": null,
        "directoryTitle": null,
        "global_category_id": "4c7ba4f6-a5c3-4fcf-bb0b-388597ecee9d",
        "has_seo_facets": true,
        "id": "4c7ba4f6-a5c3-4fcf-bb0b-388597ecee9d",
        "isPagePublished": true
      },
      "compareBasketState": [],
      "countryCode": "US",
      "csrf": "",
      "experiments": {
        "ga4": {},
        "variations": {}
      },
      "g2CompanyLookupApiKey": "pk_7874b…",
      "g2CompanyLookupUrl": "https://enrich.g2.com/quem",
      "g2EnrichHit": false
    },
    "buyersGuide": {
      "content": {
        "json": {
          "content": [
            {
              "content": [
                {
                  "data": {},
                  "marks": [],
                  "nodeType": "text",
                  "value": "Customer relationship management (CRM) software helps sales and marketing profes…"
                }
              ],
              "data": {},
              "nodeType": "paragraph"
            }
          ],
          "data": {},
          "nodeType": "document"
        },
        "links": {}
      },
      "slug": "crm",
      "title": "CRM"
    },
    "serpData": {
      "category": {
        "cta_urls": {
          "detail": "/customer-management-software/crm/"
        },
        "definition": null,
        "directoryH1": null,
        "directoryTitle": null,
        "global_category_id": "4c7ba4f6-a5c3-4fcf-bb0b-388597ecee9d",
        "has_seo_facets": true,
        "id": "4c7ba4f6-a5c3-4fcf-bb0b-388597ecee9d",
        "isPagePublished": true
      },
      "comparisons": [
        {
          "alternative": {
            "isPublished": true,
            "node": {
              "id": "2143ac98-b65c-4bb1-ae6b-a6d200b7a22f",
              "logoUrl": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/82a342f4-1d08-4265-877a-83f…",
              "name": "Zoho CRM",
              "seoId": "9908",
              "slug": "zoho-crm",
              "url": "https://www.getapp.com/customer-management-software/a/{seoSlug_1}/compare/{seoSl…"
            }
          },
          "compareUrl": "/customer-management-software/a/zoho-crm/compare/salesforce/",
          "id": "8c7f8bf5-dbf6-47ee-9df7-a6d200b64092",
          "logoUrl": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/f11ea590-5812-4ce0-a108-383…",
          "name": "Salesforce Sales Cloud",
          "seoId": "90378",
          "slug": "salesforce",
          "url": "https://www.getapp.com/customer-management-software/a/{seoSlug_1}/compare/{seoSl…"
        }
      ],
      "contentRichSection": null,
      "content_type": null,
      "crxEnabled": false,
      "facets": {
        "feature_tags_facet": [
          {
            "count": null,
            "global_product_id": "24446824-7c35-4f73-a1d2-4ba87904d3ba",
            "href": "|customer-management-software|crm|f|customer-journey-mapping|",
            "is_seo": true,
            "label": "Customer Journey Mapping",
            "selected": false,
            "value": "customer-journey-mapping"
          }
        ],
        "integrated_with_facet": [
          {
            "count": null,
            "global_product_id": "ab698308-39bc-4ec3-997e-a6d200b6d7d4",
            "href": "|customer-management-software|crm|w|tableau|",
            "is_seo": true,
            "label": "Tableau",
            "selected": false,
            "value": "tableau"
          }
        ],
        "oses_facet": [
          {
            "count": null,
            "href": "|customer-management-software|crm|os|linux|",
            "is_seo": true,
            "label": "Linux",
            "selected": false,
            "value": "linux"
          }
        ],
        "pricingcategories_facet": [
          {
            "count": null,
            "href": "|customer-management-software|crm|p|free|",
            "is_seo": true,
            "label": "Free",
            "selected": false,
            "value": "free"
          }
        ],
        "rating_stars_ge": [
          {
            "count": null,
            "href": "|customer-management-software|crm|",
            "is_seo": false,
            "label": "All Reviews",
            "selected": true,
            "value": "all"
          }
        ],
        "typecustomers_facet": [
          {
            "count": null,
            "href": "|customer-management-software|crm|org|freelancers|",
            "is_seo": true,
            "label": "Freelancers",
            "selected": false,
            "value": "freelancers"
          }
        ]
      },
      "feature": null,
      "key_features": [],
      "listings": [
        {
          "category_leaders_score": null,
          "cta_urls": {
            "cta": "https://www.capterra.com/ppc/clicks/collect/GA/directory/2143ac98-b65c-4bb1-ae6b…",
            "detail": "/customer-management-software/a/zoho-crm/",
            "features": null,
            "reviews": null,
            "sem_detail": "/p/sem/a/zoho-crm/",
            "spotlight_pricing": null
          },
          "description": "Zoho CRM records all contact, lead & account data. It also lets you assign tasks…",
          "features": {
            "popular": [
              {
                "name": "A/B Testing",
                "slug": "83ac06ef-609f-47cc-9b0d-4654f513f0a1"
              }
            ]
          },
          "global_product_id": "2143ac98-b65c-4bb1-ae6b-a6d200b7a22f",
          "id": "2143ac98-b65c-4bb1-ae6b-a6d200b7a22f",
          "is_category_leader": false,
          "is_premium": true
        }
      ],
      "pagination": {
        "first_page": "/customer-management-software/crm/",
        "items_per_page": 25,
        "num_items": 1925,
        "num_pages": 77,
        "other_page_pattern": "/customer-management-software/crm/page-PAGE/",
        "page": 1
      },
      "related_categories": [
        {
          "cta_urls": {
            "detail": "/sales-software/contact-management/"
          },
          "global_category_id": "41e2ac18-3264-4fb3-b4b8-32a2458b91c5",
          "listings": [],
          "name": "Contact Management",
          "num_listings": 0,
          "slug": "contact-management"
        }
      ],
      "route": "serp_category"
    }
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.serpData.category.id / data.serpData.category.global_category_id` | The ID of the category. Both fields hold the same value in this response. |
| `data.buyersGuide.title / data.buyersGuide.slug` | The category name (`CRM`) and its short slug (`crm`). |
| `data.buyersGuide.content.json.content[]` | The buyers guide as a rich text document. Each paragraph holds text nodes with a `value` string. |
| `data.serpData.comparisons[].name / data.serpData.comparisons[].slug` | The product name and slug for an entry in the comparison list. |
| `data.serpData.comparisons[].compareUrl` | The relative GetApp URL of the compare page for the product and its paired alternative. |
| `data.serpData.comparisons[].alternative.node.name` | The name of the product paired against the main product in that comparison. |
| `data.serpData.facets.pricingcategories_facet[]` | Pricing filter options such as `Free`, `Open Source`, and `Free Trial`. Each has a `label`, a `value`, and an `href` path. |
| `data.serpData.facets.feature_tags_facet[] / data.serpData.facets.integrated_with_facet[]` | Filter options for product features and for integrations. Each row has a `label`, a `value`, and a `global_product_id`. |
| `data.serpData.facets.typecustomers_facet[] / data.serpData.facets.oses_facet[]` | Filter options by customer type and operating system. Examples are `Freelancers`, `Large Enterprises`, `Linux`, and `Windows`. |
| `data.appData.header.breadcrumb[]` | The breadcrumb trail for the category page. Each row has a `label` and a `url`. |

### Notes

- Use the same `category_slug` format as [GetApp List Software By Category](/apis/getapp/list-software-by-category): the URL path without leading or trailing slashes.
- Call [GetApp List Categories](/apis/getapp/list-categories) to find slugs for other categories.
- Facet `count` values are `null` in this response, so do not rely on them for totals.
- Call [GetApp List Software By Category](/apis/getapp/list-software-by-category) to get the products listed in the category.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/getapp/category-leaders.json`](../../../catalog/models/getapp/category-leaders.json) · Store page: https://www.sandbase.ai/model/getapp/category-leaders
