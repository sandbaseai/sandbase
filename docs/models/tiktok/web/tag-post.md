# TikTok Tag Posts API: pricing, parameters and code examples

`tiktok/web/tag-post` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of TikTok videos associated with a specific tag or challenge ID. Supports pagination using cursor and count parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/tag-post", "challengeID": "7551"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/tag-post', {'challengeID': '7551'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/tag-post", {
  "challengeID": "7551"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/tag-post", sandbase.Params{
	"challengeID": "7551",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/tag-post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page default `30` |
| `cursor` | integer |  | Page cursor default `0` |
| `challengeID` | string | yes | Tag ID  |

## Details

Returns a page of TikTok videos that use a given hashtag challenge. Each video includes its caption, author, stats, music and playback URLs. The only required input is `challengeID`.

### Use cases

- Pull the latest videos under a hashtag such as `cat` to see what creators post for it.
- Compare `stats.playCount` and `stats.diggCount` across videos in one tag to find the top performers.
- Collect author follower counts for a hashtag to build a list of creators who post in that niche.
- Download video files from the `video.PlayAddrStruct.UrlList` links for offline review.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/tag-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"challengeID": "7551"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `challengeID` | string | Yes | Tag ID |
| `count` | integer | No | Number per page |
| `cursor` | integer | No | Page cursor |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cookie": "tt_chain…",
  "cursor": "1",
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103074430ADC687E8CD26C202B696",
    "now": 1793691870000
  },
  "hasMore": false,
  "itemList": [
    {
      "AIGCDescription": "",
      "CategoryType": 113,
      "IsHDBitrate": false,
      "ShowAIGC": true,
      "author": {
        "avatarLarger": "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/43225e8d641a71…",
        "avatarMedium": "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/43225e8d641a71…",
        "avatarThumb": "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/43225e8d641a71…",
        "commentSetting": 0,
        "downloadSetting": 3,
        "duetSetting": 0,
        "ftc": false,
        "id": "7440864094419059758"
      },
      "authorStats": {
        "diggCount": 103,
        "followerCount": 248900,
        "followingCount": 7,
        "friendCount": 0,
        "heart": 46400000,
        "heartCount": 46400000,
        "videoCount": 415
      },
      "authorStatsV2": {
        "diggCount": "103",
        "followerCount": "248900",
        "followingCount": "7",
        "friendCount": "0",
        "heart": "46400000",
        "heartCount": "46400000",
        "videoCount": "415"
      },
      "backendSourceEventTracking": "",
      "challenges": [
        {
          "coverLarger": "",
          "coverMedium": "",
          "coverThumb": "",
          "desc": "",
          "id": "7551",
          "profileLarger": "https://p19-common-sign.tiktokcdn-us.com/musically-maliva-obj/2e13829d6e18167082…",
          "profileMedium": "https://p19-common-sign.tiktokcdn-us.com/musically-maliva-obj/2e13829d6e18167082…",
          "profileThumb": "https://p19-common-sign.tiktokcdn-us.com/musically-maliva-obj/2e13829d6e18167082…"
        }
      ],
      "collected": false,
      "contents": [
        {
          "desc": "#cat ",
          "textExtra": [
            {
              "awemeId": "",
              "end": 4,
              "hashtagName": "cat",
              "isCommerce": false,
              "start": 0,
              "subType": 0,
              "type": 1
            }
          ]
        }
      ],
      "createTime": 1793639413
    }
  ],
  "log_pb": {
    "impr_id": "20261103074430ADC687E8CD26C202B696"
  },
  "statusCode": 0,
  "status_code": 0,
  "status_msg": "",
  "tt_chain_token": "i1xd4jgR…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `itemList[]` | The list of videos returned for the tag. Each entry is one video. |
| `itemList[].id / itemList[].createTime` | The video ID as a string, and the creation time as a Unix timestamp in seconds. |
| `itemList[].desc` | The video caption text, including hashtags. |
| `itemList[].stats.playCount / diggCount / commentCount / shareCount / collectCount` | View, like, comment, share and save counts for the video as numbers. |
| `itemList[].author.id` | The ID of the account that posted the video. |
| `itemList[].authorStats.followerCount / heartCount / videoCount` | The author's follower count, total likes received and number of videos. |
| `itemList[].challenges[].id` | IDs of the challenges (tags) attached to the video. The `challengeID` you searched for appears here. |
| `itemList[].music.id / music.authorName` | The ID and author name of the sound used in the video. |
| `itemList[].video.PlayAddrStruct.UrlList` | Direct playback URLs for the default video file. `Width`, `Height` and `DataSize` describe that file. |
| `hasMore / cursor` | `hasMore` tells you whether another page exists. `cursor` is the value returned for paging. |

### Notes

- `challengeID` is the numeric tag ID as a string, for example `7551`. Use [TikTok Tag Detail](/apis/tiktok/web/tag-detail) to look up details for a tag.
- Page through results with `count` (default 30) and `cursor` (default 0). Stop when `hasMore` is `false`.
- Each video also appears with string versions of its counts in `statsV2` and `authorStatsV2`.
- To get more detail on one video, pass its `id` to [TikTok Video Detail](/apis/tiktok/web/post-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/tag-post.json`](../../../../catalog/models/tiktok/web/tag-post.json) · Store page: https://www.sandbase.ai/model/tiktok/web/tag-post
