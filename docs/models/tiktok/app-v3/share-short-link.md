# TikTok Share Short Link API: pricing, parameters and code examples

`tiktok/app-v3/share-short-link` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Converts standard TikTok long links into shortened shareable URLs. Supply the full target web address to return the compressed redirect URL.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/share-short-link", "url": "https://www.tiktok.com/passport/web/logout/"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/share-short-link', {'url': 'https://www.tiktok.com/passport/web/logout/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/share-short-link", {
  "url": "https://www.tiktok.com/passport/web/logout/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/share-short-link", sandbase.Params{
	"url": "https://www.tiktok.com/passport/web/logout/",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/share-short-link` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Long link or link to convert  |

## Details

Generate shortened TikTok share links by supplying a target web address via the `url` parameter.

### Use cases

- Shorten long TikTok URLs for cleaner sharing across social channels.
- Format streamlined links for messaging campaigns and customer communications.
- Generate compact redirect links from standard web addresses.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/share-short-link" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/passport/web/logout/"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Long link or link to convert |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "shorten_url": "https://www.tiktok.com/t/ZP9D9bsTn4duw-MPwTI/",
  "status_code": 0
}
```

### Notes

- Pass the full target URL into `url` to obtain the shortened equivalent.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/share-short-link.json`](../../../../catalog/models/tiktok/app-v3/share-short-link.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/share-short-link
