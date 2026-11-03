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

Returns autocomplete and related search suggestions for a keyword on TikTok Web. Send one `keyword` string, such as `openai`.

### Use cases

- Collect autocomplete phrases for a topic to plan TikTok video titles and hashtags.
- Check how people phrase searches around a brand name or product.
- Build a keyword list for a topic by running a seed term and its variations through the API.
- Feed suggested phrases into a search tool to see what content they return.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/search-keyword-suggest" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "log_id": "2026110315442738CBBE360AAF9704603D",
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `status_code` | Status number for the call. The sample request for `openai` returned `0`. |
| `status_msg` | Status text for the call. It was an empty string in the sample response. |
| `log_id` | Identifier string for this call. Keep it if you need to refer to a specific request. |

### Notes

- The sample response for `keyword` set to `openai` held only `log_id`, `status_code` and `status_msg`. It did not include a list of suggestions, so check for extra keys before you read them.
- The API takes a single required `keyword` string and has no pagination parameters.
- To see current popular terms without a seed keyword, call [TikTok Daily Trending Search Words](/apis/tiktok/web/trending-searchwords).
- To see the results for a suggested phrase, pass it to [TikTok Web General Search](/apis/tiktok/web/general-search).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/search-keyword-suggest.json`](../../../../catalog/models/tiktok/web/search-keyword-suggest.json) · Store page: https://www.sandbase.ai/model/tiktok/web/search-keyword-suggest
