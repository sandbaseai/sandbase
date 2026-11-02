# TikTok Photo Search API: pricing, parameters and code examples

`tiktok/web/search-photo` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Searches TikTok photo posts matching a query keyword. Returns post details, author statistics, music metadata, and engagement metrics with cursor pagination support.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/search-photo", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/search-photo', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/search-photo", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/search-photo", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/search-photo` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page, it is recommended to keep the default value 20. default `20` |
| `offset` | integer |  | Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor. default `0` |
| `keyword` | string | yes | Search keyword  |
| `search_id` | string |  | Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request. default `""` |

## Details

Look up TikTok photo posts using a search term specified in `keyword`. Supports pagination controls using `offset` and `search_id`.

### Use cases

- Discover photo posts related to specific topics or keywords on TikTok.
- Analyze engagement metrics and play counts for trending photo content.
- Inspect author profiles and music metadata linked to search results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/search-photo" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `count` | integer | No | Number per page, it is recommended to keep the default value 20. |
| `offset` | integer | No | Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor. |
| `search_id` | string | No | Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "item_list": [
    {
      "CategoryType": 120,
      "createTime": 1790707203,
      "desc": "From personal agents and collaborative work spaces to a new affordable frontier model and…",
      "id": "7691028733624372493",
      "itemCommentStatus": 0,
      "textLanguage": "en",
      "textTranslatable": true,
      "titleLanguage": "un",
      "titleTranslatable": false,
      "author": {
        "id": "7256178298626032683",
        "nickname": "<user>",
        "privateAccount": false,
        "verified": true
      },
      "authorStats": {
        "diggCount": 392,
        "followerCount": 1000000,
        "followingCount": 2,
        "friendCount": 0,
        "heartCount": 6500000,
        "videoCount": 378
      },
      "authorStatsV2": {
        "diggCount": "392",
        "followerCount": "1000000",
        "followingCount": "2",
        "friendCount": "0",
        "heartCount": "6500000",
        "videoCount": "378"
      },
      "music": {
        "authorName": "vowl. & Sace",
        "duration": 60,
        "id": "7145154069236041729",
        "title": "2000"
      },
      "stats": {
        "collectCount": 180,
        "commentCount": 72,
        "diggCount": 1119,
        "playCount": 31700,
        "shareCount": 104
      }
    }
  ]
}
```

### Notes

- Set `offset` to 0 for initial calls and supply the updated cursor for subsequent pages.
- Leave `search_id` empty on the first query, then supply the value returned from the previous response.
- The `count` parameter specifies the number of items per page, with 20 recommended.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/search-photo.json`](../../../../catalog/models/tiktok/web/search-photo.json) · Store page: https://www.sandbase.ai/model/tiktok/web/search-photo
