# TikTok Top contents list API: pricing, parameters and code examples

`tiktok/ads/top-contents-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get top contents list on TikTok. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/top-contents-list", "period_end_timestamp": 1793318400}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/top-contents-list', {'period_end_timestamp': 1793318400})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/top-contents-list", {
  "period_end_timestamp": 1793318400
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/top-contents-list", sandbase.Params{
	"period_end_timestamp": 1793318400,
})
```

Same call via the path form: `POST /v1/api/tiktok/ads/top-contents-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number default `1` |
| `limit` | integer |  | Items per page, max 100 default `20` |
| `cookie` | string |  | Custom Cookie string (optional)  |
| `country_code` | string |  | Country code default `"US"` |
| `organic_only` | boolean |  | Organic content only default `false` |
| `order_by_metric` | integer |  | Order by metric default `1` |
| `period_dimension` | integer |  | 3/5 /Period dimension default `3` |
| `content_label_ids` | string |  | Content label IDs, comma separated  |
| `period_end_timestamp` | integer | yes | The caller must generate this 10-digit Unix timestamp in seconds from the target ranking date, for example 1785024000; do not pass 0 because it returns an empty result  |

## Details

This API returns a ranked list of top-performing TikTok content for one day in one country. It needs `period_end_timestamp`, a 10-digit Unix timestamp in seconds for the ranking date. Each item includes the post, its author, and view and engagement metrics.

### Use cases

- Find the posts with the most video views in the US on a given ranking day.
- Spot paid partnership posts, such as those tagged with a brand hashtag, to see which creators brands work with.
- Compare `organicVideoViews` with `videoViews` to see how much of a post's reach came from organic viewing.
- Filter by `content_label_ids` to track top posts in one category such as Fashion.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/top-contents-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"period_end_timestamp": 1793318400, "period_dimension": 3, "country_code": "US", "order_by_metric": 1, "page": 1, "limit": 20}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `period_end_timestamp` | integer | Yes | The caller must generate this 10-digit Unix timestamp in seconds from the target ranking date, for example 1785024000; do not pass 0 because it returns an empty result |
| `content_label_ids` | string | No | Content label IDs, comma separated |
| `cookie` | string | No | Custom Cookie string (optional) |
| `country_code` | string | No | Country code |
| `limit` | integer | No | Items per page, max 100 |
| `order_by_metric` | integer | No | Order by metric |
| `organic_only` | boolean | No | Organic content only |
| `page` | integer | No | Page number |
| `period_dimension` | integer | No | 3/5 /Period dimension |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "entityInfos": [
    {
      "itemAuthorInfo": {
        "avatarURI": "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/bd593306c9ed3c9…",
        "bio": "oi :) conto histórias \nyoutube:deixa falar \n@fefeschneider\nfefe@bpmat.com.br",
        "handlerName": "fefe",
        "nickName": "Fefe"
      },
      "itemAuthorMetrics": {
        "followers": "17081647"
      },
      "itemInfo": {
        "authorID": "6848399732281180166",
        "contentType": 1,
        "coverURL": "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-p-0068-tx2/ogejjeAR8AEFQ7Cv…",
        "coverURLList": [
          {
            "format": "avif",
            "imageUrl": "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-p-0068-tx2/ogejjeAR8AEFQ7Cv…"
          }
        ],
        "createTime": "1789073267",
        "creatorID": "6532037588893564929",
        "itemID": "7684011124739656991",
        "title": "Existe combinação mais perfeita do que RUFFLES®️ e um bom filme? Impossível! Tod…"
      },
      "itemMetrics": {
        "engagementRate": 0.001270212222686055,
        "engagementRateLifeTime": 0.0013676565457314666,
        "organicVideoViews": "1021860",
        "organicVideoViewsLifeTime": "3551286",
        "sixSecondsVTR": 0.02442178790796269,
        "sixSecondsVTRLifeTime": 0.024476013493258095,
        "videoViews": "35827084",
        "videoViewsLifeTime": "65278816"
      }
    }
  ],
  "pagination": {
    "hasMore": true,
    "limit": 20,
    "page": 1,
    "pageCount": 5,
    "totalCount": 100
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `entityInfos[].itemInfo.itemID` | ID of the post. |
| `entityInfos[].itemInfo.title` | Caption text of the post, including hashtags and mentions. Long captions may be cut. |
| `entityInfos[].itemInfo.createTime` | Creation time of the post as a Unix timestamp in seconds, returned as a string. |
| `entityInfos[].itemInfo.coverURL / entityInfos[].itemInfo.coverURLList[].imageUrl` | Cover image links for the post. The list gives the same cover in several formats, shown in `format` (for example `avif` and `jpeg`). |
| `entityInfos[].itemAuthorInfo.handlerName / entityInfos[].itemAuthorInfo.nickName` | Handle and display name of the author. |
| `entityInfos[].itemAuthorInfo.bio` | Profile bio text of the author. |
| `entityInfos[].itemAuthorMetrics.followers` | Follower count of the author, returned as a string. |
| `entityInfos[].itemMetrics.videoViews / entityInfos[].itemMetrics.videoViewsLifeTime` | Video views for the ranking period and over the whole life of the post. |
| `entityInfos[].itemMetrics.organicVideoViews / entityInfos[].itemMetrics.organicVideoViewsLifeTime` | Organic video views for the ranking period and over the whole life of the post. |
| `entityInfos[].itemMetrics.engagementRate / entityInfos[].itemMetrics.sixSecondsVTR` | Engagement rate and six-second view-through rate as decimal fractions. The matching `LifeTime` fields give the lifetime values. |
| `entityInfos[].contentTags[].contentLabelID / entityInfos[].contentTags[].contentLabelName` | Content label ID and name for the post. This key only appears on some items. |

### Notes

- Page through results with `page` and `limit` (max 100). The `pagination` object returns `hasMore`, `pageCount` and `totalCount`.
- Use `contentLabelID` values from `contentTags` as `content_label_ids`, comma separated, to filter by label.
- IDs such as `itemID` and `authorID` and counts such as `followers` come back as strings.
- To get more on a single post, call [TikTok Top contents item detail](/apis/tiktok/ads/top-contents-item-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/tiktok/ads/top-contents-list.json`](../../../../catalog/models/tiktok/ads/top-contents-list.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/top-contents-list
