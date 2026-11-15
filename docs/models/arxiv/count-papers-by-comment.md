# arXiv Count Papers By Comment API: pricing, parameters and code examples

`arxiv/count-papers-by-comment` · data API · arXiv · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.09 per call · **Modes:** sync

Searches arXiv for papers matching a keyword query that were originally announced in a given calendar month and whose author comments contain a given phrase, and returns the matching papers with their count.

## Pricing

- **$0.09 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "arxiv/count-papers-by-comment", "month": "2026-10", "query": "neural network", "phrase": "accepted"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('arxiv/count-papers-by-comment', {'month': '2026-10', 'query': 'neural network', 'phrase': 'accepted'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("arxiv/count-papers-by-comment", {
  "month": "2026-10",
  "query": "neural network",
  "phrase": "accepted"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "arxiv/count-papers-by-comment", sandbase.Params{
	"month": "2026-10",
	"query": "neural network",
	"phrase": "accepted",
})
```

Same call via the path form: `POST /v1/api/arxiv/count-papers-by-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `month` | string | yes | Announcement month in YYYY-MM form; papers originally announced on arXiv in that month are considered  |
| `query` | string | yes | Keyword query searched across all paper fields (title, abstract, authors, etc.), e.g. neural network  |
| `phrase` | string | yes | Word or phrase that must appear in the paper's author comments, matched case-insensitively as whole words, e.g. accepted at  |

## Details

Searches arXiv for papers matching a keyword query that were originally announced in a given calendar month and whose author comments contain a given phrase, and returns the matching papers with their count.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "arxiv/count-papers-by-comment", "month": "2026-10", "query": "neural network", "phrase": "accepted"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `month` | string | Yes | Announcement month in YYYY-MM form; papers originally announced on arXiv in that month are considered |
| `phrase` | string | Yes | Word or phrase that must appear in the paper's author comments, matched case-insensitively as whole words, e.g. accepted at |
| `query` | string | Yes | Keyword query searched across all paper fields (title, abstract, authors, etc.), e.g. neural network |

### Pricing

Flat $0.09 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/arxiv/count-papers-by-comment.json`](../../../catalog/models/arxiv/count-papers-by-comment.json) · Store page: https://www.sandbase.ai/model/arxiv/count-papers-by-comment
