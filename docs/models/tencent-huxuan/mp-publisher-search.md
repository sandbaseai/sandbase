# Tencent Huxuan Official Account Creator Search API: pricing, parameters and code examples

`tencent-huxuan/mp-publisher-search` · data API · Tencent Huxuan · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.071429 per call · **Modes:** sync

Search or browses QQ Huxuan Official Account creators by optional nickname or account keyword with page-number pagination. Use it to discover and shortlist publishers for Tencent Huxuan campaign planning.

## Pricing

- **$0.071429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent-huxuan/mp-publisher-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent-huxuan/mp-publisher-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent-huxuan/mp-publisher-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent-huxuan/mp-publisher-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tencent-huxuan/mp-publisher-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number. The first page is 1. default `1` |
| `keyword` | string |  | Creator nickname or account keyword. Leave empty to browse the default marketplace list.  |

## Details

Returns a page of QQ Huxuan Official Account creators with their audience size, 30-day article metrics, ad prices and contact type. It takes an optional `keyword` (nickname or account keyword) and a `page` number. With no keyword it returns the default marketplace list.

### Use cases

- Shortlist Official Account creators for a campaign by comparing reads, likes and fan counts.
- Search a creator by nickname to check their listed ad prices and recent posting activity.
- Filter creators by contract type, such as personal accounts or company-run accounts.
- Page through the default marketplace list to build a candidate pool of publishers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tencent-huxuan/mp-publisher-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Creator nickname or account keyword. Leave empty to browse the default marketplace list. |
| `page` | integer | No | Page number. The first page is 1. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "item": [
    {
      "advertorial_price": [
        {
          "key": "1",
          "value": 8000000
        }
      ],
      "agreement_status": 1,
      "aid_article_365_cnt": "0",
      "appid": "wxa06332d586319f7b",
      "area": {
        "city": "天津",
        "province": "天津"
      },
      "article_cnt_30d": 46,
      "article_send_pv": 46,
      "article_top_weapp": [
        "wxfaa08012777a431e"
      ],
      "articles": [],
      "avatar": "http://wx.qlogo.cn/mmhead/sTJptKvBQLLXiaATrhL8NreQyXI3Je5tLZMktXT6WlB4ibE2WHTgw0…",
      "avg_comment_cnt_30d_idx": [
        {
          "key": "1",
          "value": 344
        }
      ],
      "avg_fin_read_rate_30d_idx": [
        {
          "key": "1",
          "value": 13
        }
      ]
    }
  ],
  "msg": "",
  "ret": 0,
  "scene": 2,
  "total_num": 10000,
  "trace_id": "1f76d285-c709-425f-886b-4c95a9753ee4"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `item[].nickname / item[].appid` | The creator's display name and account ID. |
| `item[].fans_num / item[].fans_num_level` | Fan count and a fan-size label such as `500万+`. The `fans_num` value looks capped or rounded, so use the level label for a rough size. |
| `item[].often_read_fans_num` | Count of fans who read this account often. |
| `item[].advertorial_price[]` | Advertorial prices as `key` and `value` pairs. The `key` values `1`, `2` and `3` appear to be ad slot positions. Some slots show `0`. |
| `item[].first_advertorial_read_price` | A per-read price figure for the first advertorial slot. |
| `item[].mp_publisher_metrics` | Average 30-day post metrics as text: `avg_read_pv`, `mid_read_pv`, `avg_like_pv`, `avg_comment_pv`, `avg_share_pv`, `avg_zaikan_pv` and `avg_finished_read_rate`. Large read counts use a `万` suffix (ten thousand). |
| `item[].avg_read_pv_30d_idx[] / item[].avg_like_cnt_30d_idx[] / item[].avg_comment_cnt_30d_idx[]` | The same 30-day averages as numbers, split by `key` (`1`, `2`, `3`) for each post position. |
| `item[].article_cnt_30d / item[].last_article_create_time` | Number of articles in the last 30 days and the time of the latest article as a Unix timestamp string. |
| `item[].contract_type / item[].contractor_name` | Whether the account is `personal` or `company`, and the company name when one is listed. |
| `item[].area.province / item[].area.city` | The creator's listed location. Both can be empty. |

### Notes

- Send `{}` to browse the default list. Add `keyword` to search, and raise `page` (starting at 1) to move through results.
- `total_num` gives the result count for the query and `ret` is `0` on success.
- Price values such as `advertorial_price[].value` are raw integers, and the response does not state the currency or unit.
- To find creators on the video account side, use [Tencent Huxuan Video Account Creator Search](/apis/tencent-huxuan/finder-publisher-search).

### Pricing

$0.071429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tencent-huxuan/mp-publisher-search.json`](../../../catalog/models/tencent-huxuan/mp-publisher-search.json) · Store page: https://www.sandbase.ai/model/tencent-huxuan/mp-publisher-search
