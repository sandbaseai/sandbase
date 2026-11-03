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

Returns a TikTok short URL that opens the TikTok app on a direct message conversation with a given user. It needs one input, the numeric `uid` of the target user.

### Use cases

- Add a "Message me on TikTok" button to a website or email that opens a chat with a specific account.
- Build outreach links for creator collaboration campaigns, one link per creator `uid`.
- Send a support or community link in a bio page or QR code that starts a TikTok chat.
- Generate message links in bulk for a list of known user IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/open-app-to-send-private-message" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "6860674014860641286"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User id, obtained from the user profile interface. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "short_url": "https://www.tiktok.com/t/ZP9ytcR1Nvfyn-vWa0B/",
  "status": 0,
  "uid": "6860674014860641286"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `short_url` | Short TikTok link. Opening it on a phone launches the TikTok app and starts a direct message with the user. |
| `uid` | The user ID the link was built for. It matches the `uid` sent in the request. |
| `status` | Status code of the call. The value `0` appears in a successful response. |

### Notes

- Get the `uid` from the user profile API, for example [TikTok User Profile Details](/apis/tiktok/app-v3/user-profile).
- If you only have a username, call [TikTok User ID by Username](/apis/tiktok/app-v3/user-id-and-sec-user-id-by-username) first to find the ID.
- To link to a profile instead of a chat, use [TikTok User Profile Share Link](/apis/tiktok/app-v3/open-app-to-user-profile).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/open-app-to-send-private-message.json`](../../../../catalog/models/tiktok/app-v3/open-app-to-send-private-message.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/open-app-to-send-private-message
