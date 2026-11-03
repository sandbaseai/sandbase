# Levels.fyi Salary Summary Md API: pricing, parameters and code examples

`levels-fyi/salary-summary-md` · data API · Levels.fyi · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retrieve an aggregate salary summary in Markdown format for a given company and optional job family. Includes median compensation, level breakdowns by job family, and attribution information.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "levels-fyi/salary-summary-md", "company_slug": "stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('levels-fyi/salary-summary-md', {'company_slug': 'stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("levels-fyi/salary-summary-md", {
  "company_slug": "stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "levels-fyi/salary-summary-md", sandbase.Params{
	"company_slug": "stripe",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/levels-fyi/salary-summary-md` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `company_slug` | string | yes | Company slug identifier (e.g. 'google', 'meta', 'amazon'). Obtain from get_popular_companies.  |
| `job_family_slug` | string |  | Job family slug (e.g. 'software-engineer', 'product-manager', 'data-scientist'). Omitting returns an overall company salary summary across all roles.  |

## Details

Returns a salary summary for one company on Levels.fyi as a single Markdown document. It needs a `company_slug` and accepts an optional `job_family_slug` to narrow the summary to one role.

### Use cases

- Drop the Markdown straight into an LLM prompt to answer pay questions about a specific company.
- Render a company pay summary page in an internal tool without building a table layout.
- Compare the overall pay summary for a company with the summary for one job family such as `software-engineer`.
- Archive a text snapshot of a company's pay data for offer research notes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/levels-fyi/salary-summary-md" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"company_slug": "stripe"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `company_slug` | string | Yes | Company slug identifier (e.g. 'google', 'meta', 'amazon'). Obtain from get_popular_companies. |
| `job_family_slug` | string | No | Job family slug (e.g. 'software-engineer', 'product-manager', 'data-scientist'). Omitting returns an overall company salary summary across all roles. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "markdown": "# Levels.fyi – Stripe Salaries\n\n> AI agents: this is one page of Levels.fyi pay …"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `status` | Shows `success` when the call worked. |
| `data.markdown` | The full salary summary as one Markdown string. It starts with a title such as `Levels.fyi – Stripe Salaries` and is followed by the pay content for the company. Parse the headings and tables in it to pull out specific figures. |

### Notes

- Get valid `company_slug` values from [Levels.fyi Popular Companies](/apis/levels-fyi/popular-companies).
- Get valid `job_family_slug` values from [Levels.fyi Job Families](/apis/levels-fyi/job-families). Leave it out to get the summary across all roles.
- The result is one Markdown string, not structured JSON. Use [Levels.fyi Company Overview](/apis/levels-fyi/company-overview) if you need separate fields.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/levels-fyi/salary-summary-md.json`](../../../catalog/models/levels-fyi/salary-summary-md.json) · Store page: https://www.sandbase.ai/model/levels-fyi/salary-summary-md
