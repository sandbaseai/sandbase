# Glassdoor Companies API: pricing, parameters and code examples

`glassdoor/companies` · data API · Glassdoor · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search companies on Glassdoor by name and get company ID, rating, review and salary counts, size, industry and headquarters.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "glassdoor/companies"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('glassdoor/companies', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("glassdoor/companies", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "glassdoor/companies", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/glassdoor/companies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Parameter defines the name of the company to search for, like the company search box of Glassdoor (e.g., `Google` or `bank`). Without it, Glassdoor lists the companies with the most reviews.  |
| `page` | string |  | Parameter defines the page number of the results (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, etc.). Each page has up to `10` companies.  |
| `location` | string |  | Parameter defines the location of the companies' offices: a city, state or country (e.g., `New York, NY`, `Texas`, or `Germany`). We use the first location Glassdoor suggests with that name, or else its first…  |
| `min_rating` | string |  | Parameter defines the minimum overall Glassdoor rating of the companies, from `1` to `4` (e.g., `4` for companies rated 4.0 and up).  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search companies on Glassdoor by name and get company ID, rating, review and salary counts, size, industry and headquarters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/glassdoor/companies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "nvidia"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | No | Parameter defines the name of the company to search for, like the company search box of Glassdoor (e.g., `Google` or `bank`). Without it, Glassdoor lists the companies with the most reviews. |
| `location` | string | No | Parameter defines the location of the companies' offices: a city, state or country (e.g., `New York, NY`, `Texas`, or `Germany`). We use the first location Glassdoor suggests with that name, or else its first suggestion. Like on Glassdoor,  |
| `min_rating` | string | No | Parameter defines the minimum overall Glassdoor rating of the companies, from `1` to `4` (e.g., `4` for companies rated 4.0 and up). |
| `page` | string | No | Parameter defines the page number of the results (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, etc.). Each page has up to `10` companies. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/glassdoor/companies.json`](../../../catalog/models/glassdoor/companies.json) · Store page: https://www.sandbase.ai/model/glassdoor/companies
