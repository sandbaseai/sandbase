# GitHub Repository Forks API: pricing, parameters and code examples

`github/repository-forks` · data API · GitHub · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List the forks of a GitHub repository by repository URL, with each fork's owner, description, stars, language and last push. Sort by newest, oldest or most starred.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "github/repository-forks", "url": "https://github.com/openai/whisper"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('github/repository-forks', {'url': 'https://github.com/openai/whisper'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("github/repository-forks", {
  "url": "https://github.com/openai/whisper"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "github/repository-forks", sandbase.Params{
	"url": "https://github.com/openai/whisper",
})
```

Same call via the path form: `POST /v1/api/github/repository-forks` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | GitHub repository URL, e.g. https://github.com/openai/whisper.  |
| `page` | integer |  | 1-based page of forks. Request page + 1 while hasMore is true. default `1`; range 1– |
| `sort` | string |  | Order of the forks. Defaults to newest. one of: `newest`, `oldest`, `stargazers`, `watchers` |
| `limit` | integer |  | Rows per page, 1-100 (GitHub's own page-size limit). Keep it the same while walking pages, because it sets the page size. default `100`; range 1–100 |

## Details

List the forks of a GitHub repository by repository URL, with each fork's owner, description, stars, language and last push. Sort by newest, oldest or most starred.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "github/repository-forks", "url": "https://github.com/openai/whisper"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | GitHub repository URL, e.g. https://github.com/openai/whisper. |
| `limit` | integer | No | Rows per page, 1-100 (GitHub's own page-size limit). Keep it the same while walking pages, because it sets the page size. Default `100`. |
| `page` | integer | No | 1-based page of forks. Request page + 1 while hasMore is true. Default `1`. |
| `sort` | string | No | Order of the forks. Defaults to newest. One of: `newest`, `oldest`, `stargazers`, `watchers`. |

### Pricing

Billed at the actual cost of each call, about $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/github/repository-forks.json`](../../../catalog/models/github/repository-forks.json) · Store page: https://www.sandbase.ai/model/github/repository-forks
