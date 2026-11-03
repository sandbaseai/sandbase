# Hacker News Story API: pricing, parameters and code examples

`hacker-news/story` · data API · Hacker News · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0015 per call · **Modes:** sync

Get a Hacker News story by id - title, link, author, points, and comment count as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0015**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hacker-news/story", "id": "47340079"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hacker-news/story', {'id': '47340079'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hacker-news/story", {
  "id": "47340079"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hacker-news/story", sandbase.Params{
	"id": "47340079",
})
```

Same call via the path form: `POST /v1/api/hacker-news/story` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Hacker News story id, e.g. "47340079".  |

## Details

Returns the details of one Hacker News story: title, linked URL, author, points, and comment count. It needs the story `id` as input.

### Use cases

- Show the current points and comment count for a story in a dashboard or alert.
- Resolve a Hacker News story id from a saved link into its title and target URL.
- Track how a story's `points` and `comments` change by calling the API on a schedule.
- Check who submitted a story and when it was posted.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/hacker-news/story" \
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
    "author": "usefulposter",
    "comments": 1668,
    "createdUtc": 1773257369,
    "id": "47340079",
    "permalink": "https://news.ycombinator.com/item?id=47340079",
    "points": 4229,
    "title": "Don't post generated/AI-edited comments. HN is for conversation between humans",
    "url": "https://news.ycombinator.com/newsguidelines.html#generated"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.title` | Title of the story as posted on Hacker News. |
| `data.url` | Link the story points to. It can be an external page or a Hacker News page. |
| `data.permalink` | Link to the story's discussion page on Hacker News. |
| `data.author` | Username of the person who submitted the story. |
| `data.points` | Number of points the story has. |
| `data.comments` | Number of comments on the story. |
| `data.createdUtc` | Time the story was created, as a Unix timestamp in seconds (UTC). |
| `data.id` | The story id as a string. |
| `found` | `true` when the story was found. `false` when no story matches the `id`. |

### Notes

- Take the `id` from the `item?id=` part of a Hacker News story link, for example `47340079` in `https://news.ycombinator.com/item?id=47340079`.
- The result is in `outputs[0].data`. A missing story returns `found: false` instead of an error.
- To read the discussion, call [Hacker News Story Comments](/apis/hacker-news/story-comments) next.
- To look up a submitter, pass `data.author` to [Hacker News Profile](/apis/hacker-news/profile).

### Pricing

Billed at the actual cost of each call, about $0.0015 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hacker-news/story.json`](../../../catalog/models/hacker-news/story.json) · Store page: https://www.sandbase.ai/model/hacker-news/story
