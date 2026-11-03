# YouTube Video Search API: pricing, parameters and code examples

`youtube/web/search-video` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search YouTube videos by keyword and get video ID, title, channel, views, length and publish time, with country, language and upload-date filters and continuation-token pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web/search-video", "country_code": "us", "language_code": "en", "order_by": "this_month", "search_query": "AI agents"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web/search-video', {'country_code': 'us', 'language_code': 'en', 'order_by': 'this_month', 'search_query': 'AI agents'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web/search-video", {
  "country_code": "us",
  "language_code": "en",
  "order_by": "this_month",
  "search_query": "AI agents"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web/search-video", sandbase.Params{
	"country_code": "us",
	"language_code": "en",
	"order_by": "this_month",
	"search_query": "AI agents",
})
```

Same call via the path form: `POST /v1/api/youtube/web/search-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order_by` | string |  | Order by, default is this_month, optional values are this_week, this_month, this_year, last_hour, today. default `"this_month"` |
| `country_code` | string |  | Country code, default is us. default `"us"` |
| `search_query` | string | yes | Search keyword.  |
| `language_code` | string |  | Language code, default is en. default `"en"` |
| `continuation_token` | string |  | Token to continue fetching search results. Default is None.  |

## Details

This API searches YouTube videos by keyword. It returns a list of matching videos with ID, title, channel, view count, length and publish time. You only need `search_query`; country, language and time filters are optional.

### Use cases

- Track new videos that mention a brand or topic, such as OpenAI, by searching with `order_by` set to `today` or `last_hour`.
- Compare view counts across videos on one topic to see which formats and titles get attention.
- Collect `channel_id` values from search results to find creators who cover a subject, for sponsorship research.
- Build a list of video IDs for a keyword, then pull details or comments for each one.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/search-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_query": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `search_query` | string | Yes | Search keyword. |
| `continuation_token` | string | No | Token to continue fetching search results. Default is None. |
| `country_code` | string | No | Country code, default is us. |
| `language_code` | string | No | Language code, default is en. |
| `order_by` | string | No | Order by, default is this_month, optional values are this_week, this_month, this_year, last_hour, today. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "continuation_token": "EpUFEgZP…",
  "country": "US",
  "estimated_results": 3200682,
  "lang": "en",
  "number_of_videos": 20,
  "query": "OpenAI",
  "timezone": "America/New_York",
  "videos": [
    {
      "author": "Theo - t3․gg",
      "category": null,
      "channel_id": "UCbRP3c757lWg9M-U7TyEkXA",
      "description": "Just a month after their reduction, OpenAI is doubling the limits of their plans…",
      "is_live_content": null,
      "keywords": [],
      "number_of_views": 19914,
      "published_time": "2 hours ago",
      "thumbnails": [
        {
          "height": 202,
          "url": "https://i.ytimg.com/vi/Hq2c7pww1Ds/hq720_custom_3.jpg?sqp=CPyhptcG-oaymwEcCOgCEM…",
          "width": 360
        }
      ],
      "title": "OpenAI is getting desperate",
      "type": "NORMAL",
      "video_id": "Hq2c7pww1Ds"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `videos[].video_id` | The YouTube video ID. Use it to build a watch link or to call other video APIs. |
| `videos[].title` | The video title as shown in search results. |
| `videos[].author / videos[].channel_id` | The channel name and the channel ID that published the video. |
| `videos[].number_of_views` | The view count of the video as a number. |
| `videos[].published_time` | Relative publish time as text, such as `2 hours ago` or `3 days ago`. It is not a timestamp. |
| `videos[].video_length` | The video length as text, such as `15:50`. |
| `videos[].description` | A short description snippet of the video. It can be an empty string. |
| `videos[].thumbnails[].url` | Thumbnail image URL. Each entry also has `width` and `height`. |
| `estimated_results` | The estimated total number of results for the query. |
| `continuation_token` | Token that you pass back in the next request to get the next page of results. |

### Notes

- Set `order_by` to one of `last_hour`, `today`, `this_week`, `this_month` (default) or `this_year`.
- To get the next page, send the same request with the `continuation_token` value from the last response.
- `category`, `is_live_content` and `keywords` came back as `null` or empty in this response, so do not rely on them.
- Pass a `channel_id` from the results to [YouTube Channel Information](/apis/youtube/web/channel-info) to get details about the channel.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Get channel ID](/apis/youtube/web/channel-id): Get channel ID.
- [Get channel ID from URL V2](/apis/youtube/web/channel-id-v2): Convert YouTube channel URL to channel ID..
- [Get channel information](/apis/youtube/web/channel-info): Get channel information.

---
Machine-readable: [`catalog/models/youtube/web/search-video.json`](../../../../catalog/models/youtube/web/search-video.json) · Store page: https://www.sandbase.ai/model/youtube/web/search-video
