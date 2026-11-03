# Wellfound Job Autocomplete Roles API: pricing, parameters and code examples

`wellfound/job-autocomplete-roles` · data API · Wellfound · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Get a list of common job role slugs available on Wellfound. These slugs can be used to construct Wellfound role search URLs.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wellfound/job-autocomplete-roles"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wellfound/job-autocomplete-roles', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wellfound/job-autocomplete-roles", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wellfound/job-autocomplete-roles", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/wellfound/job-autocomplete-roles` with the body above minus `model`.

## Details

This API returns a list of common job roles on Wellfound. Each role has a display name and a URL slug. It takes no input.

### Use cases

- Build a role dropdown in a job search tool using the `name` values.
- Construct Wellfound role search URLs by inserting a `slug` into the URL.
- Check which role names Wellfound uses before you map your own job titles to them.
- Seed a list of roles to track across several job searches.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wellfound/job-autocomplete-roles" \
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
    "roles": [
      {
        "name": "Software Engineer",
        "slug": "software-engineer"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.roles[]` | List of common job roles available on Wellfound. |
| `data.roles[].name` | Display name of the role, for example `Software Engineer`. |
| `data.roles[].slug` | URL-friendly identifier for the role, for example `software-engineer`. Use it to build Wellfound role search URLs. |
| `status` | Result of the call. The sample shows `success`. |

### Notes

- Send an empty JSON body `{}`. The API has no parameters, so it has no pagination or filters.
- Slugs are lowercase and use hyphens between words, such as `backend-engineer`.
- To see jobs and companies on Wellfound, try [Wellfound Trending Jobs](/apis/wellfound/trending-jobs) or [Wellfound Company Jobs](/apis/wellfound/company-jobs).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/wellfound/job-autocomplete-roles.json`](../../../catalog/models/wellfound/job-autocomplete-roles.json) · Store page: https://www.sandbase.ai/model/wellfound/job-autocomplete-roles
