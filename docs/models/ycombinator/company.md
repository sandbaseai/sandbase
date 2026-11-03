# Y Combinator Company API: pricing, parameters and code examples

`ycombinator/company` · data API · Y Combinator · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retrieve full details for a YC company by its slug. Returns comprehensive company profile including founders with bios, social links, team size, description, and funding information.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ycombinator/company", "slug": "airbnb"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ycombinator/company', {'slug': 'airbnb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ycombinator/company", {
  "slug": "airbnb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ycombinator/company", sandbase.Params{
	"slug": "airbnb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ycombinator/company` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | Company slug identifier (e.g. 'airbnb', 'coinbase', 'stripe'). Obtainable from search_companies results.  |

## Details

Returns the Y Combinator profile for one company, including its batch, location, tags, team size, website and social links, and a list of founders with bios. It needs one input, the company `slug`, such as `airbnb`.

### Use cases

- Pull a YC company's founders, titles and LinkedIn or Twitter links to build an outreach list.
- Check a company's batch, founding year and `ycdc_status` to track which YC companies are still active or public.
- Enrich a CRM record with a company's one-liner, description, tags, website and team size.
- Find the YC group partner linked to a company.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ycombinator/company" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "airbnb"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Company slug identifier (e.g. 'airbnb', 'coinbase', 'stripe'). Obtainable from search_companies results. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "app_answers": [],
    "app_video_url": null,
    "batch": "W09",
    "batch_name": "Winter 2009",
    "cb_url": "https://www.crunchbase.com/organization/airbnb",
    "city": "San Francisco",
    "city_tag": "san-francisco-bay-area",
    "company_photos": [
      {
        "id": 164,
        "photo_type": "sign",
        "url": "https://bookface-images.s3.us-west-2.amazonaws.com/attachments/8a7236c94b4d9b78b…"
      }
    ],
    "country": "US",
    "dday_video_url": null,
    "fb_url": "https://www.facebook.com/airbnb/",
    "founders": [
      {
        "avatar_thumb_url": "https://bookface-images.s3.us-west-2.amazonaws.com/avatars/7415ee0d3978ae738c766…",
        "founder_bio": "Brian Chesky is the co-founder,  Head of Community, and  CEO of Airbnb, which he…",
        "full_name": "Brian Chesky",
        "has_email": true,
        "is_active": true,
        "latest_yc_company": {
          "href": "https://www.ycombinator.com/companies/airbnb",
          "name": "Airbnb"
        },
        "linkedin_url": "https://www.linkedin.com/in/brianchesky/",
        "title": "Founder/CEO",
        "twitter_url": "https://twitter.com/bchesky",
        "user_id": 21981
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.name / data.one_liner` | Company name and a short one-line description of what it does. |
| `data.long_description` | Longer text description of the company. The sample response cuts it short. |
| `data.batch / data.batch_name / data.year_founded` | YC batch code (for example `W09`), the batch's full name (`Winter 2009`), and the year the company was founded. |
| `data.team_size` | Number of people on the company's team, as an integer. |
| `data.ycdc_status` | The company's status in the YC directory, for example `Public`. |
| `data.tags[]` | Industry or category labels for the company, such as `Marketplace` and `Travel`. |
| `data.city / data.country / data.location` | Where the company is based. |
| `data.website / data.linkedin_url / data.twitter_url / data.fb_url / data.cb_url` | Links to the company's website and its LinkedIn, Twitter, Facebook and Crunchbase pages. Some links, such as `github_url`, can be `null`. |
| `data.founders[].full_name / data.founders[].title` | Each founder's name and role at the company, for example `Founder/CEO`. |
| `data.founders[].founder_bio / data.founders[].linkedin_url / data.founders[].twitter_url` | Each founder's bio and social profile links. |
| `data.primary_group_partner.full_name` | Name of the YC group partner tied to the company. `url` gives the partner's YC profile page. |

### Notes

- Get the `slug` from the `ycdc_url` of a search result, or from [Y Combinator Search Companies](/apis/ycombinator/search-companies). The slug is the last part of the URL, such as `airbnb`.
- Each founder has a numeric `user_id`. Use it to look up more about that person with [Y Combinator Person Detail](/apis/ycombinator/person-detail).
- Image URLs for logos, avatars and photos are signed links, so they carry query parameters.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/ycombinator/company.json`](../../../catalog/models/ycombinator/company.json) · Store page: https://www.sandbase.ai/model/ycombinator/company
