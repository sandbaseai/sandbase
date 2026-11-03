# Apollo People Enrichment API: pricing, parameters and code examples

`apollo/people-match` · data API · Apollo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01975 per call · **Modes:** sync

Enrich one person: give whatever identifiers you have and get back Apollo's full record for them. Send identifiers in the JSON request body, not the query string.

## Pricing

- **$0.01975 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apollo/people-match"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apollo/people-match', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apollo/people-match", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apollo/people-match", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/apollo/people-match` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string |  | The Apollo ID for the person. Each person in the Apollo database is assigned a unique ID. To find IDs, call the People API Search endpoint and identify the values for person_id. Example: 587cf802f65125cad923a266  |
| `name` | string |  | The full name of the person. This will typically be a first name and last name separated by a space. If you use this parameter, you do not need to use the first_name and last_name parameters. Example: tim zheng  |
| `email` | string |  | The email address of the person. Example: example@email.com  |
| `domain` | string |  | The domain name for the person's employer. This can be the current employer or a previous employer. Do not include www., the @ symbol, or similar. Example: apollo.io or microsoft.com  |
| `last_name` | string |  | The last name of the person. This is typically used in combination with the first_name parameter. Example: zheng  |
| `first_name` | string |  | The first name of the person. This is typically used in combination with the last_name parameter. Example: tim  |
| `hashed_email` | string |  | The hashed email of the person. The email should adhere to either the MD5 or SHA-256 hash format. Example: 8d935115b9ff4489f2d1f9249503cadf (MD5) or 97817c0c49994eb500ad0a5e7e2d8aed51977b26424d508f66e4e8887746a152…  |
| `linkedin_url` | string |  | The URL for the person's LinkedIn profile. Example: http://www.linkedin.com/in/tim-zheng-677ba010  |
| `organization_name` | string |  | The name of the person's employer. This can be the current employer or a previous employer. Example: apollo  |

## Details

Returns the Apollo record for one person, including contact details, job title, employment history and a nested record for their current employer. Send at least one identifier in the JSON body, such as `email`, `linkedin_url`, `id`, or `first_name` and `last_name` with `domain`.

### Use cases

- Fill in a work email, title and LinkedIn URL for a lead when you only have a name and a company domain.
- Check a contact's seniority and department before routing them to the right sales team.
- Pull a person's past and current roles to see their career path before outreach.
- Add employer details such as headcount, revenue and tech stack to a contact record in your CRM.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/people-match" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"first_name": "Patrick", "last_name": "Collison", "domain": "stripe.com"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | No | The domain name for the person's employer. This can be the current employer or a previous employer. Do not include www., the @ symbol, or similar. Example: apollo.io or microsoft.com |
| `email` | string | No | The email address of the person. Example: example@email.com |
| `first_name` | string | No | The first name of the person. This is typically used in combination with the last_name parameter. Example: tim |
| `hashed_email` | string | No | The hashed email of the person. The email should adhere to either the MD5 or SHA-256 hash format. Example: 8d935115b9ff4489f2d1f9249503cadf (MD5) or 97817c0c49994eb500ad0a5e7e2d8aed51977b26424d508f66e4e8887746a152 (SHA-2 |
| `id` | string | No | The Apollo ID for the person. Each person in the Apollo database is assigned a unique ID. To find IDs, call the People API Search endpoint and identify the values for person_id. Example: 587cf802f65125cad923a266 |
| `last_name` | string | No | The last name of the person. This is typically used in combination with the first_name parameter. Example: zheng |
| `linkedin_url` | string | No | The URL for the person's LinkedIn profile. Example: http://www.linkedin.com/in/tim-zheng-677ba010 |
| `name` | string | No | The full name of the person. This will typically be a first name and last name separated by a space. If you use this parameter, you do not need to use the first_name and last_name parameters. Example: tim zheng |
| `organization_name` | string | No | The name of the person's employer. This can be the current employer or a previous employer. Example: apollo |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "person": {
    "city": "San Francisco",
    "country": "United States",
    "departments": [
      "c_suite"
    ],
    "directory_url": null,
    "email": "patrick@stripe.com",
    "email_domain_catchall": true,
    "email_domain_catchall_verdict": "allow",
    "email_status": "verified",
    "employment_history": [
      {
        "_id": "6ae89c0c86ceb70001d44e2f",
        "created_at": null,
        "current": true,
        "degree": null,
        "description": null,
        "emails": null,
        "end_date": null,
        "grade_level": null,
        "id": "6ae89c0c86ceb70001d44e2f",
        "key": "6ae89c0c86ceb70001d44e2f",
        "kind": null,
        "major": null
      }
    ],
    "extrapolated_email_confidence": null,
    "facebook_url": null,
    "first_name": "Patrick"
  },
  "request_id": -9198851976104810262,
  "request_id_str": "-9198851976104810262"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `person.name / person.first_name / person.last_name` | The person's full name and its parts. |
| `person.email / person.email_status` | The email address found for the person and its status. In the example, `email_status` is `verified`. |
| `person.match_confidence / person.result` | How well the request matched a record. The example returns `high` and `Matched`. |
| `person.title / person.headline / person.seniority` | The person's current job title, profile headline and seniority level, such as `founder`. |
| `person.departments / person.subdepartments / person.functions` | Lists that place the person in a department and function inside their company. |
| `person.employment_history[]` | Past and current roles. Each row has `organization_name`, `title`, `start_date`, `end_date` and a `current` flag. |
| `person.linkedin_url / person.photo_url` | Links to the person's LinkedIn profile and profile photo. |
| `person.city / person.state / person.country / person.time_zone` | The person's location and time zone. |
| `person.organization.name / person.organization.estimated_num_employees / person.organization.annual_revenue` | The current employer's name, estimated headcount and annual revenue as a number. |
| `person.organization.funding_events[] / person.organization.current_technologies[]` | Funding rounds with `date`, `type` and `amount`, and the technologies the employer uses, each with `name` and `category`. |

### Notes

- Send parameters in the JSON body of a POST request, not in the query string.
- To get the `id` for a person, call [Apollo People API Search](/apis/apollo/people-search) and use the person ID from its results.
- `person.id` and `person.organization_id` are Apollo IDs. Dates in `employment_history[]` use the `YYYY-MM-DD` format.
- To get more detail on the employer, call [Apollo Organization Enrichment](/apis/apollo/company-enrich) with the company domain.

### Pricing

$0.01975 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apollo/people-match.json`](../../../catalog/models/apollo/people-match.json) · Store page: https://www.sandbase.ai/model/apollo/people-match
