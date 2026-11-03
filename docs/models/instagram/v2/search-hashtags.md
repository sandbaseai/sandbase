# Instagram Hashtag Search (V2) API: pricing, parameters and code examples

`instagram/v2/search-hashtags` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Search for Instagram hashtags matching a given keyword query. Returns an array of matching hashtag objects containing each hashtag identifier, name, and total media count.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/search-hashtags", "keyword": "cat"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/search-hashtags', {'keyword': 'cat'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/search-hashtags", {
  "keyword": "cat"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/search-hashtags", sandbase.Params{
	"keyword": "cat",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/search-hashtags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword  |

## Details

Returns Instagram hashtags that match a search keyword. Each result has the hashtag ID, its name, and its total media count. The only input is `keyword`.

### Use cases

- Find hashtag variations of a topic, such as `catlife` and `catlovers` for the keyword `cat`.
- Rank related hashtags by `media_count` to pick tags with larger or smaller audiences.
- Power hashtag autocomplete in a social media planning tool.
- Collect hashtag IDs and names to feed into a hashtag posts lookup.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/search-hashtags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "cat"}'
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
  "data": {
    "count": 55,
    "items": [
      {
        "allow_following": false,
        "id": "17841562906103814",
        "media_count": 314739058,
        "name": "cat",
        "profile_pic_url": null
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of hashtags matched for the keyword. |
| `data.items[].id` | Hashtag identifier as a string. |
| `data.items[].name` | Hashtag text, without the `#` sign. |
| `data.items[].media_count` | Total number of media items tagged with this hashtag. |
| `data.items[].allow_following` | Boolean flag. It is `false` for every item in this sample. |
| `data.items[].profile_pic_url` | Image URL for the hashtag. It is `null` in this sample. |

### Notes

- `keyword` is the only parameter. The response shows no pagination parameters.
- Hashtag `id` values are long numeric strings. Keep them as strings.
- To read posts under a hashtag, call [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts).
- To search across media and users for the same keyword, use [Instagram General Search (V2)](/apis/instagram/v2/general-search).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/search-hashtags.json`](../../../../catalog/models/instagram/v2/search-hashtags.json) · Store page: https://www.sandbase.ai/model/instagram/v2/search-hashtags
