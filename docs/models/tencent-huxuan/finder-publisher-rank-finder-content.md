# Tencent Huxuan Hot Content Trends API: pricing, parameters and code examples

`tencent-huxuan/finder-publisher-rank-finder-content` · data API · Tencent Huxuan · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.042857 per call · **Modes:** sync

List QQ Huxuan hot Video Account content by month and creator category, with six descending sort metrics and page-number pagination. Use it to research monthly content trends for Tencent Huxuan campaign planning.

## Pricing

- **$0.042857 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent-huxuan/finder-publisher-rank-finder-content"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent-huxuan/finder-publisher-rank-finder-content', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent-huxuan/finder-publisher-rank-finder-content", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent-huxuan/finder-publisher-rank-finder-content", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tencent-huxuan/finder-publisher-rank-finder-content` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starting at 1. Each page contains up to 48 items. default `1` |
| `sort` | string |  | Sort metric. Results are sorted in descending order. one of: `INTERACTION`, `PLAY`, `THUMB_LIKE`, `HEART_LIKE`, `COMMENT`, `SHARE`; default `"INTERACTION"` |
| `month` | string |  | Statistics month in yyyy-MM format. Omit to use the latest month available on QQ Huxuan.  |
| `category` | string |  | Creator category. ALL includes every category. one of: `ALL`, `FOOD`, `LIFESTYLE`, `COMEDY`, `EMOTION`, `SOCIETY`, `HUMANITIES_ARTS`, `DRAMA`, `ENTERTAINMENT`, `TECHNOLOGY`, `FINANCE`, `FILM_TV_VARIETY` …; default `"ALL"` |

## Details

This API returns a ranked list of hot Video Account videos from QQ Huxuan for one month. Each item includes the creator, the video description and comment count. You can filter by creator `category`, choose a `sort` metric and set the `month`. All inputs are optional.

### Use cases

- Find the top videos in the `FOOD` or `AUTOMOTIVE` category for a given month to plan a campaign.
- Compare which creators lead a month when sorted by `SHARE` versus `PLAY`.
- Check the fan size band of creators behind hot videos before shortlisting them.
- Scan video descriptions and hashtags to spot recurring topics in a category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tencent-huxuan/finder-publisher-rank-finder-content" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | No | Creator category. ALL includes every category. |
| `month` | string | No | Statistics month in yyyy-MM format. Omit to use the latest month available on QQ Huxuan. |
| `page` | integer | No | Page number, starting at 1. Each page contains up to 48 items. |
| `sort` | string | No | Sort metric. Results are sorted in descending order. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "categories": [
    {
      "label": "生活",
      "value": 3
    }
  ],
  "ds_list": [
    202609
  ],
  "list": [
    {
      "appid": "sph9pxlN4zSxI1e",
      "avatar": "https://wx.qlogo.cn/finderhead/kqodNCVWpEsJiaBUjvp0sDFwI7y5uG3ibVYTpTib0syQCIw45…",
      "category_level1": 1,
      "fans_num_level": "250万+",
      "nickname": "鸟王大叔Nice",
      "video": {
        "ad_component_status": 0,
        "ader_name": "",
        "aid": "",
        "comment_pv": "67875",
        "cover_url": "https://findera4.video.qq.com/251/20304/stodownload?encfilekey=2fG3V4WwQPmz5NHId…",
        "delete_flag": 0,
        "description": "别眨眼，让你看到幸福的鸟“凌波仙子”你见过吗?真的幸福有妈妈带着长大。也看到了母亲的不容易#鸟类育儿#凌波仙子水雉#人与自然万物和谐共处",
        "event_show_type": 0
      },
      "view_id": "f3DtaBy46K3tdPaS-GOHGa-D5gfmHup4fpJVVDN9jDqmZAdkxGUJH1RkwXMsHTxXbwzuDkjG4b0O7TvK…"
    }
  ],
  "msg": "",
  "period": "2026-09-30",
  "ret": 0,
  "total_num": 859,
  "trace_id": "c9422a1b-6f2f-4a31-9b09-82d1c41c69ae"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `list[]` | One ranked entry per video, with the creator and video details. Entries follow the chosen `sort` order. |
| `list[].nickname / list[].appid` | Creator display name and the creator's `appid`. |
| `list[].fans_num_level` | Fan count band of the creator as a text label, such as `250万+`. |
| `list[].category_level1` | Numeric ID of the creator's top-level category. It matches a `value` in `categories`. |
| `list[].video.description` | Video caption text, including hashtags. |
| `list[].video.comment_pv` | Comment count for the video, returned as a string. |
| `list[].video.cover_url / list[].avatar` | Links to the video cover image and the creator avatar image. |
| `total_num` | Total number of items for the chosen filters. |
| `categories[]` | Pairs of category `label` and numeric `value`. |
| `ds_list` | Months available for the `month` filter, written as `yyyyMM` numbers such as `202609`. |

### Notes

- Send `month` as `yyyy-MM`. The response lists available months in `ds_list` as `yyyyMM` numbers, and `period` shows the end date of the period returned.
- Each page holds up to 48 items. Raise `page` from 1 and compare against `total_num` to know when to stop.
- Match `list[].category_level1` to `categories[].value` to get the category label.
- To look up creators by name, use [Tencent Huxuan Video Account Creator Search](/apis/tencent-huxuan/finder-publisher-search).

### Pricing

$0.042857 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tencent-huxuan/finder-publisher-rank-finder-content.json`](../../../catalog/models/tencent-huxuan/finder-publisher-rank-finder-content.json) · Store page: https://www.sandbase.ai/model/tencent-huxuan/finder-publisher-rank-finder-content
