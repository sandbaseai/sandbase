# Douyin DOU+ Talent Categories API: pricing, parameters and code examples

`douyin/douplus/talent-categories` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the Douyin DOU+ talent category directory. Use this endpoint to retrieve category hierarchies for talent discovery and promotional workflows.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/douplus/talent-categories"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/douplus/talent-categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/douplus/talent-categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/douplus/talent-categories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/douplus/talent-categories` with the body above minus `model`.

## Details

Returns the list of talent categories used by Douyin DOU+. The request takes no parameters, so you send an empty JSON object.

### Use cases

- Fill a category dropdown in a tool that searches for Douyin creators to promote.
- Fetch the valid category names before you filter talents by category.
- Keep a local copy of the DOU+ category names to check user input.
- Show the category list in a creator discovery dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/douplus/talent-categories" \
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
  "data": {
    "categoryList": [
      {
        "name": "剧情"
      }
    ]
  },
  "msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `code` | Status code of the response. The sample shows `0`. |
| `msg` | Message text. It is an empty string in the sample. |
| `data.categoryList[]` | List of talent categories. Each item is one category. |
| `data.categoryList[].name` | Category name in Chinese, for example `剧情`, `音乐` or `二次元`. |

### Notes

- The response has a flat list of names. It has no IDs and no nested sub-categories.
- Pass a `name` value to [Douyin DOU+ Talents by Category](/apis/douyin/douplus/talents-by-category) to list talents in that category.
- Use [Douyin DOU+ User Search](/apis/douyin/douplus/search-user) when you want to find a specific user instead of browsing by category.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin DOU+ Promotable Items](/apis/douyin/douplus/promotable-item-list): Returns the promotable video item list for a Douyin account on the DOU+ promotion page.
- [Douyin DOU+ User Search](/apis/douyin/douplus/search-user): Searches for Douyin users in the DOU+ delivery context using a Douyin ID or nickname.
- [Douyin DOU+ Talents by Category](/apis/douyin/douplus/talents-by-category): Returns a list of DOU+ talents filtered by category name or keyword.

---
Machine-readable: [`catalog/models/douyin/douplus/talent-categories.json`](../../../../catalog/models/douyin/douplus/talent-categories.json) · Store page: https://www.sandbase.ai/model/douyin/douplus/talent-categories
