# Web3.career Intelligence Report API: pricing, parameters and code examples

`web3-career/intelligence-report` · data API · Web3.career · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Fetch the Web3 Career Intelligence Report content and statistics. Returns the report title, full text content, key statistical findings, and a link to the embedded Google Slides presentation.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "web3-career/intelligence-report"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('web3-career/intelligence-report', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("web3-career/intelligence-report", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "web3-career/intelligence-report", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/web3-career/intelligence-report` with the body above minus `model`.

## Details

Returns the Web3.career Intelligence Report as structured data. It includes the report title, the report text, a list of highlighted statistics, and the URL of the embedded Google Slides deck. The call needs no input.

### Use cases

- Pull the report's headline statistics into a dashboard or newsletter about the Web3 job market.
- Quote the report text in a research summary on remote work or AI skills in Web3 hiring.
- Embed the Google Slides deck in an internal page using `data.google_slides_url`.
- Compare the report's claims on remote jobs with live listings from a jobs API.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/web3-career/intelligence-report" \
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
    "content": "We've just released our Web3 Career Intelligence Report. It shares insights on k…",
    "google_slides_url": "https://docs.google.com/presentation/d/e/2PACX-1vSNy41c0KsQvpywoIXHHkxM8ZzuYnUcf…",
    "highlighted_stats": [
      "2025 has seen a 50% reduction in remote jobs year-over-year. This isn't a tempor…"
    ],
    "title": "Web3.Career Intelligence Report (2025)"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.title` | Title of the report, including the year. |
| `data.content` | Text of the report. It introduces the main trends the report covers, such as geographic salary arbitrage. |
| `data.highlighted_stats[]` | List of key findings, each as a text string. Examples include the change in remote jobs and the share of job descriptions that require AI workflows. |
| `data.google_slides_url` | Embed URL of the Google Slides presentation that goes with the report. |
| `status` | Shows `success` when the report was fetched. |

### Notes

- The request takes no parameters. Send an empty JSON object `{}`.
- The `highlighted_stats[]` items are plain sentences, not numbers. Parse the figures from the text if you need them as values.
- To check the report's remote work claims against current postings, call [Web3.career Remote Jobs](/apis/web3-career/remote-jobs).
- For pay data on specific roles, call [Web3.career Web3 Salaries](/apis/web3-career/web3-salaries).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/web3-career/intelligence-report.json`](../../../catalog/models/web3-career/intelligence-report.json) · Store page: https://www.sandbase.ai/model/web3-career/intelligence-report
