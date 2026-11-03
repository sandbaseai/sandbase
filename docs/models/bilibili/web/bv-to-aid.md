# Bilibili BV to AID Converter API: pricing, parameters and code examples

`bilibili/web/bv-to-aid` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Converts a Bilibili BV identifier to its corresponding numeric AID value. Input the target video BV string to return the legacy video identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/bv-to-aid", "bv_id": "BV1M1421t7hT"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/bv-to-aid', {'bv_id': 'BV1M1421t7hT'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/bv-to-aid", {
  "bv_id": "BV1M1421t7hT"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/bv-to-aid", sandbase.Params{
	"bv_id": "BV1M1421t7hT",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/bv-to-aid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bv_id` | string | yes | Video id  |

## Details

Returns the numeric AID for a Bilibili video. You send the video's BV identifier in `bv_id`, for example `BV1M1421t7hT`. The response is a single integer.

### Use cases

- Convert a BV string taken from a Bilibili video URL into its numeric AID.
- Normalize a list of mixed BV identifiers into numeric AIDs before storing them in a database.
- Match BV identifiers from one dataset against records in another dataset that keys videos by AID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/bv-to-aid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bv_id": "BV1M1421t7hT"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bv_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
1556386640
```

### Response fields

| Field | Meaning |
|---|---|
| `$` | The numeric AID of the video. This is the legacy numeric video identifier that matches the BV string you sent. |
| `$` | The value is a bare integer. No object or field names wrap it, so there are no keys to read. |
| `$` | For the sample input `BV1M1421t7hT`, the value is `1556386640`. |

### Notes

- Pass the BV string exactly as it appears in the video link, including the `BV` prefix and letter case.
- The body is a plain number, not a JSON object, so read it directly instead of looking up a key.
- To get video metadata for the same video, call [Bilibili Video Details](/apis/bilibili/web/one-video) or [Bilibili Web Video Details](/apis/bilibili/web/video-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.
- [Bilibili Comprehensive Popular Videos](/apis/bilibili/web/com-popular): Returns a comprehensive list of trending videos on Bilibili, including video metadata, author details, and engagement statistics across pages.

---
Machine-readable: [`catalog/models/bilibili/web/bv-to-aid.json`](../../../../catalog/models/bilibili/web/bv-to-aid.json) · Store page: https://www.sandbase.ai/model/bilibili/web/bv-to-aid
