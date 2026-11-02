# Douyin Hot Search API: pricing, parameters and code examples

`douyin/hot-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.027778 per call · **Modes:** sync

Search Douyin (TikTok China) content with optional keyword, category, video-type, ranking, pagination, engagement, and creator-follower filters. Use it to support trend discovery and campaign research.

## Pricing

- **$0.027778 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/hot-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/hot-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/hot-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/hot-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/hot-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (starting from 1). Page size is fixed at 10. default `1` |
| `keyword` | string |  | Optional search keyword.  |
| `sortType` | string |  | Sorting criteria for hot content results. one of: `COMPREHENSIVE`, `HIGH_INTERACTION`, `HIGH_LIKE`, `HIGH_COMMENT`, `HIGH_SHARE`; default `"COMPREHENSIVE"` |
| `videoType` | string |  | Video type filter. one of: `ALL`, `XINGTU_VIDEO`, `NATURAL_VIDEO`; default `"ALL"` |
| `contentType` | string |  | Top-level content type. Only one content type can be selected. one of: `ALL`, `FASHION`, `TECHNOLOGY`, `SCIENCE`, `PHOTOGRAPHY`, `FOOD`, `MOTHER_BABY`, `PARENTING`, `DRAMA`, `GAME`, `AUTOMOTIVE`, `ANIMAL` …; default `"ALL"` |
| `likeCountMax` | integer |  | Maximum raw like count.  |
| `likeCountMin` | integer |  | Minimum raw like count.  |
| `shareCountMax` | integer |  | Maximum raw share count.  |
| `shareCountMin` | integer |  | Minimum raw share count.  |
| `commentCountMax` | integer |  | Maximum raw comment count.  |
| `commentCountMin` | integer |  | Minimum raw comment count.  |
| `followerCountMax` | integer |  | Maximum raw creator follower count.  |
| `followerCountMin` | integer |  | Minimum raw creator follower count.  |
| `interactionCountMax` | integer |  | Maximum raw interaction count.  |
| `interactionCountMin` | integer |  | Minimum raw interaction count.  |

## Details

Search Douyin (TikTok China) content with optional keyword, category, video-type, ranking, pagination, engagement, and creator-follower filters. Use it to support trend discovery and campaign research.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/hot-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Optional search keyword. |
| `contentType` | string | No | Top-level content type. Only one content type can be selected. |
| `videoType` | string | No | Video type filter. |
| `sortType` | string | No | Sorting criteria for hot content results. |
| `page` | integer | No | Page number (starting from 1). Page size is fixed at 10. |
| `likeCountMin` | integer | No | Minimum raw like count. |
| `likeCountMax` | integer | No | Maximum raw like count. |
| `commentCountMin` | integer | No | Minimum raw comment count. |
| `commentCountMax` | integer | No | Maximum raw comment count. |
| `shareCountMin` | integer | No | Minimum raw share count. |
| `shareCountMax` | integer | No | Maximum raw share count. |
| `interactionCountMin` | integer | No | Minimum raw interaction count. |
| `interactionCountMax` | integer | No | Maximum raw interaction count. |
| `followerCountMin` | integer | No | Minimum raw creator follower count. |
| `followerCountMax` | integer | No | Maximum raw creator follower count. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/hot-search.json`](../../../catalog/models/douyin/hot-search.json) · Store page: https://www.sandbase.ai/model/douyin/hot-search
