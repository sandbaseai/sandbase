# Xiaohongshu (RED) Group Search API: pricing, parameters and code examples

`xiaohongshu/app-v2/search-groups` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Searches Xiaohongshu community groups by keyword with support for pagination, recommendation flags, and search filters.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/search-groups", "is_recommend": 0, "keyword": "OpenAI", "page_no": 0, "search_id": "", "source": "unifiedSearchGroup"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/search-groups', {'is_recommend': 0, 'keyword': 'OpenAI', 'page_no': 0, 'search_id': '', 'source': 'unifiedSearchGroup'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/search-groups", {
  "is_recommend": 0,
  "keyword": "OpenAI",
  "page_no": 0,
  "search_id": "",
  "source": "unifiedSearchGroup"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/search-groups", sandbase.Params{
	"is_recommend": 0,
	"keyword": "OpenAI",
	"page_no": 0,
	"search_id": "",
	"source": "unifiedSearchGroup",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/search-groups` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `source` | string |  | Source, default "unifiedSearchGroup" default `"unifiedSearchGroup"` |
| `keyword` | string | yes | Search keyword  |
| `page_no` | integer |  | Page number, start from 0 default `0` |
| `search_id` | string |  | Search ID, pass value from first search response for pagination default `""` |
| `is_recommend` | integer |  | Is recommend, 0=no, 1=yes default `0` |

## Details

Searches Xiaohongshu (RED) community groups by `keyword`. Each result includes the group name, ID, member count, creation time and recent activity. The response also lists the sort and location filters the search offers.

### Use cases

- Find active Xiaohongshu groups about a brand or topic such as OpenAI.
- Compare group sizes and recent activity to choose which communities to monitor.
- Collect group IDs and creator IDs to track who runs groups in a niche.
- Read the available sort options to see how group results can be ranked.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/search-groups" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `is_recommend` | integer | No | Is recommend, 0=no, 1=yes |
| `page_no` | integer | No | Page number, start from 0 |
| `search_id` | string | No | Search ID, pass value from first search response for pagination |
| `source` | string | No | Source, default "unifiedSearchGroup" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "group_info_list": [
      {
        "active_info": {
          "last_active_time": 0,
          "last_seven_day_active_user_num": 1,
          "last_seven_day_msg_num": 1,
          "yesterday_active_user_num": 0
        },
        "allow_group_map": true,
        "avatar": "https://sns-avatar-qc.xhscdn.com/im-avatar/6705aab84a43c5000181a0cf.png?imageVie…",
        "create_source": "iconEntry",
        "create_time": 1726006843000,
        "group_creator_id": "5b0a501f11be105edbf57a2c",
        "group_desc": "",
        "group_id": "137043980683949163",
        "group_live_switch": true,
        "group_master_id": "5b0a501f11be105edbf57a2c",
        "group_name": "分享尖端科技，Open最强AI",
        "group_type": 1
      }
    ],
    "group_search_filters": [
      {
        "id": "order_by",
        "name": "Sort by",
        "options": [
          {
            "id": "default",
            "name": "All",
            "need_location_permission": false
          }
        ]
      }
    ],
    "has_more": false
  },
  "debug_id": "9ccc2d5c",
  "debug_info": "gAAAAABq6ZFqTDryUFdcvIzj2g2mgpYHFrQuFEAhRKjaEDFMV9cV1Iy2BBPpdOdm9IiqQZ-jUEPNbVZM…",
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.group_info_list[].group_id` | ID of the group, returned as a string. |
| `data.group_info_list[].group_name / group_desc` | Name and description of the group. The description can be empty. |
| `data.group_info_list[].group_user_num / user_num_limit` | Current member count and the maximum number of members the group allows. |
| `data.group_info_list[].active_info.last_seven_day_active_user_num / last_seven_day_msg_num / yesterday_active_user_num` | Counts of active users and messages over the last seven days, and active users yesterday. |
| `data.group_info_list[].create_time` | Time the group was created, as a number that looks like a Unix timestamp in milliseconds. |
| `data.group_info_list[].group_creator_id / group_master_id` | User IDs of the group creator and the group master. |
| `data.group_info_list[].join_group_approval` | `true` when joining the group needs approval. |
| `data.group_info_list[].is_banned / is_dismiss / is_hidden` | Flags that show whether the group is banned, dismissed or hidden. |
| `data.group_search_filters[].id / name` | Filter group, such as `order_by` (Sort by) or `location_at` (Location). |
| `data.group_search_filters[].options[].id / name` | Choices inside a filter, such as `activity` (Most active) or `memberNum` (Most members). |
| `data.has_more` | `true` when more results are available for the next page. |

### Notes

- Set `page_no` to 0 for the first page and raise it for later pages.
- Pass the `search_id` from the first response when you request later pages. The trimmed response shown here does not include a `search_id` field, so check your own response for it.
- Check `data.has_more` to see if another page exists.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/search-groups.json`](../../../../catalog/models/xiaohongshu/app-v2/search-groups.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/search-groups
