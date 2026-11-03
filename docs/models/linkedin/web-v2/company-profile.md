# LinkedIn Company Profile API: pricing, parameters and code examples

`linkedin/web-v2/company-profile` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns LinkedIn company profile details, including affiliated organizations, using a direct company page URL.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/web-v2/company-profile", "url": "https://www.linkedin.com/company/microsoft/"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/web-v2/company-profile', {'url': 'https://www.linkedin.com/company/microsoft/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/web-v2/company-profile", {
  "url": "https://www.linkedin.com/company/microsoft/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/web-v2/company-profile", sandbase.Params{
	"url": "https://www.linkedin.com/company/microsoft/",
})
```

Same call via the path form: `POST /v1/api/linkedin/web-v2/company-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full company URL (e.g. https://www.linkedin.com/company/microsoft/).  |

## Details

Returns a LinkedIn company profile as JSON: name, about text, size, headquarters, locations, follower count, affiliated and similar pages, sample employees, and recent page updates. It needs the full LinkedIn company page URL in the `url` parameter.

### Use cases

- Enrich a CRM record with a company's industry, size, headquarters and website.
- Map a company's affiliated pages, such as GitHub or Microsoft Azure for Microsoft, from the `affiliated` list.
- Find competitor or peer companies from the `similar` list.
- Track a company's follower count and recent page updates with their like and comment counts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/web-v2/company-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/company/microsoft/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full company URL (e.g. https://www.linkedin.com/company/microsoft/). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "about": "Every company has a mission. What's ours? To empower every person and every orga…",
  "additional_information": null,
  "affiliated": [
    {
      "Links": "https://www.linkedin.com/company/github?trk=affiliated-pages",
      "location": "San Francisco, CA",
      "subtitle": "Software Development",
      "title": "GitHub"
    }
  ],
  "alumni": null,
  "alumni_information": null,
  "company_id": "1035",
  "company_size": "10,001+ employees",
  "country_code": "US,AU,CA,FR,DE,JP,GB,DK,BE,FI,IT,KR,NL,NO,ES,SE,CH,BR,CN,IN,MX,RU,ZA,TR,AT,HK,IE…",
  "country_codes_array": [
    "US"
  ],
  "description": "Microsoft | 29,433,315 followers on LinkedIn. Every company has a mission. What&…",
  "employees": [
    {
      "img": "https://media.licdn.com/dms/image/v2/D5603AQHW7wKzPb3DAg/profile-displayphoto-sh…",
      "link": "https://www.linkedin.com/in/reidhoffman?trk=org-employees",
      "subtitle": "Co-Founder, LinkedIn, Manas AI & Inflection AI. Founding Team, PayPal. Author of…",
      "title": "Reid Hoffman Reid Hoffman is an Influencer"
    }
  ],
  "employees_in_linkedin": 231131
}
```

### Response fields

| Field | Meaning |
|---|---|
| `name / id / company_id` | Company display name, the URL slug (for example `microsoft`), and the numeric LinkedIn company ID as a string. |
| `about / unformatted_about / description` | Company about text. `about` is the cleaned version, `unformatted_about` keeps raw whitespace, and `description` is a short summary that includes the follower count. |
| `industries / organization_type / company_size / specialties` | Industry label, organization type (for example `Public Company`), employee size range, and the listed specialties as one text string. |
| `followers / employees_in_linkedin` | Number of followers of the page and number of employees found on LinkedIn. |
| `headquarters / formatted_locations / locations` | Headquarters city and region, plus the list of office addresses with country codes. `formatted_locations` uses a comma-separated format. |
| `website / website_simplified` | Company website URL and the same address without the protocol. |
| `affiliated[].title / affiliated[].subtitle / affiliated[].location / affiliated[].Links` | Name, industry, optional location and LinkedIn link of each affiliated page, such as a subsidiary or showcase page. |
| `similar[].title / similar[].subtitle / similar[].Links` | Name, industry and LinkedIn link of each page LinkedIn lists as similar. |
| `employees[].title / employees[].subtitle / employees[].link` | Name, headline and profile link of a few employees shown on the company page. |
| `updates[].text / updates[].date / updates[].likes_count / updates[].comments_count / updates[].post_url` | Text, ISO timestamp, engagement counts and link of each recent page update. The `title` field holds the name of the poster. |

### Notes

- Pass the full company page URL, including `https://`, such as `https://www.linkedin.com/company/microsoft/`.
- The `employees` and `updates` lists are short samples. Use [LinkedIn Company Posts](/apis/linkedin/web-v2/company-posts) to get posts from the page.
- `updates[].post_id` and `updates[].post_url` identify each post, and the `time` field gives a relative age such as `3d`. Use [LinkedIn Post Comments](/apis/linkedin/web-v2/post-comments) to read comments on a post.

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [LinkedIn Company Posts](/apis/linkedin/web-v2/company-posts): Returns posts from a LinkedIn organization page using the company URL.
- [LinkedIn Job Details](/apis/linkedin/web-v2/job-detail): Returns detailed information for a specific LinkedIn job posting via its URL.
- [LinkedIn Post Comments](/apis/linkedin/web-v2/post-comments): Returns comments for a specific LinkedIn post using its activity URN.

---
Machine-readable: [`catalog/models/linkedin/web-v2/company-profile.json`](../../../../catalog/models/linkedin/web-v2/company-profile.json) · Store page: https://www.sandbase.ai/model/linkedin/web-v2/company-profile
