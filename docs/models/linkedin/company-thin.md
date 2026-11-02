# LinkedIn Company (basic) API: pricing, parameters and code examples

`linkedin/company-thin` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.001 per call · **Modes:** sync

Basic company: name, description, employee count, industry, logo, website, tagline. No follower count, founded year, office locations, or funding data - for those use linkedin.company.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.001**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/company-thin", "url": "https://www.linkedin.com/company/stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/company-thin', {'url': 'https://www.linkedin.com/company/stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/company-thin", {
  "url": "https://www.linkedin.com/company/stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/company-thin", sandbase.Params{
	"url": "https://www.linkedin.com/company/stripe",
})
```

Same call via the path form: `POST /v1/api/linkedin/company-thin` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full LinkedIn company page URL.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `companyType` or `coverImage`, and it is served only by a source…  |

## Details

Basic company: name, description, employee count, industry, logo, website, tagline. No follower count, founded year, office locations, or funding data - for those use linkedin.company.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/company-thin" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/company/stripe"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full LinkedIn company page URL. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `companyType` or `coverImage`, and it is served only by a source that  |

### Pricing

Billed at the actual cost of each call, usually $0.001 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/company-thin.json`](../../../catalog/models/linkedin/company-thin.json) · Store page: https://www.sandbase.ai/model/linkedin/company-thin
