# Douyin Video Search Filter Options API: pricing, parameters and code examples

`douyin/index/item-filter-options` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns all supported filter options and permissible values for Douyin video search queries. Use these criteria to construct structured search requests.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/item-filter-options"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/item-filter-options', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/item-filter-options", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/item-filter-options", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/item-filter-options` with the body above minus `model`.

## Details

Returns the filter options that Douyin video search accepts. The request takes no input. Each option has an `id`, a Chinese `name`, and an English `name_en`.

### Use cases

- Fill filter dropdowns for category, publish time, duration and video type in a Douyin video search screen.
- Check that a category, date range, duration or label `id` is valid before you send a video search request.
- Map Chinese filter names to English labels for a bilingual interface.
- Cache the option lists once and reuse them when you build search queries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/item-filter-options" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "categories": [
    {
      "id": "0",
      "name": "垂类不限",
      "name_en": "All categories"
    }
  ],
  "date_types": [
    {
      "id": 0,
      "name": "发布时间不限",
      "name_en": "Any publish time"
    }
  ],
  "duration_types": [
    {
      "id": 0,
      "name": "时长不限",
      "name_en": "Any duration"
    }
  ],
  "label_types": [
    {
      "id": 0,
      "name": "类型不限",
      "name_en": "Any type"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `categories[].id` | Category ID. The value `0` means all categories. Pass this ID when you filter by category. |
| `categories[].name / categories[].name_en` | Category name in Chinese and in English, for example `剧情` and `Drama`. |
| `date_types[].id` | Publish time filter value. It is a number such as `0`, `3` or `7`. The English names suggest `0` means any time and the others mean the last 3 or 7 days. |
| `date_types[].name / date_types[].name_en` | Publish time label in Chinese and in English, for example `Last 7 days`. |
| `duration_types[].id` | Video duration filter value. For example `1` is 0-15 seconds and `6` is 15-60 seconds. `0` means any duration. |
| `duration_types[].name / duration_types[].name_en` | Duration label in Chinese and in English, for example `15-60 seconds`. |
| `label_types[].id` | Video type filter value. For example `1` is low-follower hit and `2` is high completion rate. `0` means any type. |
| `label_types[].name / label_types[].name_en` | Video type label in Chinese and in English. |

### Notes

- Category `id` values are strings, for example `"601"`. The `id` values in `date_types`, `duration_types` and `label_types` are numbers.
- Use the `id` values from this response as filter values in the video search request. Call [Douyin Index Video Search](/apis/douyin/index/item-query) to run the search.
- Use [Douyin Video Search Suggestions](/apis/douyin/index/item-sug) to find search terms.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/item-filter-options.json`](../../../../catalog/models/douyin/index/item-filter-options.json) · Store page: https://www.sandbase.ai/model/douyin/index/item-filter-options
