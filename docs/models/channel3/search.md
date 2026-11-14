# Channel3 Search API: pricing, parameters and code examples

`channel3/search` · data API · Channel3 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007 per call · **Modes:** async

Search products across retailers by text or image URL, with offers and pagination.

## Pricing

- **$0.007 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "channel3/search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('channel3/search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("channel3/search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "channel3/search", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/channel3/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` |  |  | Products per page, 1-30. Channel3 default: 20.  |
| `query` |  |  | Text search query. Provide query, image_url or page_token.  |
| `config` | object |  |   |
| `filters` | object |  |   |
| `image_url` |  |  |   |
| `page_token` |  |  | next_page_token from a previous search's output, to fetch the next page.  |

## Details

Search products across retailers by text or image URL, with offers and pagination.

---
Machine-readable: [`catalog/models/channel3/search.json`](../../../catalog/models/channel3/search.json) · Store page: https://www.sandbase.ai/model/channel3/search
