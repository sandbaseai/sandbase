# TikTok Web Stream Search API: pricing, parameters and code examples

`tiktok/web/search-live` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches active TikTok web broadcasts matching a specified keyword. Returns stream details with pagination controls via count and offset parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/search-live", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/search-live', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/search-live", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/search-live", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/search-live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page default `20` |
| `offset` | integer |  | Page offset, 0 for the first request, need to provide for the second paging. default `0` |
| `keyword` | string | yes | Search keyword  |
| `search_id` | string |  | Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request. default `""` |

## Details

Query active streams on TikTok by providing a search term in `keyword`. Supports pagination across multiple result pages using `offset` and `search_id`.

### Use cases

- Discover active TikTok broadcasts matching specific topics or brand names.
- Track broadcast trends for targeted keywords.
- Monitor competitor streaming activity across the platform.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/search-live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `count` | integer | No | Number per page |
| `offset` | integer | No | Page offset, 0 for the first request, need to provide for the second paging. |
| `search_id` | string | No | Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request. |

### Notes

- Pass `offset` as 0 for initial queries, then advance it for subsequent pages.
- Include the `search_id` returned in the previous response when requesting additional pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/search-live.json`](../../../../catalog/models/tiktok/web/search-live.json) · Store page: https://www.sandbase.ai/model/tiktok/web/search-live
