# Perplexity Search API: pricing, parameters and code examples

`perplexity/search` · data API · Perplexity · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Ask Perplexity a web-grounded question and receive an answer with source citations.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "perplexity/search", "prompt": "What are the best practices for home composting?"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('perplexity/search', {'prompt': 'What are the best practices for home composting?'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("perplexity/search", {
  "prompt": "What are the best practices for home composting?"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "perplexity/search", sandbase.Params{
	"prompt": "What are the best practices for home composting?",
})
```

Same call via the path form: `POST /v1/api/perplexity/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Question or research prompt for Perplexity to answer using web search.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `createdUtc`, and it is served only by a source that returns every…  |

## Details

Ask Perplexity a web-grounded question and receive an answer with source citations.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "perplexity/search", "prompt": "What are the best practices for home composting?"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `prompt` | string | Yes | Question or research prompt for Perplexity to answer using web search. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `createdUtc`, and it is served only by a source that returns every one |

### Pricing

Billed at the actual cost of each call, about $0.002 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/perplexity/search.json`](../../../catalog/models/perplexity/search.json) · Store page: https://www.sandbase.ai/model/perplexity/search
