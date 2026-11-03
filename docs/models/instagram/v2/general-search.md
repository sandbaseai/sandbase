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

Returns Instagram posts and reels that match a search `keyword`. Each item includes the caption, hashtags, comment count and audio details. Send a `keyword` and optionally a `pagination_token` to get the next page.

### Use cases

- Find reels and posts that use a topic keyword such as `cat`.
- Collect the hashtags that creators attach to posts about a topic.
- Rank posts for a keyword by `comment_count` to spot those with the most discussion.
- Group results by `clips_metadata.audio_type` to see how many posts use original sounds.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/general-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "cat"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `pagination_token` | string | No | Pagination token from previous response |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "count": 8,
    "items": [
      {
        "ai_interactive_embodiment_attachment_style_info": null,
        "ai_label_info": null,
        "are_remixes_crosspostable": true,
        "attribution": null,
        "audience": null,
        "audio": null,
        "autodub_status": null,
        "basel_encoding_timeout": null,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boosted_by_sponsor": null,
        "boosted_post_id": null
      }
    ]
  },
  "pagination_token": "GU1VCxop…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of items in this page of results. |
| `data.items[].code` | Short post code for the item. Use it to identify the post on Instagram. |
| `data.items[].caption.hashtags` | List of hashtags in the post caption, each with a leading `#`. |
| `data.items[].caption.created_at / data.items[].caption.created_at_utc` | Caption creation time as a Unix timestamp in seconds. |
| `data.items[].caption.id` | ID of the caption object. |
| `data.items[].comment_count` | Number of comments on the post. |
| `data.items[].clips_metadata.audio_type` | Type of audio on the reel, for example `original_sounds`. |
| `data.items[].clips_metadata.audio_canonical_id` | ID of the audio track used in the reel. |
| `data.items[].ai_label_info.subtitle_text` | Label text shown for posts flagged as AI content. The field is `null` when no AI label exists. |
| `pagination_token` | Token to pass as `pagination_token` to request the next page. |

### Notes

- Set `keyword` to any search term. Only `keyword` is required.
- To get the next page, repeat the call with the same `keyword` and the `pagination_token` from the previous response.
- Many fields on each item are `null` when they do not apply to the post, such as `carousel_media` on a reel.
- To search only reels, use [Instagram Reels Search](/apis/instagram/v2/search-reels). To search accounts, use [Instagram User Search (V2)](/apis/instagram/v2/search-users).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.
- [Instagram Highlight Stories](/apis/instagram/v2/highlight-stories): Returns all stories contained within a specific Instagram highlight using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v2/general-search.json`](../../../../catalog/models/instagram/v2/general-search.json) · Store page: https://www.sandbase.ai/model/instagram/v2/general-search
