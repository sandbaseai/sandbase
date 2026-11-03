# Levels.fyi Popular Companies API: pricing, parameters and code examples

`levels-fyi/popular-companies` · data API · Levels.fyi · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retrieve a list of popular companies from the Levels.fyi directory with their slugs and salary page URLs. Returns approximately 24 top companies.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "levels-fyi/popular-companies"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('levels-fyi/popular-companies', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("levels-fyi/popular-companies", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "levels-fyi/popular-companies", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/levels-fyi/popular-companies` with the body above minus `model`.

## Details

Returns a list of popular companies from the Levels.fyi directory, about 24 in total. Each entry has a company slug, a display name, and a relative salary page URL. The API takes no input.

### Use cases

- Build a company picker or autocomplete list for a salary comparison tool.
- Collect valid company slugs to feed into other Levels.fyi calls.
- Link users straight to the salary page of a well-known employer.
- Seed a tracking list of top tech employers for regular salary checks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/levels-fyi/popular-companies" \
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
    "popular_companies": [
      {
        "slug": "google",
        "url": "/companies/google/salaries",
        "value": "Google"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.popular_companies[]` | One popular company in the directory. The list holds about 24 entries. |
| `data.popular_companies[].slug` | Short lowercase identifier for the company, such as `google`. Use it as the company identifier in other Levels.fyi calls. |
| `data.popular_companies[].value` | Display name of the company, such as `Google`. |
| `data.popular_companies[].url` | Relative path to the company salary page on Levels.fyi, such as `/companies/google/salaries`. |
| `status` | Result status of the call. The value is `success` when the list was returned. |

### Notes

- The `url` value is a relative path. Add the Levels.fyi site origin to open the page in a browser.
- Use `slug` as the company identifier when you call [Levels.fyi Company Overview](/apis/levels-fyi/company-overview) or [Levels.fyi Company Benefits](/apis/levels-fyi/company-benefits).
- The request has no parameters, so there is no pagination. Send an empty JSON object `{}`.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/levels-fyi/popular-companies.json`](../../../catalog/models/levels-fyi/popular-companies.json) · Store page: https://www.sandbase.ai/model/levels-fyi/popular-companies
