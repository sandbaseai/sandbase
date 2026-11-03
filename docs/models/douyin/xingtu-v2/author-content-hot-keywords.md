# Douyin Xingtu Author Content Hot Keywords API: pricing, parameters and code examples

`douyin/xingtu-v2/author-content-hot-keywords` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending content keywords for a Douyin creator. Filter results by creator ID and specify an optional keyword type.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-content-hot-keywords", "author_id": "7146074596666507300"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-content-hot-keywords', {'author_id': '7146074596666507300'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-content-hot-keywords", {
  "author_id": "7146074596666507300"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-content-hot-keywords", sandbase.Params{
	"author_id": "7146074596666507300",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-content-hot-keywords` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `author_id` | string | yes | Creator/author ID  |
| `keyword_type` | integer |  | Keyword type, default 0  |

## Details

Retrieve hot content keywords associated with a specific Douyin creator using `author_id`. You can also filter results by `keyword_type`.

### Use cases

- Analyze trending content themes for a specific Douyin creator.
- Inspect popular keywords associated with creator posts.
- Evaluate creator topic relevance based on keyword types.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-content-hot-keywords" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"author_id": "7146074596666507300"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `author_id` | string | Yes | Creator/author ID |
| `keyword_type` | integer | No | Keyword type, default 0 |

### Notes

- `author_id` is required to identify the creator.
- `keyword_type` defaults to 0.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-content-hot-keywords.json`](../../../../catalog/models/douyin/xingtu-v2/author-content-hot-keywords.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-content-hot-keywords
