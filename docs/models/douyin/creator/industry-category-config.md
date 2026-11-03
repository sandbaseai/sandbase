# Douyin Creator Industry Category Config API: pricing, parameters and code examples

`douyin/creator/industry-category-config` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns industry category configuration details for Douyin creators. Use this endpoint to inspect supported creator categories and related industry settings.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/industry-category-config"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/industry-category-config', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/industry-category-config", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/industry-category-config", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/creator/industry-category-config` with the body above minus `model`.

## Details

Returns the list of industry categories and their subcategories used on Douyin creator pages. It takes no input. Send an empty JSON object `{}`.

### Use cases

- Build a category dropdown for a Douyin creator dashboard from the `key` and `label` values.
- Map numeric category keys in other Douyin creator data to readable Chinese category names.
- Group brand or advertiser lists by top-level industry and subcategory.
- Check which subcategory keys belong to a given top-level industry.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/industry-category-config" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "industry_categories": [
      {
        "key": "-1",
        "label": "全部"
      }
    ],
    "industry_subcategories": {
      "1901": [
        {
          "key": "-1",
          "label": "全部"
        }
      ],
      "1903": [
        {
          "key": "-1",
          "label": "全部"
        }
      ],
      "1904": [
        {
          "key": "-1",
          "label": "全部"
        }
      ],
      "1905": [
        {
          "key": "-1",
          "label": "全部"
        }
      ],
      "1906": [
        {
          "key": "-1",
          "label": "全部"
        }
      ],
      "1907": [
        {
          "key": "-1",
          "label": "全部"
        }
      ],
      "1908": [
        {
          "key": "-1",
          "label": "全部"
        }
      ],
      "1909": [
        {
          "key": "-1",
          "label": "全部"
        }
      ],
      "1910": [
        {
          "key": "-1",
          "label": "全部"
        }
      ],
      "1911": [
        {
          "key": "-1",
          "label": "全部"
        }
      ],
      "1912": [
        {
          "key": "-1",
          "label": "全部"
        }
      ],
      "1913": [
        {
          "key": "-1",
          "label": "全部"
        }
      ]
    }
  },
  "status_code": 0,
  "status_msg": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.industry_categories[].key` | ID of a top-level industry category. The value `-1` stands for all categories. Other keys are numbers such as `1901`. |
| `data.industry_categories[].label` | Display name of the top-level category, in Chinese. For example `食品饮料` is the label for key `1903`. |
| `data.industry_subcategories` | Object keyed by top-level category key, such as `1901`. Each value is the list of subcategories for that industry. |
| `data.industry_subcategories.1901[].key` | ID of a subcategory under top-level category `1901`. The value `-1` stands for all subcategories. |
| `data.industry_subcategories.1901[].label` | Display name of the subcategory, in Chinese. For example `消费类电子产品` has key `190101`. |
| `status_code / status_msg` | Result of the call. `0` and `success` mean the request worked. |

### Notes

- No parameters are needed. Send `{}` as the request body.
- The first item in every list has `key` set to `-1` and label `全部` (all). Skip it if you only want real categories.
- The `key` type is mixed. The `-1` entry is a string, and the other entries are numbers. Compare keys as strings to be safe.
- To look up a subcategory list, use the top-level `key` as the property name in `data.industry_subcategories`. For content topics rather than industries, call [Douyin Content Categories](/apis/douyin/creator/creator-content-category).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/industry-category-config.json`](../../../../catalog/models/douyin/creator/industry-category-config.json) · Store page: https://www.sandbase.ai/model/douyin/creator/industry-category-config
