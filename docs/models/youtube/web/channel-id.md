# YouTube Channel ID Lookup API: pricing, parameters and code examples

`youtube/web/channel-id` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves the unique YouTube channel ID associated with a specific channel name. Provide the target channel name to receive the matching channel identifier.

## Pricing

- **$0.001 per call** (USD)
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

This API returns the YouTube channel ID that matches a channel name. It needs one input, `channel_name`, and returns the ID with the name it matched.

### Use cases

- Convert a creator's channel name into a channel ID before you store it in a database.
- Get the channel ID you need to call other YouTube channel APIs.
- Check that a channel name maps to the channel ID you expect.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/channel-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_name": "LinusTechTips"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_name` | string | Yes | Channel name. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw",
  "channel_name": "LinusTechTips"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `channel_id` | The YouTube channel ID for the matched channel. It starts with `UC`, as in `UCXuqSBlHAE6Xw-yeJA0Tunw`. |
| `channel_name` | The channel name in the response. It matches the `channel_name` you sent in the example request. |

### Notes

- Pass the channel name as plain text in `channel_name`, for example `LinusTechTips`.
- Use the returned `channel_id` as input for other YouTube channel APIs, such as [YouTube Channel Information](/apis/youtube/web/channel-info).
- To go the other way and find a channel ID from a channel URL, use [YouTube Channel ID from URL (V2)](/apis/youtube/web/channel-id-v2).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel ID from URL (V2)](/apis/youtube/web/channel-id-v2): Resolves a YouTube channel URL into its unique channel ID and standardized channel URL.
- [YouTube Channel Information](/apis/youtube/web/channel-info): Returns profile details and external links for a specified YouTube channel.
- [YouTube Channel Short Videos](/apis/youtube/web/channel-short-videos): Returns a list of YouTube Shorts from a specified channel.

---
Machine-readable: [`catalog/models/youtube/web/channel-id.json`](../../../../catalog/models/youtube/web/channel-id.json) · Store page: https://www.sandbase.ai/model/youtube/web/channel-id
