# GitHub Issue and PR Search API: pricing, parameters and code examples

`github/search-issues` · data API · GitHub · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0024 per call · **Modes:** sync

Search issues and pull requests across GitHub with GitHub's own search syntax (repo:, is:pr, is:issue, author:, label:, opened:...), with each result's author, state, labels, counts and body. Use it to find who opens issues and pull requests on a repository.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0024**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "github/search-issues", "query": "repo:openai/whisper is:pr"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('github/search-issues', {'query': 'repo:openai/whisper is:pr'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("github/search-issues", {
  "query": "repo:openai/whisper is:pr"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "github/search-issues", sandbase.Params{
	"query": "repo:openai/whisper is:pr",
})
```

Same call via the path form: `POST /v1/api/github/search-issues` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-based page of results. Request page + 1 while hasMore is true. default `1`; range 1– |
| `sort` | string |  | Sort by number of comments, creation date, last update, or reactions. Omit for best match. one of: `comments`, `created`, `updated`, `reactions` |
| `limit` | integer |  | Rows per page, 1-100 (GitHub's own page-size limit). Keep it the same while walking pages, because it sets the page size. default `100`; range 1–100 |
| `order` | string |  | Sort direction when sort is set. Defaults to desc. one of: `desc`, `asc` |
| `query` | string | yes | GitHub issue search query with any of GitHub's qualifiers, e.g. "repo:openai/whisper is:pr", "is:issue label:bug author:octocat", "repo:ggml-org/llama.cpp is:pr is:merged opened:>2026-01-01".  |

## Details

Search issues and pull requests across GitHub with GitHub's own search syntax (repo:, is:pr, is:issue, author:, label:, opened:...), with each result's author, state, labels, counts and body. Use it to find who opens issues and pull requests on a repository.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "github/search-issues", "query": "repo:openai/whisper is:pr"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | GitHub issue search query with any of GitHub's qualifiers, e.g. "repo:openai/whisper is:pr", "is:issue label:bug author:octocat", "repo:ggml-org/llama.cpp is:pr is:merged opened:>2026-01-01". |
| `limit` | integer | No | Rows per page, 1-100 (GitHub's own page-size limit). Keep it the same while walking pages, because it sets the page size. Default `100`. |
| `order` | string | No | Sort direction when sort is set. Defaults to desc. One of: `desc`, `asc`. |
| `page` | integer | No | 1-based page of results. Request page + 1 while hasMore is true. Default `1`. |
| `sort` | string | No | Sort by number of comments, creation date, last update, or reactions. Omit for best match. One of: `comments`, `created`, `updated`, `reactions`. |

### Pricing

Billed at the actual cost of each call, about $0.0024 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/github/search-issues.json`](../../../catalog/models/github/search-issues.json) · Store page: https://www.sandbase.ai/model/github/search-issues
