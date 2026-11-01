# LinkedIn Company

`linkedin/company` · api · LinkedIn

Fetch a full LinkedIn company page by URL: name, description, industry, employee count and range, follower count, founded year, headquarters and office locations, funding data, tagline, logo, website, and specialities.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/company", "url": "https://www.linkedin.com/company/stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/company', {'url': 'https://www.linkedin.com/company/stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/company", {
  "url": "https://www.linkedin.com/company/stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/company", sandbase.Params{
	"url": "https://www.linkedin.com/company/stripe",
})
```

Same call via the path form: `POST /v1/api/linkedin/company` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full LinkedIn company page URL.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `city` or `postalCode`, and it is served only by a source that…  |

## Details

Fetch a full LinkedIn company page by URL: name, description, industry, employee count and range, follower count, founded year, headquarters and office locations, funding data, tagline, logo, website, and specialities.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/company" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/company/stripe"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full LinkedIn company page URL. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `city` or `postalCode`, and it is served only by a source that returns |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/company.json`](../../../catalog/models/linkedin/company.json) · Store page: https://www.sandbase.ai/model/linkedin/company
