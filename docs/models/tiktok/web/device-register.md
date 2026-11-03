# TikTok Web Device Registration API: pricing, parameters and code examples

`tiktok/web/device-register` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Registers a virtual client session to generate a device ID and guest cookie for TikTok Web requests. Returns device tokens and session parameters.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/device-register"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/device-register', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/device-register", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/device-register", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/device-register` with the body above minus `model`.

## Details

Register a fresh TikTok web device and get its `deviceId`, a `ttwid` cookie and the user agent it was registered with. TikTok web endpoints expect a consistent device ID, cookie and user agent.

### Use cases

- Start a new crawling session with a valid device identity.
- Rotate device identities when a session gets rate limited.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/device-register" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cookie": "ttwid=1%7C0sAkVWZfNDVS5_Qlo8LP0DifeYAWTRV9QX4EOEOK6l8%7C1793670125%7C58a20d6afae…",
  "deviceId": "7703754514907055629",
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `deviceId` | Registered device ID. |
| `cookie` | Cookie string including `ttwid`. |
| `user_agent` | Use this exact user agent with the device ID and cookie. |

### Notes

- No parameters are required.
- Sign the requests you make with [TikTok Generate X-Bogus](/apis/tiktok/web/generate-xbogus) using the same user agent.

### Pricing

$0.002 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/device-register.json`](../../../../catalog/models/tiktok/web/device-register.json) · Store page: https://www.sandbase.ai/model/tiktok/web/device-register
