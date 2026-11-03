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

Search YouTube for a keyword and get matching videos with their title, channel, view count, length and publish time.

### Use cases

- Monitor new videos about a brand or topic.
- Research competitors and popular formats.
- Find creators for sponsorships.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/search-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_query": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `search_query` | string | Yes | Search keyword. |
| `order_by` | string | No | Order by, default is this_month, optional values are this_week, this_month, this_year, last_hour, today. |
| `country_code` | string | No | Country code, default is us. |
| `language_code` | string | No | Language code, default is en. |
| `continuation_token` | string | No | Token to continue fetching search results. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "query": "OpenAI",
  "country": "US",
  "lang": "en",
  "number_of_videos": 20,
  "estimated_results": 395560,
  "continuation_token": "<token>",
  "videos": [
    {
      "video_id": "Fls_onRviPM",
      "title": "OpenAI DevDay 2026 Keynote (FULL)",
      "channel_id": "UCXZCJLdBC09xxGZ6gcdrc6A",
      "number_of_views": 650665,
      "published_time": "Streamed 6 days ago",
      "video_length": "53:35",
      "type": "NORMAL",
      "author": "OpenAI"
    }
  ]
}
```

### Notes

- `order_by`: last_hour, today, this_week, this_month (default) or this_year.
- Paginate with `continuation_token`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Get channel ID](/apis/youtube/web/channel-id): Get channel ID.
- [Get channel ID from URL V2](/apis/youtube/web/channel-id-v2): Convert YouTube channel URL to channel ID..
- [Get channel information](/apis/youtube/web/channel-info): Get channel information.

---
Machine-readable: [`catalog/models/youtube/web/search-video.json`](../../../../catalog/models/youtube/web/search-video.json) · Store page: https://www.sandbase.ai/model/youtube/web/search-video
