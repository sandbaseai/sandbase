# LinkedIn Article API: pricing, parameters and code examples

`linkedin/article` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00569 per call · **Modes:** sync

Read a public LinkedIn article or newsletter issue by URL, including its full body text, author, publication time, and engagement counts.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00569**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/article", "url": "https://www.linkedin.com/pulse/artificial-intelligence-primer-stephen-dover"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/article', {'url': 'https://www.linkedin.com/pulse/artificial-intelligence-primer-stephen-dover'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/article", {
  "url": "https://www.linkedin.com/pulse/artificial-intelligence-primer-stephen-dover"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/article", sandbase.Params{
	"url": "https://www.linkedin.com/pulse/artificial-intelligence-primer-stephen-dover",
})
```

Same call via the path form: `POST /v1/api/linkedin/article` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Public LinkedIn article or newsletter issue URL, e.g. https://www.linkedin.com/pulse/your-article-slug. Pair it with the attachmentUrl returned by linkedin.search_posts_full to read the article behind a post.  |

## Details

Read a public LinkedIn article or newsletter issue by URL, including its full body text, author, publication time, and engagement counts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/article" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/pulse/artificial-intelligence-primer-stephen-dover"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Public LinkedIn article or newsletter issue URL, e.g. https://www.linkedin.com/pulse/your-article-slug. Pair it with the attachmentUrl returned by linkedin.search_posts_full to read the article behind a post. |

### Pricing

Billed at the actual cost of each call, usually $0.00569 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/article.json`](../../../catalog/models/linkedin/article.json) · Store page: https://www.sandbase.ai/model/linkedin/article
