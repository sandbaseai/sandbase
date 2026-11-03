# YouTube Channel Description API: pricing, parameters and code examples

`youtube/web-v2/channel-description` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links. Filter by country and language.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/channel-description", "channel_id": "UCeu6U67OzJhV1KwBansH3Dg", "country_code": "US", "language_code": "zh-CN", "need_format": true}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/channel-description', {'channel_id': 'UCeu6U67OzJhV1KwBansH3Dg', 'country_code': 'US', 'language_code': 'zh-CN', 'need_format': True})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/channel-description", {
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
run, err := c.Run(ctx, "youtube/web-v2/channel-description", sandbase.Params{
	"channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
	"country_code": "US",
	"language_code": "zh-CN",
	"need_format": true,
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/channel-description` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_id` | string |  | **Purpose**: Channel ID for first request to get basic channel info  |
| `need_format` | boolean |  | **Purpose**: Whether to return cleaned simplified data default `true` |
| `country_code` | string |  | **Purpose**: Set region code default `"US"` |
| `language_code` | string |  | **Purpose**: Set language preference default `"zh-CN"` |
| `continuation_token` | string |  | **Purpose**: Pagination token for second request to get advanced info  |

## Details

Returns profile details for one YouTube channel, including its title, handle, description, subscriber and video counts, and avatar and banner images. It needs a `channel_id`. You can also pass `country_code` and `language_code`.

### Use cases

- Show a channel card with its title, handle, avatar and banner in a creator directory.
- Track a channel's subscriber and video counts by saving the response over time.
- Check whether a channel has memberships, a business email, or a verified badge before outreach.
- Read a channel's keywords and description to sort it into a topic category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/channel-description" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCeu6U67OzJhV1KwBansH3Dg", "language_code": "zh-CN", "country_code": "US"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | No | **Purpose**: Channel ID for first request to get basic channel info |
| `continuation_token` | string | No | **Purpose**: Pagination token for second request to get advanced info |
| `country_code` | string | No | **Purpose**: Set region code |
| `language_code` | string | No | **Purpose**: Set language preference |
| `need_format` | boolean | No | **Purpose**: Whether to return cleaned simplified data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "avatar": [
    {
      "height": 900,
      "url": "https://yt3.googleusercontent.com/jwfgqnpI22YpsFDz25QtgITBf5tX7mFHqXWVhHoWzbk3dd…",
      "width": 900
    }
  ],
  "banner": [
    {
      "height": 175,
      "url": "https://yt3.googleusercontent.com/g9zR1vL-i8QnAWLs08CHvjci79h2AXAps29dGIOLyB9T7Z…",
      "width": 1060
    }
  ],
  "channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
  "channel_url": "https://www.youtube.com/channel/UCeu6U67OzJhV1KwBansH3Dg",
  "continuation_token": "4qmFsgJg…",
  "country": null,
  "creation_date": null,
  "description": "Minecraft ambience and cozy visuals for sleep, relaxing, studying, etc 🌿\n\nHi, I’…",
  "handle": "CozyCraftYT",
  "has_business_email": false,
  "has_membership": true,
  "is_family_safe": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title / handle` | The channel display name and its @handle without the @ sign. |
| `channel_id / channel_url / vanity_url` | The channel ID, its youtube.com/channel link, and its @handle link. |
| `subscriber_count / video_count` | Subscriber and video totals as display text. The text follows `language_code`, for example `12.3万位订阅者` and `227 个视频` with `zh-CN`. |
| `view_count / creation_date / country` | Total views, join date and channel country. These came back as `null` for this channel. |
| `description / keywords` | The channel's about text and its keyword string. Long values may be long strings with line breaks. |
| `avatar[] / banner[]` | Image variants as `url`, `width` and `height`. Pick the size you need. |
| `verified / has_membership / has_business_email / is_family_safe` | Boolean flags for the verified badge, channel memberships, a listed business email, and family-safe status. |
| `links[]` | External links from the channel profile. The list is empty when the channel shows none. |
| `rss_url` | The channel's RSS feed address for new videos. |
| `continuation_token` | A token you can send back in `continuation_token` for the second request, which returns advanced info. |

### Notes

- Counts such as `subscriber_count` and `video_count` are localized strings, not numbers. Parse them with the language you set in `language_code`.
- Send `channel_id` on the first request. Send the returned `continuation_token` on a second request for advanced info.
- If you only have a channel URL, call [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id) first to get the `channel_id`.
- To list the channel's content next, call [YouTube Channel Videos](/apis/youtube/web-v2/channel-videos) or [YouTube Channel Shorts](/apis/youtube/web-v2/channel-shorts).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.
- [YouTube Channel Shorts](/apis/youtube/web-v2/channel-shorts): Returns a list of YouTube Shorts from a specified channel.

---
Machine-readable: [`catalog/models/youtube/web-v2/channel-description.json`](../../../../catalog/models/youtube/web-v2/channel-description.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/channel-description
