# TikTok User Profile Share Link API: pricing, parameters and code examples

`tiktok/app-v3/open-app-to-user-profile` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a TikTok deep link that launches the TikTok app directly to a specified creator profile page using their user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/open-app-to-user-profile", "uid": "107955"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/open-app-to-user-profile', {'uid': '107955'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/open-app-to-user-profile", {
  "uid": "107955"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/open-app-to-user-profile", sandbase.Params{
	"uid": "107955",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/open-app-to-user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User id, obtained from the user profile interface.  |

## Details

Returns a TikTok short link that opens the TikTok app on a given creator's profile page. It needs one input, the numeric `uid` of the TikTok user.

### Use cases

- Put a profile link in an email or SMS so recipients land on the creator's page in the TikTok app.
- Build a list of short profile links for creators in an influencer outreach sheet.
- Add a tappable profile button to a mobile web page that hands off to the TikTok app.
- Turn user IDs stored in your database into shareable profile URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/open-app-to-user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "107955"}'
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
  "short_url": "https://www.tiktok.com/t/ZP9ytvwQWXNKj-TV1h1/",
  "status": 0,
  "uid": "107955"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `short_url` | Short TikTok link (`https://www.tiktok.com/t/...`) that opens the app on the requested user's profile. |
| `uid` | The user ID you sent in the request, echoed back so you can match the link to the input. |
| `status` | Status code of the call. The sample response returns `0` for a successful call. |

### Notes

- Get the `uid` from [TikTok User Profile Details](/apis/tiktok/app-v3/user-profile). To start from a username, call [TikTok User ID by Username](/apis/tiktok/app-v3/user-id-and-sec-user-id-by-username).
- Pass `uid` as a string, for example `"107955"`.
- For a link to a specific video instead of a profile, use [TikTok Video App Share Link](/apis/tiktok/app-v3/open-app-to-video-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/open-app-to-user-profile.json`](../../../../catalog/models/tiktok/app-v3/open-app-to-user-profile.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/open-app-to-user-profile
