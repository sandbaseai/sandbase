# GitHub Repository README API: pricing, parameters and code examples

`github/repository-readme` · data API · GitHub · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Get a GitHub repository's README by repository URL, as the Markdown text the maintainers wrote, with its file name, path and size. Use it to learn what a project does, which models and tools it uses, and how to reach its authors.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "github/repository-readme", "url": "https://github.com/openai/whisper"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('github/repository-readme', {'url': 'https://github.com/openai/whisper'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("github/repository-readme", {
  "url": "https://github.com/openai/whisper"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "github/repository-readme", sandbase.Params{
	"url": "https://github.com/openai/whisper",
})
```

Same call via the path form: `POST /v1/api/github/repository-readme` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | GitHub repository URL, e.g. https://github.com/openai/whisper. The README of the default branch is returned.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `content` or `size`, and it is served only by a source that returns…  |

## Details

Get a GitHub repository's README by repository URL, as the Markdown text the maintainers wrote, with its file name, path and size. Use it to learn what a project does, which models and tools it uses, and how to reach its authors.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "github/repository-readme", "url": "https://github.com/openai/whisper"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | GitHub repository URL, e.g. https://github.com/openai/whisper. The README of the default branch is returned. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `content` or `size`, and it is served only by a source that returns ev |

### Pricing

Billed at the actual cost of each call, about $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/github/repository-readme.json`](../../../catalog/models/github/repository-readme.json) · Store page: https://www.sandbase.ai/model/github/repository-readme
