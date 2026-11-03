# YouTube Channel URL Lookup API: pricing, parameters and code examples

`youtube/web/channel-url` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the standard channel URL and vanity handle URL for a specified YouTube channel. Takes a unique channel ID as input to resolve public web addresses.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web/channel-url", "channel_id": "UCeu6U67OzJhV1KwBansH3Dg"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web/channel-url', {'channel_id': 'UCeu6U67OzJhV1KwBansH3Dg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web/channel-url", {
  "channel_id": "UCeu6U67OzJhV1KwBansH3Dg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web/channel-url", sandbase.Params{
	"channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
})
```

Same call via the path form: `POST /v1/api/youtube/web/channel-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_id` | string | yes | Channel ID (e.g., UCeu6U67OzJhV1KwBansH3Dg)  |

## Details

Look up the full channel link and vanity URL for any creator using their `channel_id`.

### Use cases

- Resolving a creator vanity handle URL from a raw channel ID.
- Displaying canonical YouTube channel URLs in external profile links.
- Validating public web addresses across video catalog databases.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/channel-url" \
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

- Requires a valid `channel_id` such as `UCeu6U67OzJhV1KwBansH3Dg`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel ID Lookup](/apis/youtube/web/channel-id): Retrieves the unique YouTube channel ID associated with a specific channel name.
- [YouTube Channel ID from URL (V2)](/apis/youtube/web/channel-id-v2): Resolves a YouTube channel URL into its unique channel ID and standardized channel URL.
- [YouTube Channel Information](/apis/youtube/web/channel-info): Returns profile details and external links for a specified YouTube channel.

---
Machine-readable: [`catalog/models/youtube/web/channel-url.json`](../../../../catalog/models/youtube/web/channel-url.json) · Store page: https://www.sandbase.ai/model/youtube/web/channel-url
