# GetApp Software Details API: pricing, parameters and code examples

`getapp/software-details` · data API · GetApp · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retrieve full details for a software product including description, ratings, reviews, features, integrations, pricing, screenshots, and alternatives. The slug is the product URL path (e.g.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "getapp/software-details", "slug": "collaboration-software/a/monday-com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('getapp/software-details', {'slug': 'collaboration-software/a/monday-com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("getapp/software-details", {
  "slug": "collaboration-software/a/monday-com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "getapp/software-details", sandbase.Params{
	"slug": "collaboration-software/a/monday-com",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/getapp/software-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | Product URL path segment without leading/trailing slashes (e.g. 'collaboration-software/a/monday-com', 'customer-management-software/a/salesforce'). Obtainable from list_software_by_category listings or cta_urls.detail…  |

## Details

Returns the full GetApp listing for one software product, including its alternatives and their pricing. It needs one input, the product `slug`, which is the product URL path such as `collaboration-software/a/monday-com`.

### Use cases

- Compare a product's starting prices and plan types against its listed alternatives.
- Build a list of competitors for a product, with review counts and links to each detail page.
- Check which pricing categories, such as `free-trial` or `subscription`, a competing product offers.
- Feed product names and IDs into a market map of a software category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/getapp/software-details" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "collaboration-software/a/monday-com"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Product URL path segment without leading/trailing slashes (e.g. 'collaboration-software/a/monday-com', 'customer-management-software/a/salesforce'). Obtainable from list_software_by_category listings or cta_urls.detail f |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "aiCapability": null,
    "alternativesUrl": "/collaboration-software/a/monday-com/alternatives/",
    "alternatives_by_section": {
      "faq_contenders": [
        {
          "cta_urls": {
            "cta": "https://www.capterra.com/ppc/clicks/collect/GA/directory/40b7a6c0-fbfb-4243-bb5c…",
            "detail": "/project-management-planning-software/a/zoho-projects/",
            "visit_website": "https://www.capterra.com/ppc/clicks/collect/GA/directory/40b7a6c0-fbfb-4243-bb5c…"
          },
          "global_product_id": "40b7a6c0-fbfb-4243-bb5c-a6d200b7a22f",
          "id": "9910",
          "is_premium": true,
          "logo_url": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/90500a0b-eb4b-4bd0-a547-9b6…",
          "name": "Zoho Projects",
          "num_reviews": 878,
          "pricing": {
            "amount": "4",
            "categories": [
              "free-trial"
            ],
            "currency": "USD",
            "currency_symbol": "$",
            "no_credit_card_required": true,
            "periodicity": "month",
            "plans": [
              {
                "paymentFrequency": null,
                "pricingModel": 1,
                "startingPrice": 0
              }
            ],
            "price_range": 0
          }
        }
      ],
      "features": [
        {
          "cta_urls": {
            "cta": "https://www.capterra.com/ppc/clicks/collect/GA/directory/40b7a6c0-fbfb-4243-bb5c…",
            "detail": "/project-management-planning-software/a/zoho-projects/",
            "visit_website": "https://www.capterra.com/ppc/clicks/collect/GA/directory/40b7a6c0-fbfb-4243-bb5c…"
          },
          "global_product_id": "40b7a6c0-fbfb-4243-bb5c-a6d200b7a22f",
          "id": "9910",
          "is_premium": true,
          "logo_url": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/90500a0b-eb4b-4bd0-a547-9b6…",
          "name": "Zoho Projects",
          "num_reviews": 878,
          "pricing": {
            "amount": "4",
            "categories": [
              "free-trial"
            ],
            "currency": "USD",
            "currency_symbol": "$",
            "no_credit_card_required": true,
            "periodicity": "month",
            "plans": [
              {
                "paymentFrequency": null,
                "pricingModel": 1,
                "startingPrice": 0
              }
            ],
            "price_range": 0
          }
        }
      ],
      "overall": [
        {
          "cta_urls": {
            "cta": "https://www.capterra.com/ppc/clicks/collect/GA/directory/40b7a6c0-fbfb-4243-bb5c…",
            "detail": "/project-management-planning-software/a/zoho-projects/",
            "visit_website": "https://www.capterra.com/ppc/clicks/collect/GA/directory/40b7a6c0-fbfb-4243-bb5c…"
          },
          "global_product_id": "40b7a6c0-fbfb-4243-bb5c-a6d200b7a22f",
          "id": "9910",
          "is_premium": true,
          "logo_url": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/90500a0b-eb4b-4bd0-a547-9b6…",
          "name": "Zoho Projects",
          "num_reviews": 878,
          "pricing": {
            "amount": "4",
            "categories": [
              "free-trial"
            ],
            "currency": "USD",
            "currency_symbol": "$",
            "no_credit_card_required": true,
            "periodicity": "month",
            "plans": [
              {
                "paymentFrequency": null,
                "pricingModel": 1,
                "startingPrice": 0
              }
            ],
            "price_range": 0
          }
        }
      ],
      "value_for_money": [
        {
          "cta_urls": {
            "cta": "https://www.capterra.com/ppc/clicks/collect/GA/directory/40b7a6c0-fbfb-4243-bb5c…",
            "detail": "/project-management-planning-software/a/zoho-projects/",
            "visit_website": "https://www.capterra.com/ppc/clicks/collect/GA/directory/40b7a6c0-fbfb-4243-bb5c…"
          },
          "global_product_id": "40b7a6c0-fbfb-4243-bb5c-a6d200b7a22f",
          "id": "9910",
          "is_premium": true,
          "logo_url": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/90500a0b-eb4b-4bd0-a547-9b6…",
          "name": "Zoho Projects",
          "num_reviews": 878,
          "pricing": {
            "amount": "4",
            "categories": [
              "free-trial"
            ],
            "currency": "USD",
            "currency_symbol": "$",
            "no_credit_card_required": true,
            "periodicity": "month",
            "plans": [
              {
                "paymentFrequency": null,
                "pricingModel": 1,
                "startingPrice": 0
              }
            ],
            "price_range": 0
          }
        }
      ]
    },
    "alternatives_comparisons": [
      {
        "cta_urls": {
          "cta": "https://www.capterra.com/ppc/clicks/collect/GA/directory/40b7a6c0-fbfb-4243-bb5c…",
          "detail": "/project-management-planning-software/a/zoho-projects/",
          "visit_website": "https://www.capterra.com/ppc/clicks/collect/GA/directory/40b7a6c0-fbfb-4243-bb5c…"
        },
        "global_product_id": "40b7a6c0-fbfb-4243-bb5c-a6d200b7a22f",
        "id": "9910",
        "is_premium": true,
        "logo_url": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/90500a0b-eb4b-4bd0-a547-9b6…",
        "name": "Zoho Projects",
        "num_reviews": 878,
        "pricing": {
          "amount": "4",
          "categories": [
            "free-trial"
          ],
          "currency": "USD",
          "currency_symbol": "$",
          "no_credit_card_required": true,
          "periodicity": "month",
          "plans": [
            {
              "paymentFrequency": null,
              "pricingModel": 1,
              "startingPrice": 0
            }
          ],
          "price_range": 0
        },
        "product_canonical_id": "40b7a6c0-fbfb-4243-bb5c-a6d200b7a22f",
        "rating_avg": 4.494305239179955,
        "reviews": {
          "by_field": {
            "likelihood_to_recommend": "0.77",
            "rating_ease": "4.29",
            "rating_features": "4.41",
            "rating_support": "4.23",
            "rating_value": "4.40"
          }
        },
        "slug": "zoho-projects"
      }
    ],
    "benefits": null,
    "categories": [
      {
        "category_leaders": null,
        "cta_urls": {
          "category_leaders": null,
          "detail": "/all-software/project-management-software-for-nonprofits/"
        },
        "id": "ba2b4c28-2015-473f-bc3b-d82c0f2fd1c8",
        "isPpl": true,
        "name": "Nonprofit Project Management ",
        "slug": "project-management-software-for-nonprofits",
        "total_listings": null
      }
    ],
    "category": "task-management",
    "company_name": "monday.com",
    "countIntegrations": 35,
    "countNumReviews": 6130,
    "cta_urls": {
      "alternatives": "/collaboration-software/a/monday-com/alternatives/",
      "category_leaders": null,
      "cta": "https://www.capterra.com/ppc/clicks/collect/GA/directory/c7f00a1b-c5c0-4be8-8c9b…",
      "demo": "https://www.capterra.com/ppc/clicks/collect/GA/directory/c7f00a1b-c5c0-4be8-8c9b…",
      "detail": "/collaboration-software/a/monday-com/",
      "faq_contenders": null,
      "features": "/collaboration-software/a/monday-com/features/",
      "integrations": "/collaboration-software/a/monday-com/integrations/",
      "pricing": null,
      "reviews": null,
      "spotlight_pricing": "https://www.capterra.com/ppc/clicks/collect/GA/directory/c7f00a1b-c5c0-4be8-8c9b…",
      "trial": "https://www.capterra.com/ppc/clicks/collect/GA/directory/c7f00a1b-c5c0-4be8-8c9b…"
    },
    "customer_support_summary": {
      "cons": {
        "snippets": [
          {
            "avatar": null,
            "created": "2026-04-28T01:06:26Z",
            "first_name": "Deb",
            "frequency_of_use": "",
            "id": "Capterra___7139815",
            "is_anonymous": false,
            "is_authenticated": true,
            "is_validated": true
          }
        ],
        "summary": [
          "A small group of reviewers report slow or inconsistent response times, difficult…"
        ]
      },
      "num_review": null,
      "pros": {
        "snippets": [
          {
            "avatar": null,
            "created": "2026-04-28T06:15:44Z",
            "first_name": "Chantel",
            "frequency_of_use": "",
            "id": "Capterra___7139919",
            "is_anonymous": false,
            "is_authenticated": true,
            "is_validated": true
          }
        ],
        "summary": [
          "The majority of users highlight monday.com's customer support as fast, responsiv…"
        ]
      }
    }
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.alternativesUrl` | Path to the alternatives page for this product on the platform. |
| `data.alternatives_by_section.faq_contenders[] / data.alternatives_by_section.features[] / data.alternatives_by_section.overall[]` | Lists of alternative products, grouped by section. Each list uses the same item shape. |
| `data.alternatives_by_section.overall[].name` | Name of the alternative product. |
| `data.alternatives_by_section.overall[].num_reviews` | Number of reviews the alternative has. |
| `data.alternatives_by_section.overall[].cta_urls.detail` | Detail path of the alternative. You can use it as the `slug` after removing the leading and trailing slashes. |
| `data.alternatives_by_section.overall[].global_product_id / data.alternatives_by_section.overall[].id` | Identifiers for the alternative product. `global_product_id` is a UUID and `id` is a numeric string. |
| `data.alternatives_by_section.overall[].pricing.amount / data.alternatives_by_section.overall[].pricing.currency / data.alternatives_by_section.overall[].pricing.periodicity` | Starting price, its currency code, and the billing period, for example `4`, `USD`, `month`. |
| `data.alternatives_by_section.overall[].pricing.categories` | Pricing types the alternative offers, such as `free-trial`, `free`, `subscription` or `open-source`. |
| `data.alternatives_by_section.overall[].pricing.plans[].startingPrice` | Starting price of each listed plan. The value is `null` when no price is shown. |
| `data.alternatives_by_section.overall[].pricing.no_credit_card_required` | Whether the alternative lists that no credit card is needed to start. |

### Notes

- Find the `slug` in the `cta_urls.detail` field of a product, without the leading and trailing slashes. You can also get it from [GetApp List Software By Category](/apis/getapp/list-software-by-category).
- Each alternative has its own `cta_urls.detail` path, so you can call this API again with that value as the `slug`.
- For more depth on one product, see [GetApp Software Reviews](/apis/getapp/software-reviews) or [GetApp Software Pricing](/apis/getapp/software-pricing).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/getapp/software-details.json`](../../../catalog/models/getapp/software-details.json) · Store page: https://www.sandbase.ai/model/getapp/software-details
