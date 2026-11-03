# Bilibili Streaming Areas API: pricing, parameters and code examples

`bilibili/web/all-live-areas` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the complete list of streaming broadcast areas and categories on Bilibili. This endpoint provides category identifiers and partition structures without requiring any parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/all-live-areas"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/all-live-areas', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/all-live-areas", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/all-live-areas", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/bilibili/web/all-live-areas` with the body above minus `model`.

## Details

Returns the full list of live streaming parent categories on Bilibili, with the child areas inside each one. It needs no input. Send an empty JSON object as the request body.

### Use cases

- Build a category filter or menu for a live streaming discovery tool.
- Map a child area `id` to its Chinese area name when you process live stream data.
- Store the parent and child area structure to group live rooms by game type.
- Check which areas are marked hot or locked before you show them in a list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/all-live-areas" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": [
    {
      "id": 2,
      "list": [
        {
          "act_id": "0",
          "area_type": 0,
          "complex_area_name": "",
          "hot_status": 0,
          "id": "86",
          "lock_status": "0",
          "name": "英雄联盟",
          "old_area_id": "4"
        }
      ],
      "name": "网游"
    }
  ],
  "message": "success",
  "msg": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One parent category, such as online games, mobile games or single-player games. |
| `data[].id` | Numeric ID of the parent category. |
| `data[].name` | Name of the parent category, in Chinese. |
| `data[].list[]` | The child areas that belong to this parent category. |
| `data[].list[].id` | ID of the child area. It is returned as a string. |
| `data[].list[].name` | Name of the child area, in Chinese. Examples are game titles or groups like other single-player games. |
| `data[].list[].old_area_id` | ID of an older area that this child area maps to. It is returned as a string. |
| `data[].list[].hot_status / data[].list[].lock_status` | Flags for the child area. In the sample, `hot_status` is `0` and `lock_status` is `"0"`. |
| `data[].list[].act_id / data[].list[].area_type / data[].list[].complex_area_name` | Extra area attributes. In the sample, `act_id` is `"0"`, `area_type` is `0` and `complex_area_name` is empty. |

### Notes

- This API takes no parameters. Send `{}` as the body.
- Parent `id` values are numbers, while child `id` values are strings.
- Child areas sit under `data[].list[]`, so loop over both levels to build a flat list of areas.
- To look at a single live room, call [Bilibili Live Room Details](/apis/bilibili/web/live-room-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.
- [Bilibili Comprehensive Popular Videos](/apis/bilibili/web/com-popular): Returns a comprehensive list of trending videos on Bilibili, including video metadata, author details, and engagement statistics across pages.

---
Machine-readable: [`catalog/models/bilibili/web/all-live-areas.json`](../../../../catalog/models/bilibili/web/all-live-areas.json) · Store page: https://www.sandbase.ai/model/bilibili/web/all-live-areas
