# LinkedIn User Posts API: pricing, parameters and code examples

`linkedin/web-v2/user-posts` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** sync

Retrieves a member's posts, commented posts, or reacted posts using their profile URL. Supports filtering by activity type and paginating through results.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/web-v2/user-posts", "url": "<url>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/web-v2/user-posts', {'url': '<url>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/web-v2/user-posts", {
  "url": "<url>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/web-v2/user-posts", sandbase.Params{
	"url": "<url>",
})
```

Same call via the path form: `POST /v1/api/linkedin/web-v2/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Profile URL.  |
| `type` | string |  | posts / comments / reactions. Defaults to posts.  |
| `start` |  |  | Pagination offset — 0 for page 1, 50 for page 2, and so on.  |
| `pagination_token` |  |  | Token from the `paging` object of the previous response.  |

## Details

Retrieve post and activity history for a specific profile using the `url` parameter. You can optionally filter by interaction type and navigate pages using pagination tokens or offsets.

### Use cases

- Audit public post history for a target profile.
- Track comments and reactions left by a specific member.
- Monitor recent content shared across professional networks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/web-v2/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "<url>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Profile URL. |
| `type` | string | No | posts / comments / reactions. |
| `start` | string | No | Pagination offset — 0 for page 1, 50 for page 2, and so on. |
| `pagination_token` | string | No | Token from the `paging` object of the previous response. |

### Notes

- Filter activity using `type` with options: posts, comments, or reactions (defaults to posts).
- Pagination can be controlled using offset values in `start` (0 for page 1, 50 for page 2) or `pagination_token` from previous responses.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [LinkedIn Company Posts](/model/linkedin/web-v2/company-posts): Returns posts from a LinkedIn organization page using the company URL.
- [LinkedIn Company Profile](/model/linkedin/web-v2/company-profile): Returns LinkedIn company profile details, including affiliated organizations, using a direct company page URL.
- [LinkedIn Job Details](/model/linkedin/web-v2/job-detail): Returns detailed information for a specific LinkedIn job posting via its URL.

---
Machine-readable: [`catalog/models/linkedin/web-v2/user-posts.json`](../../../../catalog/models/linkedin/web-v2/user-posts.json) · Store page: https://www.sandbase.ai/model/linkedin/web-v2/user-posts
