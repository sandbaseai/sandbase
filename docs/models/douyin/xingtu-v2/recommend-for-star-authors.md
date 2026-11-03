# Douyin Xingtu Similar Star Authors API: pricing, parameters and code examples

`douyin/xingtu-v2/recommend-for-star-authors` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended similar Douyin Xingtu creators based on a specified list of author IDs and an optional similarity type.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/recommend-for-star-authors", "author_ids": ["1"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/recommend-for-star-authors', {'author_ids': ['1']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/recommend-for-star-authors", {
  "author_ids": [
    "1"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/recommend-for-star-authors", sandbase.Params{
	"author_ids": []any{"1"},
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/recommend-for-star-authors` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default 1  |
| `author_ids` | array | yes | List of creator/author IDs  |
| `similar_type` | string |  | Similarity type  |

## Details

Returns recommendations for similar Douyin Xingtu star authors based on the provided `author_ids` list.

### Use cases

- Discover alternative Douyin creators matching target author profiles.
- Expand creator candidate pools for marketing campaigns.
- Evaluate comparable Xingtu creators based on similarity criteria.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/recommend-for-star-authors" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"author_ids": ["7112600044674482187"]}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `author_ids` | array | Yes | List of creator/author IDs |
| `page` | integer | No | Page number, default 1 |
| `similar_type` | string | No | Similarity type |

### Notes

- Requires an array of creator identifiers passed to `author_ids`.
- Use `page` to paginate through results, defaulting to 1.
- Filter recommendations by criteria using `similar_type`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/recommend-for-star-authors.json`](../../../../catalog/models/douyin/xingtu-v2/recommend-for-star-authors.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/recommend-for-star-authors
