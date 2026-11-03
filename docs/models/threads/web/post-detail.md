# Threads Post Detail API: pricing, parameters and code examples

`threads/web/post-detail` · data API · Threads · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specific Threads post using its numeric ID. Call this endpoint to inspect post content and metadata from the web interface.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/post-detail", "post_id": "3349029093483693129"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/post-detail', {'post_id': '3349029093483693129'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/post-detail", {
  "post_id": "3349029093483693129"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/post-detail", sandbase.Params{
	"post_id": "3349029093483693129",
})
```

Same call via the path form: `POST /v1/api/threads/web/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_id` | string | yes | Post ID (numeric only), for example: 3349029093483693129, can be obtained from other APIs. If using URL to get, call /fetch_post_detail_v2 API.  |

## Details

Returns the content and metadata of one Threads post. It needs the numeric `post_id` of the post.

### Use cases

- Read the caption text of a single Threads post from its ID.
- Check whether a post caption was edited with `caption_is_edited`.
- Get the short post `code` for a post you only know by numeric ID.
- Confirm a post exists and has the type `thread` before you store it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_id": "3349029093483693129"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_id` | string | Yes | Post ID (numeric only), for example: 3349029093483693129, can be obtained from other APIs. If using URL to get, call /fetch_post_detail_v2 API. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cursor": "",
  "node": {
    "__typename": "XDTThread",
    "header": null,
    "id": "3349029093483693129",
    "thread_header_context": null,
    "thread_items": [
      {
        "line_type": "none",
        "post": {
          "accessibility_caption": null,
          "audio": null,
          "caption": {
            "has_translation": null,
            "pk": "18062882737479481",
            "text": "🦙 Today’s the day! Introducing Meta Llama 3: the next generation of our state-of…"
          },
          "caption_add_on": null,
          "caption_is_edited": false,
          "carousel_media": null,
          "code": "C56JDdzi0RJ",
          "fbid": "18062879098479481"
        },
        "should_show_ephemeral_post_timer": null
      }
    ],
    "thread_type": "thread"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `node.id` | Numeric ID of the thread. It matches the `post_id` you sent. |
| `node.thread_type` | Type of the returned node. The sample value is `thread`. |
| `node.thread_items[].post.caption.text` | Text of the post caption. Long captions may include emoji and line breaks. |
| `node.thread_items[].post.caption.pk` | ID of the caption object. |
| `node.thread_items[].post.caption_is_edited` | Boolean. It is `true` when the caption was edited after posting. |
| `node.thread_items[].post.code` | Short alphanumeric code for the post. |
| `node.thread_items[].post.fbid` | Another numeric ID for the post. |
| `node.thread_items[].post.carousel_media / node.thread_items[].post.audio` | Media details. Both are `null` when the post has no carousel or audio. |

### Notes

- `post_id` must be numeric only. Get it from other Threads APIs, such as [Threads User Posts](/apis/threads/web/user-posts) or [Threads Recent Content Search](/apis/threads/web/search-recent).
- To look up a post by URL instead of ID, use [Threads Post Detail (V2)](/apis/threads/web/post-detail-v2).
- `cursor` came back as an empty string in this response.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Threads Post Detail (V2)](/apis/threads/web/post-detail-v2): Returns detailed information for a specific Threads post.
- [Threads Profile Search](/apis/threads/web/search-profiles): Searches Threads user profiles based on a specified text query string.
- [Threads Recent Content Search](/apis/threads/web/search-recent): Searches recent Threads content matching a specified keyword query.

---
Machine-readable: [`catalog/models/threads/web/post-detail.json`](../../../../catalog/models/threads/web/post-detail.json) · Store page: https://www.sandbase.ai/model/threads/web/post-detail
