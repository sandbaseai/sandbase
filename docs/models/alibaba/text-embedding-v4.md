# Alibaba Text Embedding v4

`alibaba/text-embedding-v4` · embedding · Alibaba

Alibaba Cloud Model Studio text-embedding-v4 is a Qwen3-Embedding series text embedding model for semantic search, retrieval-augmented generation, clustering, classification, and multilingual code/text retrieval. It supports configurable output dimensions and OpenAI-compatible embeddings requests.

## Pricing

- Input **$0.1** / output **$0** per 1M tokens (USD)

## Call it

```bash
curl https://api.sandbase.ai/v1/embeddings \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/text-embedding-v4", "input": "hello"}'
```
## Details

Alibaba text-embedding-v4 converts text into dense vectors for semantic search, RAG, clustering, classification, and multilingual retrieval. It belongs to the Qwen3-Embedding series and supports configurable output dimensions: 2048, 1536, 1024, 768, 512, 256, 128, and 64.

---
Machine-readable: [`catalog/models/alibaba/text-embedding-v4.json`](../../../catalog/models/alibaba/text-embedding-v4.json) · Store page: https://www.sandbase.ai/model/alibaba/text-embedding-v4
