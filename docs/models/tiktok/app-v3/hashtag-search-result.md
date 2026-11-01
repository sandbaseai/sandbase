# TikTok Hashtag Search Results

`tiktok/app-v3/hashtag-search-result` · api · TikTok

Returns TikTok hashtag search results matching a specified search keyword. Includes challenge details such as hashtag name, use count, and user count.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/hashtag-search-result", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/hashtag-search-result', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/hashtag-search-result", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/hashtag-search-result", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/hashtag-search-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `20` |
| `offset` | integer |  | Offset default `0` |
| `keyword` | string | yes | Keyword  |

## Details

Look up TikTok hashtag information by passing a search term into `keyword`. Supports pagination controls using `count` and `offset`.

### Use cases

- Look up hashtag usage statistics and popularity on TikTok.
- Discover related challenge tags matching specific search queries.
- Track hashtag adoption metrics across the platform.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/hashtag-search-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `count` | integer | No | Number |
| `offset` | integer | No | Offset |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "challenge_list": [
    {
      "challenge_info": {
        "cha_name": "openai",
        "search_cha_name": "openai",
        "sub_type": 0,
        "type": 1,
        "use_count": 363501,
        "user_count": 363501
      }
    }
  ]
}
```

### Notes

- Specify the query term using `keyword`.
- Manage pagination by setting the `count` and `offset` parameters.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/hashtag-search-result.json`](../../../../catalog/models/tiktok/app-v3/hashtag-search-result.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/hashtag-search-result
