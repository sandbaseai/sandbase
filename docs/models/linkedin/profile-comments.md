# LinkedIn Profile Comments API: pricing, parameters and code examples

`linkedin/profile-comments` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0029 per call · **Modes:** sync

List the comments a LinkedIn member has left on other people's posts - the comment text, its permalink and timestamp, plus the post it was left on and that post's author and engagement.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0029**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/profile-comments", "url": "https://www.linkedin.com/in/jeffweiner08"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/profile-comments', {'url': 'https://www.linkedin.com/in/jeffweiner08'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/profile-comments", {
  "url": "https://www.linkedin.com/in/jeffweiner08"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/profile-comments", sandbase.Params{
	"url": "https://www.linkedin.com/in/jeffweiner08",
})
```

Same call via the path form: `POST /v1/api/linkedin/profile-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full URL of the LinkedIn member profile whose comments on other people's posts should be listed.  |
| `limit` | integer |  | Maximum number of comments to return. default `100`; range 1–100 |
| `postedLimit` | string |  | Only return comments posted within this window (default any). one of: `any`, `24h`, `week`, `month` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `edited` or `isAuthor`, and it is served only by a source that…  |

## Details

List the comments a LinkedIn member has left on other people's posts - the comment text, its permalink and timestamp, plus the post it was left on and that post's author and engagement.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/profile-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/in/jeffweiner08", "limit": 10}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full URL of the LinkedIn member profile whose comments on other people's posts should be listed. |
| `limit` | integer | No | Maximum number of comments to return. Default `100`. |
| `postedLimit` | string | No | Only return comments posted within this window (default any). One of: `any`, `24h`, `week`, `month`. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `edited` or `isAuthor`, and it is served only by a source that returns |

### Pricing

Billed at the actual cost of each call, usually $0.0029 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/profile-comments.json`](../../../catalog/models/linkedin/profile-comments.json) · Store page: https://www.sandbase.ai/model/linkedin/profile-comments
