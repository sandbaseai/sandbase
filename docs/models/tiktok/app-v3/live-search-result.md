# TikTok Stream Search Results API: pricing, parameters and code examples

`tiktok/app-v3/live-search-result` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns search results for active broadcasts matching a specified keyword. Supports filtering by country code and paginating via offset and count limits.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/live-search-result", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/live-search-result', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/live-search-result", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/live-search-result", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/live-search-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number, do not exceed 20 default `20` |
| `offset` | integer |  | Offset, starting from 0, the second page gets the cursor value from the response as the offset to continue the request. default `0` |
| `region` | string |  | Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. default `"US"` |
| `keyword` | string | yes | Keyword  |

## Details

Look up active stream search results by providing a query in `keyword`. You can optionally adjust the geographic market with `region` and navigate results using `offset` and `count`.

### Use cases

- Discover active streams relevant to specific product keywords.
- Track regional broadcast trends by country code.
- Monitor niche discussions during real-time events.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/live-search-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `count` | integer | No | Number, do not exceed 20 |
| `offset` | integer | No | Offset, starting from 0, the second page gets the cursor value from the response as the offset to continue the request. |
| `region` | string | No | Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. |

### Notes

- `count` must not exceed 20.
- `offset` starts at 0, and subsequent pages use the cursor value returned in the response.
- `region` defaults to US and accepts ISO 3166-1 alpha-2 country codes.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/live-search-result.json`](../../../../catalog/models/tiktok/app-v3/live-search-result.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/live-search-result
