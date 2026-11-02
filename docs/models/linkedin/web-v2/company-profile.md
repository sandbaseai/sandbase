# LinkedIn Company Profile API: pricing, parameters and code examples

`linkedin/web-v2/company-profile` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns LinkedIn company profile details, including affiliated organizations, using a direct company page URL.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/web-v2/company-profile", "url": "https://www.linkedin.com/company/microsoft/"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/web-v2/company-profile', {'url': 'https://www.linkedin.com/company/microsoft/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/web-v2/company-profile", {
  "url": "https://www.linkedin.com/company/microsoft/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/web-v2/company-profile", sandbase.Params{
	"url": "https://www.linkedin.com/company/microsoft/",
})
```

Same call via the path form: `POST /v1/api/linkedin/web-v2/company-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full company URL (e.g. https://www.linkedin.com/company/microsoft/).  |

## Details

Look up company profile information by providing the target LinkedIn company page in the `url` parameter.

### Use cases

- Retrieve profile information for corporate research.
- Identify affiliated organizations linked to a specific company page.
- Verify corporate affiliations from public LinkedIn URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/web-v2/company-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/company/microsoft/"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full company URL (e.g. https://www.linkedin.com/company/microsoft/). |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "affiliated": [
    {
      "Links": "https://www.linkedin.com/company/github?trk=affiliated-pages",
      "subtitle": "Software Development",
      "title": "GitHub"
    }
  ]
}
```

### Notes

- Supply the full company URL including the protocol in `url`, such as https://www.linkedin.com/company/microsoft/.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [LinkedIn Company Posts](/model/linkedin/web-v2/company-posts): Returns posts from a LinkedIn organization page using the company URL.
- [LinkedIn Job Details](/model/linkedin/web-v2/job-detail): Returns detailed information for a specific LinkedIn job posting via its URL.
- [LinkedIn Post Comments](/model/linkedin/web-v2/post-comments): Returns comments for a specific LinkedIn post using its activity URN.

---
Machine-readable: [`catalog/models/linkedin/web-v2/company-profile.json`](../../../../catalog/models/linkedin/web-v2/company-profile.json) · Store page: https://www.sandbase.ai/model/linkedin/web-v2/company-profile
