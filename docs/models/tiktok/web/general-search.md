# TikTok Web General Search

`tiktok/web/general-search` · api · TikTok

Returns general TikTok search results matching a specified keyword. Supports pagination through offset and search ID parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/general-search", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/general-search', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/general-search", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/general-search", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/general-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor. default `0` |
| `keyword` | string | yes | Search keyword  |
| `search_id` | string |  | Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request. default `""` |

## Details

Call this endpoint with a `keyword` to look up general search results across TikTok Web, using `offset` and `search_id` for subsequent page queries.

### Use cases

- Look up TikTok search listings for specific keywords.
- Retrieve user and content search cards across TikTok Web.
- Paginate through multi-category search results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/general-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `offset` | integer | No | Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor. |
| `search_id` | string | No | Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "card_title": "Users",
      "type": 4,
      "common": {
        "doc_id_str": "1"
      }
    }
  ]
}
```

### Notes

- Set `offset` to 0 on initial requests, then pass subsequent cursor offsets for pagination.
- Leave `search_id` empty on the initial request and pass the returned identifier in subsequent calls.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/general-search.json`](../../../../catalog/models/tiktok/web/general-search.json) · Store page: https://www.sandbase.ai/model/tiktok/web/general-search
