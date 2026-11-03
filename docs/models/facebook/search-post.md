# Facebook Post Search API: pricing, parameters and code examples

`facebook/search-post` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Search public Facebook posts by keyword with optional inclusive date-range filters and cursor pagination. Use it to find topic-related posts or continue a time-bounded public-content search.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/search-post", "keyword": "iphone"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/search-post', {'keyword': 'iphone'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/search-post", {
  "keyword": "iphone"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/search-post", sandbase.Params{
	"keyword": "iphone",
})
```

Same call via the path form: `POST /v1/api/facebook/search-post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor for fetching the next set of results.  |
| `endDate` | string |  | End date for the search range (inclusive), formatted as yyyy-MM-dd.  |
| `keyword` | string | yes | Keyword to search for in public posts. Supports basic text matching.  |
| `startDate` | string |  | Start date for the search range (inclusive), formatted as yyyy-MM-dd.  |

## Details

Returns public Facebook posts that match a keyword. Each result includes the post text, author, reaction counts, a Unix timestamp and the post URL. The only required input is `keyword`.

### Use cases

- Track public posts that mention a product such as `iphone` and see how people talk about it.
- Find resale or marketplace-style posts in Facebook groups and read the prices in the post text.
- Collect posts from a set date window by combining `startDate` and `endDate`.
- Rank posts on a topic by `reactions_count`, `comments_count` and `reshare_count` to find the ones with the most engagement.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/search-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "iphone"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword to search for in public posts. Supports basic text matching. |
| `cursor` | string | No | Pagination cursor for fetching the next set of results. |
| `endDate` | string | No | End date for the search range (inclusive), formatted as yyyy-MM-dd. |
| `startDate` | string | No | Start date for the search range (inclusive), formatted as yyyy-MM-dd. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cursor": "{\"page_number\": 0, \"flow_cursors_serialized\": {\"INTERNAL_DEBUG_MODULE\": \"{}\", \"S…",
  "results": [
    {
      "album_preview": [
        {
          "id": "10247538089934137",
          "image_file_uri": "https://scontent.fbts7-1.fna.fbcdn.net/v/t51.82787-15/881518759_1814603034459415…",
          "type": "photo",
          "url": "https://www.facebook.com/photo.php?fbid=10247538089934137&set=a.1021736408468286…"
        }
      ],
      "associated_group": null,
      "associated_group_id": null,
      "attached_event": null,
      "attached_group": null,
      "attached_post": null,
      "attached_post_url": null,
      "author": {
        "delegate_page_id": null,
        "id": "pfbid0o7seBmPbqJSH3mNoByH3PqufHNfsWWDNHpVQWw3ug1e7RRARyYDw89Q6CKrwgRyWl",
        "name": "Erin Jimenez",
        "profile_picture_url": "https://scontent.fbts7-1.fna.fbcdn.net/v/t39.30808-1/482276981_10237393528566443…",
        "url": "https://www.facebook.com/pfbid0o7seBmPbqJSH3mNoByH3PqufHNfsWWDNHpVQWw3ug1e7RRARy…"
      },
      "author_title": null,
      "authors": [
        {
          "delegate_page_id": null,
          "id": "pfbid0o7seBmPbqJSH3mNoByH3PqufHNfsWWDNHpVQWw3ug1e7RRARyYDw89Q6CKrwgRyWl",
          "name": "Erin Jimenez",
          "profile_picture_url": "https://scontent.fbts7-1.fna.fbcdn.net/v/t39.30808-1/482276981_10237393528566443…",
          "url": "https://www.facebook.com/pfbid0o7seBmPbqJSH3mNoByH3PqufHNfsWWDNHpVQWw3ug1e7RRARy…"
        }
      ],
      "comments_count": 0,
      "comments_id": "10247538090374148"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results[]` | List of matching posts. Each item is one post. |
| `results[].message` | Text of the post. `message_rich` holds the same text in this response. |
| `results[].post_id` | ID of the post. `comments_id` and `shares_id` carry the same value in these results. |
| `results[].url` | Link to the post on Facebook. |
| `results[].timestamp` | Time the post was made, as a Unix timestamp in seconds. |
| `results[].author.name / results[].author.id / results[].author.url` | Name, ID and profile link of the account that wrote the post. |
| `results[].reactions_count` | Total number of reactions on the post. |
| `results[].reactions.like / reactions.love / reactions.care / reactions.haha / reactions.wow / reactions.sad / reactions.angry` | Count of each reaction type. The keys sit under `results[].reactions`. |
| `results[].comments_count / results[].reshare_count` | Number of comments and number of reshares on the post. |
| `results[].associated_group.name` | Name of the group the post was made in. It is `null` when the post is not in a group. |
| `results[].album_preview[].image_file_uri` | Image link for each photo in the post's album preview. `images_count` gives the number of images in the post. |

### Notes

- Use `startDate` and `endDate` in `yyyy-MM-dd` format. Both dates are inclusive.
- For the next page, pass the top-level `cursor` value from the response as the `cursor` parameter.
- To read the full comment thread of a result, call [Facebook Post Comments](/apis/facebook/post-comments) with the post.
- To read more posts from one group, use [Facebook Group Posts](/apis/facebook/group-posts).

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/search-post.json`](../../../catalog/models/facebook/search-post.json) · Store page: https://www.sandbase.ai/model/facebook/search-post
