# TikTok Video Detail API: pricing, parameters and code examples

`tiktok/web/post-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed data for a single TikTok video using its item ID. Supports filtering by region code to view localized post content.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/post-detail", "itemId": "7218694761253735723"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/post-detail', {'itemId': '7218694761253735723'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/post-detail", {
  "itemId": "7218694761253735723"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/post-detail", sandbase.Params{
	"itemId": "7218694761253735723",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | Video id  |
| `region` | string |  | Region code, optional; affects content region, e.g. US/GB/JP/ID, default US.  |

## Details

Returns the full record for one TikTok video: caption, author, stats, music, hashtags and posting settings. It needs the video's `itemId`, with an optional `region` code.

### Use cases

- Pull play, like, comment, share and save counts for a single video to log its performance.
- Read the caption, hashtags and music of a video to study how a trend is built.
- Check the author's follower and video counts next to a specific post.
- Compare a video's data across regions by changing `region`, for example `US`, `GB`, `JP` or `ID`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "7339393672959757570"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | Video id |
| `region` | string | No | Region code, optional; affects content region, e.g. US/GB/JP/ID, default US. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611030744289D1BCEAFB0AA6802D6F7",
    "now": 1793691868000
  },
  "itemInfo": {
    "itemStruct": {
      "AIGCDescription": "",
      "CategoryType": 119,
      "IsHDBitrate": false,
      "ShowAIGC": false,
      "author": {
        "UserStoryStatus": 0,
        "avatarLarger": "https://p16-common-sign.tiktokcdn-us.com/tos-alisg-avt-0068/d7e8c4a3573642d087e4…",
        "avatarMedium": "https://p19-common-sign.tiktokcdn-us.com/tos-alisg-avt-0068/d7e8c4a3573642d087e4…",
        "avatarThumb": "https://p16-common-sign.tiktokcdn-us.com/tos-alisg-avt-0068/d7e8c4a3573642d087e4…",
        "commentSetting": 0,
        "downloadSetting": 0,
        "duetSetting": 0,
        "ftc": false
      },
      "authorStats": {
        "diggCount": 65500,
        "followerCount": 3900000,
        "followingCount": 552,
        "friendCount": 0,
        "heart": 115000000,
        "heartCount": 115000000,
        "videoCount": 640
      },
      "authorStatsV2": {
        "diggCount": "65500",
        "followerCount": "3900000",
        "followingCount": "552",
        "friendCount": "0",
        "heart": "115000000",
        "heartCount": "115000000",
        "videoCount": "640"
      },
      "backendSourceEventTracking": "",
      "challenges": [
        {
          "coverLarger": "",
          "coverMedium": "",
          "coverThumb": "",
          "desc": "",
          "id": "7066697838675099650",
          "profileLarger": "",
          "profileMedium": "",
          "profileThumb": ""
        }
      ],
      "collected": false,
      "contents": [
        {
          "desc": "Singing that Chinese dance meme song. #科目三 #chinese #cover",
          "textExtra": [
            {
              "awemeId": "",
              "end": 42,
              "hashtagId": "7066697838675099650",
              "hashtagName": "科目三",
              "isCommerce": false,
              "start": 38,
              "subType": 0,
              "type": 1
            }
          ]
        }
      ],
      "createTime": 1708835760
    }
  },
  "log_pb": {
    "impr_id": "202611030744289D1BCEAFB0AA6802D6F7"
  },
  "shareMeta": {
    "desc": "Singing that Chinese dance meme song. #科目三 #chinese #cover",
    "title": "sugar on TikTok"
  },
  "statusCode": 0,
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `itemInfo.itemStruct.id` | The video ID. It matches the `itemId` you sent. |
| `itemInfo.itemStruct.desc` | The video caption text, including hashtags. |
| `itemInfo.itemStruct.createTime` | When the video was posted, as a Unix timestamp in seconds. |
| `itemInfo.itemStruct.stats.playCount / diggCount / commentCount / shareCount / collectCount` | Counts for plays, likes, comments, shares and saves. Large values are rounded. |
| `itemInfo.itemStruct.statsV2.playCount / diggCount / commentCount / shareCount / collectCount / repostCount` | The same counts as strings. `collectCount` here is more exact than in `stats`. |
| `itemInfo.itemStruct.author` | The author's avatar image URLs and settings such as `commentSetting`, `duetSetting` and `downloadSetting`. |
| `itemInfo.itemStruct.authorStats.followerCount / followingCount / videoCount / heartCount` | The author's follower, following, video and total like counts. |
| `itemInfo.itemStruct.music.id / authorName / duration` | The sound used in the video: its ID, the name of its author and its length. `duration` is `32` in this example. |
| `itemInfo.itemStruct.challenges[].id / desc` | The hashtags on the video. `desc` is empty for some hashtags. |
| `itemInfo.itemStruct.textExtra[].hashtagName / start / end` | Each hashtag in the caption and its character position in `desc`. |

### Notes

- Get the `itemId` from a video link with [TikTok Video ID from URL](/apis/tiktok/web/aweme-id), or for many links at once with [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id).
- `itemId` is a numeric string such as `7339393672959757570`. Send it as a string.
- Image URLs in the response carry expiry parameters, so save the images if you need them later.
- [TikTok Post Details (V2)](/apis/tiktok/web/post-detail-v2) is another detail endpoint for a single post.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/post-detail.json`](../../../../catalog/models/tiktok/web/post-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/web/post-detail
