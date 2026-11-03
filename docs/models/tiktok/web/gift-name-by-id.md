# TikTok Gift Name by ID API: pricing, parameters and code examples

`tiktok/web/gift-name-by-id` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the gift name associated with a specific TikTok gift identifier. Look up gift metadata using the required gift ID parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/gift-name-by-id", "gift_id": "10001"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/gift-name-by-id', {'gift_id': '10001'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/gift-name-by-id", {
  "gift_id": "10001"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/gift-name-by-id", sandbase.Params{
	"gift_id": "10001",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/gift-name-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gift_id` | string | yes | Gift ID  |

## Details

Returns the name of one TikTok gift for a given gift ID. The only input is `gift_id`, passed as a string.

### Use cases

- Turn numeric gift IDs from live stream messages into readable gift names.
- Label gift columns in a live stream analytics report.
- Build a lookup table of gift IDs and names for a single gift you see in your data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/gift-name-by-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"gift_id": "10001"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `gift_id` | string | Yes | Gift ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "gift_id": "10001",
  "gift_name": "鞭炮"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `code` | Status code of the lookup. The sample response shows `0`. |
| `gift_id` | The gift ID you sent in the request, returned as a string. |
| `gift_name` | The name of the gift. The sample returns `鞭炮` for `10001`, so names can be in Chinese. |

### Notes

- To look up several gifts in one call, use [TikTok Gift Names by IDs](/apis/tiktok/web/gift-names-by-ids).
- To see which gifts are available in a live room, call [TikTok Room Gift List](/apis/tiktok/web/live-gift-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/gift-name-by-id.json`](../../../../catalog/models/tiktok/web/gift-name-by-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/gift-name-by-id
