# Telegram Channel Post Details API: pricing, parameters and code examples

`telegram/web/post-detail` · data API · Telegram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves details for a single public Telegram channel post parsed from the web embed view. Provide the channel username and post ID to view reactions and post data.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "telegram/web/post-detail", "channel": "durov", "post_id": 510}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('telegram/web/post-detail', {'channel': 'durov', 'post_id': 510})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("telegram/web/post-detail", {
  "channel": "durov",
  "post_id": 510
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "telegram/web/post-detail", sandbase.Params{
	"channel": "durov",
	"post_id": 510,
})
```

Same call via the path form: `POST /v1/api/telegram/web/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel` | string | yes | Channel username (required).  |
| `post_id` | integer | yes | Post ID (required, auto-incremented integer within the channel).  |

## Details

Returns one public Telegram channel post, parsed from the web embed view. It needs the channel username (`channel`) and the numeric post ID (`post_id`). The response includes the post text, media links, view count, and reactions.

### Use cases

- Read the full text and photo links of a single announcement from a public channel.
- Record the view count and reaction counts of one post at the time you call it.
- Check whether a post is forwarded or replies to another post.
- Build a link to a post from its `channel` and `id` and confirm the post exists.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/telegram/web/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel": "durov", "post_id": 510}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel` | string | Yes | Channel username (required). |
| `post_id` | integer | Yes | Post ID (required, auto-incremented integer within the channel). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "author": "Pavel Durov",
  "channel": "durov",
  "date": "2026-05-12T17:28:39+00:00",
  "forwarded_from": null,
  "id": 510,
  "is_forwarded": false,
  "link_preview": null,
  "media": {
    "has_unsupported": true,
    "photos": [
      "https://cdn4.telesco.pe/file/iw0nUCyqIulL0q3pX-lSNo9-_oaB0eX3MMQgjzDggf_QZEMrMic…"
    ],
    "videos": []
  },
  "reactions": [
    {
      "count": "8.25K",
      "emoji": "⭐",
      "paid": true
    }
  ],
  "reply_to": null,
  "text": "🌍 With 400 validators across 6 continents, TON is one of the most decentralized …",
  "text_html": "🌍 With 400 validators across 6 continents, TON is one of the most decentralized …"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `text / text_html` | Post body as plain text and as HTML. The HTML version keeps line breaks as `<br>` tags. |
| `date` | Publication time of the post in ISO 8601 format with a UTC offset, such as `2026-05-12T17:28:39+00:00`. |
| `type` | Kind of post. The example post is an `album`, which holds more than one photo. |
| `media.photos[] / media.videos[]` | Lists of media URLs attached to the post. `videos` is empty in the example. |
| `media.has_unsupported` | `true` when the post holds media that the embed view could not parse. |
| `reactions[].emoji / reactions[].count` | Reaction emoji and how many people used it. Counts are shortened strings such as `8.25K`. The emoji can be an empty string. |
| `reactions[].paid` | `true` for a paid reaction. The `⭐` reaction in the example has this flag set. |
| `views` | View count of the post as a shortened string, such as `3.86M`. |
| `is_forwarded / forwarded_from / reply_to` | Show whether the post is forwarded or a reply. All three are empty or `false` in the example. |
| `url` | Public `t.me` link to the post. |

### Notes

- Take `channel` from the `t.me` link of the channel, without the `@`. `post_id` is the integer at the end of the post URL.
- `views` and `reactions[].count` are strings with `K` or `M` suffixes, so parse them before you do math.
- To list recent posts and find IDs, call [Telegram Channel Posts](/apis/telegram/web/channel-posts).
- To read replies to a post, use [Telegram Post Comments](/apis/telegram/web/post-comments).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Telegram Batch Channel Info](/apis/telegram/web/batch-channel-info): Returns basic channel profile details including title, description, and verified status for multiple public Telegram channels at once.
- [Telegram Channel Info](/apis/telegram/web/channel-info): Returns public metadata for a Telegram channel, including title, description, verified status, and username, using the public web preview.
- [Telegram Channel Posts](/apis/telegram/web/channel-posts): Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor pagination.

---
Machine-readable: [`catalog/models/telegram/web/post-detail.json`](../../../../catalog/models/telegram/web/post-detail.json) · Store page: https://www.sandbase.ai/model/telegram/web/post-detail
