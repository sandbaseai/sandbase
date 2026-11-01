# LinkedIn Post Reactions

`linkedin/post-reactions` · api · LinkedIn

List who reacted to a LinkedIn post - reactor name, profile URL, job title, and reaction type. Lead-gen grade.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0029**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/post-reactions", "url": "https://www.linkedin.com/posts/satyanadella_today-were-bringing-skills-to-copilot-for-activity-7475945433668694017--kvG"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/post-reactions', {'url': 'https://www.linkedin.com/posts/satyanadella_today-were-bringing-skills-to-copilot-for-activity-7475945433668694017--kvG'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/post-reactions", {
  "url": "https://www.linkedin.com/posts/satyanadella_today-were-bringing-skills-to-copilot-for-activity-7475945433668694017--kvG"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/post-reactions", sandbase.Params{
	"url": "https://www.linkedin.com/posts/satyanadella_today-were-bringing-skills-to-copilot-for-activity-7475945433668694017--kvG",
})
```

Same call via the path form: `POST /v1/api/linkedin/post-reactions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | URL of the LinkedIn post to list reactions for (a /posts/...-activity-... or /feed/update/urn:li:activity:... link).  |
| `limit` | integer |  | Maximum number of reactions to return (1-100, default 100). range 1–100 |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `postId`, and it is served only by a source that returns every one…  |

## Details

List who reacted to a LinkedIn post - reactor name, profile URL, job title, and reaction type. Lead-gen grade.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/post-reactions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/posts/satyanadella_today-were-bringing-skills-to-copilot-for-activity-7475945433668694017--kvG", "limit": 5}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | URL of the LinkedIn post to list reactions for (a /posts/...-activity-... or /feed/update/urn:li:activity:... link). |
| `limit` | integer | No | Maximum number of reactions to return (1-100, default 100). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `postId`, and it is served only by a source that returns every one of  |

### Pricing

Billed at the actual cost of each call, usually $0.0029 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/post-reactions.json`](../../../catalog/models/linkedin/post-reactions.json) · Store page: https://www.sandbase.ai/model/linkedin/post-reactions
