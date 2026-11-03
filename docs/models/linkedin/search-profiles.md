# LinkedIn Profile Search API: pricing, parameters and code examples

`linkedin/search-profiles` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.198 per call · **Modes:** sync

Search LinkedIn profiles by keyword with optional location and job-title filters. Each match returns a full profile record: name, headline, location, current position, work experience, education, and skills, plus the profile URL, handle, and id. For a cheaper name/headline/URL-only search use linkedin.search_profiles_thin; add emails with linkedin.search_profiles_email.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.198**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/search-profiles", "query": "engineer"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/search-profiles', {'query': 'engineer'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/search-profiles", {
  "query": "engineer"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/search-profiles", sandbase.Params{
	"query": "engineer",
})
```

Same call via the path form: `POST /v1/api/linkedin/search-profiles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of full profiles to return (1-25, default 10). You are billed per profile returned, so a lower limit costs less. range 1–25 |
| `query` | string | yes | Search query for LinkedIn profiles: a role, name, or keywords (e.g. 'Marketing Manager').  |
| `schools` | array |  | Filter to people who attended any of these schools, by name.  |
| `jobTitle` | string |  | Optional current job title filter (e.g. 'Software Engineer').  |
| `location` | string |  | Optional location filter (e.g. 'San Francisco').  |
| `lastNames` | array |  | Filter to people whose last name matches any of these.  |
| `firstNames` | array |  | Filter to people whose first name matches any of these.  |
| `functionIds` | array |  | Filter by job function. Codes: 1=Accounting, 2=Administrative, 3=Arts and Design, 4=Business Development, 5=Community and Social Services, 6=Consulting, 7=Education, 8=Engineering, 9=Entrepreneurship, 10=Finance,…  |
| `pastCompanies` | array |  | Filter to people who previously worked at any of these companies, by name.  |
| `pastJobTitles` | array |  | Filter by a past job title the person held (e.g. ['Product Manager']).  |
| `excludeSchools` | array |  | Exclude people who attended any of these schools, by name.  |
| `companyHeadcount` | array |  | Filter by current company size (employee count). Codes: A=Self-Employed, B=1-10, C=11-50, D=51-200, E=201-500, F=501-1,000, G=1,001-5,000, H=5,001-10,000, I=10,001+.  |
| `currentCompanies` | array |  | Filter to people who currently work at any of these companies, by name (e.g. ['Google','Meta']). Multiple names widen the match (OR).  |
| `excludeLocations` | array |  | Exclude people in any of these locations, by place name.  |
| `profileLanguages` | array |  | Filter by the profile's primary language.  |
| `seniorityLevelIds` | array |  | Filter by seniority level. Codes: 100=In Training, 110=Entry Level, 120=Senior, 130=Strategic, 200=Entry Level Manager, 210=Experienced Manager, 220=Director, 300=Vice President, 310=CXO, 320=Owner/Partner.  |
| `excludeFunctionIds` | array |  | Exclude these job functions (same codes as functionIds).  |
| `recentlyChangedJobs` | boolean |  | When true, only return people who recently changed jobs (a strong sales/recruiting signal).  |
| `excludePastCompanies` | array |  | Exclude people who previously worked at any of these companies, by name.  |
| `excludePastJobTitles` | array |  | Exclude people who held any of these past job titles.  |
| `yearsOfExperienceIds` | array |  | Filter by total years of experience. Codes: 1=Less than 1 year, 2=1 to 2 years, 3=3 to 5 years, 4=6 to 10 years, 5=More than 10 years.  |
| `excludeCurrentCompanies` | array |  | Exclude people who currently work at any of these companies, by name.  |
| `excludeCurrentJobTitles` | array |  | Exclude people whose current job title matches any of these.  |
| `excludeSeniorityLevelIds` | array |  | Exclude these seniority levels (same codes as seniorityLevelIds).  |
| `recentlyPostedOnLinkedIn` | boolean |  | When true, only return people who recently posted on LinkedIn (an activity signal).  |
| `yearsAtCurrentCompanyIds` | array |  | Filter by tenure at the current company. Codes: 1=Less than 1 year, 2=1 to 2 years, 3=3 to 5 years, 4=6 to 10 years, 5=More than 10 years.  |
| `companyHeadquarterLocations` | array |  | Filter by the location of the person's current company headquarters, by place name (e.g. ['United States']).  |
| `excludeCompanyHeadquarterLocations` | array |  | Exclude people whose current company is headquartered in any of these locations.  |

## Details

Returns full LinkedIn profile records that match a keyword search. The only required input is `query`, and you can narrow results with filters such as `currentCompanies`, `location`, `jobTitle`, `schools`, and `seniorityLevelIds`.

### Use cases

- Build a list of engineers who currently work at a target company, with their work history and skills.
- Find recruiting candidates by job function, seniority level, and years of experience.
- Spot people who recently changed jobs and reach out while the move is new.
- Collect profile URLs and ids for a set of people, then pull their posts or activity with other LinkedIn APIs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/search-profiles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "query": "engineer", "currentCompanies": ["Google"]}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query for LinkedIn profiles: a role, name, or keywords (e.g. 'Marketing Manager'). |
| `companyHeadcount` | array | No | Filter by current company size (employee count). Codes: A=Self-Employed, B=1-10, C=11-50, D=51-200, E=201-500, F=501-1,000, G=1,001-5,000, H=5,001-10,000, I=10,001+. |
| `companyHeadquarterLocations` | array | No | Filter by the location of the person's current company headquarters, by place name (e.g. ['United States']). |
| `currentCompanies` | array | No | Filter to people who currently work at any of these companies, by name (e.g. ['Google','Meta']). Multiple names widen the match (OR). |
| `excludeCompanyHeadquarterLocations` | array | No | Exclude people whose current company is headquartered in any of these locations. |
| `excludeCurrentCompanies` | array | No | Exclude people who currently work at any of these companies, by name. |
| `excludeCurrentJobTitles` | array | No | Exclude people whose current job title matches any of these. |
| `excludeFunctionIds` | array | No | Exclude these job functions (same codes as functionIds). |
| `excludeLocations` | array | No | Exclude people in any of these locations, by place name. |
| `excludePastCompanies` | array | No | Exclude people who previously worked at any of these companies, by name. |
| `excludePastJobTitles` | array | No | Exclude people who held any of these past job titles. |
| `excludeSchools` | array | No | Exclude people who attended any of these schools, by name. |
| `excludeSeniorityLevelIds` | array | No | Exclude these seniority levels (same codes as seniorityLevelIds). |
| `firstNames` | array | No | Filter to people whose first name matches any of these. |
| `functionIds` | array | No | Filter by job function. Codes: 1=Accounting, 2=Administrative, 3=Arts and Design, 4=Business Development, 5=Community and Social Services, 6=Consulting, 7=Education, 8=Engineering, 9=Entrepreneurship, 10=Finance, 11=Heal |
| `jobTitle` | string | No | Optional current job title filter (e.g. 'Software Engineer'). |
| `lastNames` | array | No | Filter to people whose last name matches any of these. |
| `limit` | integer | No | Maximum number of full profiles to return (1-25, default 10). You are billed per profile returned, so a lower limit costs less. |
| `location` | string | No | Optional location filter (e.g. 'San Francisco'). |
| `pastCompanies` | array | No | Filter to people who previously worked at any of these companies, by name. |
| `pastJobTitles` | array | No | Filter by a past job title the person held (e.g. ['Product Manager']). |
| `profileLanguages` | array | No | Filter by the profile's primary language. |
| `recentlyChangedJobs` | boolean | No | When true, only return people who recently changed jobs (a strong sales/recruiting signal). |
| `recentlyPostedOnLinkedIn` | boolean | No | When true, only return people who recently posted on LinkedIn (an activity signal). |
| `schools` | array | No | Filter to people who attended any of these schools, by name. |
| `seniorityLevelIds` | array | No | Filter by seniority level. Codes: 100=In Training, 110=Entry Level, 120=Senior, 130=Strategic, 200=Entry Level Manager, 210=Experienced Manager, 220=Director, 300=Vice President, 310=CXO, 320=Owner/Partner. |
| `yearsAtCurrentCompanyIds` | array | No | Filter by tenure at the current company. Codes: 1=Less than 1 year, 2=1 to 2 years, 3=3 to 5 years, 4=6 to 10 years, 5=More than 10 years. |
| `yearsOfExperienceIds` | array | No | Filter by total years of experience. Codes: 1=Less than 1 year, 2=1 to 2 years, 3=3 to 5 years, 4=6 to 10 years, 5=More than 10 years. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "about": "Software engineer focused on Gemini AI agent security and safety. Experience in …",
        "city": "San Francisco",
        "connectionsCount": 773,
        "country": "United States",
        "countryCode": "US",
        "coverImage": "https://media.licdn.com/dms/image/v2/D5616AQF4qWL-k2s3EA/profile-displaybackgrou…",
        "creator": false,
        "currentPosition": [
          {
            "companyId": "1594050",
            "companyLinkedinUrl": "https://www.linkedin.com/company/googledeepmind/",
            "companyLogo": {
              "sizes": [
                {
                  "height": 400,
                  "url": "https://media.licdn.com/dms/image/v2/D4E0BAQEntrYwxPlbQA/company-logo_400_400/co…",
                  "width": 400
                }
              ],
              "url": "https://media.licdn.com/dms/image/v2/D4E0BAQEntrYwxPlbQA/company-logo_400_400/co…"
            },
            "companyName": "Google DeepMind",
            "companyUniversalName": "googledeepmind",
            "description": "- Building systems for agentic AI security for the latest Gemini models, includi…",
            "duration": "5 mos",
            "employmentType": "Full-time"
          }
        ],
        "education": [
          {
            "degree": "BS",
            "description": "Selected Coursework:\nCS 61A: Structure and Interpretation of Computer Programs\nC…",
            "endDate": {
              "month": "Dec",
              "text": "Dec 2020",
              "year": 2020
            },
            "fieldOfStudy": "Electrical Engineering and Computer Science",
            "insights": null,
            "period": "Aug 2017 - Dec 2020",
            "schoolId": "2517",
            "schoolLinkedinUrl": "https://www.linkedin.com/company/2517/"
          }
        ],
        "experience": [
          {
            "companyId": "1594050",
            "companyLinkedinUrl": "https://www.linkedin.com/company/googledeepmind/",
            "companyLogo": {
              "sizes": [
                {
                  "height": 400,
                  "url": "https://media.licdn.com/dms/image/v2/D4E0BAQEntrYwxPlbQA/company-logo_400_400/co…",
                  "width": 400
                }
              ],
              "url": "https://media.licdn.com/dms/image/v2/D4E0BAQEntrYwxPlbQA/company-logo_400_400/co…"
            },
            "companyName": "Google DeepMind",
            "companyUniversalName": "googledeepmind",
            "description": "- Building systems for agentic AI security for the latest Gemini models, includi…",
            "duration": "5 mos",
            "employmentType": "Full-time"
          }
        ],
        "firstName": "Rahul",
        "followerCount": 790
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].url / data.items[].handle` | The LinkedIn profile URL and the handle at the end of it, for example `rahulrathi123`. |
| `data.items[].id` | The LinkedIn member id of the profile, in a form like `ACoAABALO9MBdW_ZVdXWockmbgrIFGDCWGhX-WE`. |
| `data.items[].firstName / data.items[].lastName` | The person's first and last name. |
| `data.items[].headline` | The headline text shown under the person's name, such as a job title and employer. |
| `data.items[].location / data.items[].city / data.items[].state / data.items[].country / data.items[].countryCode` | Where the person is based. `location` is the area text shown on the profile. The other fields split it into city, state, country, and country code. |
| `data.items[].currentPosition[]` | The person's current job or jobs. Each row has `companyName`, `companyUniversalName`, `companyLinkedinUrl`, `description`, `duration`, and `employmentType`. |
| `data.items[].experience[]` | The work history. Each row has the same fields as `currentPosition[]`, for example `companyName`, `duration`, and `description`. |
| `data.items[].education[]` | Schools the person attended. Each row has `degree`, `fieldOfStudy`, `period`, `endDate`, `schoolId`, and `schoolLinkedinUrl`. |
| `data.items[].skills[].name` | The name of each skill listed on the profile. |
| `data.items[].connectionsCount / data.items[].followerCount` | The number of connections and the number of followers on the profile. |

### Notes

- Set `limit` between 1 and 25 to control how many profiles come back. The default is 10.
- Use `companyUniversalName` and `companyId` from `currentPosition[]` and `experience[]` to identify companies in other LinkedIn APIs, such as [LinkedIn Company](/apis/linkedin/company).
- For a lighter search that returns only name, headline, and URL, use [LinkedIn Profile Search (basic)](/apis/linkedin/search-profiles-thin).
- To read the posts of a person you found, pass the profile URL to [LinkedIn Profile Posts (full)](/apis/linkedin/profile-posts-full).

### Pricing

Billed at the actual cost of each call, about $0.198 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/search-profiles.json`](../../../catalog/models/linkedin/search-profiles.json) · Store page: https://www.sandbase.ai/model/linkedin/search-profiles
