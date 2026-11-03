# YouTube Channel ID from URL (V2) API: pricing, parameters and code examples

`youtube/web/channel-id-v2` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Resolves a YouTube channel URL into its unique channel ID and standardized channel URL. Accepts various URL formats including handles, custom URLs, and user links.

## Pricing

- **$0.001 per call** (USD)
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

Takes a YouTube channel URL and returns the channel's unique ID and its standard channel URL. The input is `channel_url`, which can be a handle, custom URL, user link, or channel link.

### Use cases

- Convert a creator's `@handle` link into a `UC...` channel ID before you call other channel APIs.
- Clean up channel links that users paste in different formats and store one standard URL per channel.
- Check that a submitted channel link points to a real channel.
- Build a lookup table that maps handles from a spreadsheet to channel IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/channel-id-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_url": "https://www.youtube.com/@CozyCraftYT"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_url` | string | Yes | Channel URL. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
  "channel_url": "https://www.youtube.com/channel/UCeu6U67OzJhV1KwBansH3Dg"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `channel_id` | The unique YouTube channel ID. It starts with `UC`, for example `UCeu6U67OzJhV1KwBansH3Dg`. |
| `channel_url` | The standard channel URL built from the ID, in the form `https://www.youtube.com/channel/<channel_id>`. |

### Notes

- Pass the full URL in `channel_url`. The example uses a handle URL: `https://www.youtube.com/@CozyCraftYT`.
- The response gives the same ID in `channel_id` and inside `channel_url`, so you can use either one.
- To go the other way and get a URL from an ID, use [YouTube Channel URL by ID](/apis/youtube/web-v2/channel-url).
- For profile details of the channel, call [YouTube Channel Information](/apis/youtube/web/channel-info) next.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel ID Lookup](/apis/youtube/web/channel-id): Retrieves the unique YouTube channel ID associated with a specific channel name.
- [YouTube Channel Information](/apis/youtube/web/channel-info): Returns profile details and external links for a specified YouTube channel.
- [YouTube Channel Short Videos](/apis/youtube/web/channel-short-videos): Returns a list of YouTube Shorts from a specified channel.

---
Machine-readable: [`catalog/models/youtube/web/channel-id-v2.json`](../../../../catalog/models/youtube/web/channel-id-v2.json) · Store page: https://www.sandbase.ai/model/youtube/web/channel-id-v2
