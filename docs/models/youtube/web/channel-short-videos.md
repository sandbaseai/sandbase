# YouTube Channel Short Videos API: pricing, parameters and code examples

`youtube/web/channel-short-videos` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of YouTube Shorts from a specified channel. Supports pagination through an optional continuation token to browse additional short videos.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web/channel-short-videos", "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web/channel-short-videos', {'channel_id': 'UCXuqSBlHAE6Xw-yeJA0Tunw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web/channel-short-videos", {
  "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web/channel-short-videos", sandbase.Params{
	"channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw",
})
```

Same call via the path form: `POST /v1/api/youtube/web/channel-short-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_id` | string | yes | Channel ID.  |
| `continuation_token` | string |  | Token to continue fetching channel short videos. Default is None.  |

## Details

Fetch YouTube Shorts uploaded by a creator by supplying a `channel_id`. Use `continuation_token` to paginate through subsequent sets of short videos.

### Use cases

- List all short-form videos belonging to a target YouTube channel.
- Track recent YouTube Shorts releases for content monitoring tools.
- Paginate through a channel's Shorts catalog for analytics dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/channel-short-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | Yes | Channel ID. |
| `continuation_token` | string | No | Token to continue fetching channel short videos. |

### Notes

- Pass `continuation_token` to retrieve the next page of short videos.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel ID Lookup](/apis/youtube/web/channel-id): Retrieves the unique YouTube channel ID associated with a specific channel name.
- [YouTube Channel ID from URL (V2)](/apis/youtube/web/channel-id-v2): Resolves a YouTube channel URL into its unique channel ID and standardized channel URL.
- [YouTube Channel Information](/apis/youtube/web/channel-info): Returns profile details and external links for a specified YouTube channel.

---
Machine-readable: [`catalog/models/youtube/web/channel-short-videos.json`](../../../../catalog/models/youtube/web/channel-short-videos.json) · Store page: https://www.sandbase.ai/model/youtube/web/channel-short-videos
