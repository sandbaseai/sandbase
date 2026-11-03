# Web3.career Web3 Salaries API: pricing, parameters and code examples

`web3-career/web3-salaries` · data API · Web3.career · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Fetch average salaries for various Web3 roles. Returns a list of roles with their average salary and a link to the role's detail page.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "web3-career/web3-salaries"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('web3-career/web3-salaries', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("web3-career/web3-salaries", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "web3-career/web3-salaries", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/web3-career/web3-salaries` with the body above minus `model`.

## Details

Returns a list of Web3 job roles from Web3.career, each with an average salary and a link to the role's detail page. The API takes no input, so you send an empty JSON object.

### Use cases

- Compare average pay across Web3 roles such as Unity Developer and Flutter Developer.
- Build a salary table for a Web3 hiring guide or career site.
- Check a role's average salary before you set a pay range for a job offer.
- Collect role names and detail page links to feed a crawler or a content pipeline.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/web3-career/web3-salaries" \
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
    "salaries": [
      {
        "average_salary": "$130k",
        "role": "Unity Developer",
        "url": "https://web3.career/web3-salaries/unity-developer"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.salaries[]` | One entry per Web3 role in the list. |
| `data.salaries[].role` | Name of the job role, for example `Unity Developer`. |
| `data.salaries[].average_salary` | Average salary for the role as a short text string, for example `$130k`. It includes a dollar sign and a `k` suffix, so parse it before you do math. |
| `data.salaries[].url` | Link to the Web3.career salary page for that role. |
| `status` | Shows `success` when the call worked. |

### Notes

- The API has no parameters. Send `{}` as the request body.
- `average_salary` is a string, not a number. Strip the `$` and convert `k` to thousands if you need a numeric value.
- To look at open positions, call [Web3.career Job Listings](/apis/web3-career/job-listings) or [Web3.career Search Jobs](/apis/web3-career/search-jobs).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/web3-career/web3-salaries.json`](../../../catalog/models/web3-career/web3-salaries.json) · Store page: https://www.sandbase.ai/model/web3-career/web3-salaries
