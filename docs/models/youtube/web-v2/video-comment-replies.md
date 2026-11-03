# YouTube Video Comment Replies API: pricing, parameters and code examples

`youtube/web-v2/video-comment-replies` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns second-level replies for a YouTube video comment using a continuation token, with optional filters for region, language, and formatted output.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/video-comment-replies", "continuation_token": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/video-comment-replies', {'continuation_token': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/video-comment-replies", {
  "continuation_token": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/video-comment-replies", sandbase.Params{
	"continuation_token": "example",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/video-comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | **Purpose**: Whether to return cleaned simplified data  |
| `country_code` | string |  | **Purpose**: Region code  |
| `language_code` | string |  | **Purpose**: Language preference for comments  |
| `continuation_token` | string | yes | **Purpose**: Reply continuation token from first-level comment  |

## Details

Returns the second-level replies to one YouTube video comment. You pass the `continuation_token` of that comment, and each reply comes with its text, author details, like count, and age.

### Use cases

- Show the full reply thread under a popular comment on a video.
- Collect reply text and author channels to study how viewers respond to a specific comment.
- Find the channel IDs of users who reply, so you can look up their channels.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/video-comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"continuation_token": "Eg0SC2RRdzR3OVdnWGNRGAYygwEaUBIaVWd6S1lrc3FlUTVnQTN0MGcwRjRBYUFCQWciAggAKhhVQ3VBWEZrZ3N3MUw3eGFDZm5kNUpKT3cyC2RRdzR3OVdnWGNRQAFICoIBAggBQi9jb21tZW50LXJlcGxpZXMtaXRlbS1VZ3pLWWtzcWVRNWdBM3QwZzBGNEFhQUJBZw%3D%3D"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `continuation_token` | string | Yes | **Purpose**: Reply continuation token from first-level comment |
| `country_code` | string | No | **Purpose**: Region code |
| `language_code` | string | No | **Purpose**: Language preference for comments |
| `need_format` | boolean | No | **Purpose**: Whether to return cleaned simplified data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comments": [
    {
      "author": {
        "avatar_thumbnails": null,
        "avatar_url": "https://yt3.ggpht.com/1glim4K6lUrgwfThCmliOU7tTxWQ6Tnl2VSEZKFQNxn5braBtYx8bcljKc…",
        "channel_id": "UCWU69Qbi3A6Bzx4xU-UeK7g",
        "channel_url": "https://www.youtube.com/@egdog_tm",
        "display_name": "@egdog_tm",
        "is_artist": false,
        "is_creator": false,
        "is_verified": false
      },
      "comment_id": "UgzKYksqeQ5gA3t0g0F4AaABAg.91a9XW7osVT952pvnnAzll",
      "content": "The biggest comrade ever",
      "creator_thumbnail_url": null,
      "like_count": "6993",
      "like_count_a11y": "6993 次赞",
      "published_time": "6年前",
      "reply_count": "0",
      "reply_count_a11y": "2 条回复",
      "reply_level": 1
    }
  ],
  "continuation_token": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[]` | List of replies to the comment. Each item is one reply. |
| `comments[].comment_id` | ID of the reply. It starts with the ID of the parent comment, followed by a dot and a reply suffix. |
| `comments[].content` | Text of the reply. |
| `comments[].like_count` | Number of likes on the reply. The value is a string. |
| `comments[].published_time` | Age of the reply as shown on YouTube, for example `6年前`. It is localized text, not a timestamp. |
| `comments[].reply_level` | Depth of the reply in the thread. Replies in this response have the value `1`. |
| `comments[].author.display_name / comments[].author.channel_url` | Handle and channel page URL of the reply author. |
| `comments[].author.channel_id` | YouTube channel ID of the reply author. |
| `comments[].author.is_verified / comments[].author.is_creator / comments[].author.is_artist` | Flags that show whether the author is verified, is the video creator, or is an artist. |
| `continuation_token` | Token for the next page of replies. The value is `null` when there are no more pages. |

### Notes

- Take the `continuation_token` from a first-level comment. Get those comments from [YouTube Video Comments](/apis/youtube/web-v2/video-comments).
- To get the next page, send the returned top-level `continuation_token` as the new `continuation_token` request value. A `null` value means the last page.
- `reply_count` is `0` on every reply here, so read the number of nested replies from `reply_count_a11y`, which is a localized text string.
- `country_code` and `language_code` are optional. Set `language_code` to choose the language of the text YouTube returns, such as `published_time` and the `_a11y` fields.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/video-comment-replies.json`](../../../../catalog/models/youtube/web-v2/video-comment-replies.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/video-comment-replies
