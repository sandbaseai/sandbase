# Douyin XingTu KOL Profile API: pricing, parameters and code examples

`douyin/xingtu/kol-base-info-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get the XingTu (Douyin creator marketplace) profile of a KOL: followers, location, category tags, online status and available collaboration types.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-base-info-v1", "kolId": "7038603512770461703", "platformChannel": "_1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-base-info-v1', {'kolId': '7038603512770461703', 'platformChannel': '_1'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-base-info-v1", {
  "kolId": "7038603512770461703",
  "platformChannel": "_1"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-base-info-v1", sandbase.Params{
	"kolId": "7038603512770461703",
	"platformChannel": "_1",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-base-info-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |
| `platformChannel` | string | yes | Platform channel, supports the following parameters: _1: Douyin Video; _10: Douyin Live  |

## Details

This API returns the XingTu (Douyin creator marketplace) profile of one KOL. It needs a XingTu `kolId` and a `platformChannel` value (`_1` for Douyin video, `_10` for Douyin live).

### Use cases

- Check follower count and city of a Douyin creator before adding them to a campaign shortlist.
- Filter creators by content theme labels such as pet or cat content.
- Check `is_online` and `has_phone` to see whether a creator is active and reachable.
- Store `core_user_id` and `id` to join XingTu profiles with other creator records.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-base-info-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"kolId": "7038603512770461703", "platformChannel": "_1"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id` |
| `platformChannel` | string | Yes | Platform channel, supports the following parameters: _1: Douyin Video; _10: Douyin Live |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "abandon_sign_result": 0,
  "appeal_id": "0",
  "author_avatar_frame_icon": 20,
  "author_type": 1,
  "avatar_uri": "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_8c900db621…",
  "avg_play": 0,
  "aweme_tags": [],
  "base64_qrcode": "iVBORw0KGgoAAAANSUhEUgAAAWgAAAFoAQAAAABSnlx4AAACZElEQVR4nO2bzW7DMAyDySHv/8rcQT+2…",
  "base_resp": {
    "status_code": 0,
    "status_message": "Success"
  },
  "category_id": "1",
  "city": "长沙市",
  "content_theme_labels": [
    "宠物猫日常"
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | The XingTu `kolId` of the creator. It matches the `kolId` you sent. |
| `nick_name` | Display name of the creator. |
| `follower` | Follower count of the creator. |
| `city` | City of the creator, as a Chinese place name. |
| `content_theme_labels[]` | Content theme tags for the creator, such as pet cat topics. |
| `is_online / online_status` | Whether the creator is currently online on XingTu. `is_online` is a boolean and `online_status` is a numeric flag. |
| `is_star / e_commerce_enable / is_game_author` | Flags for creator type: XingTu star author, e-commerce enabled, and game author. |
| `opened_task_category` | List of task category IDs open for collaboration. It is returned as a string that holds a list. |
| `platform_channel[]` | Channel codes the creator is available on. The values `1` and `10` match `_1` (Douyin video) and `_10` (Douyin live). |
| `create_time / modify_time` | Unix timestamps in seconds as strings. |

### Notes

- Get `kolId` from [Douyin XingTu kolId Lookup](/apis/douyin/xingtu/xingtu-kolid-by-sec-user-id), [Douyin XingTu KOL ID by User ID](/apis/douyin/xingtu/xingtu-kolid-by-uid) or [Douyin XingTu KOL ID by Unique ID](/apis/douyin/xingtu/xingtu-kolid-by-unique-id).
- `platformChannel` accepts `_1` for Douyin video and `_10` for Douyin live.
- For rates per collaboration type, call [Douyin XingTu KOL Price](/apis/douyin/xingtu/kol-service-price-v1) next.

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin XingTu KOL Cost Metrics](/apis/douyin/xingtu/kol-cp-info-v1): Get expected campaign metrics for a Douyin KOL from XingTu: expected views, CPM and CPE estimates, and hot-video counts.
- [Douyin XingTu KOL Audience](/apis/douyin/xingtu/kol-fans-portrait-v1): Get the audience portrait of a Douyin KOL from XingTu: fan age, gender, region, device and interest distributions.
- [Douyin XingTu KOL Price](/apis/douyin/xingtu/kol-service-price-v1): Get the XingTu rate card of a Douyin KOL: price per collaboration type (sponsored video, live and more), settlement type and industry tags.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-base-info-v1.json`](../../../../catalog/models/douyin/xingtu/kol-base-info-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-base-info-v1
