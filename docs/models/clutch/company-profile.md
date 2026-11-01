# Clutch Company Profile

`clutch/company-profile` · api · Clutch

Get detailed profile of a company by its slug. Returns company name, rating, tagline, key details (project size, hourly rate, employees, year founded), website URL, and service line breakdown with percentages.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "clutch/company-profile", "slug": "simform"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('clutch/company-profile', {'slug': 'simform'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("clutch/company-profile", {
  "slug": "simform"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "clutch/company-profile", sandbase.Params{
	"slug": "simform",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/clutch/company-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | Company profile slug from search_companies results (e.g. 'simform').  |

## Details

Get detailed profile of a company by its slug. Returns company name, rating, tagline, key details (project size, hourly rate, employees, year founded), website URL, and service line breakdown with percentages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/clutch/company-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "simform"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Company profile slug from search_companies results (e.g. 'simform'). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/clutch/company-profile.json`](../../../catalog/models/clutch/company-profile.json) · Store page: https://www.sandbase.ai/model/clutch/company-profile
