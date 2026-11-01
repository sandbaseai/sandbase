# Bilibili User ID Extraction

`bilibili/web/get-user-id` · api · Bilibili

Extracts and returns a Bilibili user ID from a provided space share link. Takes a user profile URL and resolves the numeric account identifier.

## Pricing

- **$0.0015 per call** (USD)
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

Resolve a user's unique numeric identifier by providing their profile URL in `share_link`. This endpoint extracts account IDs directly from standard Bilibili space links.

### Use cases

- Convert user profile share links into raw numeric Bilibili IDs.
- Resolve account identifiers for downstream Bilibili profile queries.
- Normalize user URLs collected from external web sources.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/get-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_link": "https://space.bilibili.com/178360345"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_link` | string | Yes | User share link |

### Notes

- Requires a valid profile share link passed to `share_link`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/get-user-id.json`](../../../../catalog/models/bilibili/web/get-user-id.json) · Store page: https://www.sandbase.ai/model/bilibili/web/get-user-id
