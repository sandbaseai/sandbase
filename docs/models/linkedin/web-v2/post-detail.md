# LinkedIn Post or Article Detail

`linkedin/web-v2/post-detail` · api · LinkedIn

Returns content and metadata for a LinkedIn post or article using its web address. Works with both standard post and pulse article links.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/web-v2/post-detail", "url": "https://www.linkedin.com/posts/...-activity-...-xxxx"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/web-v2/post-detail', {'url': 'https://www.linkedin.com/posts/...-activity-...-xxxx'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/web-v2/post-detail", {
  "url": "https://www.linkedin.com/posts/...-activity-...-xxxx"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/web-v2/post-detail", sandbase.Params{
	"url": "https://www.linkedin.com/posts/...-activity-...-xxxx",
})
```

Same call via the path form: `POST /v1/api/linkedin/web-v2/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full post or article URL (both /posts/... and /pulse/... are  |

## Details

Fetch detailed information about a LinkedIn post or article by supplying its link in `url`.

### Use cases

- Retrieve LinkedIn post metadata and content from post URLs.
- Inspect LinkedIn Pulse articles directly from article links.
- Integrate public LinkedIn post details into external dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/web-v2/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/posts/...-activity-...-xxxx"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full post or article URL (both /posts/... and /pulse/... are |

### Notes

- Supports both `/posts/...` and `/pulse/...` link formats in `url`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [LinkedIn Company Posts](/model/linkedin/web-v2/company-posts): Returns posts from a LinkedIn organization page using the company URL.
- [LinkedIn Company Profile](/model/linkedin/web-v2/company-profile): Returns LinkedIn company profile details, including affiliated organizations, using a direct company page URL.
- [LinkedIn Job Details](/model/linkedin/web-v2/job-detail): Returns detailed information for a specific LinkedIn job posting via its URL.

---
Machine-readable: [`catalog/models/linkedin/web-v2/post-detail.json`](../../../../catalog/models/linkedin/web-v2/post-detail.json) · Store page: https://www.sandbase.ai/model/linkedin/web-v2/post-detail
