# YouTube Channel Community Posts API: pricing, parameters and code examples

`youtube/web-v2/channel-community-posts` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts. Supports pagination via a continuation token.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/channel-community-posts", "channel_id": "UCeu6U67OzJhV1KwBansH3Dg"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/channel-community-posts', {'channel_id': 'UCeu6U67OzJhV1KwBansH3Dg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/channel-community-posts", {
  "channel_id": "UCeu6U67OzJhV1KwBansH3Dg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/channel-community-posts", sandbase.Params{
	"channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/channel-community-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_id` | string | yes | Channel ID  |
| `need_format` | boolean |  | Whether to format data, default `true` default `true` |
| `country_code` | string |  | Country code, default `"US"` default `"US"` |
| `language_code` | string |  | Language code, default `"zh-CN"` default `"zh-CN"` |
| `continuation_token` | string |  | Next page pagination token  |

## Details

Returns community posts from a YouTube channel, including post text, poll or image attachments, vote counts, and comment counts. It needs a `channel_id` and returns a page of posts with a token for the next page.

### Use cases

- Archive the text and polls a creator publishes on their community tab.
- Compare `comment_count` and `vote_count` across posts to see which topics get the most reaction.
- Collect poll questions and answer choices from a channel to study what the creator asks their audience.
- Page through a channel's older posts to build a history of its announcements.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/channel-community-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCeu6U67OzJhV1KwBansH3Dg"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | Yes | Channel ID |
| `continuation_token` | string | No | Next page pagination token |
| `country_code` | string | No | Country code, default `"US"` |
| `language_code` | string | No | Language code, default `"zh-CN"` |
| `need_format` | boolean | No | Whether to format data, default `true` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
  "continuation_token": "4qmFsgKB…",
  "has_more": true,
  "posts": [
    {
      "attachment": {
        "choices": [
          {
            "text": "Yes, slow 'em down",
            "vote_count": "",
            "vote_percentage": ""
          }
        ],
        "total_votes": "1919 票",
        "type": "poll"
      },
      "author_channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
      "author_name": "CozyCraft",
      "author_thumbnails": [
        {
          "height": 32,
          "url": "//yt3.googleusercontent.com/jwfgqnpI22YpsFDz25QtgITBf5tX7mFHqXWVhHoWzbk3ddAz9Fab…",
          "width": 32
        }
      ],
      "author_url": "/@CozyCraftYT",
      "comment_count": "9",
      "content_text": "Would you like to see more slowed versions of songs? 🤔",
      "post_id": "Ugkxarbrw7GyCGm2je0mLftFSKUOIMp3CUkE",
      "post_url": "https://www.youtube.com/post/Ugkxarbrw7GyCGm2je0mLftFSKUOIMp3CUkE",
      "published_time": "6个月前",
      "vote_count": "102"
    }
  ],
  "total_count": 9
}
```

### Response fields

| Field | Meaning |
|---|---|
| `posts[].post_id` | ID of the community post. |
| `posts[].post_url` | Link to the post on YouTube. |
| `posts[].content_text` | Text of the post. Long text may be cut off with an ellipsis. |
| `posts[].published_time` | Relative publish time as a text label, such as `6个月前`. It is not a date or timestamp. |
| `posts[].vote_count / posts[].comment_count` | Counts for the post, returned as strings. `vote_count` is the like-style vote count, and `comment_count` is the number of comments. |
| `posts[].author_name / posts[].author_channel_id / posts[].author_url` | Name, channel ID and channel path (such as `/@CozyCraftYT`) of the channel that wrote the post. |
| `posts[].attachment.type` | Kind of attachment on the post. This response shows `poll` and `image`. |
| `posts[].attachment.choices[].text` | Text of each poll option. `vote_count` and `vote_percentage` inside each choice were empty strings in this response. |
| `posts[].attachment.total_votes` | Total votes on a poll as a text label, for example `1919 票`. |
| `posts[].attachment.images[].url` | Image URL for image posts, listed with its `width` and `height`. Several sizes of the same image are returned. |
| `has_more / continuation_token` | `has_more` is `true` when more posts exist. Pass `continuation_token` in the next request to get them. |

### Notes

- Get the `channel_id` from a channel URL with [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id). Channel IDs start with `UC`.
- To page, send the returned `continuation_token` as `continuation_token` along with the same `channel_id`. Stop when `has_more` is `false`.
- To read the comments on a single post, call [YouTube Community Post Comments](/apis/youtube/web-v2/post-comments) with its `post_id`.
- `published_time` and `total_votes` follow `language_code`, which defaults to `zh-CN`. Set another value if you want labels in a different language.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.
- [YouTube Channel Shorts](/apis/youtube/web-v2/channel-shorts): Returns a list of YouTube Shorts from a specified channel.

---
Machine-readable: [`catalog/models/youtube/web-v2/channel-community-posts.json`](../../../../catalog/models/youtube/web-v2/channel-community-posts.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/channel-community-posts
