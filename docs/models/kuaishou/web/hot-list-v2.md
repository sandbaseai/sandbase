# Kuaishou Web Hot List (V2) API: pricing, parameters and code examples

`kuaishou/web/hot-list-v2` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns current trending search rankings and hot topics on Kuaishou web. Supports selecting different ranking boards using the board type parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/hot-list-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/hot-list-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/hot-list-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/hot-list-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/web/hot-list-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `board_type` | string |  | 榜单类型 (board_type)/Board Type default `"1"` |

## Details

Retrieve trending search keywords and popularity metrics from Kuaishou web. Filter topic categories using the optional `board_type` parameter.

### Use cases

- Track real-time trending topics and viral search terms across Kuaishou.
- Analyze keyword popularity scores and topic classifications.
- Monitor emerging discussions and public interest trends on the platform.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/hot-list-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `board_type` | string | No | — |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "hots": [
    {
      "hotValue": 12445774,
      "hotWordType": 0,
      "id": "6279572",
      "keyword": "国足vs塔吉克斯坦",
      "viewCount": 0
    }
  ]
}
```

### Notes

- Pass `board_type` to specify the ranking board category.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Web Share Short URL](/model/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/model/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/model/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/hot-list-v2.json`](../../../../catalog/models/kuaishou/web/hot-list-v2.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/hot-list-v2
