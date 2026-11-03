# YouTube Community Post Details API: pricing, parameters and code examples

`youtube/web-v2/post-detail` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a YouTube community post, including post text, media attachments, and engagement metrics. Filter results by post ID, language, and country.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/post-detail", "post_id": "UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/post-detail', {'post_id': 'UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/post-detail", {
  "post_id": "UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/post-detail", sandbase.Params{
	"post_id": "UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_id` | string | yes | **Purpose**: Post ID  |
| `need_format` | boolean |  | Whether to format data, default `true` default `true` |
| `country_code` | string |  | Country code, default `"US"` default `"US"` |
| `language_code` | string |  | Language code, default `"zh-CN"` default `"zh-CN"` |

## Details

Returns one YouTube community post with its text, image attachments, author details, and vote count. The only required input is the `post_id` of the post.

### Use cases

- Read the full text and image attachments of a single community post.
- Track the vote count of a specific post by calling it again later.
- Identify which channel published a post from its author name and channel ID.
- Build a link back to the post on YouTube using the returned post URL.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_id": "UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_id` | string | Yes | **Purpose**: Post ID |
| `country_code` | string | No | Country code, default `"US"` |
| `language_code` | string | No | Language code, default `"zh-CN"` |
| `need_format` | boolean | No | Whether to format data, default `true` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel_metadata": {
    "avatar_url": "",
    "channel_id": "UCkRfArvrzheW2E7b6SVT7vQ",
    "channel_url": "",
    "description": "",
    "title": "YouTube Creators"
  },
  "comments_continuation_token": "4qmFsgKz…",
  "post": {
    "attachment": {
      "images": [
        {
          "height": 288,
          "url": "https://yt3.ggpht.com/wbxSQ9KLMZWcSCw2Q78wZ1YfvUb9zpWRs6QYRSHt4n277DENaKkLxd9WYZ…",
          "width": 288
        }
      ],
      "type": "image"
    },
    "author_channel_id": "UCkRfArvrzheW2E7b6SVT7vQ",
    "author_name": "YouTube Creators",
    "author_thumbnails": [
      {
        "height": 32,
        "url": "//yt3.googleusercontent.com/LZeUOuOM8lzINkYAKi1X3pCQz1xsSD_EndPUR1vOGesaGavUtyM_…",
        "width": 32
      }
    ],
    "author_url": "/@youtubecreators",
    "comment_count": "",
    "content_text": "🎉 Posts are rolling out to more creators than ever before!! 🎉 \n\nWe're so excited…",
    "post_id": "UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy",
    "post_url": "https://www.youtube.com/post/UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy",
    "published_time": "2年前（修改过）",
    "vote_count": "4409"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `post.post_id / post.post_url` | The ID of the post and its full YouTube link. |
| `post.content_text` | The text of the post. |
| `post.vote_count` | The number of votes on the post, returned as a string such as `"4409"`. |
| `post.comment_count` | The comment count of the post. It is an empty string in this response. |
| `post.published_time` | The publish time as display text in the requested language, for example `2年前（修改过）`. It is relative text, not a date. |
| `post.author_name / post.author_channel_id / post.author_url` | The name of the posting channel, its channel ID, and its relative channel path. |
| `post.author_thumbnails[].url` | Avatar image URLs for the author at several sizes. Each row has `width` and `height`. |
| `post.attachment.images[].url` | Image URLs attached to the post, one per size, with `width` and `height`. `post.attachment.type` is `image` here. |
| `channel_metadata.channel_id / channel_metadata.title` | The ID and title of the channel that owns the post. |
| `comments_continuation_token` | A token for loading the comments of this post. |

### Notes

- Take `post_id` from the post list of a channel. [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts) returns posts for a channel.
- Use `comments_continuation_token` with [YouTube Community Post Comments](/apis/youtube/web-v2/post-comments) to read the comments on this post.
- `language_code` defaults to `zh-CN`, so text such as `published_time` comes back in Chinese unless you set another value like `en-US`.
- In this response, `channel_metadata.avatar_url`, `channel_metadata.channel_url`, and `channel_metadata.description` are empty strings. Use `post.author_thumbnails` and `post.author_url` for these values.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/post-detail.json`](../../../../catalog/models/youtube/web-v2/post-detail.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/post-detail
