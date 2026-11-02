# LinkedIn Ad Details API: pricing, parameters and code examples

`linkedin/ad` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Look up a single LinkedIn Ad Library ad by URL and get the advertiser, headline, creative text, format, CTA, targeting, run dates, and impressions as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/ad", "url": "https://www.linkedin.com/ad-library/detail/1487405616"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/ad', {'url': 'https://www.linkedin.com/ad-library/detail/1487405616'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/ad", {
  "url": "https://www.linkedin.com/ad-library/detail/1487405616"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/ad", sandbase.Params{
	"url": "https://www.linkedin.com/ad-library/detail/1487405616",
})
```

Same call via the path form: `POST /v1/api/linkedin/ad` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | LinkedIn Ad Library ad URL (e.g. "https://www.linkedin.com/ad-library/detail/666281156").  |

## Details

Look up a single LinkedIn Ad Library ad by URL and get the advertiser, headline, creative text, format, CTA, targeting, run dates, and impressions as clean JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/ad" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/ad-library/detail/1487405616"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | LinkedIn Ad Library ad URL (e.g. "https://www.linkedin.com/ad-library/detail/666281156"). |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/ad.json`](../../../catalog/models/linkedin/ad.json) · Store page: https://www.sandbase.ai/model/linkedin/ad
