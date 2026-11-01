# TikTok Web ID

`tiktok/web/generate-webid` · api · TikTok

Returns a TikTok web_id value for web session handling. Accepts optional parameters including url, app_id, referer, user_agent, and user_unique_id.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/generate-webid"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/generate-webid', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/generate-webid", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/generate-webid", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/generate-webid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | Url  |
| `app_id` | integer |  | App Id  |
| `referer` | string |  | Referer  |
| `user_agent` | string |  | User Agent  |
| `user_unique_id` | string |  | User Unique Id  |

## Details

Retrieve a valid `web_id` for TikTok web requests using optional session metadata like `url`, `user_agent`, and `app_id`.

### Use cases

- Obtain a web identifier for downstream TikTok web requests.
- Configure simulated web sessions using custom `user_agent` and `referer` values.
- Track distinct browser contexts by pairing with a `user_unique_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-webid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | No | — |
| `app_id` | integer | No | — |
| `referer` | string | No | — |
| `user_agent` | string | No | — |
| `user_unique_id` | string | No | — |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "web_id": "7693533461642692109"
}
```

### Notes

- All input parameters including `url`, `app_id`, and `user_agent` are optional.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-webid.json`](../../../../catalog/models/tiktok/web/generate-webid.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-webid
