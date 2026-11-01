# YouTube Channel URL by ID

`youtube/web-v2/channel-url` · api · YouTube

Returns standard and vanity channel URLs for a specified YouTube channel. Takes a unique channel ID to look up the corresponding handle and profile links.

## Pricing

- **$0.0015 per call** (USD)
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

Look up YouTube profile and vanity URLs by supplying a `channel_id`. This endpoint resolves standard channel identifiers into formatted handle URLs.

### Use cases

- Resolve a channel handle from an existing channel identifier.
- Display formatted vanity links for creator profile pages.
- Convert legacy YouTube identifiers into current handle URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/channel-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCeu6U67OzJhV1KwBansH3Dg"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | Yes | Channel ID (e.g., UCeu6U67OzJhV1KwBansH3Dg) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
  "channel_url": "https://www.youtube.com/channel/UCeu6U67OzJhV1KwBansH3Dg",
  "vanity_url": "http://www.youtube.com/@CozyCraftYT"
}
```

### Notes

- Requires a valid `channel_id` starting with UC.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/channel-url.json`](../../../../catalog/models/youtube/web-v2/channel-url.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/channel-url
