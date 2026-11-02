# Naver AI Overview API: pricing, parameters and code examples

`naver/ai-overview` · data API · Naver · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Naver's AI-generated overview answer for a search query, with the cited sources.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "naver/ai-overview", "query": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('naver/ai-overview', {'query': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("naver/ai-overview", {
  "query": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "naver/ai-overview", sandbase.Params{
	"query": "coffee",
})
```

Same call via the path form: `POST /v1/api/naver/ai-overview` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | param name inferred from sibling engine=naver, not independently confirmed  |

## Details

Naver's AI-generated overview answer for a search query, with the cited sources.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/naver/ai-overview" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "coffee"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | param name inferred from sibling engine=naver, not independently confirmed |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/naver/ai-overview.json`](../../../catalog/models/naver/ai-overview.json) · Store page: https://www.sandbase.ai/model/naver/ai-overview
