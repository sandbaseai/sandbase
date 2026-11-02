# LinkedIn Company Posts API: pricing, parameters and code examples

`linkedin/company-posts` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0029 per call · **Modes:** sync

List a LinkedIn company page's recent posts by URL: full text, canonical link, publish date, author, engagement counts with a per-reaction breakdown, and attached media.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0029**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/company-posts", "url": "https://www.linkedin.com/company/stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/company-posts', {'url': 'https://www.linkedin.com/company/stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/company-posts", {
  "url": "https://www.linkedin.com/company/stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/company-posts", sandbase.Params{
	"url": "https://www.linkedin.com/company/stripe",
})
```

Same call via the path form: `POST /v1/api/linkedin/company-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full LinkedIn company page URL.  |
| `limit` | integer |  | Maximum number of posts to return. default `10`; range 1–50 |
| `postedLimit` | string |  | Only return posts published within this window (default any). one of: `any`, `1h`, `24h`, `week`, `month`, `3months`, `6months`, `year` |
| `includeReposts` | boolean |  | Include reposts (posts shared without an added comment). Defaults to true; set false to exclude them.  |
| `includeQuotePosts` | boolean |  | Include quote posts (posts shared with an added comment). Defaults to true; set false to exclude them.  |

## Details

List a LinkedIn company page's recent posts by URL: full text, canonical link, publish date, author, engagement counts with a per-reaction breakdown, and attached media.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/company-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/company/stripe", "limit": 10}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full LinkedIn company page URL. |
| `includeQuotePosts` | boolean | No | Include quote posts (posts shared with an added comment). Defaults to true; set false to exclude them. |
| `includeReposts` | boolean | No | Include reposts (posts shared without an added comment). Defaults to true; set false to exclude them. |
| `limit` | integer | No | Maximum number of posts to return. Default `10`. |
| `postedLimit` | string | No | Only return posts published within this window (default any). One of: `any`, `1h`, `24h`, `week`, `month`, `3months`, `6months`, `year`. |

### Pricing

Billed at the actual cost of each call, usually $0.0029 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/company-posts.json`](../../../catalog/models/linkedin/company-posts.json) · Store page: https://www.sandbase.ai/model/linkedin/company-posts
