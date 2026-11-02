# TikTok Direct Message Share Link API: pricing, parameters and code examples

`tiktok/app-v3/open-app-to-send-private-message` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a TikTok share short URL to launch the TikTok application and open a direct message conversation with a designated user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/open-app-to-send-private-message", "uid": "6860674014860641286"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/open-app-to-send-private-message', {'uid': '6860674014860641286'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/open-app-to-send-private-message", {
  "uid": "6860674014860641286"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/open-app-to-send-private-message", sandbase.Params{
	"uid": "6860674014860641286",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/open-app-to-send-private-message` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User id, obtained from the user profile interface.  |

## Details

Generates a direct message short URL using a specified `uid`. Opening the link directs users to the TikTok mobile application to begin a conversation.

### Use cases

- Direct users into a TikTok direct message conversation via external links.
- Launch the TikTok app directly to a specific user chat screen.
- Generate mobile deep links for creator collaboration outreach.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/open-app-to-send-private-message" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "6860674014860641286"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User id, obtained from the user profile interface. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "short_url": "https://www.tiktok.com/t/ZP9D9gF4pxcad-bubD8/",
  "status": 0
}
```

### Notes

- Obtain the required `uid` parameter from the user profile interface.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/open-app-to-send-private-message.json`](../../../../catalog/models/tiktok/app-v3/open-app-to-send-private-message.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/open-app-to-send-private-message
