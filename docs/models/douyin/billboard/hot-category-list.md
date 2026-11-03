# Douyin Billboard Hot Category List API: pricing, parameters and code examples

`douyin/billboard/hot-category-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns category IDs and popularity metrics from Douyin hot list billboards. Supports filtering by billboard type, search keywords, and snapshot time ranges.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-category-list", "billboard_type": "rise"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-category-list', {'billboard_type': 'rise'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-category-list", {
  "billboard_type": "rise"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-category-list", sandbase.Params{
	"billboard_type": "rise",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-category-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Hot search term  |
| `end_date` | string |  | Snapshot end time  |
| `start_date` | string |  | Snapshot start time  |
| `snapshot_time` | string |  | Snapshot time  |
| `billboard_type` | string | yes | Billboard type  |

## Details

Returns a list of Douyin hot list categories for a given billboard type, with a category label, a count, and numeric category IDs. It needs one input, `billboard_type` (for example `rise`). You can narrow results with `keyword`, `snapshot_time`, or a `start_date` and `end_date` range.

### Use cases

- Pull the category labels and IDs for the `rise` billboard to build a category filter for other billboard calls.
- Compare the `num` counts across categories such as food and travel to see which categories have more entries.
- Run the call with different `snapshot_time` values to compare how the category list looks at different times.
- Search a `keyword` to check which categories a hot search term falls under.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-category-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"billboard_type": "rise"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `billboard_type` | string | Yes | Billboard type |
| `end_date` | string | No | Snapshot end time |
| `keyword` | string | No | Hot search term |
| `snapshot_time` | string | No | Snapshot time |
| `start_date` | string | No | Snapshot start time |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": [
    {
      "label": "美食",
      "num": 74,
      "value": [
        9000
      ]
    }
  ],
  "extra": {
    "now": 1793691107000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].label` | Category name in Chinese, for example `美食` (food) or `旅行` (travel). |
| `data[].num` | A count for the category. Larger numbers appear for broader categories, such as 326 for `站内玩法`. |
| `data[].value[]` | List of numeric category IDs for this label. Most labels have one ID, and some have several, such as `1004`, `1000` and `1002`. |
| `code / message` | `code` is `0` on success. `message` is an empty string in this response. |
| `extra.now` | Server time of the response as a Unix timestamp in milliseconds. |

### Notes

- `billboard_type` is the only required parameter. The example uses `rise`.
- Time filters are `snapshot_time` for a single snapshot, or `start_date` and `end_date` for a range.
- The response is a single list with no pagination fields.
- For the rising search items themselves, see [Douyin Rising Hot Search List](/apis/douyin/billboard/hot-rise-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-category-list.json`](../../../../catalog/models/douyin/billboard/hot-category-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-category-list
