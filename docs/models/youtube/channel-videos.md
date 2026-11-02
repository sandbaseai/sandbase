# YouTube Channel Videos API: pricing, parameters and code examples

`youtube/channel-videos` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get public videos from a YouTube channel, with optional cursor-based pagination. Use it to browse a channel's uploads and continue through additional result pages.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/channel-videos", "channelId": "UCuAXFkgsw1L7xaCfnd5JJOw"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/channel-videos', {'channelId': 'UCuAXFkgsw1L7xaCfnd5JJOw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/channel-videos", {
  "channelId": "UCuAXFkgsw1L7xaCfnd5JJOw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/channel-videos", sandbase.Params{
	"channelId": "UCuAXFkgsw1L7xaCfnd5JJOw",
})
```

Same call via the path form: `POST /v1/api/youtube/channel-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | The cursor for pagination.  |
| `channelId` | string | yes | The unique identifier for a YouTube channel.  |

## Details

Get public videos from a YouTube channel, with optional cursor-based pagination. Use it to browse a channel's uploads and continue through additional result pages.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/channel-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channelId": "UCuAXFkgsw1L7xaCfnd5JJOw"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channelId` | string | Yes | The unique identifier for a YouTube channel. |
| `cursor` | string | No | The cursor for pagination. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/youtube/channel-videos.json`](../../../catalog/models/youtube/channel-videos.json) · Store page: https://www.sandbase.ai/model/youtube/channel-videos
