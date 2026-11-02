# Google AI Overview API: pricing, parameters and code examples

`google/ai-overview` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0015 per call · **Modes:** sync

Ask Google Search a prompt and receive the AI Overview it generated for that scrape, with every source Google listed. Google regenerates the overview per search, so the same prompt can return different wording and a different source list.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0015**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/ai-overview", "prompt": "How does photosynthesis work?"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/ai-overview', {'prompt': 'How does photosynthesis work?'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/ai-overview", {
  "prompt": "How does photosynthesis work?"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/ai-overview", sandbase.Params{
	"prompt": "How does photosynthesis work?",
})
```

Same call via the path form: `POST /v1/api/google/ai-overview` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The question or prompt to answer with a Google AI Overview.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `scrapedAt`, and it is served only by a source that returns every…  |

## Details

Ask Google Search a prompt and receive the AI Overview it generated for that scrape, with every source Google listed. Google regenerates the overview per search, so the same prompt can return different wording and a different source list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/ai-overview" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "How does photosynthesis work?"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `prompt` | string | Yes | The question or prompt to answer with a Google AI Overview. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `scrapedAt`, and it is served only by a source that returns every one  |

### Pricing

Billed at the actual cost of each call, usually $0.0015 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/google/ai-overview.json`](../../../catalog/models/google/ai-overview.json) · Store page: https://www.sandbase.ai/model/google/ai-overview
