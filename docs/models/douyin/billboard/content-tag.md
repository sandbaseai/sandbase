# Douyin Billboard Vertical Content Tags API: pricing, parameters and code examples

`douyin/billboard/content-tag` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of vertical content tags available on the Douyin billboard platform. Useful for categorizing trending topics and discovering niche content segments.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/content-tag"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/content-tag', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/content-tag", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/content-tag", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/content-tag` with the body above minus `model`.

## Details

Returns the list of vertical content tags used on the Douyin billboard. Each top-level category has child tags. The API needs no input parameters.

### Use cases

- Build a category picker for a Douyin trend dashboard from the top-level tags and their children.
- Map Douyin vertical tags to your own content taxonomy by matching `label` and `value`.
- Find niche segments under a category such as food or travel before you pull billboard rankings.
- Store tag `value` IDs so you can reuse them as filters in other billboard calls.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/content-tag" \
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
      "children": [
        {
          "label": "品酒教学",
          "value": 62808
        }
      ],
      "count": 0,
      "label": "美食",
      "value": 628
    }
  ],
  "extra": {
    "now": 1793691103000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One top-level vertical category. |
| `data[].label` | Category name in Chinese, for example `美食` (food) or `旅行` (travel). |
| `data[].value` | Numeric ID of the top-level category, for example `628`. |
| `data[].children[]` | Sub-tags that belong to the category. |
| `data[].children[].label` | Sub-tag name in Chinese, for example `美食教程`. |
| `data[].children[].value` | Numeric ID of the sub-tag, for example `62804`. It starts with the parent `value` in the sample. |
| `data[].count` | Count value on the category. It is `0` in the sample response. |
| `extra.now` | Timestamp of the response, as a 13-digit number that looks like milliseconds since the Unix epoch. |
| `code / message` | `code` is `0` on success. `message` is an empty string in the sample. |

### Notes

- Send an empty JSON body `{}`. The API has no request parameters.
- Child `value` IDs in the sample begin with the parent `value`. For example, `62804` sits under `628`.
- The `label` fields are in Chinese. Keep the `value` IDs as your stable keys.
- For ranked content, call [Douyin Billboard Hot Category List](/apis/douyin/billboard/hot-category-list) or [Douyin Total Hot Billboard](/apis/douyin/billboard/hot-total-list) next.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.
- [Douyin Account Fan Interest Search Terms](/apis/douyin/billboard/hot-account-fans-interest-search-list): Returns the top ten search terms reflecting fan interest over the last three days for a specified Douyin creator account using their user sec_id.

---
Machine-readable: [`catalog/models/douyin/billboard/content-tag.json`](../../../../catalog/models/douyin/billboard/content-tag.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/content-tag
