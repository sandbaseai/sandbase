# YouTube Channel ID from URL (V2) API: pricing, parameters and code examples

`youtube/web/channel-id-v2` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Resolves a YouTube channel URL into its unique channel ID and standardized channel URL. Accepts various URL formats including handles, custom URLs, and user links.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web/channel-id-v2", "channel_url": "https://static.sandbase.ai/examples/1e292b4d-4702-4fe1-a012-cba3b931bb0e/input/456962a8-0887-4ca6-aee3-9be7a5538cd5.bin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web/channel-id-v2', {'channel_url': 'https://static.sandbase.ai/examples/1e292b4d-4702-4fe1-a012-cba3b931bb0e/input/456962a8-0887-4ca6-aee3-9be7a5538cd5.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web/channel-id-v2", {
  "channel_url": "https://static.sandbase.ai/examples/1e292b4d-4702-4fe1-a012-cba3b931bb0e/input/456962a8-0887-4ca6-aee3-9be7a5538cd5.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web/channel-id-v2", sandbase.Params{
	"channel_url": "https://static.sandbase.ai/examples/1e292b4d-4702-4fe1-a012-cba3b931bb0e/input/456962a8-0887-4ca6-aee3-9be7a5538cd5.bin",
})
```

Same call via the path form: `POST /v1/api/youtube/web/channel-id-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_url` | string | yes | Channel URL.  |

## Details

Resolve a YouTube channel ID from a link by passing `channel_url`. The endpoint supports handle formats, custom URLs, user links, and standard channel paths.

### Use cases

- Resolve creator handle URLs into canonical channel IDs for downstream data queries.
- Normalize user-submitted YouTube channel links into standard channel identifiers.
- Verify channel existence and retrieve canonical channel URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/channel-id-v2" \
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

- `channel_url` supports multiple URL formats including `@username`, `/channel/`, `/c/`, and `/user/`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel ID Lookup](/model/youtube/web/channel-id): Retrieves the unique YouTube channel ID associated with a specific channel name.
- [YouTube Channel Information](/model/youtube/web/channel-info): Returns profile details and external links for a specified YouTube channel.
- [YouTube Channel Short Videos](/model/youtube/web/channel-short-videos): Returns a list of YouTube Shorts from a specified channel.

---
Machine-readable: [`catalog/models/youtube/web/channel-id-v2.json`](../../../../catalog/models/youtube/web/channel-id-v2.json) · Store page: https://www.sandbase.ai/model/youtube/web/channel-id-v2
