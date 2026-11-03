# Built In Suggest Job Titles API: pricing, parameters and code examples

`builtin/suggest-job-titles` · data API · Built In · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns up to 10 autocomplete suggestions for job title searches, matching the query prefix against Built In's job title index. Useful for building type-ahead search interfaces.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "builtin/suggest-job-titles", "query": "software engineer"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('builtin/suggest-job-titles', {'query': 'software engineer'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("builtin/suggest-job-titles", {
  "query": "software engineer"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "builtin/suggest-job-titles", sandbase.Params{
	"query": "software engineer",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/builtin/suggest-job-titles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Partial job title prefix to get suggestions for  |

## Details

Returns up to 10 autocomplete suggestions for job titles on Built In. It needs one input, `query`, a partial job title prefix such as `software engineer`.

### Use cases

- Power a type-ahead job title box in a job search form.
- Normalize free-text job titles typed by users into titles that exist on Built In.
- Build a list of related title variants to use as keywords in a job board crawler.
- Check which title wording is common for a role before writing a job post.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/builtin/suggest-job-titles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "software engineer"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Partial job title prefix to get suggestions for |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "suggestions": [
      "Software Engineering"
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `status` | Result of the call. The value `success` means the request worked. |
| `data.suggestions[]` | Suggested job titles that match the `query` prefix. Each item is a plain string, such as `Junior Software Engineer`. |

### Notes

- The API takes no pagination parameter. It returns one list of suggestions per call.
- Send a short prefix in `query`. The response in this example includes titles with extra words before or after the prefix, such as `Junior Software Engineer` and `Software Engineering Manager`.
- The call runs asynchronously. Poll `GET /v1/run/{id}` and read the result from `outputs[0].data`.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/builtin/suggest-job-titles.json`](../../../catalog/models/builtin/suggest-job-titles.json) · Store page: https://www.sandbase.ai/model/builtin/suggest-job-titles
