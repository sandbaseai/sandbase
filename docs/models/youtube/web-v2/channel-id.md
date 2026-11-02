# YouTube Channel ID from URL API: pricing, parameters and code examples

`youtube/web-v2/channel-id` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Resolves a YouTube channel URL to its canonical channel ID. Accepts various channel URL structures including handle, channel, custom, and user formats.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/channel-id", "channel_url": "https://www.youtube.com/@CozyCraftYT"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/channel-id', {'channel_url': 'https://www.youtube.com/@CozyCraftYT'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/channel-id", {
  "channel_url": "https://www.youtube.com/@CozyCraftYT"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/channel-id", sandbase.Params{
	"channel_url": "https://www.youtube.com/@CozyCraftYT",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/channel-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_url` | string | yes | Channel URL.  |

## Details

Look up a canonical YouTube channel ID by supplying any standard channel URL in `channel_url`.

### Use cases

- Convert channel handle URLs into canonical IDs for downstream data retrieval.
- Normalize various YouTube channel URL formats into a single channel ID identifier.
- Verify channel identifiers before calling channel-specific endpoints.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/channel-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_url": "https://www.youtube.com/@CozyCraftYT"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_url` | string | Yes | Channel URL. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
  "channel_url": "https://www.youtube.com/channel/UCeu6U67OzJhV1KwBansH3Dg"
}
```

### Notes

- Supports handle (@username), /channel/, /c/, and /user/ URL formats via `channel_url`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel Shorts](/model/youtube/web-v2/channel-shorts): Returns a list of YouTube Shorts from a specified channel.

---
Machine-readable: [`catalog/models/youtube/web-v2/channel-id.json`](../../../../catalog/models/youtube/web-v2/channel-id.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/channel-id
