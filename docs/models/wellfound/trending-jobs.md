# Wellfound Trending Jobs API: pricing, parameters and code examples

`wellfound/trending-jobs` · data API · Wellfound · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Fetch featured/trending jobs from the Wellfound homepage, organized by category (trending, engineering, product, design, data, sales, marketing, operations, recruiting, finance). Each category contains 3 recently.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wellfound/trending-jobs"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wellfound/trending-jobs', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wellfound/trending-jobs", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wellfound/trending-jobs", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/wellfound/trending-jobs` with the body above minus `model`.

## Details

Returns featured jobs from the Wellfound homepage, grouped by category such as engineering, product, design, data, marketing, operations and finance. It takes no input. Each category holds a short list of recent jobs with title, pay, location and the hiring startup.

### Use cases

- Show a daily feed of featured startup jobs on a job board or newsletter.
- Compare the pay ranges and equity ranges shown for roles in different categories.
- Collect startup names and slugs from featured jobs to find companies that are hiring.
- Track which remote roles Wellfound features in each category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wellfound/trending-jobs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "data": [
      {
        "compensation": "$150k – $200k • 0.01% – 0.2%",
        "id": "3834594",
        "liveStartAt": 1793664000,
        "locationNames": [
          "New York City"
        ],
        "remote": false,
        "slug": "data-engineer",
        "startup": {
          "id": "9887955",
          "logoUrl": "https://photos.wellfound.com/startups/i/9887955-98a0c6d25725d9b4919463ebd3fc0169…",
          "name": "Stuut",
          "slug": "stuut-1"
        },
        "title": "Data Engineer",
        "url": "https://wellfound.com/jobs/3834594-data-engineer"
      }
    ],
    "design": [
      {
        "compensation": "R$36k – R$48k • No equity",
        "id": "4895709",
        "liveStartAt": 1793009682,
        "locationNames": [
          "Sheridan"
        ],
        "remote": true,
        "slug": "motion-designer-brazil-latam",
        "startup": {
          "id": "11300796",
          "logoUrl": "https://photos.wellfound.com/startups/i/11300796-d213645a086d764263af53705b88cec…",
          "name": "Design Shifu",
          "slug": "design-shifu-1"
        },
        "title": "Motion Designer (Brazil/LATAM)",
        "url": "https://wellfound.com/jobs/4895709-motion-designer-brazil-latam"
      }
    ],
    "engineering": [
      {
        "compensation": "$200k – $240k • 0.08% – 0.18%",
        "id": "4965882",
        "liveStartAt": 1793666110,
        "locationNames": [
          "New York City"
        ],
        "remote": false,
        "slug": "senior-software-engineer-ai-agents",
        "startup": {
          "id": "9413568",
          "logoUrl": "https://photos.wellfound.com/startups/i/9413568-13482b87426021829e2ed84449b563d0…",
          "name": "Traba",
          "slug": "traba-work"
        },
        "title": "Senior Software Engineer (AI Agents)",
        "url": "https://wellfound.com/jobs/4965882-senior-software-engineer-ai-agents"
      }
    ],
    "finance": [
      {
        "compensation": "$150k – $225k",
        "id": "4965920",
        "liveStartAt": 1793667400,
        "locationNames": [
          "United States"
        ],
        "remote": true,
        "slug": "finance-manager",
        "startup": {
          "id": "10894775",
          "logoUrl": "https://photos.wellfound.com/startups/i/10894775-28b242c56b7ea6ac1a9cdb135d5ddb0…",
          "name": "Jerry.ai",
          "slug": "jerry-ai-1"
        },
        "title": "Finance Manager",
        "url": "https://wellfound.com/jobs/4965920-finance-manager"
      }
    ],
    "marketing": [
      {
        "compensation": "$36k – $36k",
        "id": "4943288",
        "liveStartAt": 1793390783,
        "locationNames": [
          "Wyoming"
        ],
        "remote": true,
        "slug": "technical-digital-marketer",
        "startup": {
          "id": "11336419",
          "logoUrl": "https://photos.wellfound.com/startups/i/11336419-b809e657002002dfdf637c6284d0096…",
          "name": "Level 5 Mentoring",
          "slug": "level-5-mentoring"
        },
        "title": "Technical Digital Marketer",
        "url": "https://wellfound.com/jobs/4943288-technical-digital-marketer"
      }
    ],
    "operations": [
      {
        "compensation": "$60k – $80k",
        "id": "4965903",
        "liveStartAt": 1793666996,
        "locationNames": [
          "San Francisco"
        ],
        "remote": true,
        "slug": "growth-event-coordinator",
        "startup": {
          "id": "3840097",
          "logoUrl": "https://photos.wellfound.com/startups/i/3840097-81876de8ee63d0bdf47d72659782b512…",
          "name": "Clipboard",
          "slug": "clipboard"
        },
        "title": "Growth Event Coordinator",
        "url": "https://wellfound.com/jobs/4965903-growth-event-coordinator"
      }
    ],
    "product": [
      {
        "compensation": "$150k – $230k • 0.03% – 0.08%",
        "id": "4967204",
        "liveStartAt": 1793678350,
        "locationNames": [
          "United States"
        ],
        "remote": true,
        "slug": "product-manager-growth-technical-or-ex-product-engineer",
        "startup": {
          "id": "8224317",
          "logoUrl": "https://photos.wellfound.com/startups/i/8224317-b5e6c8d7d35d4ef7e446119da212bdfa…",
          "name": "Kovo",
          "slug": "kovocredit"
        },
        "title": "Product Manager - Growth (technical or ex-product engineer)",
        "url": "https://wellfound.com/jobs/4967204-product-manager-growth-technical-or-ex-produc…"
      }
    ],
    "recruiting": [
      {
        "compensation": "$140k – $175k",
        "id": "4965940",
        "liveStartAt": 1793667564,
        "locationNames": [
          "Alameda"
        ],
        "remote": false,
        "slug": "senior-technical-recruiter",
        "startup": {
          "id": "10941864",
          "logoUrl": "https://photos.wellfound.com/startups/i/10941864-beec4dd2dc3198ed17e1f2732b225c9…",
          "name": "Epia Neuro",
          "slug": "epia-neuro"
        },
        "title": "Senior Technical Recruiter",
        "url": "https://wellfound.com/jobs/4965940-senior-technical-recruiter"
      }
    ],
    "sales": [
      {
        "compensation": "$60k – $130k • 0.0% – 1.5%",
        "id": "4953850",
        "liveStartAt": 1793482829,
        "locationNames": [
          "San Francisco"
        ],
        "remote": true,
        "slug": "founding-account-executive-full-cycle-law-firms-dental-practices",
        "startup": {
          "id": "11341870",
          "logoUrl": "https://photos.wellfound.com/startups/i/11341870-b1311b66bfb8e3fb34b5329469eb21c…",
          "name": "Cited",
          "slug": "cited-5"
        },
        "title": "Founding Account Executive (Full-Cycle), Law Firms & Dental Practices",
        "url": "https://wellfound.com/jobs/4953850-founding-account-executive-full-cycle-law-fir…"
      }
    ],
    "trending": [
      {
        "compensation": "$60k – $90k • No equity",
        "id": "4893903",
        "liveStartAt": 1793671611,
        "locationNames": [
          "Santa Cruz"
        ],
        "remote": true,
        "slug": "b2b-sales-representative-20-hr-or-30-commission-remote",
        "startup": {
          "id": "11298785",
          "logoUrl": "https://photos.wellfound.com/startups/i/11298785-fb878cce819e767996939d6ac414464…",
          "name": "Toolhaus",
          "slug": "toolhaus"
        },
        "title": "B2B Sales Representative — $20/hr or 30% Commission (Remote)",
        "url": "https://wellfound.com/jobs/4893903-b2b-sales-representative-20-hr-or-30-commissi…"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.data[]` | Jobs in the `data` category. Other categories such as `design`, `engineering`, `finance`, `marketing`, `operations` and `product` use the same job shape. |
| `data.engineering[].title` | Job title as shown on Wellfound. |
| `data.engineering[].compensation` | Pay range text, often followed by an equity range or `No equity`. The currency symbol is part of the string, for example `$` or `₹`. |
| `data.engineering[].locationNames[]` | City or region names for the job. The list can be empty. |
| `data.engineering[].remote` | `true` if the job is marked remote. |
| `data.engineering[].liveStartAt` | Unix timestamp in seconds for when the job went live. |
| `data.engineering[].url` | Link to the job page on Wellfound. |
| `data.engineering[].id / data.engineering[].slug` | Job ID and URL slug. The `url` combines them as `/jobs/<id>-<slug>`. |
| `data.engineering[].startup.name / data.engineering[].startup.slug` | Name and slug of the startup that posted the job. |
| `data.engineering[].startup.id / data.engineering[].startup.logoUrl` | Startup ID and a link to its logo image. |

### Notes

- The request takes no parameters, and the response has no pagination.
- Each category key holds a short list. The sample shows 3 jobs per category.
- To see more jobs from one startup, pass its `startup.slug` to [Wellfound Company Jobs](/apis/wellfound/company-jobs).
- For startup details, use [Wellfound Company Profile](/apis/wellfound/company-profile), or see [Wellfound Trending Startups](/apis/wellfound/trending-startups) for featured companies.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/wellfound/trending-jobs.json`](../../../catalog/models/wellfound/trending-jobs.json) · Store page: https://www.sandbase.ai/model/wellfound/trending-jobs
