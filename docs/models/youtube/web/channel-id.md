# YouTube Channel ID Lookup API: pricing, parameters and code examples

`youtube/web/channel-id` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Retrieves the unique YouTube channel ID associated with a specific channel name. Provide the target channel name to receive the matching channel identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web/channel-id", "channel_name": "LinusTechTips"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web/channel-id', {'channel_name': 'LinusTechTips'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web/channel-id", {
  "channel_name": "LinusTechTips"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web/channel-id", sandbase.Params{
	"channel_name": "LinusTechTips",
})
```

Same call via the path form: `POST /v1/api/youtube/web/channel-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_name` | string | yes | Channel name.  |

## Details

Look up the unique YouTube channel ID for a creator by supplying the target name in `channel_name`.

### Use cases

- Resolve a YouTube channel name into its official channel ID.
- Obtain channel identifiers required for downstream channel data lookups.
- Verify the channel ID associated with a specific creator handle or username.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/channel-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_name": "LinusTechTips"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_name` | string | Yes | Channel name. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw",
  "channel_name": "LinusTechTips"
}
```

### Notes

- Requires `channel_name` as an input string.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel ID from URL (V2)](/model/youtube/web/channel-id-v2): Resolves a YouTube channel URL into its unique channel ID and standardized channel URL.
- [YouTube Channel Information](/model/youtube/web/channel-info): Returns profile details and external links for a specified YouTube channel.
- [YouTube Channel Short Videos](/model/youtube/web/channel-short-videos): Returns a list of YouTube Shorts from a specified channel.

---
Machine-readable: [`catalog/models/youtube/web/channel-id.json`](../../../../catalog/models/youtube/web/channel-id.json) · Store page: https://www.sandbase.ai/model/youtube/web/channel-id
