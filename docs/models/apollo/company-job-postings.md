# Apollo Organization Job Postings API: pricing, parameters and code examples

`apollo/company-job-postings` · data API · Apollo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01975 per call · **Modes:** sync

Live job postings for one company, by Apollo organization id. Each posting carries its title, location, posted date and source URL. Useful as a hiring signal — which functions a company is expanding, and where.

## Pricing

- **$0.01975 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apollo/company-job-postings", "organization_id": "5d0a0fbff6512580bf33a120"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apollo/company-job-postings', {'organization_id': '5d0a0fbff6512580bf33a120'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apollo/company-job-postings", {
  "organization_id": "5d0a0fbff6512580bf33a120"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apollo/company-job-postings", sandbase.Params{
	"organization_id": "5d0a0fbff6512580bf33a120",
})
```

Same call via the path form: `POST /v1/api/apollo/company-job-postings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable and improve the performance of the endpoint. Example: 4  |
| `per_page` | integer |  | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page parameter to search the different pages of data. Example: 10  |
| `organization_id` | string | yes | The organization ID of the company for which you want to find job postings. Each company in the Apollo database is assigned a unique ID. To find IDs, call the Organization Search endpoint and identify the values for…  |

## Details

Live job postings for one company, by Apollo organization id. Each posting carries its title, location, posted date and source URL. Useful as a hiring signal — which functions a company is expanding, and where.

The response is the official Apollo API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/company-job-postings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"organization_id": "5d0a0fbff6512580bf33a120"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `organization_id` | string | Yes | The organization ID of the company for which you want to find job postings. Each company in the Apollo database is assigned a unique ID. To find IDs, call the O |
| `page` | integer | No | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable |
| `per_page` | integer | No | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page pa |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apollo/company-job-postings.json`](../../../catalog/models/apollo/company-job-postings.json) · Store page: https://www.sandbase.ai/model/apollo/company-job-postings
