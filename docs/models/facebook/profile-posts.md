# Facebook Get Profile Posts API: pricing, parameters and code examples

`facebook/profile-posts` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get public posts for a Facebook profile ID with cursor pagination. Use it to browse a known profile's public posting history or continue through subsequent post pages.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/profile-posts", "profileId": "4"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/profile-posts', {'profileId': '4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/profile-posts", {
  "profileId": "4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/profile-posts", sandbase.Params{
	"profileId": "4",
})
```

Same call via the path form: `POST /v1/api/facebook/profile-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor for fetching the next set of results.  |
| `profileId` | string | yes | The unique Facebook profile ID.  |

## Details

Returns a page of public posts for a Facebook profile, with message text, reaction counts, comment and share counts, media, and top comments. It needs a Facebook profile ID in `profileId`. The response includes a `cursor` for the next page.

### Use cases

- Pull the recent posting history of a public figure to track what they publish and how people react.
- Compare reaction mix (`like`, `love`, `haha`, `angry`) across posts to see which topics get which responses.
- Collect post URLs and `post_id` values to feed into comment or transcript lookups.
- Monitor a brand or executive profile for new posts that include external links or attached posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/profile-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"profileId": "4"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `profileId` | string | Yes | The unique Facebook profile ID. |
| `cursor` | string | No | Pagination cursor for fetching the next set of results. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cursor": "Cg8Ob3JnYW5pY19jdXJzb3IJAAACGkFRSFRyRXRuWmxKaUJ3SXVGNFpFaVg0RkxtSW9PX293c1VHaGdM…",
  "results": [
    {
      "album_preview": [
        {
          "id": "10118155440653191",
          "image_file_uri": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.99422-6/885149443_1824040011869927_32…",
          "type": "photo",
          "url": "https://www.facebook.com/photo.php?fbid=10118155440653191&set=a.612287952871&typ…"
        }
      ],
      "associated_group": null,
      "associated_group_id": null,
      "attached_event": null,
      "attached_group": null,
      "attached_post": null,
      "attached_post_url": null,
      "author": {
        "delegate_page_id": "111895498378878",
        "id": "4",
        "name": "Mark Zuckerberg",
        "profile_picture_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.30808-1/824997889_10117988912521901_6…",
        "url": "https://www.facebook.com/zuck"
      },
      "author_title": null,
      "authors": [
        {
          "delegate_page_id": "111895498378878",
          "id": "4",
          "name": "Mark Zuckerberg",
          "profile_picture_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.30808-1/824997889_10117988912521901_6…",
          "url": "https://www.facebook.com/zuck"
        }
      ],
      "comments_count": 15054,
      "comments_id": "10118155444854771"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `cursor` | Pagination cursor. Send it as `cursor` in the next request to get the next page of posts. |
| `results[].post_id` | ID of the post. Also appears as `comments_id` and `shares_id` in the sample. |
| `results[].message` | Text of the post. Long text may be cut in the response. |
| `results[].url` | Public Facebook URL of the post. |
| `results[].timestamp` | Post creation time as a Unix timestamp in seconds. |
| `results[].reactions_count` | Total number of reactions on the post. |
| `results[].reactions.like / reactions.love / reactions.haha / reactions.care / reactions.wow / reactions.sad / reactions.angry` | Count of each reaction type on the post. |
| `results[].comments_count / results[].reshare_count` | Number of comments and number of reshares for the post. |
| `results[].author.id / results[].author.name / results[].author.url` | ID, display name, and profile URL of the post author. |
| `results[].top_comments[].text` | Text of a top comment on the post. Each entry also has `author.name`, `created_time`, and `id`. |
| `results[].attached_post.url` | URL of another post attached to this one. It is `null` when nothing is attached. |

### Notes

- Use the Facebook profile ID as `profileId`. For example, `4` is the profile at `https://www.facebook.com/zuck`. If you only have a profile URL, try [Facebook Profile ID](/apis/facebook/profile-id).
- For the next page, pass the returned `cursor` value as `cursor` with the same `profileId`.
- Fields such as `video`, `image`, and `album_preview` are `null` when the post has no matching media. `images_count` is `null` when the post has no images.
- To get all comments on a post, call [Facebook Post Comments](/apis/facebook/post-comments).

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/profile-posts.json`](../../../catalog/models/facebook/profile-posts.json) · Store page: https://www.sandbase.ai/model/facebook/profile-posts
