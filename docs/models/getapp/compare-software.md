# GetApp Compare Software API: pricing, parameters and code examples

`getapp/compare-software` · data API · GetApp · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Compare two software products side-by-side, including features, pricing, reviews, pros/cons, and support options. slug1 is the full product path, slug2 is the comparison product slug.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "getapp/compare-software", "slug1": "collaboration-software/a/monday-com", "slug2": "trello"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('getapp/compare-software', {'slug1': 'collaboration-software/a/monday-com', 'slug2': 'trello'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("getapp/compare-software", {
  "slug1": "collaboration-software/a/monday-com",
  "slug2": "trello"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "getapp/compare-software", sandbase.Params{
	"slug1": "collaboration-software/a/monday-com",
	"slug2": "trello",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/getapp/compare-software` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug1` | string | yes | Full product URL path for the first product (e.g. 'collaboration-software/a/monday-com').  |
| `slug2` | string | yes | Product slug for the second product to compare (e.g. 'notion', 'trello'). Obtainable from popular_comparisons in get_software_details.  |

## Details

Returns a GetApp comparison page for two software products as JSON. It needs `slug1` (the full path of the first product) and `slug2` (the slug of the second product). The response includes page metadata, a list of compared features and integrations, and alternative products with ratings.

### Use cases

- Pull the feature and integration lists for a pair of project management tools to build a comparison table.
- Find alternative products to a given tool, with their ratings and review counts.
- Collect the canonical GetApp comparison URL and page title for a product pair, for SEO or content research.
- Check the category breadcrumb a comparison page belongs to, to group product pairs by category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/getapp/compare-software" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug1": "collaboration-software/a/monday-com", "slug2": "trello"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug1` | string | Yes | Full product URL path for the first product (e.g. 'collaboration-software/a/monday-com'). |
| `slug2` | string | Yes | Product slug for the second product to compare (e.g. 'notion', 'trello'). Obtainable from popular_comparisons in get_software_details. |

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
      "category": {},
      "compareBasketState": [],
      "countryCode": "US",
      "csrf": "",
      "experiments": {
        "currentPageActiveExperimentIds": [],
        "ga4": {
          "User_Information_GAExperimentId": null,
          "User_Information_GAExperimentUserId": "bf2233cc-a966-4a57-84c9-a31625968d26"
        },
        "variations": {}
      },
      "g2CompanyLookupApiKey": "pk_7874b…",
      "g2CompanyLookupUrl": "https://enrich.g2.com/quem",
      "g2EnrichHit": false
    },
    "compareData": {
      "alternatives": [
        {
          "add_to_compare_url": "|project-management-planning-software|a|trello|compare|monday-com-vs-any-do|",
          "id": "103189",
          "logo_url": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/452debc4-40c0-426e-9275-c73…",
          "name": "Any.do",
          "rating": 4.729401561144839,
          "rating_avg": 4.729401561144839,
          "slug": "any-do"
        }
      ],
      "comparisonReviews": {
        "first": null,
        "last": null
      },
      "features": [
        "360 Degree Feedback"
      ],
      "integrations": [
        "Adobe Creative Cloud"
      ],
      "listings": [
        {
          "aiCapability": null,
          "alternatives": [
            {
              "compare_page": {
                "is_seo": true,
                "url": "https://www.getapp.com/project-management-planning-software/a/trello/compare/any…"
              },
              "compare_url": "https://www.getapp.com/project-management-planning-software/a/trello/compare/any…",
              "cta_url": "/any-do/",
              "detail_url": "/any-do/",
              "id": "103189",
              "is_premium": false,
              "logo": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/452debc4-40c0-426e-9275-c73…",
              "name": "Any.do"
            }
          ],
          "alternativesUrl": "/project-management-planning-software/a/trello/alternatives/",
          "alternatives_by_section": {
            "faq_contenders": [
              {
                "cta_urls": {
                  "cta": "/project-management-planning-software/a/jira/",
                  "detail": "/project-management-planning-software/a/jira/",
                  "visit_website": null
                },
                "global_product_id": "21baee7f-1996-4d76-9942-a6d200b4bc5b",
                "id": "9953",
                "is_premium": false,
                "logo_url": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/e1b492c5-8a97-4b86-a422-d31…",
                "name": "Jira",
                "num_reviews": 15777,
                "pricing": {
                  "categories": []
                }
              }
            ],
            "features": [
              {
                "cta_urls": {
                  "cta": "/project-management-planning-software/a/jira/",
                  "detail": "/project-management-planning-software/a/jira/",
                  "visit_website": null
                },
                "global_product_id": "21baee7f-1996-4d76-9942-a6d200b4bc5b",
                "id": "9953",
                "is_premium": false,
                "logo_url": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/e1b492c5-8a97-4b86-a422-d31…",
                "name": "Jira",
                "num_reviews": 15777,
                "pricing": {
                  "categories": []
                }
              }
            ],
            "overall": [
              {
                "cta_urls": {
                  "cta": "/project-management-planning-software/a/jira/",
                  "detail": "/project-management-planning-software/a/jira/",
                  "visit_website": null
                },
                "global_product_id": "21baee7f-1996-4d76-9942-a6d200b4bc5b",
                "id": "9953",
                "is_premium": false,
                "logo_url": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/e1b492c5-8a97-4b86-a422-d31…",
                "name": "Jira",
                "num_reviews": 15777,
                "pricing": {
                  "categories": []
                }
              }
            ],
            "value_for_money": [
              {
                "cta_urls": {
                  "cta": "/project-management-planning-software/a/jira/",
                  "detail": "/project-management-planning-software/a/jira/",
                  "visit_website": null
                },
                "global_product_id": "21baee7f-1996-4d76-9942-a6d200b4bc5b",
                "id": "9953",
                "is_premium": false,
                "logo_url": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/e1b492c5-8a97-4b86-a422-d31…",
                "name": "Jira",
                "num_reviews": 15777,
                "pricing": {
                  "categories": []
                }
              }
            ]
          },
          "alternatives_comparisons": [
            {
              "cta_urls": {
                "cta": "/project-management-planning-software/a/jira/",
                "detail": "/project-management-planning-software/a/jira/",
                "visit_website": null
              },
              "global_product_id": "21baee7f-1996-4d76-9942-a6d200b4bc5b",
              "id": "9953",
              "is_premium": false,
              "logo_url": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/e1b492c5-8a97-4b86-a422-d31…",
              "name": "Jira",
              "num_reviews": 15777,
              "pricing": {
                "categories": []
              }
            }
          ],
          "categories": [
            {
              "category_leaders": null,
              "cta_urls": {
                "category_leaders": null,
                "detail": "/hr-employee-management-software/okr/"
              },
              "id": "b4c4028d-e593-430d-b37c-8b1be18b6eee",
              "isPpl": true,
              "name": "OKR",
              "slug": "okr",
              "total_listings": null
            }
          ],
          "category": "web-collaboration",
          "category_leader_score": null
        }
      ],
      "title": "Trello vs monday AI Work Platform Comparison (2026)"
    }
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.compareData.features[]` | Names of features covered by the comparison, such as `API` and `@mentions`. |
| `data.compareData.integrations[]` | Names of integrations listed for the compared products. |
| `data.compareData.alternatives[].name` | Name of a suggested alternative product. |
| `data.compareData.alternatives[].rating / data.compareData.alternatives[].rating_avg` | Average rating of the alternative product. Both keys hold the same value in the sample. |
| `data.compareData.alternatives[].slug / data.compareData.alternatives[].id` | Slug and numeric ID of the alternative product. Use the slug in a later comparison. |
| `data.compareData.listings[].alternatives[].compare_url` | Full GetApp URL of the comparison page between the listed product and an alternative. |
| `data.compareData.listings[].alternatives_by_section.overall[].num_reviews` | Number of reviews for each alternative in the overall alternatives list. |
| `data.appData.head.title` | Title of the comparison page, for example `Trello vs monday AI Work Platform`. |
| `data.appData.head.link_rel[].url` | Canonical URL of the comparison page on GetApp. |
| `data.appData.header.breadcrumb[].label` | Category and page labels in the breadcrumb of the comparison page. |

### Notes

- The response mirrors a web page payload, so it also holds page settings and tracking fields that you can ignore.
- `slug1` is the full product path, such as `collaboration-software/a/monday-com`. `slug2` is a short slug, such as `trello`.
- Get product paths and comparison slugs from [GetApp Software Details](/apis/getapp/software-details). Use [GetApp Software Alternatives](/apis/getapp/software-alternatives) for a fuller list of alternatives.
- For pricing and review data on a single product, call [GetApp Software Pricing](/apis/getapp/software-pricing) or [GetApp Software Reviews](/apis/getapp/software-reviews).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/getapp/compare-software.json`](../../../catalog/models/getapp/compare-software.json) · Store page: https://www.sandbase.ai/model/getapp/compare-software
