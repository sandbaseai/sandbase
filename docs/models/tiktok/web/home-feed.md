# TikTok Web Home Feed API: pricing, parameters and code examples

`tiktok/web/home-feed` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended video items and metadata from the TikTok web home feed. Supports filtering by target region code and page item count.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/home-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/home-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/home-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/home-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/home-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page default `15` |
| `region` | string |  | Region code, optional parameter, affects the region of recommended content, e.g. US/GB/JP/KR/SG, default US. default `"US"` |

## Details

Returns a page of recommended TikTok videos from the web home feed. Each item includes the caption, author, author stats, music, and engagement counts. The request needs no input, and you can set `region` and `count` to change the feed.

### Use cases

- Sample what TikTok recommends in a region such as `US`, `GB`, or `JP` by changing the `region` value.
- Collect `stats` counts for recommended videos to compare how much attention each one gets.
- Find hashtags used in recommended videos by reading `textExtra[].hashtagName`.
- Check author size by reading `authorStats.followerCount` for each creator in the feed.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/home-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number per page |
| `region` | string | No | Region code, optional parameter, affects the region of recommended content, e.g. US/GB/JP/KR/SG, default US. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cookie": "tt_chain…",
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611030744251010435B508133018A93",
    "now": 1793691866000
  },
  "hasMore": true,
  "itemList": [
    {
      "AIGCDescription": "",
      "CategoryType": 120,
      "IsHDBitrate": false,
      "ShowAIGC": true,
      "aigcLabelType": 2,
      "author": {
        "avatarLarger": "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/7761710511d4467…",
        "avatarMedium": "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/7761710511d4467…",
        "avatarThumb": "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/7761710511d4467…",
        "commentSetting": 0,
        "downloadSetting": 0,
        "duetSetting": 0,
        "ftc": false,
        "id": "6916577766381569029"
      },
      "authorStats": {
        "diggCount": 2882,
        "followerCount": 13900,
        "followingCount": 170,
        "friendCount": 0,
        "heart": 638700,
        "heartCount": 638700,
        "videoCount": 185
      },
      "authorStatsV2": {
        "diggCount": "2882",
        "followerCount": "13900",
        "followingCount": "170",
        "friendCount": "0",
        "heart": "638700",
        "heartCount": "638700",
        "videoCount": "185"
      },
      "backendSourceEventTracking": "fyp_35",
      "challenges": [
        {
          "coverLarger": "",
          "coverMedium": "",
          "coverThumb": "",
          "desc": "",
          "id": "7690364272014000142",
          "profileLarger": "",
          "profileMedium": "",
          "profileThumb": ""
        }
      ],
      "collected": false,
      "contentContext": {
        "status_tag": "{\"traffic_structure_info\":\"{\\\"slate_group_type\\\":\\\"0\\\"}\"}"
      }
    }
  ],
  "log_pb": {
    "impr_id": "202611030744251010435B508133018A93"
  },
  "statusCode": 0,
  "status_code": 0,
  "status_msg": "",
  "tt_chain_token": "8e8wZ0N6…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `itemList[]` | The list of recommended video items in this page of the feed. |
| `itemList[].id` | The ID of the video, as a string. Pass it to a video detail API to look up one video. |
| `itemList[].desc` | The caption of the video, including its hashtags. |
| `itemList[].createTime` | When the video was posted, as a Unix timestamp in seconds. |
| `itemList[].author.id` | The ID of the creator who posted the video. |
| `itemList[].stats.playCount / diggCount / commentCount / shareCount / collectCount` | Engagement counts for the video. `statsV2` holds the same counts as strings. |
| `itemList[].authorStats.followerCount / heartCount / videoCount` | Counts for the creator: followers, total likes received (`heartCount`), and number of videos posted. `authorStatsV2` holds the same values as strings. |
| `itemList[].textExtra[].hashtagName` | The name of each hashtag in the caption. `start` and `end` give its position in `desc`. |
| `itemList[].music.id / authorName / duration` | The ID of the sound used in the video, the name of its author, and its `duration` value. |
| `itemList[].isAd` | Whether the item is marked as an ad. |
| `hasMore` | Whether the response reports more items after this page. |

### Notes

- `region` takes a region code such as `US`, `GB`, `JP`, `KR`, or `SG`. The default is `US`.
- `count` sets the number of items per page. The default is 15.
- Both parameters are optional, so an empty request body `{}` works.
- To get full data for one video, take its `id` and call [TikTok Video Detail](/apis/tiktok/web/post-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/home-feed.json`](../../../../catalog/models/tiktok/web/home-feed.json) · Store page: https://www.sandbase.ai/model/tiktok/web/home-feed
