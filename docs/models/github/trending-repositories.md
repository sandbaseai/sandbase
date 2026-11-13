# GitHub Trending Repositories API: pricing, parameters and code examples

`github/trending-repositories` · data API · GitHub · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List GitHub Trending repositories (rank, stars, stars gained today, language, and description), filterable by language and time window.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "github/trending-repositories"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('github/trending-repositories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("github/trending-repositories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "github/trending-repositories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/github/trending-repositories` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `since` | string |  | Trending window. one of: `daily`, `weekly`, `monthly`; default `"daily"` |
| `language` | string |  | Filter by programming language (e.g. "go", "typescript"). Omit for all languages.  |

## Details

List GitHub Trending repositories (rank, stars, stars gained today, language, and description), filterable by language and time window.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "github/trending-repositories", "since": "daily", "language": "python"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language` | string | No | Filter by programming language (e.g. "go", "typescript"). Omit for all languages. |
| `since` | string | No | Trending window. One of: `daily`, `weekly`, `monthly`. Default `"daily"`. |

### Pricing

Billed at the actual cost of each call, about $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/github/trending-repositories.json`](../../../catalog/models/github/trending-repositories.json) · Store page: https://www.sandbase.ai/model/github/trending-repositories
