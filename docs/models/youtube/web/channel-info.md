# YouTube Channel Information

`youtube/web/channel-info` · api · YouTube

Returns profile details and external links for a specified YouTube channel. Look up channel data using a channel identifier.

## Pricing

- **$0.0015 per call** (USD)
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

Retrieve channel profile data and associated links by providing a valid `channel_id`.

### Use cases

- Look up public links and metadata associated with a YouTube channel.
- Audit channel information and external web links.
- Collect channel details for creator research and monitoring.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/channel-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | Yes | Channel ID. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "links": [
    {
      "name": "lttstore.com"
    }
  ]
}
```

### Notes

- Requires a valid `channel_id` representing the target YouTube channel.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel ID Lookup](/model/youtube/web/channel-id): Retrieves the unique YouTube channel ID associated with a specific channel name.
- [YouTube Channel ID from URL (V2)](/model/youtube/web/channel-id-v2): Resolves a YouTube channel URL into its unique channel ID and standardized channel URL.
- [YouTube Channel Short Videos](/model/youtube/web/channel-short-videos): Returns a list of YouTube Shorts from a specified channel.

---
Machine-readable: [`catalog/models/youtube/web/channel-info.json`](../../../../catalog/models/youtube/web/channel-info.json) · Store page: https://www.sandbase.ai/model/youtube/web/channel-info
