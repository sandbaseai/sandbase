# Akta News By Id API: pricing, parameters and code examples

`akta/news-by-id` · data API · Akta · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0005 per call · **Modes:** async

Fetch complete news article records by their article ids.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0005**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "akta/news-by-id", "news_ids": ["<news_ids>"]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('akta/news-by-id', {'news_ids': ['<news_ids>']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("akta/news-by-id", {
  "news_ids": [
    "<news_ids>"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "akta/news-by-id", sandbase.Params{
	"news_ids": []any{"<news_ids>"},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/akta/news-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `news_ids` | array | yes | Article ids from the 'id' field of news search results. Comma-separated on the wire.  |

## Details

Fetch complete news article records by their article ids.

### Pricing

- Inspect reference unit price: $0.0005 USD per result.
- Inspect flat fee: $0.005 USD per call.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/akta/news-by-id.json`](../../../catalog/models/akta/news-by-id.json) · Store page: https://www.sandbase.ai/model/akta/news-by-id
