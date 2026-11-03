# Douyin Xingtu IP Activity List API: pricing, parameters and code examples

`douyin/xingtu-v2/ip-activity-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns Xingtu IP calendar activities across designated time windows, with optional filters for activity status, categories, and industries.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/ip-activity-list", "query_end_time": "1774972799", "query_start_time": "1767196800"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/ip-activity-list', {'query_end_time': '1774972799', 'query_start_time': '1767196800'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/ip-activity-list", {
  "query_end_time": "1774972799",
  "query_start_time": "1767196800"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/ip-activity-list", sandbase.Params{
	"query_end_time": "1774972799",
	"query_start_time": "1767196800",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/ip-activity-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `status_list` |  |  | IP status list  |
| `category_list` |  |  | IP category list  |
| `query_end_time` | string | yes | Query end timestamp, e.g. `1774972799`  |
| `industry_id_list` |  |  | Industry ID list  |
| `query_start_time` | string | yes | Query start timestamp, e.g. `1767196800`  |

## Details

Returns the Xingtu IP calendar activities that fall inside a time window. You pass a start and end Unix timestamp, and you can narrow the list by status, category, and industry.

### Use cases

- Build a calendar of Douyin Xingtu IP campaigns that run in a given quarter.
- List only the activities tied to certain industry IDs to find campaigns that fit a brand's sector.
- Track the investment (sign-up) window of each IP activity to plan when a brand must join.
- Pull activity names and descriptions to compare the content formats that Xingtu promotes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/ip-activity-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query_end_time": "1774972799", "query_start_time": "1767196800"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query_end_time` | string | Yes | Query end timestamp, e.g. `1774972799` |
| `query_start_time` | string | Yes | Query start timestamp, e.g. `1767196800` |
| `category_list` | string | No | IP category list |
| `industry_id_list` | string | No | Industry ID list |
| `status_list` | string | No | IP status list |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "ip_activity_detail_list": [
    {
      "description": "巨量星图首个AI漫剧合作项目，引入头部AI短剧机构、AI短剧创作者供给，为品牌方带来AI漫剧植入合作与定制漫剧合作；通过「好内容」+「促消费」全链模式，为品牌带…",
      "hero_image": "https://p3-star-fe-sign.byteimg.com/tos-cn-i-9hvokabxw2/1f29c4e773574ec6ac9dd414…",
      "id": "371",
      "invest_end_time": "1798688233",
      "invest_start_time": "1770521833",
      "ip_category": 1,
      "ip_end_time": "1798688207",
      "ip_industry": "1901,1903,1913",
      "ip_start_time": "1770521807",
      "name": "AI影漫计划",
      "status": 50
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `ip_activity_detail_list[]` | One IP activity per item. The list holds every activity that matches the time window and filters. |
| `ip_activity_detail_list[].id` | ID of the IP activity, returned as a string. Use it to look up one activity in the detail API. |
| `ip_activity_detail_list[].name` | Title of the IP activity. |
| `ip_activity_detail_list[].description` | Free-text description of the activity and its cooperation model. It is written in Chinese and may contain line breaks. |
| `ip_activity_detail_list[].hero_image` | URL of the cover image for the activity. The link is signed and carries an expiry value in its query string. |
| `ip_activity_detail_list[].ip_start_time / ip_activity_detail_list[].ip_end_time` | Start and end of the IP activity itself, as Unix timestamps in seconds, returned as strings. |
| `ip_activity_detail_list[].invest_start_time / ip_activity_detail_list[].invest_end_time` | Start and end of the investment period for the activity, as Unix timestamps in seconds, returned as strings. |
| `ip_activity_detail_list[].ip_category` | Integer code for the category of the activity. You can pass the same kind of value in `category_list`. |
| `ip_activity_detail_list[].ip_industry` | Comma-separated string of industry IDs linked to the activity. Each ID is a value you can use in `industry_id_list`. |
| `ip_activity_detail_list[].status` | Integer status code of the activity. You can filter on it with `status_list`. |

### Notes

- `query_start_time` and `query_end_time` are Unix timestamps in seconds, sent as strings, for example `1767196800`.
- `status_list` and `category_list` take arrays of integers. `industry_id_list` takes an array of strings.
- Call [Douyin Xingtu IP Activity Industry List](/apis/douyin/xingtu-v2/ip-activity-industry-list) to see industry IDs, and pass an activity `id` to [Douyin Xingtu IP Activity Detail](/apis/douyin/xingtu-v2/ip-activity-detail) for more data on one activity.
- A `base_resp.status_code` of `0` means the call succeeded.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/ip-activity-list.json`](../../../../catalog/models/douyin/xingtu-v2/ip-activity-list.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/ip-activity-list
