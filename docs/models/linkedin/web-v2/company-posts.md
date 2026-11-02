# LinkedIn Company Posts API: pricing, parameters and code examples

`linkedin/web-v2/company-posts` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** sync

Returns posts from a LinkedIn organization page using the company URL. Supports ordering by top or recent posts and offset or token pagination.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/web-v2/company-posts", "url": "<url>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/web-v2/company-posts', {'url': '<url>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/web-v2/company-posts", {
  "url": "<url>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/web-v2/company-posts", sandbase.Params{
	"url": "<url>",
})
```

Same call via the path form: `POST /v1/api/linkedin/web-v2/company-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Company URL.  |
| `start` |  |  | Pagination offset — 0 for page 1, 50 for page 2, and so on.  |
| `sort_by` |  |  | top or recent.  |
| `pagination_token` |  |  | Token from the `paging` object of the previous response.  |

## Details

Retrieve posts from a company's profile by supplying the organization `url`. Adjust feed ordering with `sort_by` and manage multi-page results using `start` or `pagination_token`.

### Use cases

- Monitor recent announcements and feed activity from target company pages.
- Analyze post performance trends by reviewing entries ranked as top content.
- Aggregate competitor content feeds into marketing intelligence dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/web-v2/company-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "<url>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Company URL. |
| `start` | string | No | Pagination offset — 0 for page 1, 50 for page 2, and so on. |
| `sort_by` | string | No | top or recent. |
| `pagination_token` | string | No | Token from the `paging` object of the previous response. |

### Notes

- Set `sort_by` to `top` or `recent` to adjust output order.
- Paginate using `start` in increments of 50 or by passing the `pagination_token` returned in the previous response.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [LinkedIn Company Profile](/model/linkedin/web-v2/company-profile): Returns LinkedIn company profile details, including affiliated organizations, using a direct company page URL.
- [LinkedIn Job Details](/model/linkedin/web-v2/job-detail): Returns detailed information for a specific LinkedIn job posting via its URL.
- [LinkedIn Post Comments](/model/linkedin/web-v2/post-comments): Returns comments for a specific LinkedIn post using its activity URN.

---
Machine-readable: [`catalog/models/linkedin/web-v2/company-posts.json`](../../../../catalog/models/linkedin/web-v2/company-posts.json) · Store page: https://www.sandbase.ai/model/linkedin/web-v2/company-posts
