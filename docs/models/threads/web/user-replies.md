# Threads User Replies API: pricing, parameters and code examples

`threads/web/user-replies` · data API · Threads · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns a list of replies posted by a specific Threads user. Query replies using a target user identifier and an optional pagination cursor.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/user-replies", "user_id": "63625256886"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/user-replies', {'user_id': '63625256886'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/user-replies", {
  "user_id": "63625256886"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/user-replies", sandbase.Params{
	"user_id": "63625256886",
})
```

Same call via the path form: `POST /v1/api/threads/web/user-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User ID, for example: 63625256886  |
| `end_cursor` | string |  | Pagination cursor (optional), used to get next page data  |

## Details

Returns a list of Threads posts from a user's replies tab. It needs a numeric `user_id` and accepts an optional `end_cursor` to fetch the next page.

### Use cases

- Review what a news account says in reply to other users' threads.
- Collect the text of a user's recent replies for topic or sentiment analysis.
- Match reply `code` values to post URLs to link back to the original conversation.
- Page through a user's reply history with `end_cursor` and `has_next_page`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/user-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "63625256886"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID, for example: 63625256886 |
| `end_cursor` | string | No | Pagination cursor (optional), used to get next page data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "mediaData": {
    "edges": [
      {
        "__typename": "XDTUserTextPostsResponseEdge",
        "cursor": "",
        "node": {
          "__typename": "XDTThread",
          "id": "3850504812358707776",
          "thread_items": [
            {
              "__typename": "XDTThreadItem",
              "post": {
                "accessibility_caption": null,
                "audio": null,
                "caption": {
                  "has_translation": null,
                  "pk": "17947992846069632",
                  "text": "Iran's military command said the world should be prepared for oil to hit $200 a …"
                },
                "caption_add_on": null,
                "caption_is_edited": false,
                "carousel_media": null,
                "code": "DVvvbnakqpA",
                "gen_ai_detection_method": null
              }
            }
          ]
        }
      }
    ],
    "page_info": {
      "end_cursor": null,
      "has_next_page": false,
      "has_previous_page": false,
      "start_cursor": null
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `mediaData.edges[].node.id` | ID of the thread that holds the reply. |
| `mediaData.edges[].node.thread_items[].post.caption.text` | Text of the reply. Long text may be cut and can end with a link. |
| `mediaData.edges[].node.thread_items[].post.caption.pk` | ID of the caption object for the reply. |
| `mediaData.edges[].node.thread_items[].post.code` | Short post code, the kind Threads uses in post URLs. |
| `mediaData.edges[].node.thread_items[].post.caption_is_edited` | `true` if the reply text was edited after posting. |
| `mediaData.edges[].node.thread_items[].post.carousel_media` | Media items attached to the reply. It is `null` when the reply has no carousel. |
| `mediaData.edges[].cursor` | Cursor value attached to each edge. It was an empty string in this response. |
| `mediaData.page_info.end_cursor` | Cursor to pass as `end_cursor` for the next page. It is `null` when no more pages exist. |
| `mediaData.page_info.has_next_page` | `true` if more replies can be fetched. |

### Notes

- To get the next page, send the `mediaData.page_info.end_cursor` value as `end_cursor` along with the same `user_id`.
- If you only have a username, look up the numeric ID with [Threads User Profile](/apis/threads/web/user-info) first.
- Use [Threads Post Detail](/apis/threads/web/post-detail) to load a full post, and [Threads User Posts](/apis/threads/web/user-posts) for the user's own top-level posts.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Threads Post Detail](/apis/threads/web/post-detail): Returns detailed information for a specific Threads post using its numeric ID.
- [Threads Post Detail (V2)](/apis/threads/web/post-detail-v2): Returns detailed information for a specific Threads post.
- [Threads Profile Search](/apis/threads/web/search-profiles): Searches Threads user profiles based on a specified text query string.

---
Machine-readable: [`catalog/models/threads/web/user-replies.json`](../../../../catalog/models/threads/web/user-replies.json) · Store page: https://www.sandbase.ai/model/threads/web/user-replies
