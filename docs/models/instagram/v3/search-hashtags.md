# Instagram Hashtag Search (V3) API: pricing, parameters and code examples

`instagram/v3/search-hashtags` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Searches Instagram hashtags by keyword and returns matching hashtag names, IDs, and media counts. Supports pagination via rank tokens.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/search-hashtags", "query": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/search-hashtags', {'query': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/search-hashtags", {
  "query": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/search-hashtags", sandbase.Params{
	"query": "openai",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/search-hashtags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword  |
| `rank_token` | string |  | Rank token from previous search response for pagination  |

## Details

Searches Instagram hashtags by keyword and returns matching hashtag names, IDs, and media counts. It needs one input: a search keyword in `query`.

### Use cases

- Compare the `media_count` of similar hashtags to pick which tags to use in a campaign.
- Find spin-off or misspelled variants of a brand or topic keyword, such as `openair` next to `openai`.
- Collect hashtag IDs and names for a list of keywords to feed a hashtag monitoring job.
- Check whether a hashtag exists for a new product name before launch.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/search-hashtags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword |
| `rank_token` | string | No | Rank token from previous search response for pagination |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "3f439430dc5ce",
  "count": 20,
  "hashtags": [
    {
      "id": "17841553213093056",
      "media_count": 2360486,
      "name": "openai",
      "profile_pic_url": null
    }
  ],
  "items": [
    {
      "id": "17841553213093056",
      "media_count": 2360486,
      "name": "openai",
      "profile_pic_url": null
    }
  ],
  "rank_token": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `hashtags[].name` | Hashtag text without the `#` sign. |
| `hashtags[].id` | Instagram ID of the hashtag, returned as a string. |
| `hashtags[].media_count` | Number of posts that use the hashtag. |
| `hashtags[].profile_pic_url` | Image URL for the hashtag. It is `null` in the sample response. |
| `items[].name / items[].id / items[].media_count` | The same hashtag entries as in `hashtags`, repeated under `items`. |
| `count` | Number of hashtags returned in this response. |
| `rank_token` | Token for requesting the next page of results. It is `null` in the sample response. |

### Notes

- Pass the `rank_token` from a response into the next request along with the same `query` to get more results. When `rank_token` is `null`, the response gave no token for another page.
- `hashtags` and `items` hold the same entries, so you can read either one.
- To list posts under a hashtag, call [Instagram Hashtag Posts (V3)](/apis/instagram/v3/hashtag-posts).
- To search across users, hashtags, and places in one call, use [Instagram General Search (V3)](/apis/instagram/v3/general-search).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/search-hashtags.json`](../../../../catalog/models/instagram/v3/search-hashtags.json) · Store page: https://www.sandbase.ai/model/instagram/v3/search-hashtags
