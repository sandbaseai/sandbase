# Instagram General Search (V2) API: pricing, parameters and code examples

`instagram/v2/general-search` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/general-search", "keyword": "cat"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/general-search', {'keyword': 'cat'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/general-search", {
  "keyword": "cat"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/general-search", sandbase.Params{
	"keyword": "cat",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/general-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword  |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Query Instagram posts and related media content by specifying a `keyword`. Use `pagination_token` to retrieve subsequent pages of results.

### Use cases

- Discover trending media posts and reels related to specific topics.
- Monitor engagement metrics and captions across keyword-specific posts.
- Identify active creators producing content around target search terms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/general-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "cat"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `pagination_token` | string | No | Pagination token from previous response |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "items": [
      {
        "caption_is_edited": false,
        "coauthor_producer_can_see_organic_insights": false,
        "comment_count": 1150,
        "device_timestamp": 908953868710284,
        "filter_type": 0,
        "id": "3773673916037486064",
        "like_and_view_counts_disabled": false,
        "like_count": 54439,
        "media_name": "reel",
        "media_type": 2,
        "caption": {
          "content_type": "comment",
          "id": "3773673916037486064",
          "private_reply_status": 0,
          "status": "Active",
          "text": "#catsoftheday #cat #cutecats #catlovers❤️",
          "type": 1
        },
        "clips_metadata": {
          "audio_canonical_id": "18438577903101394",
          "audio_type": "original_sounds",
          "professional_clips_upsell_type": 0
        },
        "user": {
          "follower_count": 240938,
          "full_name": "𝐂𝐀𝐓𝐘 𝐂𝐑𝐔𝐒𝐇",
          "id": "47539634885",
          "profile_pic_id": "3737640702256854188",
          "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-19/562433378_18068299718586…",
          "type": "XDTUserDict"
        }
      }
    ]
  }
}
```

### Notes

- Pass `pagination_token` from a previous response to paginate through search results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.
- [Instagram Highlight Stories](/model/instagram/v2/highlight-stories): Returns all stories contained within a specific Instagram highlight using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v2/general-search.json`](../../../../catalog/models/instagram/v2/general-search.json) · Store page: https://www.sandbase.ai/model/instagram/v2/general-search
