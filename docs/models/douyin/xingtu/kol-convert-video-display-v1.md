# Douyin Xingtu KOL Conversion Video Display

`douyin/xingtu/kol-convert-video-display-v1` · api · Douyin

Returns Xingtu KOL conversion video metrics and product data for a specific creator. Filter records by detail type and navigate results using page numbers.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-convert-video-display-v1", "detailType": "<detailType>", "kolId": "<kolId>", "page": "<page>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-convert-video-display-v1', {'detailType': '<detailType>', 'kolId': '<kolId>', 'page': '<page>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-convert-video-display-v1", {
  "detailType": "<detailType>",
  "kolId": "<kolId>",
  "page": "<page>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-convert-video-display-v1", sandbase.Params{
	"detailType": "<detailType>",
	"kolId": "<kolId>",
	"page": "<page>",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-convert-video-display-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer | yes | Page number, starting from 1  |
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |
| `detailType` | string | yes | Detail type, supports the following parameters: _1: Video Data; _2: Product Data  |

## Details

This endpoint retrieves conversion metrics for a Douyin Xingtu creator based on the specified `kolId` and `detailType`.

### Use cases

- Inspect conversion video performance metrics for a specific Douyin Xingtu creator.
- Track product conversion records linked to creator promotional videos.
- Paginate through creator conversion analytics across marketing campaigns.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-convert-video-display-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"detailType": "<detailType>", "kolId": "<kolId>", "page": "<page>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | Yes | Page number, starting from 1 |
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xin… |
| `detailType` | string | Yes | Detail type, supports the following parameters: _1: Video Data; _2: Product Data |

### Notes

- `kolId` can be retrieved via Xingtu KOL ID endpoints using uid, sec-user-id, or unique-id.
- Set `detailType` to `_1` for video data or `_2` for product data.
- The `page` parameter starts from 1 for pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/model/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/model/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/model/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-convert-video-display-v1.json`](../../../../catalog/models/douyin/xingtu/kol-convert-video-display-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-convert-video-display-v1
