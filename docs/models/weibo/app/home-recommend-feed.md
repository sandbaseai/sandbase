# Weibo Home Recommend Feed API: pricing, parameters and code examples

`weibo/app/home-recommend-feed` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/home-recommend-feed", "count": 15}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/home-recommend-feed', {'count': 15})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/home-recommend-feed", {
  "count": 15
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/home-recommend-feed", sandbase.Params{
	"count": 15,
})
```

Same call via the path form: `POST /v1/api/weibo/app/home-recommend-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` |  |  | Page number, don't pass for first page, pass "2" for second page, and so on  |
| `count` | integer |  | Items per page, default 15, max 50 default `15`; range 1–50 |

## Details

Returns a page of recommended feed items from the Weibo app home screen. It needs no input. You can pass `count` to set the page size and `page` to move to later pages.

### Use cases

- Sample the posts Weibo recommends on the home screen and compare their `attitudes_count` values.
- Separate paid ad items from regular recommended posts using the ad fields and `itemExt.adCountInfo.isAd`.
- Collect post and video IDs from the recommend stream, then fetch full details for the ones you care about.
- Study which recommend sources and list names produce the items shown in the feed.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/home-recommend-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Items per page, default 15, max 50 |
| `page` | string | No | Page number, don't pass for first page, pass "2" for second page, and so on |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "config": "{}",
  "items": [
    {
      "category": "feed",
      "data": {
        "ad_marked": false,
        "analysis_extra": "ui:C@video34|finalRank:0|recommend_source:251|hot_request_id:1793691964393041000…",
        "analysis_media": "recommend_source:251|listName:interest|recommend_source_ex:source_ids#841_1519_1…",
        "annotations": [
          {
            "photo_sub_type": ""
          }
        ],
        "appid": 2825286,
        "attitudes_animation": 1,
        "attitudes_count": 42039,
        "attitudes_status": 0
      },
      "itemExt": {
        "adCountInfo": {
          "intervalCount": 1
        }
      }
    }
  ],
  "loadedInfo": "{}",
  "moreInfo": {
    "error": "网络加载失败，请稍后尝试",
    "loading": "正在加载更多",
    "moreType": "default",
    "pagingType": "cursor",
    "params": {
      "count": 15,
      "lastAdInterval": 4,
      "max_id": 1
    }
  },
  "pageData": "{}",
  "refreshInfo": "{}"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].category` | Type of the entry. The sample items show `feed`. |
| `items[].data.attitudes_count` | Number of likes (attitudes) on the post. |
| `items[].data.ad_marked` | Boolean flag on the post. It is `false` in the sample items. |
| `items[].data.ad_state / items[].data.ad_object` | Present only on ad items. They hold the ad state and the ad tracking object. |
| `items[].itemExt.adCountInfo.isAd` | Set to `true` on items that are ads. Regular items carry `intervalCount` instead. |
| `items[].data.analysis_extra` | Pipe-separated string of ranking and source tags, such as `finalRank`, `recommend_source` and `listName`. |
| `items[].data.annotations[].client_mblogid` | Client-side post ID string that appears in the annotations of some items. |
| `moreInfo.pagingType` | Paging style reported by the response. The sample value is `cursor`. |
| `moreInfo.params.count / moreInfo.params.max_id` | Paging values the feed reports for the next request: the item count and a `max_id` cursor. |

### Notes

- Leave `page` out for the first page. Pass `"2"` for the second page, and so on. `page` is a string.
- `count` accepts 1 to 50 and defaults to 15.
- Some items are ads. Check `items[].itemExt.adCountInfo.isAd` before you treat an item as an organic post.
- To go deeper on a post you found here, call [Weibo Post Detail (App)](/apis/weibo/app/status-detail) or [Weibo Post Comments (App)](/apis/weibo/app/status-comments).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.
- [Weibo Hot Search Categories](/apis/weibo/app/hot-search-categories): Returns all available hot search categories from Weibo.

---
Machine-readable: [`catalog/models/weibo/app/home-recommend-feed.json`](../../../../catalog/models/weibo/app/home-recommend-feed.json) · Store page: https://www.sandbase.ai/model/weibo/app/home-recommend-feed
