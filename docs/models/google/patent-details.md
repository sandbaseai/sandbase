# Google Patent Details API: pricing, parameters and code examples

`google/patent-details` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get a Google Patents record by patent ID with title, abstract, claims, inventors, assignees, dates, classifications, citations and family members.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/patent-details", "patent_id": "patent/US11734097B1/en"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/patent-details', {'patent_id': 'patent/US11734097B1/en'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/patent-details", {
  "patent_id": "patent/US11734097B1/en"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/patent-details", sandbase.Params{
	"patent_id": "patent/US11734097B1/en",
})
```

Same call via the path form: `POST /v1/api/google/patent-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `patent_id` | string | yes | Parameter defines the ID of the patent you want to retrieve. You can get it from the results of our Google Patents API. It can be: - A patent ID: `patent/<publication number>/<two-letter country code>`, the country…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get a Google Patents record by patent ID with title, abstract, claims, inventors, assignees, dates, classifications, citations and family members.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/patent-details" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"patent_id": "patent/US11734097B1/en"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `patent_id` | string | Yes | Parameter defines the ID of the patent you want to retrieve. You can get it from the results of our Google Patents API. It can be: - A patent ID: `patent/<publication number>/<two-letter country code>`, the country code can be omitted (e.g. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/patent-details.json`](../../../catalog/models/google/patent-details.json) · Store page: https://www.sandbase.ai/model/google/patent-details
