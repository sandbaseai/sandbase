# YouTube Channel URL by ID API: pricing, parameters and code examples

`youtube/web-v2/channel-url` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns standard and vanity channel URLs for a specified YouTube channel. Takes a unique channel ID to look up the corresponding handle and profile links.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/channel-url", "channel_id": "UCeu6U67OzJhV1KwBansH3Dg"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/channel-url', {'channel_id': 'UCeu6U67OzJhV1KwBansH3Dg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/channel-url", {
  "channel_id": "UCeu6U67OzJhV1KwBansH3Dg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/channel-url", sandbase.Params{
	"channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/channel-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_id` | string | yes | Channel ID (e.g., UCeu6U67OzJhV1KwBansH3Dg)  |

## Details

Returns the standard channel URL and the vanity (handle) URL for a YouTube channel. It needs one input, the `channel_id`.

### Use cases

- Turn a stored `channel_id` into the public `@handle` link for a creator profile page.
- Build a clickable link to a channel when your database only holds the ID.
- Find the handle of a channel so you can match it against handles found in social media bios.
- Check that a `channel_id` maps to a real channel before you run other channel lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/channel-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCeu6U67OzJhV1KwBansH3Dg"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | Yes | Channel ID (e.g., UCeu6U67OzJhV1KwBansH3Dg) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
  "channel_url": "https://www.youtube.com/channel/UCeu6U67OzJhV1KwBansH3Dg",
  "vanity_url": "http://www.youtube.com/@CozyCraftYT"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `channel_id` | The channel ID you sent in the request, returned unchanged. |
| `channel_url` | The standard channel URL, built as `https://www.youtube.com/channel/` followed by the channel ID. |
| `vanity_url` | The handle-based URL for the channel, such as `http://www.youtube.com/@CozyCraftYT`. The part after `@` is the channel handle. |

### Notes

- The `channel_id` is a string that starts with `UC`, for example `UCeu6U67OzJhV1KwBansH3Dg`.
- The `vanity_url` in the example uses `http://`, not `https://`. Normalize the scheme if you need secure links.
- If you only have a channel URL, call [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id) first to get the ID.
- For subscriber counts, video totals and the joined date, call [YouTube Channel Description](/apis/youtube/web-v2/channel-description) next.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/channel-url.json`](../../../../catalog/models/youtube/web-v2/channel-url.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/channel-url
