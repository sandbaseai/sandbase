# TikTok User Mix Video List API: pricing, parameters and code examples

`tiktok/web/user-mix` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns videos compiled inside a specific TikTok user mix or playlist. Supports pagination through cursor and count parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/user-mix", "mixId": "7101538765474106158"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/user-mix', {'mixId': '7101538765474106158'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/user-mix", {
  "mixId": "7101538765474106158"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/user-mix", sandbase.Params{
	"mixId": "7101538765474106158",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/user-mix` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page default `30` |
| `mixId` | string | yes | Mix id  |
| `cursor` | integer |  | Page cursor default `0` |

## Details

Returns the videos in a TikTok user mix (playlist). You send a `mixId` and get one page of videos with their text, author, stats and hashtags.

### Use cases

- Export every video in a creator's playlist with its caption and posting time.
- Compare `playCount` and `diggCount` across the videos of one mix to see which parts perform best.
- Collect the hashtags used across a themed mix to study how a creator tags a series.
- Page through a long mix with `cursor` and `count` to build a full video ID list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-mix" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mixId": "7101538765474106158"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `mixId` | string | Yes | Mix id |
| `count` | integer | No | Number per page |
| `cursor` | integer | No | Page cursor |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cookie": "tt_chain…",
  "cursor": "19",
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103154431BD2354D80FEE59050E02",
    "now": 1793691871000
  },
  "hasMore": false,
  "itemList": [
    {
      "AIGCDescription": "",
      "CategoryType": 110,
      "IsHDBitrate": false,
      "ShowAIGC": true,
      "author": {
        "avatarLarger": "https://p16-common-sign.tiktokcdn.com/tos-maliva-avt-0068/7310736459579785262~tp…",
        "avatarMedium": "https://p16-common-sign.tiktokcdn.com/tos-maliva-avt-0068/7310736459579785262~tp…",
        "avatarThumb": "https://p16-common-sign.tiktokcdn.com/tos-maliva-avt-0068/7310736459579785262~tp…",
        "commentSetting": 0,
        "downloadSetting": 0,
        "duetSetting": 0,
        "ftc": false,
        "id": "6762702053111383045"
      },
      "authorStats": {
        "diggCount": 8342,
        "followerCount": 456500,
        "followingCount": 361,
        "friendCount": 0,
        "heart": 7700000,
        "heartCount": 7700000,
        "videoCount": 951
      },
      "authorStatsV2": {
        "diggCount": "8342",
        "followerCount": "456500",
        "followingCount": "361",
        "friendCount": "0",
        "heart": "7700000",
        "heartCount": "7700000",
        "videoCount": "951"
      },
      "backendSourceEventTracking": "",
      "challenges": [
        {
          "coverLarger": "",
          "coverMedium": "",
          "coverThumb": "",
          "desc": "",
          "id": "229207",
          "profileLarger": "",
          "profileMedium": "",
          "profileThumb": ""
        }
      ],
      "collected": false,
      "contents": [
        {
          "desc": "Pit in my stomach when I think ab going to the bathroom lol #fyp #pathologicalde…",
          "textExtra": [
            {
              "awemeId": "",
              "end": 64,
              "hashtagName": "fyp",
              "isCommerce": false,
              "start": 60,
              "subType": 0,
              "type": 1
            }
          ]
        }
      ],
      "createTime": 1669790506
    }
  ],
  "log_pb": {
    "impr_id": "20261103154431BD2354D80FEE59050E02"
  },
  "statusCode": 0,
  "status_code": 0,
  "status_msg": "",
  "tt_chain_token": "0k5cdiqY…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `itemList[]` | The videos on this page of the mix. |
| `itemList[].id` | ID of the video. |
| `itemList[].desc` | Caption of the video, including hashtags. |
| `itemList[].createTime` | Creation time of the video as a Unix timestamp in seconds. |
| `itemList[].stats.playCount / itemList[].stats.diggCount / itemList[].stats.commentCount / itemList[].stats.shareCount / itemList[].stats.collectCount` | Play, like, comment, share and save counts for the video, as numbers. |
| `itemList[].statsV2` | The same counts as strings, plus `repostCount`. |
| `itemList[].author.id` | ID of the account that posted the video. |
| `itemList[].authorStats.followerCount / itemList[].authorStats.videoCount` | Follower count and number of videos for the author. |
| `itemList[].textExtra[].hashtagName` | Name of each hashtag in the caption. `start` and `end` give its position in `desc`. |
| `itemList[].playlistId` | ID of the mix the video belongs to. It matches the `mixId` you sent. |
| `hasMore` | Shows whether more pages exist after this one. |
| `cursor` | Cursor value returned with this page. |

### Notes

- `mixId` is the only required parameter. `count` defaults to 30 and `cursor` defaults to 0.
- To get the next page, check `hasMore`, then send the returned `cursor` value in the next request.
- The `cursor` in the response is a string, while the request parameter `cursor` is an integer.
- Use the video `id` values from `itemList[]` to look up a single video with [TikTok Video Detail](/apis/tiktok/web/post-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-mix.json`](../../../../catalog/models/tiktok/web/user-mix.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-mix
