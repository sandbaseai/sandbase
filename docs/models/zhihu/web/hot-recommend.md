# Zhihu Hot Recommendations API: pricing, parameters and code examples

`zhihu/web/hot-recommend` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns hot recommendation items and content snippets from Zhihu Web. Supports pagination through offset and page_number alongside an optional session_token.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/hot-recommend"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/hot-recommend', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/hot-recommend", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/hot-recommend", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/zhihu/web/hot-recommend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | string |  | Offset default `"0"` |
| `page_number` | string |  | Page Number default `"1"` |
| `session_token` | string |  | Session Token default `""` |

## Details

This endpoint retrieves trending recommendations from the Zhihu web feed. Control pagination using `offset` and `page_number`, or pass `session_token` to maintain session context.

### Use cases

- Track trending topics and discussions across Zhihu.
- Aggregate recommended feed snippets for content curation.
- Monitor popular questions and opinions on the platform.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/hot-recommend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `offset` | string | No | Offset |
| `page_number` | string | No | Page Number |
| `session_token` | string | No | Session Token |

### Notes

- Paginate results using `offset` and `page_number`.
- Provide `session_token` when maintaining session-based recommendations.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/hot-recommend.json`](../../../../catalog/models/zhihu/web/hot-recommend.json) · Store page: https://www.sandbase.ai/model/zhihu/web/hot-recommend
