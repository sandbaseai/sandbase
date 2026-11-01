# TikTok Gift Names by IDs

`tiktok/web/gift-names-by-ids` · api · TikTok

Returns gift names for a batch of TikTok gift identifiers. Provide a list of gift IDs to look up their corresponding gift labels.

## Pricing

- **$0.0375 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/gift-names-by-ids", "gift_ids": ["10001", "10002", "10003"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/gift-names-by-ids', {'gift_ids': ['10001', '10002', '10003']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/gift-names-by-ids", {
  "gift_ids": [
    "10001",
    "10002",
    "10003"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/gift-names-by-ids", sandbase.Params{
	"gift_ids": []any{"10001", "10002", "10003"},
})
```

Same call via the path form: `POST /v1/api/tiktok/web/gift-names-by-ids` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gift_ids` | array | yes | Gift ID list, recommend 50/call for best value ($0.025), auto-process first 50 if more than 50  |

## Details

Look up gift names for multiple items using `gift_ids`. The endpoint resolves names for each specified gift identifier in batches.

### Use cases

- Map raw TikTok gift identifiers to readable gift names.
- Enrich live stream gift event logs with display labels.
- Build a local catalog of TikTok virtual gifts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/gift-names-by-ids" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"gift_ids": "<gift_ids>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `gift_ids` | array | Yes | Gift ID list, recommend 50/call for best value ($0.025), auto-process first 50 if more than 50 |

### Notes

- Accepts a list of identifiers via `gift_ids` and automatically processes the first 50 if more are provided.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/gift-names-by-ids.json`](../../../../catalog/models/tiktok/web/gift-names-by-ids.json) · Store page: https://www.sandbase.ai/model/tiktok/web/gift-names-by-ids
