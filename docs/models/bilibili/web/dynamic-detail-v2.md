# Bilibili Dynamic Details (V2) API: pricing, parameters and code examples

`bilibili/web/dynamic-detail-v2` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed data for a specific Bilibili dynamic post using its dynamic ID. Designed for video dynamics, providing author modules and engagement metrics such as comments, shares, and likes.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/dynamic-detail-v2", "dynamic_id": "1172584638000922630"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/dynamic-detail-v2', {'dynamic_id': '1172584638000922630'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/dynamic-detail-v2", {
  "dynamic_id": "1172584638000922630"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/dynamic-detail-v2", sandbase.Params{
	"dynamic_id": "1172584638000922630",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/dynamic-detail-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `dynamic_id` | string | yes | Dynamic id  |

## Details

Retrieve detailed dynamic information from Bilibili by querying a specific `dynamic_id`. This endpoint specializes in video dynamic posts and returns structured dynamic module metadata.

### Use cases

- Inspect video dynamic post content and author information.
- Track engagement statistics such as comments, forwards, and likes.
- Parse structured dynamic module metadata for Bilibili feeds.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/dynamic-detail-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"dynamic_id": "1172584638000922630"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `dynamic_id` | string | Yes | Dynamic id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "item": {
      "modules": [
        {
          "module_type": "MODULE_TYPE_AUTHOR",
          "module_author": {
            "pub_text": "2026年02月23日 21:07"
          }
        }
      ]
    }
  }
}
```

### Notes

- Requires `dynamic_id` to specify the target dynamic post.
- Intended for video dynamics (DYNAMIC_TYPE_AV), returning metrics for comments, forwards, and likes.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/dynamic-detail-v2.json`](../../../../catalog/models/bilibili/web/dynamic-detail-v2.json) · Store page: https://www.sandbase.ai/model/bilibili/web/dynamic-detail-v2
