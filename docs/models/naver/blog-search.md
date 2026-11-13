# Naver Blog Search API: pricing, parameters and code examples

`naver/blog-search` · data API · Naver · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.032 per call · **Modes:** sync

Search up to five enriched Naver blog results by keyword with stable cursor pagination: result rank, title, excerpt, post and blogger URLs, blogger name, publish time, and Naver's total match count.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.032**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "naver/blog-search", "query": "제주도 맛집"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('naver/blog-search', {'query': '제주도 맛집'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("naver/blog-search", {
  "query": "제주도 맛집"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "naver/blog-search", sandbase.Params{
	"query": "제주도 맛집",
})
```

Same call via the path form: `POST /v1/api/naver/blog-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Order posts by Naver relevance or newest publication date (default relevance). one of: `relevance`, `recent` |
| `limit` | integer |  | Maximum number of title-enriched posts to return, from 1 to 5 (default 5). range 1–5 |
| `query` | string | yes | Keyword phrase to search across Naver blogs.  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor.  |

## Details

Search up to five enriched Naver blog results by keyword with stable cursor pagination: result rank, title, excerpt, post and blogger URLs, blogger name, publish time, and Naver's total match count.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "naver/blog-search", "sort": "relevance", "limit": 5, "query": "제주도 맛집"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword phrase to search across Naver blogs. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. |
| `limit` | integer | No | Maximum number of title-enriched posts to return, from 1 to 5 (default 5). |
| `sort` | string | No | Order posts by Naver relevance or newest publication date (default relevance). One of: `relevance`, `recent`. |

### Pricing

Billed at the actual cost of each call, about $0.032 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/naver/blog-search.json`](../../../catalog/models/naver/blog-search.json) · Store page: https://www.sandbase.ai/model/naver/blog-search
