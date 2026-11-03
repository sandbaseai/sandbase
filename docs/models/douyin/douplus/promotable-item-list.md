# Douyin DOU+ Promotable Items API: pricing, parameters and code examples

`douyin/douplus/promotable-item-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the promotable video item list for a Douyin account on the DOU+ promotion page. Includes item details based on specified promotion targets and optimization objectives.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/douplus/promotable-item-list", "sec_uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/douplus/promotable-item-list', {'sec_uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/douplus/promotable-item-list", {
  "sec_uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/douplus/promotable-item-list", sandbase.Params{
	"sec_uid": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/douplus/promotable-item-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` |  |  | Number of items, default 30  |
| `aim_ids` |  |  | Optional advanced parameter — optimization objective code(s), comma separated.  |
| `sec_uid` | string | yes | sec_uid of the delivery account (required)  |
| `target_id` |  |  | Promotion target (the goal card on the DOU+ page), default 31 (likes & comments).  |

## Details

Returns the list of videos on a Douyin account that can be promoted with DOU+, with the author and basic video details for each. It needs the account's `sec_uid`. You can also set the promotion goal with `target_id` and the number of items with `count`.

### Use cases

- Build a list of videos on a Douyin account that can be chosen for a DOU+ campaign.
- Skip videos that are already promoted or too old by checking `is_item_promotional` and `is_over_90_days`.
- Page through all promotable videos of an account to review its recent posts.
- Compare which videos qualify under different `target_id` goals.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/douplus/promotable-item-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | sec_uid of the delivery account (required) |
| `aim_ids` | string | No | Optional advanced parameter — optimization objective code(s), comma separated. |
| `count` | string | No | Number of items, default 30 |
| `target_id` | string | No | Promotion target (the goal card on the DOU+ page), default 31 (likes & comments). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cursor": "1779354857000",
  "has_more": 1,
  "item_info_list": [
    {
      "aweme_info": {
        "author": {
          "avatar_medium": {
            "uri": "720x720/aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c745843",
            "url_list": [
              "https://p26.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_9186d2f6f96…"
            ]
          },
          "nickname": "栗子味",
          "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"
        },
        "aweme_id": "7701639863695617457",
        "can_play": false,
        "create_time": 1793177767000,
        "desc": "伊人妆 秋眉晃 宛在水中央",
        "is_daily_story": false,
        "is_photo": false,
        "is_slides": false
      },
      "disable_multi_select": false,
      "douplus_user_post_tag": "爆款预定",
      "is_ad": false,
      "is_friend_video": false,
      "is_item_promotional": false,
      "is_over_90_days": false,
      "item_can_mount_enterprise_cart": 0,
      "item_source": {
        "item_generaion": 0,
        "source_type": 0
      },
      "playlet_type": 0
    }
  ],
  "status_code": 0,
  "status_msg": "",
  "support_tabs": [
    1
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `item_info_list[]` | One promotable video with its details and promotion flags. |
| `item_info_list[].aweme_info.aweme_id` | ID of the video, as a string. |
| `item_info_list[].aweme_info.desc` | Caption text of the video. |
| `item_info_list[].aweme_info.create_time` | Time the video was posted, as a 13-digit number that looks like a millisecond Unix timestamp. |
| `item_info_list[].aweme_info.author.nickname / item_info_list[].aweme_info.author.sec_uid` | Display name and `sec_uid` of the account that posted the video. |
| `item_info_list[].aweme_info.is_photo / item_info_list[].aweme_info.is_slides / item_info_list[].aweme_info.is_daily_story` | Flags that show whether the item is a photo post, a slideshow, or a daily story. |
| `item_info_list[].is_item_promotional / item_info_list[].is_over_90_days / item_info_list[].is_ad` | Flags for whether the item is already promotional, is older than 90 days, or is an ad. |
| `item_info_list[].douplus_user_post_tag` | Short label shown on some items, such as `爆款预定`. It is missing on other items. |
| `cursor / has_more` | Paging values. `has_more` is `1` when more items are available. |
| `support_tabs` | List of tab codes the account supports on the DOU+ page. |

### Notes

- `sec_uid` is the long string that starts with `MS4w`. It is the same value that appears in `item_info_list[].aweme_info.author.sec_uid`.
- `count` sets the number of items per call. `target_id` defaults to `31` (likes and comments). `aim_ids` takes comma separated codes.
- `cursor` and `has_more` are returned in the response. The request schema has no cursor parameter, so use `count` to control the size of the list.
- To get full video data for an `aweme_id`, call [Douyin Douplus Video Detail](/apis/douyin/douplus/video-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin DOU+ User Search](/apis/douyin/douplus/search-user): Searches for Douyin users in the DOU+ delivery context using a Douyin ID or nickname.
- [Douyin DOU+ Talent Categories](/apis/douyin/douplus/talent-categories): Returns the Douyin DOU+ talent category directory.
- [Douyin DOU+ Talents by Category](/apis/douyin/douplus/talents-by-category): Returns a list of DOU+ talents filtered by category name or keyword.

---
Machine-readable: [`catalog/models/douyin/douplus/promotable-item-list.json`](../../../../catalog/models/douyin/douplus/promotable-item-list.json) · Store page: https://www.sandbase.ai/model/douyin/douplus/promotable-item-list
