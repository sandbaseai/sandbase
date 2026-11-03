# Douyin Search Field Options API: pricing, parameters and code examples

`douyin/xingtu-v2/search-field-options` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call · **Modes:** sync

Get Search Field Options on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.002 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/search-field-options"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/search-field-options', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/search-field-options", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/search-field-options", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/search-field-options` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `task_category` | integer |  | Task category, 1=Douyin video, 6=Douyin live, 11=Toutiao article default `1` |
| `platform_source` | integer |  | Platform source, 1=Douyin, 2=Toutiao default `1` |

## Details

Returns the filter option lists that Douyin Xingtu uses in its creator search. Each option set is a JSON string that holds codes and labels, such as audience groups, video labels, brands and local-life ranges. It needs `platform_source` and `task_category`, and both have defaults.

### Use cases

- Build a filter UI for creator search by loading the audience group and video label options.
- Map numeric label codes to their Chinese names before you filter or report on creators.
- Fill a city picker from the province and city lists in `service_options.local_location`.
- List the brand options so users can pick a brand for order experience filters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/search-field-options" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"platform_source": 1, "task_category": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `platform_source` | integer | No | Platform source, 1=Douyin, 2=Toutiao |
| `task_category` | integer | No | Task category, 1=Douyin video, 6=Douyin live, 11=Toutiao article |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "service_options": {
    "aa_live_character_label": "[{\"value\":11101,\"label\":\"出镜人性别\",\"children\":[{\"value\":1110101,\"label\":\"男\"},{\"valu…",
    "aa_live_content_label": "[{\"value\":10901,\"label\":\"传奇游戏\"},{\"value\":10902,\"label\":\"仙侠游戏\"},{\"value\":10903,\"l…",
    "aa_live_game_category_label": "[{\"value\":11201,\"label\":\"角色扮演\"},{\"value\":11202,\"label\":\"动作游戏\"},{\"value\":11203,\"l…",
    "aa_live_order_label": "[{\"value\":11001,\"label\":\"传奇游戏\"},{\"value\":11002,\"label\":\"仙侠游戏\"},{\"value\":11003,\"l…",
    "fans_crowd_profile": "[{\"value\":58,\"label\":\"Z世代\"},{\"value\":60,\"label\":\"小镇青年\"},{\"value\":55,\"label\":\"新锐白…",
    "fuse_video_labels_v2": "[{\"label_index\":631,\"label_name\":\"时尚\",\"label_level\":1,\"children\":[{\"label_index\"…",
    "game_brand_fans_limit": "[{\"game_brand_fans_limit_min\":100000},{\"game_brand_fans_limit_min\":50000,\"game_b…",
    "link_crowd_profile": "[{\"value\":58,\"label\":\"Z世代\"},{\"value\":60,\"label\":\"小镇青年\"},{\"value\":55,\"label\":\"新锐白…",
    "local_gmv": "[{\"local_gmv_ge\":500000},{\"local_gmv_ge\":100000,\"local_gmv_le\":500000},{\"local_g…",
    "local_item_cnt": "[{\"local_item_cnt__ge\":20},{\"local_item_cnt__ge\":10},{\"local_item_cnt__ge\":5},{\"…",
    "local_item_rate": "[{\"local_item_rate__ge\":0.05},{\"local_item_rate__ge\":0.10},{\"local_item_rate__ge…",
    "local_item_type": "[{\"label\":\"美食\",\"value\":1000000,\"children\":[{\"label\":\"火锅\",\"value\":1003000},{\"labe…"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `base_resp.status_code / base_resp.status_message` | Status of the call. `0` with an empty message means the request succeeded. |
| `service_options.fuse_video_labels_v2` | JSON string with a nested video label tree. Each node has `label_index`, `label_name`, `label_level` and `children`. For example, `63101` is a level 2 label under `631`. |
| `service_options.fans_crowd_profile / service_options.link_crowd_profile` | JSON strings with audience group options as `value` and `label` pairs, such as `58` for Z世代 and `60` for 小镇青年. |
| `service_options.aa_live_content_label / service_options.aa_live_game_category_label / service_options.aa_live_character_label` | JSON strings with label options for live content, game categories and on-screen persona traits. The character label has `children` under each group. |
| `service_options.playlet_label` | JSON string with genre label options for short dramas, as `value` and `label` pairs. |
| `service_options.local_item_type / service_options.local_item_type_all` | JSON strings with nested category trees for local-life items, such as 美食 with 火锅 as a child. Each node has `label`, `value` and `children`. |
| `service_options.local_location` | JSON string that maps each province name to a list of its city names. |
| `service_options.local_gmv / service_options.local_order_cnt / service_options.local_order_atv / service_options.local_order_gpm` | JSON strings with range buckets for local-life filters. Bounds use keys that end in `_ge` (at least) and `_le` (at most). |
| `service_options.order_experience_brand / service_options.order_experience_compare_brands` | JSON strings with lists of single-entry objects. Each maps a brand ID to a brand name, such as `1094492` to 立白. |
| `service_options.order_experience_industry` | JSON string with an industry tree. Each node has `id`, `name` and `children`. |

### Notes

- Every value inside `service_options` is a string that holds JSON. Parse it again to read the options.
- `platform_source` takes `1` for Douyin or `2` for Toutiao. `task_category` takes `1` for Douyin video, `6` for Douyin live or `11` for Toutiao article.
- Use the option codes as filter values when you search creators with [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v2/search-creator).

### Pricing

$0.002 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/search-field-options.json`](../../../../catalog/models/douyin/xingtu-v2/search-field-options.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/search-field-options
