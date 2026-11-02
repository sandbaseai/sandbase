# LinkedIn Ads Library API: pricing, parameters and code examples

`linkedin/ads` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0331 per call · **Modes:** sync

Search the LinkedIn Ad Library by search URL and list the matching ads (advertiser, creative text, format).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0331**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/ads", "url": "https://www.linkedin.com/company/stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/ads', {'url': 'https://www.linkedin.com/company/stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/ads", {
  "url": "https://www.linkedin.com/company/stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/ads", sandbase.Params{
	"url": "https://www.linkedin.com/company/stripe",
})
```

Same call via the path form: `POST /v1/api/linkedin/ads` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | LinkedIn Ad Library search URL or a LinkedIn company URL (e.g. https://www.linkedin.com/ad-library/search?companyIds=1035).  |
| `limit` | integer |  | Maximum number of results to return (1-20, default 20). You are billed per result returned, so a lower limit costs less. range 1–20 |

## Details

Search the LinkedIn Ad Library by search URL and list the matching ads (advertiser, creative text, format).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/ads" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/company/stripe", "limit": 3}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | LinkedIn Ad Library search URL or a LinkedIn company URL (e.g. https://www.linkedin.com/ad-library/search?companyIds=1035). |
| `limit` | integer | No | Maximum number of results to return (1-20, default 20). You are billed per result returned, so a lower limit costs less. |

### Pricing

Billed at the actual cost of each call, usually $0.0331 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/ads.json`](../../../catalog/models/linkedin/ads.json) · Store page: https://www.sandbase.ai/model/linkedin/ads
