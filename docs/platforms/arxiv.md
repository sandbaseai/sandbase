# arXiv API: 4 endpoints with pricing and code examples

Call 4 arXiv endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`arxiv/category-taxonomy`](../models/arxiv/category-taxonomy.md) | Browse the full arXiv category taxonomy organized by discipline groups. Each group contains categories with their ID, name, and… | $0.03 per call |
| [`arxiv/count-papers-by-comment`](../models/arxiv/count-papers-by-comment.md) | Searches arXiv for papers matching a keyword query that were originally announced in a given calendar month and whose author comments… | $0.09 per call |
| [`arxiv/paper`](../models/arxiv/paper.md) | Fetch detailed metadata for a specific paper by its arXiv ID. Returns title, authors, abstract, categories, publication dates, PDF and… | $0.03 per call |
| [`arxiv/search-papers`](../models/arxiv/search-papers.md) | Full-text search over arXiv papers using keyword, author, title, and category filters combined with AND logic. | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "arxiv/category-taxonomy"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
