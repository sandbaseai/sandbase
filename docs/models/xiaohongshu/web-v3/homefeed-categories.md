# Xiaohongshu (RED) Homepage Categories API: pricing, parameters and code examples

`xiaohongshu/web-v3/homefeed-categories` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns a list of available homefeed category channels on Xiaohongshu (RED). Use this endpoint to inspect valid category identifiers for content discovery.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/web-v3/homefeed-categories"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/web-v3/homefeed-categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/web-v3/homefeed-categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/web-v3/homefeed-categories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/web-v3/homefeed-categories` with the body above minus `model`.

## Details

Returns the list of homefeed category channels on Xiaohongshu (RED). Each entry has a category `id` and a display `name`. The API takes no input parameters.

### Use cases

- Build a channel menu that mirrors the homefeed tabs on Xiaohongshu.
- Look up the valid `id` values, such as `homefeed.food_v3`, before you request a category feed.
- Map category `id` values to their Chinese `name` labels in a dashboard or report.
- Check the current set of top-level channels by comparing the list between runs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/web-v3/homefeed-categories" \
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
    "categories": [
      {
        "id": "homefeed.fashion_v3",
        "name": "穿搭"
      }
    ]
  },
  "msg": "成功",
  "ok": true,
  "status": 200,
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.categories[]` | List of homefeed category channels. Each item is one channel. |
| `data.categories[].id` | Category identifier, for example `homefeed.fashion_v3`. Use this value when you need to refer to a channel. |
| `data.categories[].name` | Display name of the category in Chinese, for example `穿搭` (fashion) or `美食` (food). |
| `code / ok / success` | Status flags. `code` is `0` and `ok` and `success` are `true` when the call worked. |
| `msg` | Status message text. It is `成功` on a successful call. |

### Notes

- Send an empty JSON object `{}` as the request body. There are no parameters and no pagination.
- Category `id` values follow the pattern `homefeed.<channel>_v3`.
- To read posts from the homepage, call [Xiaohongshu (RED) Homepage Feed](/apis/xiaohongshu/web-v3/homefeed).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Homepage Feed](/apis/xiaohongshu/web-v3/homefeed): Retrieves recommended notes from the Xiaohongshu homepage feed.
- [Xiaohongshu (RED) Web Note Details](/apis/xiaohongshu/web-v3/note-detail): Returns detailed information for a specific Xiaohongshu note using its identifier and security token obtained from a web share link.
- [Xiaohongshu (RED) Search Suggestions](/apis/xiaohongshu/web-v3/search-suggest): Returns search query suggestions and autocomplete terms from Xiaohongshu (RED).

---
Machine-readable: [`catalog/models/xiaohongshu/web-v3/homefeed-categories.json`](../../../../catalog/models/xiaohongshu/web-v3/homefeed-categories.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/web-v3/homefeed-categories
