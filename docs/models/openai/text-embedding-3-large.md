# OpenAI: Text Embedding 3 Large API: pricing, parameters and code examples

`openai/text-embedding-3-large` · embedding model · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.13 input / $0 output per 1M tokens · **Modes:** sync

OpenAI text-embedding-3-large creates embeddings for semantic search, retrieval, clustering, and classification.

## Pricing

- Input **$0.13** / output **$0** per 1M tokens (USD)

## Call it

```bash
curl https://api.sandbase.ai/v1/embeddings \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/text-embedding-3-large", "input": "hello"}'
```
## Details

OpenAI text-embedding-3-large produces embeddings with up to 3072 dimensions.

---
Machine-readable: [`catalog/models/openai/text-embedding-3-large.json`](../../../catalog/models/openai/text-embedding-3-large.json) · Store page: https://www.sandbase.ai/model/openai/text-embedding-3-large
