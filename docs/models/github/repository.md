# GitHub Repository API: pricing, parameters and code examples

`github/repository` · data API · GitHub · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch a GitHub repository's metadata by URL (stars, forks, language, topics, license, and timestamps).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "github/repository", "url": "https://github.com/facebook/react"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('github/repository', {'url': 'https://github.com/facebook/react'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("github/repository", {
  "url": "https://github.com/facebook/react"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "github/repository", sandbase.Params{
	"url": "https://github.com/facebook/react",
})
```

Same call via the path form: `POST /v1/api/github/repository` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | GitHub repository URL (e.g. https://github.com/facebook/react).  |

## Details

Fetch a GitHub repository's metadata by URL (stars, forks, language, topics, license, and timestamps).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "github/repository", "url": "https://github.com/facebook/react"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | GitHub repository URL (e.g. https://github.com/facebook/react). |

### Pricing

Billed at the actual cost of each call, about $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/github/repository.json`](../../../catalog/models/github/repository.json) · Store page: https://www.sandbase.ai/model/github/repository
