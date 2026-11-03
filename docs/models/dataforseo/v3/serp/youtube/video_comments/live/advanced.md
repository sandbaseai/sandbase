# DataForSEO YouTube Video Comments API: pricing, parameters and code examples

`dataforseo/v3/serp/youtube/video_comments/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Top-level comments on a YouTube video by video id, with author, text, likes, reply counts and timestamps.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/youtube/video_comments/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/youtube/video_comments/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/youtube/video_comments/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/youtube/video_comments/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/youtube/video_comments/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video_id` | string |  | YouTube video id, e.g. "dQw4w9WgXcQ".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns top-level comments for a YouTube video. Send the `video_id`, plus an optional `location_code` and `language_code`. The response lists each comment's author, like count, reply count and a relative publication date, along with the video's total comment count.

### Use cases

- Pull the most-liked comments on a competitor's video to see what viewers react to.
- Track the total comment count of a video over repeated calls to measure engagement.
- Collect commenter channel URLs to find active fans or potential collaborators.
- Sort comments by reply count to find the threads that start the most discussion.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/youtube/video_comments/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |
| `video_id` | string | No | YouTube video id, e.g. "dQw4w9WgXcQ". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "serp",
        "device": "desktop",
        "function": "live",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "youtube",
        "se_type": "video_comments"
      },
      "id": "11030829-1614-0139-0000-1c3ba5adbc30",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
          "comments_count": 2461259,
          "datetime": "2026-11-03 08:29:39 +00:00",
          "item_types": [
            "youtube_comment"
          ],
          "items": [
            {
              "author_name": "@LK-ht7qz",
              "author_thumbnail": "https://yt3.ggpht.com/RJnrz4JwDmHNgtFdnVdJ6FKLiuo59IuHkY6bvqaEJM0mxTSlq0GKQs_ItA…",
              "author_url": "https://www.youtube.com/@LK-ht7qz",
              "likes_count": 220000,
              "publication_date": "6 years ago",
              "rank_absolute": 1,
              "rank_group": 1,
              "reply_count": 613
            }
          ],
          "items_count": 20,
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "6.6753 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "6.7705 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].comments_count` | Total number of comments on the video. |
| `tasks[].result[].items_count` | Number of comments returned in this response. |
| `tasks[].result[].check_url` | YouTube watch URL for the video that was queried. |
| `tasks[].result[].items[].author_name` | Handle of the comment author, for example `@LK-ht7qz`. |
| `tasks[].result[].items[].author_url / tasks[].result[].items[].author_thumbnail` | Link to the author's YouTube channel and to their profile image. |
| `tasks[].result[].items[].likes_count` | Number of likes on the comment. |
| `tasks[].result[].items[].reply_count` | Number of replies to the comment. |
| `tasks[].result[].items[].publication_date` | Relative age of the comment, as text such as `6 years ago`. |
| `tasks[].result[].items[].rank_absolute / tasks[].result[].items[].rank_group` | Position of the comment in the returned list, starting at 1. |
| `tasks[].result[].datetime` | Time of the request in UTC, formatted as `YYYY-MM-DD HH:MM:SS +00:00`. |

### Notes

- The `video_id` is the value after `v=` in a YouTube watch URL, such as `dQw4w9WgXcQ` in `https://www.youtube.com/watch?v=dQw4w9WgXcQ`.
- Results are in `tasks[].result[]`. Each call sends one task, so read the first entry.
- The sample response has `items_count` of 20, while `comments_count` shows the video has millions of comments. Each call returns only a part of them.
- `publication_date` is relative text, not an exact timestamp.

### Pricing

Billed at the actual cost of each call, about $0.002 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/youtube/video_comments/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/youtube/video_comments/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/youtube/video_comments/live/advanced
