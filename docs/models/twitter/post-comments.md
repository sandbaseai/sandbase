# Twitter Post Comments API: pricing, parameters and code examples

`twitter/post-comments` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get the latest comments for an X (Twitter) post identified by tweet ID, with cursor pagination. Use it to review recent discussion on a known post and continue through additional comment pages.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/post-comments", "tweetId": "1585341984679469056"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/post-comments', {'tweetId': '1585341984679469056'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/post-comments", {
  "tweetId": "1585341984679469056"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/post-comments", sandbase.Params{
	"tweetId": "1585341984679469056",
})
```

Same call via the path form: `POST /v1/api/twitter/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor returned by the previous response.  |
| `tweetId` | string | yes | The unique identifier of the X (Twitter) post.  |

## Details

Returns the latest comments (replies) on an X (Twitter) post. It needs the post's `tweetId`, and it returns a `timeline` list of comments plus cursors for paging.

### Use cases

- Read recent replies under a known post to review how people respond.
- Collect reply text and commenter profiles to analyze sentiment on a post.
- Find commenters with large follower counts who replied to a post.
- Page through a long reply thread by passing the returned cursor back into the next call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tweetId": "1585341984679469056"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tweetId` | string | Yes | The unique identifier of the X (Twitter) post. |
| `cursor` | string | No | Pagination cursor returned by the previous response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "next_cursor": "DAADDAABCgABHWLH-s7WQHYKAAIdWkn2RRqgiQAIAAIAAAACCAADAAAAAAgABAAAAAAKAAUdYvRGxAAn…",
  "prev_cursor": "DAADDAABCgABHWLH-s7WQHYKAAIdWkn2RRqgiQAIAAIAAAABCAADAAAAAAgABAAAAAAKAAUdYvRGxAAn…",
  "status": "ok",
  "timeline": [
    {
      "bookmarks": 0,
      "conversation_id": "1585341984679469056",
      "created_at": "Tue Nov 03 04:31:13 +0000 2026",
      "display_text_range": [
        10
      ],
      "entities": {
        "hashtags": [],
        "symbols": [],
        "timestamps": [],
        "urls": [],
        "user_mentions": [
          {
            "id_str": "44196397",
            "indices": [
              0
            ],
            "name": "Elon Musk",
            "screen_name": "elonmusk"
          }
        ]
      },
      "favorites": 0,
      "in_reply_to_screen_name": "elonmusk",
      "in_reply_to_status_id_str": "1585341984679469056",
      "in_reply_to_user_id_str": "44196397",
      "lang": "en",
      "media": [],
      "quotes": 0
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `timeline[]` | List of comments on the post. Each item is one reply. |
| `timeline[].tweet_id` | ID of the comment itself. |
| `timeline[].text` | Full text of the comment, including the leading @mention. |
| `timeline[].created_at` | Time the comment was posted, in a format like `Tue Nov 03 04:31:13 +0000 2026`. |
| `timeline[].screen_name` | Handle of the user who wrote the comment. |
| `timeline[].conversation_id` | ID of the post the comment belongs to. It matches the `tweetId` you sent. |
| `timeline[].in_reply_to_status_id_str / timeline[].in_reply_to_screen_name` | The tweet and user this comment replies to. It can be another comment instead of the main post. |
| `timeline[].favorites / timeline[].retweets / timeline[].replies / timeline[].quotes / timeline[].bookmarks` | Engagement counts for the comment. |
| `timeline[].views` | View count for the comment, returned as a string. |
| `timeline[].user_info.followers_count` | Follower count of the commenter. Other fields in `user_info` include `avatar`, `location` and the account `created_at`. |
| `next_cursor / prev_cursor` | Cursors for the next and previous pages of comments. |

### Notes

- Pass `next_cursor` from the response as `cursor` in the next request to get more comments.
- The `tweetId` is the numeric ID at the end of a post URL.
- Dates use the format `Tue Nov 03 04:31:13 +0000 2026`.
- Some fields such as `description`, `friends_count` and `source` can be `null`. To fetch the post itself, call [Twitter Tweet Detail](/apis/twitter/web/tweet-detail).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/post-comments.json`](../../../catalog/models/twitter/post-comments.json) · Store page: https://www.sandbase.ai/model/twitter/post-comments
