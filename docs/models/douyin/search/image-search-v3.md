# Douyin Image-Text Search

`douyin/search/image-search-v3` · api · Douyin

Returns image-text content search results from Douyin based on a target query keyword. Supports pagination using cursor and search session identifiers.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/image-search-v3", "cursor": 0, "keyword": "猫咪", "search_id": ""}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/image-search-v3', {'cursor': 0, 'keyword': '猫咪', 'search_id': ''})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/image-search-v3", {
  "cursor": 0,
  "keyword": "猫咪",
  "search_id": ""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/image-search-v3", sandbase.Params{
	"cursor": 0,
	"keyword": "猫咪",
	"search_id": "",
})
```

Same call via the path form: `POST /v1/api/douyin/search/image-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first request) default `0` |
| `keyword` | string | yes | Search keyword, e.g., "food"  |
| `search_id` | string |  | Search ID for pagination (use value from previous response) default `""` |

## Details

Query Douyin for image-text posts matching a target `keyword`. You can paginate through result sets using `cursor` and `search_id`.

### Use cases

- Search Douyin image-text posts for specific keywords or topics.
- Track visual content trends and user posts across Douyin.
- Retrieve image post identifiers for downstream content processing.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/image-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "猫咪"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword, e.g., "food" |
| `cursor` | integer | No | Pagination cursor (0 for first request) |
| `search_id` | string | No | Search ID for pagination (use value from previous response) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "business_data": [
    {
      "card_id": "douyin.doctype_aweme_image",
      "data_id": "0_7693107447376465529",
      "type": 12,
      "data": {
        "card_id": "douyin.doctype_aweme_image",
        "card_type": 1,
        "doc_type": 303,
        "provider_doc_id": 7693107447376465529,
        "provider_doc_id_str": "7693107447376465529",
        "type": 1
      },
      "log": {
        "rank": "1"
      }
    }
  ]
}
```

### Notes

- Set `cursor` to 0 on the first request.
- Pass the `search_id` from a previous response to paginate through additional results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Challenge Search](/model/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/model/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/model/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/image-search-v3.json`](../../../../catalog/models/douyin/search/image-search-v3.json) · Store page: https://www.sandbase.ai/model/douyin/search/image-search-v3
