# TikTok Top contents item detail API: pricing, parameters and code examples

`tiktok/ads/top-contents-item-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get top contents item detail on TikTok. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/top-contents-item-detail", "item_id": "7684011124739656991", "period_end_timestamp": 1793318400}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/top-contents-item-detail', {'item_id': '7684011124739656991', 'period_end_timestamp': 1793318400})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/top-contents-item-detail", {
  "item_id": "7684011124739656991",
  "period_end_timestamp": 1793318400
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/top-contents-item-detail", sandbase.Params{
	"item_id": "7684011124739656991",
	"period_end_timestamp": 1793318400,
})
```

Same call via the path form: `POST /v1/api/tiktok/ads/top-contents-item-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cookie` | string |  | Custom Cookie string (optional)  |
| `item_id` | string | yes | Video item ID  |
| `country_code` | string |  | Country code of the ranking default `"US"` |
| `period_dimension` | integer |  | 3/5 /Period dimension default `3` |
| `period_end_timestamp` | integer | yes | The caller must generate this 10-digit Unix timestamp in seconds from the target ranking date, for example 1785024000; do not pass 0 because it returns an empty result  |

## Details

Returns the detail record for one video in the TikTok Creative Center top contents ranking. It includes the video info, author info, top comments, and view and engagement metrics for the ranking period. You need an `item_id`, a `period_end_timestamp`, and optionally a `country_code`.

### Use cases

- Compare a ranked video's period views with its lifetime views to see how much of its reach came in the ranking window.
- Pull the author's follower count and bio to judge which creators to contact for a brand partnership.
- Read the top comments on a ranked video to see how viewers respond to a sponsored post.
- Save the cover and video URLs of a top video for a creative reference board.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/top-contents-item-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7684011124739656991", "period_end_timestamp": 1793318400, "period_dimension": 3, "country_code": "US"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video item ID |
| `period_end_timestamp` | integer | Yes | The caller must generate this 10-digit Unix timestamp in seconds from the target ranking date, for example 1785024000; do not pass 0 because it returns an empty result |
| `cookie` | string | No | Custom Cookie string (optional) |
| `country_code` | string | No | Country code of the ranking |
| `period_dimension` | integer | No | 3/5 /Period dimension |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "entityInfo": {
    "commentInfos": [
      {
        "createTime": "1792820854",
        "likeCnt": "51",
        "objectID": "7700106831570731796",
        "text": "To viciada na Ruffles sabor churrasco",
        "userAvatarLink": "https://p16-common-sign.tiktokcdn-us.com/tos-alisg-avt-0068/bfb71ec3eca2b3e35dc8…",
        "userID": "7630573810387977236",
        "userName": "ʚAnaɞ 🐰"
      }
    ],
    "itemAuthorInfo": {
      "avatarURI": "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/bd593306c9ed3c9…",
      "bio": "oi :) conto histórias \nyoutube:deixa falar \n@fefeschneider\nfefe@bpmat.com.br",
      "creatorType": 1,
      "handlerName": "fefe",
      "nickName": "Fefe",
      "riskInfo": {
        "disciplineInfoList": [],
        "riskEventInfoList": []
      },
      "storeRegion": "US"
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
      "title": "Existe combinação mais perfeita do que RUFFLES®️ e um bom filme? Impossível! Tod…",
      "videoURL": "https://v16m-default.tiktokcdn-us.com/775392842ba38f70fe68b7834bdaf1d2/6ae9e53d/…"
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
}
```

### Response fields

| Field | Meaning |
|---|---|
| `entityInfo.itemInfo.itemID / entityInfo.itemInfo.title` | The video ID and its caption text, including hashtags and mentions. |
| `entityInfo.itemInfo.createTime` | When the video was posted, as a 10-digit Unix timestamp in seconds, returned as a string. |
| `entityInfo.itemInfo.coverURL / entityInfo.itemInfo.videoURL` | Links to the cover image and the video file. |
| `entityInfo.itemMetrics.videoViews / entityInfo.itemMetrics.videoViewsLifeTime` | Video views for the ranking period and for the whole life of the video. |
| `entityInfo.itemMetrics.organicVideoViews / entityInfo.itemMetrics.organicVideoViewsLifeTime` | Organic video views for the ranking period and for the whole life of the video. |
| `entityInfo.itemMetrics.engagementRate / entityInfo.itemMetrics.engagementRateLifeTime` | Engagement rate as a decimal ratio, for the ranking period and for the whole life of the video. |
| `entityInfo.itemMetrics.sixSecondsVTR / entityInfo.itemMetrics.sixSecondsVTRLifeTime` | Six-second view-through rate as a decimal ratio, for the ranking period and for the whole life of the video. |
| `entityInfo.itemAuthorInfo.nickName / entityInfo.itemAuthorInfo.handlerName / entityInfo.itemAuthorInfo.bio` | The author's display name, handle, and profile bio. |
| `entityInfo.itemAuthorMetrics.followers` | The author's follower count, returned as a string. |
| `entityInfo.commentInfos[].text / entityInfo.commentInfos[].likeCnt` | The text of a top comment and its like count. |

### Notes

- Get `item_id` from the `itemID` values in [TikTok Top contents list](/apis/tiktok/ads/top-contents-list). Use the same `period_end_timestamp` and `country_code` as in that call.
- `period_end_timestamp` is a 10-digit Unix timestamp in seconds. Do not pass `0`, because it returns an empty result.
- Counts and timestamps such as `videoViews`, `followers`, and `createTime` arrive as strings. Rates such as `engagementRate` arrive as numbers.
- `cookie` is optional.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/tiktok/ads/top-contents-item-detail.json`](../../../../catalog/models/tiktok/ads/top-contents-item-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/top-contents-item-detail
