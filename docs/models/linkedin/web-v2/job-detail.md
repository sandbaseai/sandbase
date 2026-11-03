# LinkedIn Job Details API: pricing, parameters and code examples

`linkedin/web-v2/job-detail` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** sync

Returns detailed information for a specific LinkedIn job posting via its URL. Allows optional inclusion of required skills and hiring team details.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/web-v2/job-detail", "url": "<url>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/web-v2/job-detail', {'url': '<url>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/web-v2/job-detail", {
  "url": "<url>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/web-v2/job-detail", sandbase.Params{
	"url": "<url>",
})
```

Same call via the path form: `POST /v1/api/linkedin/web-v2/job-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Job URL, e.g. https://www.linkedin.com/jobs/view/3766410207/.  |
| `include_skills` | boolean |  | Whether to include the required skills.  |
| `include_hiring_team` | boolean |  | Whether to include hiring team information.  |

## Details

Retrieve job posting information by submitting a LinkedIn job `url`. Set `include_skills` and `include_hiring_team` to expand the returned job dataset.

### Use cases

- Extract job posting details and requirements from LinkedIn listings.
- Review hiring team profiles associated with target job openings.
- Track required job skills to analyze industry hiring trends.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/web-v2/job-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "<url>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Job URL, e.g. https://www.linkedin.com/jobs/view/3766410207/. |
| `include_skills` | boolean | No | Whether to include the required skills. |
| `include_hiring_team` | boolean | No | Whether to include hiring team information. |

### Notes

- Supply a full LinkedIn job posting link in `url`.
- Set `include_skills` to true to receive associated skill requirements.
- Set `include_hiring_team` to true to retrieve hiring team details.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [LinkedIn Company Posts](/apis/linkedin/web-v2/company-posts): Returns posts from a LinkedIn organization page using the company URL.
- [LinkedIn Company Profile](/apis/linkedin/web-v2/company-profile): Returns LinkedIn company profile details, including affiliated organizations, using a direct company page URL.
- [LinkedIn Post Comments](/apis/linkedin/web-v2/post-comments): Returns comments for a specific LinkedIn post using its activity URN.

---
Machine-readable: [`catalog/models/linkedin/web-v2/job-detail.json`](../../../../catalog/models/linkedin/web-v2/job-detail.json) · Store page: https://www.sandbase.ai/model/linkedin/web-v2/job-detail
