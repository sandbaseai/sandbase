# GitHub Trending Developers API: pricing, parameters and code examples

`github/trending-developers` · data API · GitHub · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List trending GitHub developers (rank, username, name, avatar, and their most popular repository), optionally filtered by programming language and time range.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "github/trending-developers"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('github/trending-developers', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("github/trending-developers", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "github/trending-developers", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/github/trending-developers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `since` | string |  | Trending range: daily, weekly, or monthly (defaults to daily). one of: `daily`, `weekly`, `monthly` |
| `language` | string |  | Programming language to filter trending developers (e.g. javascript, python, go).  |

## Details

List trending GitHub developers (rank, username, name, avatar, and their most popular repository), optionally filtered by programming language and time range.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "github/trending-developers", "since": "weekly", "language": "go"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language` | string | No | Programming language to filter trending developers (e.g. javascript, python, go). |
| `since` | string | No | Trending range: daily, weekly, or monthly (defaults to daily). One of: `daily`, `weekly`, `monthly`. |

### Pricing

Billed at the actual cost of each call, about $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/github/trending-developers.json`](../../../catalog/models/github/trending-developers.json) · Store page: https://www.sandbase.ai/model/github/trending-developers
