# Douyin Creator Hot Spot Billboard API: pricing, parameters and code examples

`douyin/creator/creator-hot-spot-billboard` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending hot spot billboard rankings for Douyin creators, including hot scores and query identifiers filtered by search type, tag, or city code.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-hot-spot-billboard", "billboard_tag": "0", "hot_search_type": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-hot-spot-billboard', {'billboard_tag': '0', 'hot_search_type': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-hot-spot-billboard", {
  "billboard_tag": "0",
  "hot_search_type": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-hot-spot-billboard", sandbase.Params{
	"billboard_tag": "0",
	"hot_search_type": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-hot-spot-billboard` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `city_code` |  |  | City code - required when hot_search_type=2  |
| `billboard_tag` | string |  | Hot spot tag - multiple tags separated by comma default `"0"` |
| `hot_search_type` | integer |  | Hot search type default `1` |

## Details

Returns a ranked list of trending hot spot topics on Douyin, each with a title, category, hot score and rank. All inputs are optional: `hot_search_type`, `billboard_tag` and `city_code` filter the board.

### Use cases

- Track which news, sports and other topics lead the Douyin hot spot board at a given time.
- Compare `rank_diff` values across calls to spot topics that are climbing or falling.
- Pull the top topics by `hot_score` to pick themes for new creator content.
- Request a city board with `hot_search_type` set to `2` and a `city_code` to see local hot spots.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-hot-spot-billboard" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `billboard_tag` | string | No | Hot spot tag - multiple tags separated by comma |
| `city_code` | string | No | City code - required when hot_search_type=2 |
| `hot_search_type` | integer | No | Hot search type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "item_list": [
    {
      "aweme_list": null,
      "category": "时政",
      "cover": {
        "uri": "tos-cn-i-dy/073d66416d0d41f89a655bfa94f143c5",
        "url_list": [
          "https://p26-sign.douyinpic.com/tos-cn-i-dy/073d66416d0d41f89a655bfa94f143c5~tplv…"
        ]
      },
      "hot_score": 12100275,
      "key_words": null,
      "query_id": "2726467",
      "rank": 1,
      "rank_diff": 0,
      "related_item_ids": null,
      "title": "美官员称美袭击伊朗格什姆岛"
    }
  ],
  "status_code": 0,
  "status_msg": "",
  "update_time": 20261103152500
}
```

### Response fields

| Field | Meaning |
|---|---|
| `item_list[].title` | Name of the hot spot topic. |
| `item_list[].rank` | Position of the topic on the billboard. `1` is the top entry. |
| `item_list[].rank_diff` | Change in rank for the topic. A value of `0` appears for topics with no change. |
| `item_list[].hot_score` | Numeric heat value for the topic. Higher values rank higher. |
| `item_list[].category` | Topic category label, for example `时政` (current affairs) or `体育` (sports). |
| `item_list[].query_id` | Identifier of the hot spot query, returned as a string. |
| `item_list[].cover.url_list[]` | Cover image URLs for the topic. Each entry points to a different image host for the same image. |
| `item_list[].cover.uri` | Internal path of the cover image. |
| `item_list[].aweme_list / key_words / related_item_ids` | Related videos, keywords and item IDs. These were `null` in this response. |
| `update_time` | Timestamp of the board, written as `YYYYMMDDHHMMSS` digits, for example `20261103152500`. |

### Notes

- `city_code` is required when `hot_search_type` is `2`.
- Pass several tags in `billboard_tag` separated by commas. The default is `0`.
- Cover image URLs are signed links and include an `x-expires` value.
- To browse related Douyin trends, call [Douyin Creator Hot Topic Billboard](/apis/douyin/creator/creator-hot-topic-billboard) or [Douyin Hot Search List](/apis/douyin/app-v3/hot-search-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-hot-spot-billboard.json`](../../../../catalog/models/douyin/creator/creator-hot-spot-billboard.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-hot-spot-billboard
