# GitHub User Contributions API: pricing, parameters and code examples

`github/user-contributions` · data API · GitHub · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch a GitHub user's contribution graph for a year (total contributions plus per-day counts and heatmap intensity).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "github/user-contributions", "handle": "torvalds"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('github/user-contributions', {'handle': 'torvalds'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("github/user-contributions", {
  "handle": "torvalds"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "github/user-contributions", sandbase.Params{
	"handle": "torvalds",
})
```

Same call via the path form: `POST /v1/api/github/user-contributions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `year` | integer |  | Calendar year of the contribution graph. Defaults to the current year.  |
| `handle` | string | yes | GitHub username.  |

## Details

Fetch a GitHub user's contribution graph for a year (total contributions plus per-day counts and heatmap intensity).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "github/user-contributions", "year": 2024, "handle": "torvalds"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | GitHub username. |
| `year` | integer | No | Calendar year of the contribution graph. Defaults to the current year. |

### Pricing

Billed at the actual cost of each call, about $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/github/user-contributions.json`](../../../catalog/models/github/user-contributions.json) · Store page: https://www.sandbase.ai/model/github/user-contributions
