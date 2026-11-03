# YouTube Channel API: pricing, parameters and code examples

`youtube/channel` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00045 per call · **Modes:** sync

Fetch a YouTube channel's stats (subscribers, video count, total views, description) and the links on its About page, by handle or channel ID.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00045**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/channel"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/channel', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/channel", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/channel", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/channel` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string |  | YouTube channel handle.  |
| `channelId` | string |  | YouTube channel ID (UC...). Pass it directly when you have it: some sources accept only the ID and otherwise look up the handle first, which adds a step.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `views`, and it is served only by a source that returns every one of…  |

## Details

Returns public stats for one YouTube channel: title, handle, channel ID, subscriber count, video count, total views, description and avatar. It needs a channel `handle` such as `@mkbhd` or a `channelId` that starts with `UC`.

### Use cases

- Track a creator's subscriber and view totals over time by calling the API on a schedule.
- Check a channel's size and description before you add it to an influencer outreach list.
- Convert a `handle` into a `channelId` so you can call other channel endpoints.
- Show a channel card with its avatar, title and link in your own app.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/channel" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "@mkbhd"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channelId` | string | No | YouTube channel ID (UC...). Pass it directly when you have it: some sources accept only the ID and otherwise look up the handle first, which adds a step. |
| `handle` | string | No | YouTube channel handle. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `views`, and it is served only by a source that returns every one of t |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "avatarUrl": "https://yt3.ggpht.com/qu4TmIaYUlS41-dJ9gZ7DUR3nilvmB5_11i6OKSdvNnBNiyOusZP1bMN6I…",
    "channelId": "UCBJycsmduvYEL83R_U4JriQ",
    "description": "MKBHD: Quality Tech Videos | YouTuber | Geek | Consumer Electronics | Tech Head …",
    "handle": "@mkbhd",
    "subscribers": 21400000,
    "title": "Marques Brownlee",
    "url": "https://www.youtube.com/channel/UCBJycsmduvYEL83R_U4JriQ",
    "videos": 1863,
    "views": 5860083118
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the channel exists. A lookup that finds nothing returns `found: false`. |
| `data.channelId` | The channel's ID. It starts with `UC`. |
| `data.handle` | The channel handle, including the leading `@`. |
| `data.title` | The channel's display name. |
| `data.subscribers` | Subscriber count as a whole number. |
| `data.videos` | Number of videos on the channel. |
| `data.views` | Total view count across the channel, as a whole number. |
| `data.description` | The channel description text. It can contain line breaks and contact details. |
| `data.url / data.avatarUrl` | `url` is the channel page link built from the channel ID. `avatarUrl` is the link to the channel's profile image. |

### Notes

- Send either `handle` or `channelId`. Pass `channelId` when you have it, because it skips a handle lookup.
- Use `requireFields` with values such as `links` or `views` if you need those fields. The response shown here did not include a `links` field, so a request that requires it may be served by a different source.
- To list the channel's content next, call [YouTube Channel Videos](/apis/youtube/channel-videos) or [YouTube Channel Shorts](/apis/youtube/channel-shorts) with the `channelId`.
- To find a channel ID from a channel URL, use [YouTube Channel ID Lookup](/apis/youtube/web/channel-id).

### Pricing

Billed at the actual cost of each call, about $0.00045 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/channel.json`](../../../catalog/models/youtube/channel.json) · Store page: https://www.sandbase.ai/model/youtube/channel
