# Douyin Video Search API: pricing, parameters and code examples

`douyin/search-video` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Search Douyin (TikTok China) videos by keyword with sort, publish-time, duration, and page filters; later pages require the previous search ID. Use it to support content discovery and trend research.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search-video", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search-video', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search-video", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search-video", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/douyin/search-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (starting from 1). default `1` |
| `keyword` | string | yes | The search keyword.  |
| `duration` | string |  | Filter by video duration. one of: `_0`, `_1`, `_2`, `_3`; default `"_0"` |
| `searchId` | string |  | Search ID; required for pages > 1. Use data.business_config.next_page.search_id from the previous response, and stop paging when data.business_config.has_more is 0.  |
| `sortType` | string |  | Sorting criteria for search results. one of: `_0`, `_1`, `_2`; default `"_0"` |
| `publishTime` | string |  | Filter by video publish time range. one of: `_0`, `_1`, `_7`, `_180`; default `"_0"` |

## Details

Search Douyin (TikTok China) videos by keyword with sort, publish-time, duration, and page filters; later pages require the previous search ID. Use it to support content discovery and trend research.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "美食"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | The search keyword. |
| `sortType` | string | No | Sorting criteria for search results. |
| `publishTime` | string | No | Filter by video publish time range. |
| `duration` | string | No | Filter by video duration. |
| `page` | integer | No | Page number (starting from 1). |
| `searchId` | string | No | Search ID; required for pages > 1. Use data.business_config.next_page.search_id from the previous response, and stop paging when data.business_config.has_more is 0. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/search-video.json`](../../../catalog/models/douyin/search-video.json) · Store page: https://www.sandbase.ai/model/douyin/search-video
