# arXiv Paper API: pricing, parameters and code examples

`arxiv/paper` · data API · arXiv · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Fetch detailed metadata for a specific paper by its arXiv ID. Returns title, authors, abstract, categories, publication dates, PDF and abstract page URLs, and optional fields like DOI, journal reference, and author comments.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "arxiv/paper", "arxiv_id": "2301.00001"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('arxiv/paper', {'arxiv_id': '2301.00001'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("arxiv/paper", {
  "arxiv_id": "2301.00001"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "arxiv/paper", sandbase.Params{
	"arxiv_id": "2301.00001",
})
```

Same call via the path form: `POST /v1/api/arxiv/paper` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `arxiv_id` | string | yes | The arXiv paper ID (e.g., 2301.00001, 2301.00001v1, or hep-th/9901001)  |

## Details

Fetch detailed metadata for a specific paper by its arXiv ID. Returns title, authors, abstract, categories, publication dates, PDF and abstract page URLs, and optional fields like DOI, journal reference, and author comments.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "arxiv/paper", "arxiv_id": "2301.00001"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `arxiv_id` | string | Yes | The arXiv paper ID (e.g., 2301.00001, 2301.00001v1, or hep-th/9901001) |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/arxiv/paper.json`](../../../catalog/models/arxiv/paper.json) · Store page: https://www.sandbase.ai/model/arxiv/paper
