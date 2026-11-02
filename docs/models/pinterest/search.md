# Pinterest Search API: pricing, parameters and code examples

`pinterest/search` · data API · Pinterest · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.018 per call · **Modes:** sync

Search Pinterest pins by keyword and get pin IDs, URLs, titles, descriptions and images, with cursor pagination.

## Pricing

- **$0.018 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pinterest/search", "query": "modern kitchen design"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pinterest/search', {'query': 'modern kitchen design'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pinterest/search", {
  "query": "modern kitchen design"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pinterest/search", sandbase.Params{
	"query": "modern kitchen design",
})
```

Same call via the path form: `POST /v1/api/pinterest/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `trim` | boolean |  | Set to true for a trimmed down version of the response.  |
| `query` | string | yes | Search query for Pinterest pins.  |
| `cursor` | string |  | Pagination cursor from a previous response to fetch the next page.  |

## Details

Search Pinterest for a query and get matching pins. Set `trim` for a compact response.

### Use cases

- Research visual trends for a product category.
- Find inspiration and competitor creatives.
- Collect pins for mood boards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pinterest/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "home office ideas", "trim": true}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query for Pinterest pins. |
| `trim` | boolean | No | Set to true for a trimmed down version of the response. |
| `cursor` | string | No | Pagination cursor from a previous response to fetch the next page. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "cursor": "<next cursor>",
  "pins": [
    {
      "id": "4887421732865150",
      "url": "https://www.pinterest.com/pin/4887421732865150",
      "images": {
        "url": "https://i.pinimg.com/…"
      }
    }
  ]
}
```

### Notes

- Paginate with the `cursor` from the previous response.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/pinterest/search.json`](../../../catalog/models/pinterest/search.json) · Store page: https://www.sandbase.ai/model/pinterest/search
