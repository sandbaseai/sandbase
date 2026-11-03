# Linktree Profile API: pricing, parameters and code examples

`linktree/profile` · data API · Linktree · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Get a public Linktree page by URL: title, bio, picture, contact email, linked social accounts, and every link card with its destination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linktree/profile", "url": "https://linktr.ee/mkbhd"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linktree/profile', {'url': 'https://linktr.ee/mkbhd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linktree/profile", {
  "url": "https://linktr.ee/mkbhd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linktree/profile", sandbase.Params{
	"url": "https://linktr.ee/mkbhd",
})
```

Same call via the path form: `POST /v1/api/linktree/profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The Linktree profile URL, e.g. https://linktr.ee/mkbhd.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `title`, and it is served only by a source that returns every one of…  |

## Details

Returns the public data of a Linktree page: its title, username, avatar, contact email, linked social account URLs, and every link card with its destination. It needs the full Linktree profile URL, such as `https://linktr.ee/mkbhd`.

### Use cases

- Collect a creator's contact email and social account URLs from one page.
- Check which platforms a creator links to, such as YouTube, Spotify, or Apple Podcasts.
- Build a list of the destination URLs a profile promotes, with each link's title and type.
- Match a Linktree username to the same person's accounts on other platforms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linktree/profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://linktr.ee/mkbhd"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The Linktree profile URL, e.g. https://linktr.ee/mkbhd. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `title`, and it is served only by a source that returns every one of t |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "appleMusic": null,
    "applePodcast": "https://podcasts.apple.com/us/podcast/waveform-the-mkbhd-podcast/id1474429475",
    "avatarUrl": "https://ugc.production.linktr.ee/USl9Uq9GR8y5K2Gdj0UL_74v07R9H8U7Iayn4",
    "description": null,
    "email": "podcast@mkbhd.com",
    "facebook": "https://facebook.com/WVFRM",
    "id": "12430309",
    "instagram": "https://instagram.com/wvfrmpodcast",
    "linkedin": null,
    "links": [
      {
        "id": "64107392",
        "locked": false,
        "thumbnailUrl": null,
        "title": "YouTube",
        "type": "YOUTUBE_CHANNEL",
        "url": "https://www.youtube.com/channel/UCEcrRXW3oEYfUctetZTAWLw"
      }
    ],
    "soundcloud": null,
    "spotify": "https://open.spotify.com/show/6o81QuW22s5m2nfcXWjucc"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the profile exists. A lookup that finds nothing returns `found: false`. |
| `data.username / data.title` | The Linktree handle and the display title of the page. In the example, `MKBHD` and `Waveform`. |
| `data.id` | The numeric ID of the profile, as a string. |
| `data.email` | The contact email shown on the page. It is `null` when the page has none. |
| `data.avatarUrl` | URL of the profile picture. |
| `data.x / data.instagram / data.facebook / data.youtube / data.spotify / data.applePodcast` | Full URLs of the social accounts linked on the profile. Platforms the page does not link, such as `tiktok` or `linkedin`, are `null`. |
| `data.verticals` | List of category labels for the profile, such as `Creator`. |
| `data.timezone` | Timezone name set for the profile, such as `America/New_York`. |
| `data.links[].title / data.links[].url` | The label and destination URL of each link card. |
| `data.links[].type / data.links[].locked` | The card type, such as `YOUTUBE_CHANNEL` or `CLASSIC`, and whether the card is locked. `locked` is a boolean. |

### Notes

- Pass the full profile URL in `url`, in the form `https://linktr.ee/<username>`.
- Use `requireFields` with `locked`, `thumbnailUrl`, or `title` only if you need the call served by a source that returns those fields. This can raise the price.
- Social fields and `thumbnailUrl` are `null` when the page does not have them, so check for `null` before use.
- Each link card has its own `id`, a numeric string.

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linktree/profile.json`](../../../catalog/models/linktree/profile.json) · Store page: https://www.sandbase.ai/model/linktree/profile
