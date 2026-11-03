# Bilibili User ID Extraction API: pricing, parameters and code examples

`bilibili/web/get-user-id` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Extracts and returns a Bilibili user ID from a provided space share link. Takes a user profile URL and resolves the numeric account identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/get-user-id", "share_link": "https://static.sandbase.ai/examples/1d420101-6aa7-4cbd-a4d5-e04674de7ca9/input/1094426c-12a0-4ab7-aa39-e91b0f14d3c4.bin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/get-user-id', {'share_link': 'https://static.sandbase.ai/examples/1d420101-6aa7-4cbd-a4d5-e04674de7ca9/input/1094426c-12a0-4ab7-aa39-e91b0f14d3c4.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/get-user-id", {
  "share_link": "https://static.sandbase.ai/examples/1d420101-6aa7-4cbd-a4d5-e04674de7ca9/input/1094426c-12a0-4ab7-aa39-e91b0f14d3c4.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/get-user-id", sandbase.Params{
	"share_link": "https://static.sandbase.ai/examples/1d420101-6aa7-4cbd-a4d5-e04674de7ca9/input/1094426c-12a0-4ab7-aa39-e91b0f14d3c4.bin",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/get-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `share_link` | string | yes | User share link  |

## Details

This API takes a Bilibili user space share link in `share_link` and returns the numeric user ID found in it. The response has one field, `user_id`, returned as a string.

### Use cases

- Turn a copied `https://space.bilibili.com/...` link into a numeric ID for storage or matching.
- Clean a list of creator profile URLs collected from web pages into one ID column.
- Get the user ID you need before calling Bilibili profile, video, or dynamic endpoints.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/get-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_link": "https://space.bilibili.com/178360345"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_link` | string | Yes | User share link |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "user_id": "178360345"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user_id` | The numeric Bilibili account ID taken from the share link. For the example link `https://space.bilibili.com/178360345`, the value is `"178360345"`. |
| `user_id` | The value is a JSON string, not a number. Keep it as text when you store it or pass it on. |
| `user_id` | This is the only field in the response. It matches the number at the end of the space link in `share_link`. |

### Notes

- Pass a full space link such as `https://space.bilibili.com/178360345` in `share_link`.
- `user_id` is a string, so keep it as text if you pass it on to other calls.
- Use the ID with [Bilibili User Profile](/apis/bilibili/web/user-profile) to get account details, or with [Bilibili User Post Videos](/apis/bilibili/web/user-post-videos) to list the user's videos.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/get-user-id.json`](../../../../catalog/models/bilibili/web/get-user-id.json) · Store page: https://www.sandbase.ai/model/bilibili/web/get-user-id
