# Bilibili Dynamic Detail

`bilibili/web/dynamic-detail` · api · Bilibili

Returns detailed information for a specified Bilibili dynamic post, such as image, text, or article dynamics, using its unique dynamic ID.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/dynamic-detail", "dynamic_id": "1172584638000922630"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/dynamic-detail', {'dynamic_id': '1172584638000922630'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/dynamic-detail", {
  "dynamic_id": "1172584638000922630"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/dynamic-detail", sandbase.Params{
	"dynamic_id": "1172584638000922630",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/dynamic-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `dynamic_id` | string | yes | Dynamic id  |

## Details

Retrieve detailed module data for an image, text, or article post on Bilibili using `dynamic_id`.

### Use cases

- Inspect post content and module components for a specific dynamic post.
- Display text, image, or article dynamic metadata on an external dashboard.
- Analyze dynamic post structures across community feeds.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/dynamic-detail" \
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
          "module_type": "MODULE_TYPE_TOP"
        }
      ]
    }
  }
}
```

### Notes

- Requires a valid post identifier in `dynamic_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/dynamic-detail.json`](../../../../catalog/models/bilibili/web/dynamic-detail.json) · Store page: https://www.sandbase.ai/model/bilibili/web/dynamic-detail
