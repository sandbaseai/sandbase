# YouTube Channel Information API: pricing, parameters and code examples

`youtube/web/channel-info` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns profile details and external links for a specified YouTube channel. Look up channel data using a channel identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web/channel-info", "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web/channel-info', {'channel_id': 'UCXuqSBlHAE6Xw-yeJA0Tunw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web/channel-info", {
  "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web/channel-info", sandbase.Params{
	"channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw",
})
```

Same call via the path form: `POST /v1/api/youtube/web/channel-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_id` | string | yes | Channel ID.  |

## Details

Returns the public profile of a YouTube channel: title, description, country, creation date, subscriber, video and view counts, avatar and banner images, and external links. It needs one input, the `channel_id`.

### Use cases

- Build a creator profile card with the channel title, avatar, banner and verified status.
- Collect a channel's external links, such as store and membership pages, for outreach or link audits.
- Track a channel's subscriber, video and view counts for creator research.
- Check whether a channel lists a business email before you plan contact.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/channel-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | Yes | Channel ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "avatar": [
    {
      "height": 72,
      "url": "https://yt3.googleusercontent.com/gnvYLhXy8FAlPXZ2RTrkrgj-5kyt0vdE2FUGVOiKGdEZIa…",
      "width": 72
    }
  ],
  "banner": [
    {
      "height": 175,
      "url": "https://yt3.googleusercontent.com/U_7GWetO6k4sq3pAkbFEIIWzZLKcIJlGJqNz6NQAhgqF6D…",
      "width": 1060
    }
  ],
  "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw",
  "country": "Canada",
  "creation_date": "Nov 24, 2008",
  "description": "Linus Tech Tips is a passionate team of \"professionally curious\" experts in cons…",
  "has_business_email": true,
  "links": [
    {
      "endpoint": "lttstore.com",
      "name": "lttstore.com"
    }
  ],
  "subscriber_count": "16.9M subscribers",
  "title": "Linus Tech Tips",
  "verified": true,
  "video_count": "7.9K videos"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title / channel_id` | The channel name and its YouTube channel ID. |
| `description` | The channel's about text. Long text may be cut. |
| `country / creation_date` | The country shown on the channel and the date the channel was created, for example `Nov 24, 2008`. |
| `subscriber_count / video_count / view_count` | Display strings for audience size, number of videos and total views, for example `16.9M subscribers` and `9,961,845,838 views`. Parse the text before you do math on it. |
| `verified` | `true` when the channel carries a verified status. |
| `has_business_email` | `true` when the channel has a business email listed. The email address is not in the response. |
| `links[].name / links[].endpoint` | The label of an external link on the channel and its target address, such as `floatplane.com/ltt`. |
| `avatar[].url / avatar[].width / avatar[].height` | Profile image URLs at several sizes. Pick the size you need. |
| `banner[].url / banner[].width / banner[].height` | Banner image URLs at several sizes. |

### Notes

- Channel IDs start with `UC`, as in `UCXuqSBlHAE6Xw-yeJA0Tunw`.
- If you only have a channel URL, call [YouTube Channel ID from URL (V2)](/apis/youtube/web/channel-id-v2) first to get the `channel_id`.
- If you only have a channel name, call [YouTube Channel ID Lookup](/apis/youtube/web/channel-id).
- To list the channel's Shorts, use [YouTube Channel Short Videos](/apis/youtube/web/channel-short-videos).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel ID Lookup](/apis/youtube/web/channel-id): Retrieves the unique YouTube channel ID associated with a specific channel name.
- [YouTube Channel ID from URL (V2)](/apis/youtube/web/channel-id-v2): Resolves a YouTube channel URL into its unique channel ID and standardized channel URL.
- [YouTube Channel Short Videos](/apis/youtube/web/channel-short-videos): Returns a list of YouTube Shorts from a specified channel.

---
Machine-readable: [`catalog/models/youtube/web/channel-info.json`](../../../../catalog/models/youtube/web/channel-info.json) · Store page: https://www.sandbase.ai/model/youtube/web/channel-info
