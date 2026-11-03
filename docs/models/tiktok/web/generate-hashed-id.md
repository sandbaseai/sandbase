# TikTok Web Hashed ID API: pricing, parameters and code examples

`tiktok/web/generate-hashed-id` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Calculates a hashed identifier for TikTok Web based on a provided email address. This endpoint takes an email input and returns the corresponding hashed ID value.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/generate-hashed-id", "email": "test@example.com"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/generate-hashed-id', {'email': 'test@example.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/generate-hashed-id", {
  "email": "test@example.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/generate-hashed-id", sandbase.Params{
	"email": "test@example.com",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/generate-hashed-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `email` | string | yes | Email address  |

## Details

Returns a hashed identifier for an email address, as used by TikTok Web. It needs one input, the `email` string. The response holds a single `hashed_id` value.

### Use cases

- Turn a plain email address into a `hashed_id` before you use it in a TikTok Web workflow.
- Compare `hashed_id` values for a list of emails without keeping the raw addresses in your own records.
- Build a lookup table that maps each email in your user list to its `hashed_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-hashed-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `email` | string | Yes | Email address |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "hashed_id": "7dd39e8713c40837f6ca56a44ba13da737eb608737b40e0b3c4975528c607309"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `hashed_id` | The hashed identifier calculated from the `email` you sent. |
| `hashed_id` | The value is a lowercase hexadecimal string, 64 characters long. |
| `hashed_id` | This is the only field in the response, so you can read it straight from the top level of the JSON object. |

### Notes

- Send the address in the `email` parameter as a plain string. The call has no other parameters, so there is no pagination.
- For other TikTok Web identifiers, see [TikTok Web ID](/apis/tiktok/web/generate-webid) and [TikTok Web TTWID Identifier](/apis/tiktok/web/generate-ttwid).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-hashed-id.json`](../../../../catalog/models/tiktok/web/generate-hashed-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-hashed-id
