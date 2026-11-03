# YouTube Channel Video Search API: pricing, parameters and code examples

`youtube/web/search-channel` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches videos within a specific YouTube channel using a keyword query. Returns matching video details including title, view count, post date, and video ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web/search-channel", "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw", "country_code": "us", "language_code": "en", "search_query": "AMD"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web/search-channel', {'channel_id': 'UCXuqSBlHAE6Xw-yeJA0Tunw', 'country_code': 'us', 'language_code': 'en', 'search_query': 'AMD'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web/search-channel", {
  "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw",
  "country_code": "us",
  "language_code": "en",
  "search_query": "AMD"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web/search-channel", sandbase.Params{
	"channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw",
	"country_code": "us",
	"language_code": "en",
	"search_query": "AMD",
})
```

Same call via the path form: `POST /v1/api/youtube/web/search-channel` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_id` | string | yes | Channel ID  |
| `country_code` | string |  | Country code, default is us. default `"us"` |
| `search_query` | string | yes | Search keyword.  |
| `language_code` | string |  | Language code, default is en. default `"en"` |
| `continuation_token` | string |  | Token to continue fetching search results. Default is None.  |

## Details

Returns videos from one YouTube channel that match a keyword. You send a `channel_id` and a `search_query`. Each result includes the title, view count, relative post time, length, and `video_id`.

### Use cases

- Find every video a creator has posted about a brand or product, such as AMD on Linus Tech Tips.
- Check how often a channel covers a topic and which of those videos get the most views.
- Collect `video_id` values from a channel search, then pass them to a video details API.
- Pull thumbnails and descriptions of matching videos for a content report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/search-channel" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw", "search_query": "AMD"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | Yes | Channel ID |
| `search_query` | string | Yes | Search keyword. |
| `continuation_token` | string | No | Token to continue fetching search results. Default is None. |
| `country_code` | string | No | Country code, default is us. |
| `language_code` | string | No | Language code, default is en. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw",
  "continuation_token": "4qmFsgJl…",
  "country": "US",
  "lang": "en",
  "number_of_videos": 28,
  "query": "AMD",
  "timezone": "America/New_York",
  "videos": [
    {
      "author": "Linus Tech Tips",
      "category": null,
      "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw",
      "description": "Thanks to AMD for sponsoring this series and being a great partner! Check out th…",
      "is_live_content": null,
      "keywords": [],
      "number_of_views": 2165933,
      "published_time": "1 year ago",
      "thumbnails": [
        {
          "height": 94,
          "url": "https://i.ytimg.com/vi/GIqnvU1tgPg/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDgg…",
          "width": 168
        }
      ],
      "title": "I made her Upgrade her Husband's PC - AMD $5000 Ultimate Tech Upgrade",
      "type": "NORMAL",
      "video_id": "GIqnvU1tgPg"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `videos[].video_id` | The YouTube ID of the matching video. |
| `videos[].title` | Title of the video. |
| `videos[].number_of_views` | View count as a number. |
| `videos[].published_time` | Relative post time as text, such as `1 year ago`. It is not an exact date. |
| `videos[].video_length` | Video duration as text, such as `25:45`. |
| `videos[].description` | Start of the video description. Long text is cut off. |
| `videos[].thumbnails[].url / videos[].thumbnails[].width / videos[].thumbnails[].height` | Thumbnail image links with their pixel sizes. Each video has several sizes. |
| `videos[].author / videos[].channel_id` | Name and ID of the channel that posted the video. |
| `number_of_videos` | Count of videos in this response. |
| `continuation_token` | Token that fetches the next page of results for the same search. |

### Notes

- Get `channel_id` from [YouTube Channel ID Lookup](/apis/youtube/web/channel-id) or [YouTube Channel ID from URL (V2)](/apis/youtube/web/channel-id-v2). The example ID starts with `UC`.
- To get more results, send the returned `continuation_token` as `continuation_token` in the next request with the same other parameters.
- Fields such as `category`, `is_live_content` and `keywords` were empty (`null` or `[]`) in the example response.
- `country_code` defaults to `us` and `language_code` defaults to `en`. The response shows them as `country` and `lang`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel ID Lookup](/apis/youtube/web/channel-id): Retrieves the unique YouTube channel ID associated with a specific channel name.
- [YouTube Channel ID from URL (V2)](/apis/youtube/web/channel-id-v2): Resolves a YouTube channel URL into its unique channel ID and standardized channel URL.
- [YouTube Channel Information](/apis/youtube/web/channel-info): Returns profile details and external links for a specified YouTube channel.

---
Machine-readable: [`catalog/models/youtube/web/search-channel.json`](../../../../catalog/models/youtube/web/search-channel.json) · Store page: https://www.sandbase.ai/model/youtube/web/search-channel
