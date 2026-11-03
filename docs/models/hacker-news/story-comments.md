# Hacker News Story Comments API: pricing, parameters and code examples

`hacker-news/story-comments` · data API · Hacker News · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0015 per call · **Modes:** sync

List the comments on a Hacker News story by id - text, author, and timestamp as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0015**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hacker-news/story-comments", "id": "47340079"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hacker-news/story-comments', {'id': '47340079'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hacker-news/story-comments", {
  "id": "47340079"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hacker-news/story-comments", sandbase.Params{
	"id": "47340079",
})
```

Same call via the path form: `POST /v1/api/hacker-news/story-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Hacker News story id, e.g. "47340079".  |

## Details

Returns the comments on a Hacker News story as a flat list. Each comment has its author, text, timestamp, and the id of the item it replies to. You send the story `id` as input.

### Use cases

- Pull the full discussion of a Hacker News post to run sentiment or topic analysis.
- Rebuild the reply tree of a thread using the `id` and `parentId` of each comment.
- Track what a specific user said on a story by filtering on `author`.
- Archive the text of a discussion together with permalinks back to the original comments.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/hacker-news/story-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "47340079"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Hacker News story id, e.g. "47340079". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "comments": [
      {
        "author": "fcpguru",
        "createdUtc": 1773257417,
        "id": "47340089",
        "parentId": "47340079",
        "permalink": "https://news.ycombinator.com/item?id=47340089",
        "postId": "47340079",
        "text": "i agree but how is this ever going to be enforced verified? https://proofofhuman…"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.comments[].id` | Id of the comment, as a string. |
| `data.comments[].author` | Hacker News username of the person who wrote the comment. |
| `data.comments[].text` | Text of the comment. |
| `data.comments[].createdUtc` | Time the comment was posted, as a Unix timestamp in seconds. |
| `data.comments[].parentId` | Id of the item this comment replies to. It equals the story id for top-level comments and another comment's `id` for replies. |
| `data.comments[].postId` | Id of the story the comment belongs to. |
| `data.comments[].permalink` | Link to the comment on news.ycombinator.com. |
| `found` | `true` when the story was found. A lookup that finds nothing returns `found: false`. |

### Notes

- The `id` is the number in the story URL, for example `item?id=47340079`.
- The list is flat. Replies are linked to their parent through `parentId`, so group by `parentId` to build the thread tree.
- To get the title, score, or link of the story itself, call [Hacker News Story](/apis/hacker-news/story).
- To find a story id by keyword, call [Hacker News Search](/apis/hacker-news/search).

### Pricing

Billed at the actual cost of each call, about $0.0015 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hacker-news/story-comments.json`](../../../catalog/models/hacker-news/story-comments.json) · Store page: https://www.sandbase.ai/model/hacker-news/story-comments
