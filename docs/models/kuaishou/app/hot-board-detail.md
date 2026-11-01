# Kuaishou Hot Board Detail

`kuaishou/app/hot-board-detail` · api · Kuaishou

Returns trending topics and search keywords from Kuaishou hot boards based on the specified board identifier and board type.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/hot-board-detail"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/hot-board-detail', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/hot-board-detail", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/hot-board-detail", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/hot-board-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `boardId` | integer |  | 榜单ID/Board ID  |
| `boardType` | integer |  | 榜单类型/Board type default `1` |

## Details

Access trending keywords and ranking metrics from Kuaishou hot boards by passing `boardId` and `boardType`.

### Use cases

- Track trending keywords and their view counts on Kuaishou.
- Analyze hot topic rankings across different board categories.
- Monitor changes in popular search terms and popularity values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/hot-board-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `boardId` | integer | No | — |
| `boardType` | integer | No | — |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "hots": [
    {
      "hotValue": 11045606,
      "hotWordType": 0,
      "id": "6279572",
      "keyword": "国足vs塔吉克斯坦",
      "viewCount": 11491602,
      "wordId": "6279572"
    }
  ]
}
```

### Notes

- Accepts optional `boardId` and `boardType` parameters to target specific hot board lists.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/hot-board-detail.json`](../../../../catalog/models/kuaishou/app/hot-board-detail.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/hot-board-detail
