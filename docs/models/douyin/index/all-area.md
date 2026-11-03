# Douyin Index Area List API: pricing, parameters and code examples

`douyin/index/all-area` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the complete list of supported geographic areas available for Douyin Index queries. Use this data to map regional codes and locations for trend analysis.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/all-area"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/all-area', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/all-area", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/all-area", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/all-area` with the body above minus `model`.

## Details

Returns the full tree of geographic areas used by Douyin Index, from the national level down to districts. The response also lists the content categories. The request takes no input, so send an empty JSON object.

### Use cases

- Fill a region dropdown in a dashboard with province, city and district names.
- Map six-digit area codes such as `110105` to their district names.
- Build a lookup table of area codes before you run regional Douyin Index queries.
- Fetch the category IDs and names to label category-based reports.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/all-area" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "all_area_list": [
    {
      "area_level": "1",
      "children": [
        {
          "area_level": "2",
          "children": [
            {
              "area_level": "3",
              "children": [
                {
                  "area_level": "4",
                  "label": "东城区",
                  "value": "110101"
                }
              ],
              "label": "北京",
              "value": "110000"
            }
          ],
          "label": "北京",
          "value": "11"
        }
      ],
      "label": "全国",
      "value": "86"
    }
  ],
  "all_category_list": [
    {
      "category_id": "0",
      "category_name": "全部"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `all_area_list[]` | Top-level list of areas. The one entry in the sample is the country node, with `label` `全国` and `value` `86`. |
| `all_area_list[].children[]` | Nested child areas. The tree goes province, city, district, and each node has its own `children` list until the lowest level. |
| `all_area_list[].area_level / all_area_list[].children[].area_level` | Depth of the node in the tree, sent as a string. `1` is the country, `2` is a province-level area, `3` is a city, `4` is a district. |
| `all_area_list[].label / all_area_list[].children[].label` | Area name in Chinese, for example `北京`, `河北` or `东城区`. |
| `all_area_list[].value / all_area_list[].children[].value` | Area code for the node. Province-level codes have two digits, such as `11`. City and district codes have six digits, such as `130100` and `130102`. |
| `all_area_list[].children[].children[].children[].value` | District-level code, for example `110101` for `东城区`. These are the leaf nodes in the sample. |
| `all_category_list[].category_id` | ID of a content category, sent as a string. `0` is used for the all-categories entry. |
| `all_category_list[].category_name` | Category name in Chinese, for example `全部`, `酒店` or `餐饮`. |
| `BaseResp.StatusCode / BaseResp.StatusMessage` | Status of the call. `StatusCode` is `0` and `StatusMessage` is empty in the sample response. |

### Notes

- The request has no parameters. Send `{}` as the body.
- Area codes are strings. Keep them as strings so you do not lose any digits.
- Municipalities such as `北京` appear at both the province level (`11`) and the city level (`110000`) with the same label.
- To check which dates you can query next, call [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.
- [Douyin Brand Hot Videos Time Scope](/apis/douyin/index/brand-hot-videos-time-scope): Returns the queryable time scope for Douyin brand hot videos.

---
Machine-readable: [`catalog/models/douyin/index/all-area.json`](../../../../catalog/models/douyin/index/all-area.json) · Store page: https://www.sandbase.ai/model/douyin/index/all-area
