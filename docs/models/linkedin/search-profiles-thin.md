# LinkedIn Profile Search (basic) API: pricing, parameters and code examples

`linkedin/search-profiles-thin` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.036 per call · **Modes:** sync

Cheap people search: name/handle, headline, VANITY profile URL, location. No full profile or email - for full profiles per hit use linkedin.search_profiles, add emails with linkedin.search_profiles_email.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.036**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/search-profiles-thin", "query": "recruiter"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/search-profiles-thin', {'query': 'recruiter'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/search-profiles-thin", {
  "query": "recruiter"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/search-profiles-thin", sandbase.Params{
	"query": "recruiter",
})
```

Same call via the path form: `POST /v1/api/linkedin/search-profiles-thin` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query for LinkedIn profiles - a role, name, or keywords (e.g. 'Marketing Manager').  |
| `title` | string |  | Filter by job title or headline (e.g. Head of Talent).  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; a page holds 10 profiles.  |
| `lastName` | string |  | Filter by last name (e.g. Okafor).  |
| `schoolId` | string |  | Filter by school, using a LinkedIn school id.  |
| `firstName` | string |  | Filter by first name (e.g. Jane).  |
| `industryId` | string |  | Filter by industry, using a LinkedIn industry id.  |
| `locationId` | string |  | Filter by location, using a LinkedIn geocode id.  |
| `followerOfUrn` | string |  | Return only people who follow this member, given the member's LinkedIn URN.  |
| `pastCompanyId` | string |  | Filter by a previous employer, using a numeric LinkedIn company id.  |
| `profileLanguage` | string |  | Filter by the language the profile is written in (ISO 2-letter code, e.g. en).  |
| `currentCompanyId` | string |  | Filter by current employer, using a numeric LinkedIn company id. Comma-separate for several.  |
| `serviceCategoryId` | string |  | Filter by service category, using a numeric service-category id.  |

## Details

Searches LinkedIn people by keyword and returns a short card for each match: name, headline, location, and profile URL. It needs a `query` such as a role, name, or keywords, and you can narrow results with filters like `title`, `locationId`, or `currentCompanyId`.

### Use cases

- Build a list of recruiters in one region by searching `recruiter` with a `locationId` filter.
- Find the profile URL of a person when you only know their name and job title.
- Collect candidate profiles at a target employer using `currentCompanyId`, then pass them to a full profile lookup.
- Check which profiles in a search are marked `premium` or `verified`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/search-profiles-thin" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "recruiter"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query for LinkedIn profiles - a role, name, or keywords (e.g. 'Marketing Manager'). |
| `currentCompanyId` | string | No | Filter by current employer, using a numeric LinkedIn company id. Comma-separate for several. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; a page holds 10 profiles. |
| `firstName` | string | No | Filter by first name (e.g. Jane). |
| `followerOfUrn` | string | No | Return only people who follow this member, given the member's LinkedIn URN. |
| `industryId` | string | No | Filter by industry, using a LinkedIn industry id. |
| `lastName` | string | No | Filter by last name (e.g. Okafor). |
| `locationId` | string | No | Filter by location, using a LinkedIn geocode id. |
| `pastCompanyId` | string | No | Filter by a previous employer, using a numeric LinkedIn company id. |
| `profileLanguage` | string | No | Filter by the language the profile is written in (ISO 2-letter code, e.g. en). |
| `schoolId` | string | No | Filter by school, using a LinkedIn school id. |
| `serviceCategoryId` | string | No | Filter by service category, using a numeric service-category id. |
| `title` | string | No | Filter by job title or headline (e.g. Head of Talent). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "handle": "linkedwithruby",
        "headline": "A Technical Recruiter That Doesn’t Suck | Sardonic & Security | I used the spark…",
        "id": "ACoAAB1QQOgBnODVSz6xioyOGmm8jw8iY8A8o-Y",
        "image": "https://media.licdn.com/dms/image/v2/D5603AQEB2rD3RM2HRg/profile-displayphoto-sc…",
        "location": "Los Angeles Metropolitan Area",
        "name": "✨Ruby Murphy✨",
        "premium": true,
        "url": "https://www.linkedin.com/in/linkedwithruby",
        "verified": false
      }
    ],
    "nextCursor": "cur_eapzt1SXZH784D2SuVfdqA"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].name` | Display name of the person as shown on their profile. It can include emojis. |
| `data.items[].headline` | Headline text under the person's name. |
| `data.items[].location` | Location text shown on the profile, such as a metro area or country. |
| `data.items[].handle` | Vanity handle of the profile. It is the last part of the profile URL. |
| `data.items[].url` | Full LinkedIn profile URL built from the handle. |
| `data.items[].id` | LinkedIn member ID string for the person. It starts with `ACo`. |
| `data.items[].image` | URL of the profile photo. It is an empty string when the profile has no photo in the result. |
| `data.items[].premium / data.items[].verified` | Boolean flags for whether the profile shows a Premium badge and a verified badge. |
| `data.nextCursor` | Cursor string for the next page of results. |
| `found` | `true` when the search returned results. |

### Notes

- Each page holds 10 profiles. Pass `data.nextCursor` as `cursor` in the next request to get the next page, and omit `cursor` for the first page.
- Filters that take IDs, such as `locationId`, `industryId`, `schoolId`, and `currentCompanyId`, need LinkedIn ID values, not names. `currentCompanyId` accepts several comma-separated IDs.
- This API returns no full profile data and no emails. For full profile details call [LinkedIn Profile Search](/apis/linkedin/search-profiles) or [LinkedIn User Profile](/apis/linkedin/user-detail).
- Use `data.items[].handle` or `data.items[].url` to identify each person in follow-up calls.

### Pricing

Billed at the actual cost of each call, about $0.036 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/search-profiles-thin.json`](../../../catalog/models/linkedin/search-profiles-thin.json) · Store page: https://www.sandbase.ai/model/linkedin/search-profiles-thin
