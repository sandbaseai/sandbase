# TikTok User Reposts API: pricing, parameters and code examples

`tiktok/web/user-repost` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of reposted videos for a specified TikTok profile. Results include video metadata, author statistics, and engagement metrics via user secUid.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/user-repost", "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/user-repost', {'secUid': 'MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/user-repost", {
  "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/user-repost", sandbase.Params{
	"secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/user-repost` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page, default is 20, cannot be changed.  |
| `cursor` | integer |  | Page cursor  |
| `secUid` | string | yes | User secUid  |
| `coverFormat` | integer |  | Cover format, default is 2, optional values are 1 or 2.  |

## Details

Returns a page of videos that a TikTok user has reposted, with video details, author totals, and engagement counts. It needs the user's `secUid` as input.

### Use cases

- Review which videos a creator reposts to see what content they endorse.
- Compare `playCount` and `diggCount` across reposted videos to find which ones perform best.
- Collect hashtags and captions from reposted videos to study the topics a creator follows.
- Download reposted video files or cover images from the playback URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-repost" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | Yes | User secUid |
| `count` | integer | No | Number per page, default is 20, cannot be changed. |
| `coverFormat` | integer | No | Cover format, default is 2, optional values are 1 or 2. |
| `cursor` | integer | No | Page cursor |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cookie": "tt_chain…",
  "cursor": "20",
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611030744324566AD1DDD14C902E263",
    "now": 1793691872000
  },
  "hasMore": true,
  "itemList": [
    {
      "AIGCDescription": "",
      "CategoryType": 105,
      "IsHDBitrate": false,
      "ShowAIGC": true,
      "author": {
        "avatarLarger": "https://p19-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/7330740761455820805…",
        "avatarMedium": "https://p19-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/7330740761455820805…",
        "avatarThumb": "https://p19-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/7330740761455820805…",
        "commentSetting": 0,
        "downloadSetting": 0,
        "duetSetting": 0,
        "ftc": false,
        "id": "6653919748492099589"
      },
      "authorStats": {
        "diggCount": 302,
        "followerCount": 22600,
        "followingCount": 15,
        "friendCount": 0,
        "heart": 539300,
        "heartCount": 539300,
        "videoCount": 742
      },
      "authorStatsV2": {
        "diggCount": "302",
        "followerCount": "22600",
        "followingCount": "15",
        "friendCount": "0",
        "heart": "539300",
        "heartCount": "539300",
        "videoCount": "742"
      },
      "backendSourceEventTracking": "",
      "challenges": [
        {
          "coverLarger": "",
          "coverMedium": "",
          "coverThumb": "",
          "desc": "",
          "id": "1619172155642885",
          "profileLarger": "",
          "profileMedium": "",
          "profileThumb": ""
        }
      ],
      "collected": false,
      "contents": [
        {
          "desc": "Over 2 million skilled trades jobs are sitting unfilled. @TikTok has been the bi…",
          "textExtra": [
            {
              "awemeId": "",
              "end": 64,
              "hashtagName": "",
              "isCommerce": false,
              "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
              "start": 57,
              "subType": 0,
              "type": 0
            }
          ]
        }
      ],
      "createTime": 1792023471
    }
  ],
  "log_pb": {
    "impr_id": "202611030744324566AD1DDD14C902E263"
  },
  "statusCode": 0,
  "status_code": 0,
  "status_msg": "",
  "tt_chain_token": "uWGiRtoC…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `itemList[].id` | ID of the reposted video. |
| `itemList[].desc` | Caption text of the video. Hashtags and mentions are included in the text. |
| `itemList[].createTime` | Time the video was created, as a Unix timestamp in seconds. |
| `itemList[].stats.playCount / stats.diggCount / stats.commentCount / stats.shareCount / stats.collectCount` | Engagement counts for the video: plays, likes, comments, shares and saves. `statsV2` repeats them as strings. |
| `itemList[].author.id` | ID of the account that made the original video. |
| `itemList[].authorStats.followerCount / followingCount / videoCount / heartCount` | Totals for the video's author: followers, accounts followed, videos posted and total likes received. |
| `itemList[].music.id / music.authorName / music.duration` | ID, author name and duration of the sound used in the video. |
| `itemList[].video.cover` | URL of the cover image for the video. |
| `itemList[].video.PlayAddrStruct.UrlList` | Playback URLs for the video file. `Width`, `Height` and `DataSize` describe the file. |
| `itemList[].textExtra[].hashtagName` | Hashtag name found in the caption. `start` and `end` give its position in `desc`. |

### Notes

- Pass `cursor` from the previous response to get the next page. The response also returns `hasMore`, which is `true` when more results exist.
- `count` is fixed at 20 per page and cannot be changed.
- The `secUid` value starts with `MS4w`. Get it from [TikTok Profile Sec User ID](/apis/tiktok/web/sec-user-id) or [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id).
- To see the videos the user posted themselves, call [TikTok User Posts](/apis/tiktok/web/user-post).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-repost.json`](../../../../catalog/models/tiktok/web/user-repost.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-repost
