# Douyin Keyword Search Share Link API: pricing, parameters and code examples

`douyin/app-v3/open-app-to-keyword-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns a Douyin short share link that launches the Douyin application directly to search results for a specified query term.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/open-app-to-keyword-search", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/open-app-to-keyword-search', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/open-app-to-keyword-search", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/open-app-to-keyword-search", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/open-app-to-keyword-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Keyword  |

## Details

This endpoint produces a Douyin short link for opening search results in the Douyin mobile app based on a provided `keyword`.

### Use cases

- Direct mobile users to specific search topics inside the Douyin application.
- Generate clickable deep links for marketing campaigns and external landing pages.
- Route users to curated discovery terms from third-party interfaces.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/open-app-to-keyword-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "keyword": "人工智能",
  "short_url": "https://v.douyin.com/w_Rhf9duAgs/",
  "status": "success"
}
```

### Notes

- Supply the desired query string using the required `keyword` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/open-app-to-keyword-search.json`](../../../../catalog/models/douyin/app-v3/open-app-to-keyword-search.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/open-app-to-keyword-search
