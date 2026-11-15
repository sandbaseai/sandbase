# arXiv Search Papers API: pricing, parameters and code examples

`arxiv/search-papers` · data API · arXiv · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Full-text search over arXiv papers using keyword, author, title, and category filters combined with AND logic.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "arxiv/search-papers"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('arxiv/search-papers', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("arxiv/search-papers", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "arxiv/search-papers", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/arxiv/search-papers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string |  | General keyword search across all fields  |
| `start` | integer |  | Starting index for pagination (0-based) default `0` |
| `title` | string |  | Title keywords to search for  |
| `author` | string |  | Author name to search for  |
| `sort_by` | string |  | Sort field for results one of: `lastUpdatedDate`, `relevance`, `submittedDate`; default `"relevance"` |
| `category` | string |  | arXiv category code (e.g., cs.AI, math.CO, hep-th)  |
| `sort_order` | string |  | Sort direction for results one of: `descending`, `ascending`; default `"descending"` |
| `max_results` | integer |  | Maximum number of results to return (max 100) default `10` |

## Details

Full-text search over arXiv papers using keyword, author, title, and category filters combined with AND logic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "arxiv/search-papers", "query": "neural network", "start": 0, "title": "", "author": "", "sort_by": "lastUpdatedDate", "category": "", "sort_order": "descending", "max_results": 5}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `author` | string | No | Author name to search for |
| `category` | string | No | arXiv category code (e.g., cs.AI, math.CO, hep-th) |
| `max_results` | integer | No | Maximum number of results to return (max 100) |
| `query` | string | No | General keyword search across all fields |
| `sort_by` | string | No | Sort field for results One of: `lastUpdatedDate`, `relevance`, `submittedDate`. |
| `sort_order` | string | No | Sort direction for results One of: `descending`, `ascending`. |
| `start` | integer | No | Starting index for pagination (0-based) |
| `title` | string | No | Title keywords to search for |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/arxiv/search-papers.json`](../../../catalog/models/arxiv/search-papers.json) · Store page: https://www.sandbase.ai/model/arxiv/search-papers
