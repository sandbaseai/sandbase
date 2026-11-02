# TikTok Search Keyword Suggestions API: pricing, parameters and code examples

`tiktok/web/search-keyword-suggest` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns autocomplete and related search suggestions for a given query term on TikTok Web. Use this to discover trending search variations based on input keywords.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/search-keyword-suggest", "keyword": "TikTok"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/search-keyword-suggest', {'keyword': 'TikTok'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/search-keyword-suggest", {
  "keyword": "TikTok"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/search-keyword-suggest", sandbase.Params{
	"keyword": "TikTok",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/search-keyword-suggest` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword  |

## Details

Returns search keyword suggestions based on a query term passed via `keyword`. Use it to discover autocomplete phrases and related query terms on TikTok Web.

### Use cases

- Suggest relevant query terms in search autocomplete interfaces.
- Discover trending search phrases associated with a target topic.
- Optimize content discovery by analyzing suggested search queries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/search-keyword-suggest" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "group_id": "1357815902537310788",
      "word": "ai generated video"
    }
  ]
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/search-keyword-suggest.json`](../../../../catalog/models/tiktok/web/search-keyword-suggest.json) · Store page: https://www.sandbase.ai/model/tiktok/web/search-keyword-suggest
