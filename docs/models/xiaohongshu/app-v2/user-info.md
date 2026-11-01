# Xiaohongshu (RED) User Information

`xiaohongshu/app-v2/user-info` · api · Xiaohongshu

Returns detailed profile data for a Xiaohongshu user. Look up accounts by providing either a specific user identifier or a profile share link.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/user-info", "user_id": "5c668b3e0000000012021605"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/user-info', {'user_id': '5c668b3e0000000012021605'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/user-info", {
  "user_id": "5c668b3e0000000012021605"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/user-info", sandbase.Params{
	"user_id": "5c668b3e0000000012021605",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User ID, e.g. "61b46d790000000010008153" default `""` |
| `share_text` | string |  | Xiaohongshu sharing link (support APP and Web sharing link) default `""` |

## Details

Retrieve detailed profile information for an account using either `user_id` or a profile URL in `share_text`.

### Use cases

- Inspect user profiles using direct account IDs.
- Extract account details from shared mobile or web URLs.
- Gather creator profile metadata for analytics workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | No | User ID, e.g. "61b46d790000000010008153" |
| `share_text` | string | No | Xiaohongshu sharing link (support APP and Web sharing link) |

### Notes

- Accepts queries by `user_id` or `share_text`.
- `share_text` supports both mobile app and web sharing links.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/model/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/model/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/model/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/user-info.json`](../../../../catalog/models/xiaohongshu/app-v2/user-info.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/user-info
