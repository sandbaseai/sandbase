# LinkedIn Post Comments

`linkedin/post-comments` · api · LinkedIn

List comments on a LinkedIn post - full text, commenter name/URL/job title, timestamps, and engagement.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0029**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/post-comments", "url": "https://www.linkedin.com/posts/stripe_philip-kl%C3%B6ckner-in-conversation-with-conor-activity-7477791740645564416-tIbZ"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/post-comments', {'url': 'https://www.linkedin.com/posts/stripe_philip-kl%C3%B6ckner-in-conversation-with-conor-activity-7477791740645564416-tIbZ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/post-comments", {
  "url": "https://www.linkedin.com/posts/stripe_philip-kl%C3%B6ckner-in-conversation-with-conor-activity-7477791740645564416-tIbZ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/post-comments", sandbase.Params{
	"url": "https://www.linkedin.com/posts/stripe_philip-kl%C3%B6ckner-in-conversation-with-conor-activity-7477791740645564416-tIbZ",
})
```

Same call via the path form: `POST /v1/api/linkedin/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full URL of the LinkedIn post to list comments for.  |
| `limit` | integer |  | Maximum number of comments to return. default `100`; range 1–100 |
| `postedLimit` | string |  | Only return comments posted within this window (default any). one of: `any`, `24h`, `week`, `month`, `3months`, `6months`, `year` |

## Details

List comments on a LinkedIn post - full text, commenter name/URL/job title, timestamps, and engagement.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/posts/stripe_philip-kl%C3%B6ckner-in-conversation-with-conor-activity-7477791740645564416-tIbZ", "limit": 10}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full URL of the LinkedIn post to list comments for. |
| `limit` | integer | No | Maximum number of comments to return. Default `100`. |
| `postedLimit` | string | No | Only return comments posted within this window (default any). One of: `any`, `24h`, `week`, `month`, `3months`, `6months`, `year`. |

### Pricing

Billed at the actual cost of each call, usually $0.0029 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/post-comments.json`](../../../catalog/models/linkedin/post-comments.json) · Store page: https://www.sandbase.ai/model/linkedin/post-comments
