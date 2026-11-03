# Douyin Recommended Insight Reports API: pricing, parameters and code examples

`douyin/index/insight-recommend` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended trend insight reports featured on the Douyin index home page. Useful for tracking high-level platform trends and discovering top reports without specifying filters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/insight-recommend"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/insight-recommend', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/insight-recommend", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/insight-recommend", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/insight-recommend` with the body above minus `model`.

## Details

Returns a list of recommended trend insight reports shown on the Douyin index home page. It takes no input. Each item has a title, author, summary, keywords, cover images and a home page slot.

### Use cases

- Pull the reports currently featured on the Douyin index home page into a content feed.
- Track which report topics and keywords the platform promotes, such as brand advertising themes.
- Collect report IDs and titles, then fetch full report content for offline reading or archiving.
- Compare the `slot` order and `create_time` of featured reports over repeated calls to see how the home page selection changes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/insight-recommend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "author": "动见",
    "category": "1",
    "coop_institution": "",
    "cover": [
      {
        "cover_url": "https://lf3-trendinsight.bytetos.com/obj/ad-count-platform/454a8cf56cab9237",
        "height": "338",
        "width": "592"
      }
    ],
    "create_time": "2022-06-21 12:52:42",
    "id": "728",
    "introduction": "营销是围绕“人”展开的经营活动，一切广告的背后都是真实的“人”，尤其是品牌广告，更需要围绕用户需求、用户心智展开。有用户，流量才有价值，才能产生效用。",
    "keywords": "品牌广告 ROI 长效经营",
    "result_type": "",
    "slot": "home-1",
    "summary": "品牌投放的关键是“真实的人”。企业需要放弃“品牌广告=曝光广告”的旧思维，建立“用户为中心”的投放思维，进行体系化、科学化的投放，就能找够人、找对人、留住人，并…",
    "title": "动见首发 | 人群比流量更重要，品牌广告如何高效抓住“人”"
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | Report ID as a string. Use it to look up the full report. |
| `title` | Report title in Chinese. |
| `author` | Name of the report author, for example `动见`. |
| `introduction / summary` | Short text about the report. `introduction` is a lead-in and `summary` is a longer description of the main argument. |
| `keywords` | Space-separated keywords for the report topic. |
| `create_time` | Report creation time as a `YYYY-MM-DD HH:MM:SS` string. |
| `slot` | Position of the report on the home page, such as `home-1`, `home-2`, `home-3`. |
| `cover[].cover_url` | URL of a cover image for the report. |
| `cover[].width / cover[].height` | Size of the cover image, given as strings. |
| `category / visit_cnt` | `category` is a category code as a string. `visit_cnt` is a visit count as a string and shows `0` in this sample. |

### Notes

- The request body is an empty object `{}`. The response is a top-level array with no pagination parameters.
- `id` and numeric values such as `visit_cnt`, `width` and `height` come back as strings.
- `coop_institution` and `result_type` are empty strings in this sample.
- To read a full report, pass its `id` to [Douyin Trend Report Detail](/apis/douyin/index/report-detail). To find other reports, use [Douyin Trend Report Search](/apis/douyin/index/report-search).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/insight-recommend.json`](../../../../catalog/models/douyin/index/insight-recommend.json) · Store page: https://www.sandbase.ai/model/douyin/index/insight-recommend
