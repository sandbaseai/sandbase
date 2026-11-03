# YouTube Channel Videos API: pricing, parameters and code examples

`youtube/web-v2/channel-videos` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of videos for a specified YouTube channel, including title, duration, URLs, and view counts. Supports pagination and region or language filters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/channel-videos", "channel_id": "UCeu6U67OzJhV1KwBansH3Dg", "country_code": "US", "language_code": "zh-CN", "need_format": true}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/channel-videos', {'channel_id': 'UCeu6U67OzJhV1KwBansH3Dg', 'country_code': 'US', 'language_code': 'zh-CN', 'need_format': True})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/channel-videos", {
  "channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
  "country_code": "US",
  "language_code": "zh-CN",
  "need_format": true
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/channel-videos", sandbase.Params{
	"channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
	"country_code": "US",
	"language_code": "zh-CN",
	"need_format": true,
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/channel-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_id` | string | yes | **Purpose**: Channel ID  |
| `need_format` | boolean |  | **Purpose**: Whether to return cleaned simplified data default `true` |
| `country_code` | string |  | **Purpose**: Set region code default `"US"` |
| `language_code` | string |  | **Purpose**: Set language preference default `"zh-CN"` |
| `continuation_token` | string |  | **Purpose**: Pagination token for next page  |

## Details

Retrieve video uploads from a YouTube channel by providing its `channel_id`. You can optionally localize results using `country_code` and `language_code`.

### Use cases

- Display recent video uploads from a specific creator channel.
- Track video view counts and release timelines for channel analysis.
- Paginate through a channel catalog to extract video links and playback details.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/channel-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCeu6U67OzJhV1KwBansH3Dg"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | Yes | Purpose: Channel ID |
| `need_format` | boolean | No | Purpose: Whether to return cleaned simplified data |
| `country_code` | string | No | Purpose: Set region code |
| `language_code` | string | No | Purpose: Set language preference |
| `continuation_token` | string | No | Purpose: Pagination token for next page |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "videos": [
    {
      "duration": "11:00:00",
      "duration_accessibility": "11小时",
      "playback_url": "https://rr10---sn-8xgp1vo-ab5d.googlevideo.com/initplayback?source=youtube&oeis=…",
      "published_time": "1天前",
      "short_view_count": "5775次观看",
      "title": "it's getting late, you should probably sleep… (minecraft music & ambience)",
      "url": "https://www.youtube.com/watch?v=AuzYA0smxXU",
      "video_id": "AuzYA0smxXU",
      "view_count": "5775次观看"
    }
  ]
}
```

### Notes

- Use `continuation_token` to retrieve the next page of video results.
- Set `need_format` to true to receive cleaned and simplified data.
- Specify `country_code` and `language_code` to tailor regional and language results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/channel-videos.json`](../../../../catalog/models/youtube/web-v2/channel-videos.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/channel-videos
