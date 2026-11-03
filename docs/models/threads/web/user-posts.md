# Threads User Posts API: pricing, parameters and code examples

`threads/web/user-posts` · data API · Threads · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns a list of posts from a specified Threads account. Accepts a user identifier and an optional pagination cursor to retrieve subsequent pages of data.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/user-posts", "user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/user-posts', {'user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/user-posts", {
  "user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/user-posts", sandbase.Params{
	"user_id": "example",
})
```

Same call via the path form: `POST /v1/api/threads/web/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User ID, for example: 63625256886, can be obtained from user profile API  |
| `end_cursor` | string |  | Pagination cursor (optional), used to get next page data  |

## Details

Returns a list of text posts from a Threads account. It needs the numeric `user_id` of the account and takes an optional `end_cursor` to fetch the next page.

### Use cases

- Pull the latest posts from a news or brand account on Threads.
- Archive the caption text and short codes of an account's posts for later review.
- Track which links a publisher shares by reading the caption text of each post.
- Page through an account's older posts by passing the cursor from the previous response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "63625256886"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID, for example: 63625256886, can be obtained from user profile API |
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
          "id": "4022095224599806479",
          "thread_header_context": null,
          "thread_items": [
            {
              "__typename": "XDTThreadItem",
              "line_type": "none",
              "post": {
                "accessibility_caption": "How NATO states on the Black Sea are being drawn into Ukraine war escalation",
                "audio": null,
                "caption": {
                  "has_translation": null,
                  "pk": "18121968424969344",
                  "text": "How NATO states on the Black Sea are being drawn into Ukraine war escalation reu…"
                },
                "caption_add_on": null,
                "caption_is_edited": false,
                "carousel_media": null,
                "code": "DfRWkv7EQIP",
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                }
              },
              "should_show_ephemeral_post_timer": null
            }
          ],
          "thread_type": "thread"
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
| `mediaData.edges[]` | One entry per thread in the account's post list. |
| `mediaData.edges[].node.id` | ID of the thread, returned as a string. |
| `mediaData.edges[].node.thread_type` | Type of the thread. The sample value is `thread`. |
| `mediaData.edges[].node.thread_items[].post.caption.text` | Text of the post. Long text may be cut, and links appear as short URLs. |
| `mediaData.edges[].node.thread_items[].post.caption.pk` | Numeric ID of the caption, returned as a string. |
| `mediaData.edges[].node.thread_items[].post.code` | Short code of the post. It is the code that identifies the post on Threads. |
| `mediaData.edges[].node.thread_items[].post.accessibility_caption` | Alt-text style description of the post. It is `null` when none is set. |
| `mediaData.edges[].node.thread_items[].post.caption_is_edited` | `true` if the caption was edited after posting. |
| `mediaData.page_info.has_next_page` | `true` if more posts are available on another page. |
| `mediaData.page_info.end_cursor` | Cursor for the next page. It is `null` when there is no further page. |

### Notes

- Get `user_id` from [Threads User Profile](/apis/threads/web/user-info). The example value is `63625256886`.
- To get the next page, send the `end_cursor` from `mediaData.page_info` as the `end_cursor` parameter. In the sample response it is `null` and `has_next_page` is `false`.
- For details on a single post, call [Threads Post Detail](/apis/threads/web/post-detail).
- To see what an account replied to others, use [Threads User Replies](/apis/threads/web/user-replies).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Threads Post Detail](/apis/threads/web/post-detail): Returns detailed information for a specific Threads post using its numeric ID.
- [Threads Post Detail (V2)](/apis/threads/web/post-detail-v2): Returns detailed information for a specific Threads post.
- [Threads Profile Search](/apis/threads/web/search-profiles): Searches Threads user profiles based on a specified text query string.

---
Machine-readable: [`catalog/models/threads/web/user-posts.json`](../../../../catalog/models/threads/web/user-posts.json) · Store page: https://www.sandbase.ai/model/threads/web/user-posts
