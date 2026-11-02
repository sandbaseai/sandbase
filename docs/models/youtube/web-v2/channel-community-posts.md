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

Use this endpoint to look up community feed entries for a channel using `channel_id`. Paginate through past updates with `continuation_token`.

### Use cases

- Track creator audience polls and status updates.
- Monitor engagement metrics on channel community announcements.
- Archive text posts and audience interactions from specific channels.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/channel-community-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCeu6U67OzJhV1KwBansH3Dg"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | Yes | Channel ID |
| `need_format` | boolean | No | Whether to format data, default `true` |
| `country_code` | string | No | Country code, default `"US"` |
| `language_code` | string | No | Language code, default `"zh-CN"` |
| `continuation_token` | string | No | Next page pagination token |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "posts": [
    {
      "author_channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
      "author_name": "<user>",
      "author_url": "/@CozyCraftYT",
      "comment_count": "9",
      "content_text": "Would you like to see more slowed versions of songs? 🤔",
      "post_id": "Ugkxarbrw7GyCGm2je0mLftFSKUOIMp3CUkE",
      "post_url": "https://www.youtube.com/post/Ugkxarbrw7GyCGm2je0mLftFSKUOIMp3CUkE",
      "published_time": "5个月前",
      "vote_count": "98",
      "attachment": {
        "type": "poll"
      }
    }
  ]
}
```

### Notes

- Pass `continuation_token` from previous results to navigate through older community posts.
- `country_code` defaults to "US" and `language_code` defaults to "zh-CN".
- `need_format` defaults to true to format the returned output.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.
- [YouTube Channel Shorts](/model/youtube/web-v2/channel-shorts): Returns a list of YouTube Shorts from a specified channel.

---
Machine-readable: [`catalog/models/youtube/web-v2/channel-community-posts.json`](../../../../catalog/models/youtube/web-v2/channel-community-posts.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/channel-community-posts
