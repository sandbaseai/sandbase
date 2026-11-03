# Douyin Xingtu Content Trend Guide API: pricing, parameters and code examples

`douyin/xingtu-v2/content-trend-guide` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns content trend guide data from Douyin Xingtu via static CDN JSON. Provides insights into trending content directions without requiring session cookies.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/content-trend-guide"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/content-trend-guide', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/content-trend-guide", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/content-trend-guide", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/content-trend-guide` with the body above minus `model`.

## Details

Returns a list of Xingtu content trend guide entries and a list of industry categories used to group them. The request needs no input parameters.

### Use cases

- Build a list of Douyin marketing reports and trend articles with titles, descriptions, links and thumbnails.
- Filter guide entries by industry by matching each entry's `industry` value to a category `id`.
- Show only the guides whose `start_date` and `end_date` cover today's date.
- Track new trend reports and campaign pages that Xingtu publishes for brands.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/content-trend-guide" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "bee_dsrc_15973": [
    {
      "id": 1597300000013,
      "name": "电商平台",
      "order": 13
    }
  ],
  "bee_dsrc_15974": [
    {
      "description": "2026抖音明星营销报告",
      "end_date": "2026-12-31",
      "id": 1597400000077,
      "industry": "1597300000007",
      "link": "https://mp.weixin.qq.com/s/gGXBDob4hkUWNCEI6dXuVQ",
      "link_source": "other",
      "name": "2026明星营销增长新范式",
      "start_date": "2026-07-01",
      "thumb": "https://lf3-beecdn.bytetos.com/obj/ies-fe-bee-upload/bee_prod/biz_631/tos_93c411…",
      "type": "content"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `bee_dsrc_15973[].id / bee_dsrc_15973[].name` | ID and Chinese name of an industry category, such as 电商平台 (e-commerce platform), 服装配饰 (clothing and accessories) or 汽车 (cars). |
| `bee_dsrc_15973[].order` | Sort position of the category in the list. |
| `bee_dsrc_15974[].id` | ID of a trend guide entry. |
| `bee_dsrc_15974[].name / bee_dsrc_15974[].description` | Title of the guide and a short summary. The description can be an empty string. |
| `bee_dsrc_15974[].industry` | ID of the industry category the guide belongs to. It matches an `id` in `bee_dsrc_15973`, and it is returned as a string. |
| `bee_dsrc_15974[].link` | URL of the full report or article. |
| `bee_dsrc_15974[].link_source` | Where the link is hosted, for example `feishu` or `other`. |
| `bee_dsrc_15974[].start_date / bee_dsrc_15974[].end_date` | Dates in `YYYY-MM-DD` format that bound the period of the guide. |
| `bee_dsrc_15974[].thumb` | URL of the cover image for the guide. |
| `bee_dsrc_15974[].type` | Type label of the guide entry, such as `content`. |

### Notes

- The request body is an empty object `{}`. There are no pagination parameters.
- The top-level keys `bee_dsrc_15973` and `bee_dsrc_15974` hold the industry list and the guide list. Join them on the industry ID.
- To find creators for a trend, call [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v2/search-creator).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/content-trend-guide.json`](../../../../catalog/models/douyin/xingtu-v2/content-trend-guide.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/content-trend-guide
