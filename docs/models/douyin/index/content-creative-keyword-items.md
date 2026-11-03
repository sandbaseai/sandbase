# Douyin Creative Keyword Related Videos API: pricing, parameters and code examples

`douyin/index/content-creative-keyword-items` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns videos associated with a specific trending keyword in a category. Filters include category ID, target keyword, analysis period, and end date.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/content-creative-keyword-items", "end_date": "1735660799", "keyword": "人工智能", "tag_id": "2027"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/content-creative-keyword-items', {'end_date': '1735660799', 'keyword': '人工智能', 'tag_id': '2027'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/content-creative-keyword-items", {
  "end_date": "1735660799",
  "keyword": "人工智能",
  "tag_id": "2027"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/content-creative-keyword-items", sandbase.Params{
	"end_date": "1735660799",
	"keyword": "人工智能",
	"tag_id": "2027",
})
```

Same call via the path form: `POST /v1/api/douyin/index/content-creative-keyword-items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `period` | string |  | "1" / "3" / "7" days one of: `1`, `3`, `7` |
| `tag_id` | string | yes | Category ID (same as category_id in fetch_item_query)  |
| `keyword` | string | yes | Hot keyword (typically from fetch_content_creative_keywords)  |
| `end_date` | string | yes | End date YYYYMMDD. **Must be a Sunday only when period=7**; any day for period=1/3  |

## Details

Returns videos linked to a trending keyword in one Douyin category. You send a category ID in `tag_id`, a `keyword`, and an `end_date`. You can also set `period` to `1`, `3` or `7` days.

### Use cases

- Find the videos behind a rising keyword such as `人工智能` in a single category.
- Compare which videos match a keyword over a 1, 3 or 7 day window.
- Check which video styles a category uses for a trending term before planning new content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-creative-keyword-items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "1735660799", "keyword": "人工智能", "tag_id": "2027"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End date YYYYMMDD. **Must be a Sunday only when period=7**; any day for period=1/3 |
| `keyword` | string | Yes | Hot keyword (typically from fetch_content_creative_keywords) |
| `tag_id` | string | Yes | Category ID (same as category_id in fetch_item_query) |
| `period` | string | No | "1" / "3" / "7" days |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": -1,
    "StatusMessage": "json data error，key:ca,2027,人工智能,1735660799,keyword_items_v2,aweme,7"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `BaseResp` | Status wrapper for the call. It is the only top-level object in the sample response. |
| `BaseResp.StatusCode` | Numeric status of the lookup. The sample request returned `-1`, which marks a failed lookup. |
| `BaseResp.StatusMessage` | Text describing the status. In the sample it reads `json data error` and then lists the values used for the lookup: `2027`, `人工智能`, `1735660799` and `7`. |

### Notes

- The sample request used `end_date` `1735660799` and returned `StatusCode` `-1`. The schema asks for `end_date` in `YYYYMMDD` format, so send a date like `20241229`.
- When `period` is `7`, `end_date` must be a Sunday. For `1` or `3`, any day works.
- Take `keyword` from [Douyin Content Creative Keywords](/apis/douyin/index/content-creative-keywords). Use the same category ID as `tag_id`.
- `period` accepts only the strings `1`, `3` and `7`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-creative-keyword-items.json`](../../../../catalog/models/douyin/index/content-creative-keyword-items.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-creative-keyword-items
