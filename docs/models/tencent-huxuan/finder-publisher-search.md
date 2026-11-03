# Tencent Huxuan Video Account Creator Search API: pricing, parameters and code examples

`tencent-huxuan/finder-publisher-search` · data API · Tencent Huxuan · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.071429 per call · **Modes:** sync

Search or browses QQ Huxuan Video Account creators by optional nickname keyword with page-number pagination. Use it to discover and shortlist video creators for Tencent Huxuan campaign planning.

## Pricing

- **$0.071429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent-huxuan/finder-publisher-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent-huxuan/finder-publisher-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent-huxuan/finder-publisher-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent-huxuan/finder-publisher-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tencent-huxuan/finder-publisher-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number. The first page is 1. default `1` |
| `keyword` | string |  | Creator nickname keyword. Leave empty to browse the default marketplace list.  |

## Details

Returns a page of WeChat Channels (Video Account) creators listed in the Tencent Huxuan marketplace. Each creator comes with an `appid`, profile labels, audience size band, average engagement figures and pricing or cost indexes. The only inputs are an optional nickname `keyword` and a `page` number.

### Use cases

- Shortlist video creators in a given niche by reading `auth_profession`, `category_level1` and `city_label`.
- Compare creators by `expected_cpm`, `expected_cpe` and `cost_effectiveness_index` when planning a campaign budget.
- Find fast-growing accounts using `fans_num_growth_rate` and `fans_num_increment`.
- Look up a known creator by nickname keyword and collect their `appid` for follow-up queries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tencent-huxuan/finder-publisher-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Creator nickname keyword. Leave empty to browse the default marketplace list. |
| `page` | integer | No | Page number. The first page is 1. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "item": [
    {
      "ader_long_video_price": "0",
      "ader_short_video_price": "0",
      "aid_avg_read_rate": 0,
      "aid_heart_rate": "0",
      "aid_interaction_rate": "0",
      "aid_share_rate": "0",
      "appid": "sphubNYn8stSgto",
      "auth_company": "",
      "auth_profession": "母婴育儿自媒体",
      "avatar": "https://wx.qlogo.cn/finderhead/CdoXZ7ia64HTeHFbN9iaXHygE2UUf7Eoa8ia2HYN95Wy9A/0",
      "avg_comment_pv": "6491",
      "avg_fav_pv": "6万+"
    }
  ],
  "msg": "",
  "r0_token": "",
  "ret": 0,
  "scene": 2,
  "total_num": 10000,
  "trace_id": "dae68ecf-918e-4331-8963-2c7bc60dd7d7"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `item[].appid` | Creator account ID, for example `sphubNYn8stSgto`. Use it to identify the creator in other calls. |
| `item[].auth_profession` | Verified profession label of the creator, such as a parenting or finance self-media tag. It can be an empty string. |
| `item[].city_label / item[].finder_sex` | City label of the creator and a numeric gender code. The response does not explain what each code means. |
| `item[].fans_num_level` | Follower count band, for example `500万+`. It is a range label, not an exact count. |
| `item[].fans_num_growth_rate / item[].fans_num_increment / item[].fans_num_growth_range` | Follower growth figures. The growth rate is a number, the increment is a band such as `5千~1万`, and the range is a band such as `<5%`. |
| `item[].avg_read_count / item[].avg_interaction_count / item[].avg_like_count` | Average views, interactions and likes per video, shown as banded text such as `290万+`. |
| `item[].avg_comment_pv / item[].avg_share_pv / item[].avg_fav_pv / item[].avg_heart_pv` | Average comment, share, favorite and heart counts per video, shown as text values or bands. |
| `item[].expected_cpm / item[].expected_cpe` | Expected cost per thousand impressions and expected cost per engagement for this creator. |
| `item[].cooperation_index / item[].cost_effectiveness_index` | Marketplace index scores for how well the creator fits cooperation and cost. Higher values are not defined in the response, so compare them only across creators. |
| `item[].component_metrics[]` | Click metrics per component category (`all`, `game`, `net_service`). Each row has `click_avg`, `click_rate` and `video_count`. |

### Notes

- Send an empty body to browse the default marketplace list. Set `keyword` to filter by creator nickname.
- Set `page` to move through results. The first page is 1. The response gives `total_num` (10000 in this sample).
- `ret` is `0` and `msg` is empty when the call succeeds. `trace_id` identifies the request.
- To search official account creators instead, use [Tencent Huxuan Official Account Creator Search](/apis/tencent-huxuan/mp-publisher-search).

### Pricing

$0.071429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tencent-huxuan/finder-publisher-search.json`](../../../catalog/models/tencent-huxuan/finder-publisher-search.json) · Store page: https://www.sandbase.ai/model/tencent-huxuan/finder-publisher-search
