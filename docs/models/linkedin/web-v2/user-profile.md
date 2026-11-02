# LinkedIn User Profile API: pricing, parameters and code examples

`linkedin/web-v2/user-profile` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Retrieves public profile details for a LinkedIn member. Input the full profile link to look up member information.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/web-v2/user-profile", "url": "https://www.linkedin.com/posts/...-activity-...-xxxx"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/web-v2/user-profile', {'url': 'https://www.linkedin.com/posts/...-activity-...-xxxx'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/web-v2/user-profile", {
  "url": "https://www.linkedin.com/posts/...-activity-...-xxxx"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/web-v2/user-profile", sandbase.Params{
	"url": "https://www.linkedin.com/posts/...-activity-...-xxxx",
})
```

Same call via the path form: `POST /v1/api/linkedin/web-v2/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full profile URL (e.g. https://www.linkedin.com/in/williamhgates/).  |

## Details

Retrieve public LinkedIn member profile information using a valid member link. Provide the target link using the `url` parameter.

### Use cases

- Look up public professional background details using a member profile link.
- Enrich internal contact records with public LinkedIn profile data.
- Verify professional profiles via their canonical profile link.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/web-v2/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/posts/...-activity-...-xxxx"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full profile URL (e.g. https://www.linkedin.com/in/williamhgates/). |

### Notes

- Pass a complete profile link to the `url` parameter, such as https://www.linkedin.com/in/williamhgates/.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [LinkedIn Company Posts](/model/linkedin/web-v2/company-posts): Returns posts from a LinkedIn organization page using the company URL.
- [LinkedIn Company Profile](/model/linkedin/web-v2/company-profile): Returns LinkedIn company profile details, including affiliated organizations, using a direct company page URL.
- [LinkedIn Job Details](/model/linkedin/web-v2/job-detail): Returns detailed information for a specific LinkedIn job posting via its URL.

---
Machine-readable: [`catalog/models/linkedin/web-v2/user-profile.json`](../../../../catalog/models/linkedin/web-v2/user-profile.json) · Store page: https://www.sandbase.ai/model/linkedin/web-v2/user-profile
