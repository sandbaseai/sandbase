# TikTok Photo Search API: pricing, parameters and code examples

`tiktok/web/search-photo` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches TikTok photo posts matching a query keyword. Returns post details, author statistics, music metadata, and engagement metrics with cursor pagination support.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/search-photo", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/search-photo', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/search-photo", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/search-photo", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/search-photo` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page, it is recommended to keep the default value 20. default `20` |
| `offset` | integer |  | Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor. default `0` |
| `keyword` | string | yes | Search keyword  |
| `search_id` | string |  | Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request. default `""` |

## Details

Returns TikTok photo posts that match a search keyword. Each post includes its caption, images, hashtags, author statistics, music and engagement counts. The only required input is `keyword`.

### Use cases

- Collect photo posts about a brand or topic, such as `openai`, and read their captions and hashtags.
- Rank photo posts by `stats.playCount` or `stats.diggCount` to find the ones that perform best.
- Check the follower and like totals of the authors who post about a keyword.
- Download the image URLs of a post for review or archiving.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/search-photo" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `count` | integer | No | Number per page, it is recommended to keep the default value 20. |
| `offset` | integer | No | Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor. |
| `search_id` | string | No | Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "backtrace": "",
  "cookie": "tt_chain…",
  "cursor": 20,
  "extra": {
    "api_debug_info": null,
    "fatal_item_ids": [],
    "logid": "202611030744288C32E7C0DEB25902A31E",
    "now": 1793691869000,
    "search_request_id": ""
  },
  "has_more": 1,
  "item_list": [
    {
      "AIGCDescription": "",
      "CategoryType": 120,
      "IsHDBitrate": false,
      "author": {
        "avatarLarger": "https://p16-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/0f21de2969ec6273b0c…",
        "avatarMedium": "https://p16-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/0f21de2969ec6273b0c…",
        "avatarThumb": "https://p19-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/0f21de2969ec6273b0c…",
        "commentSetting": 0,
        "downloadSetting": 0,
        "duetSetting": 0,
        "ftc": false,
        "id": "7668351969518470166"
      },
      "authorStats": {
        "diggCount": 372,
        "followerCount": 7747,
        "followingCount": 0,
        "friendCount": 0,
        "heart": 292700,
        "heartCount": 292700,
        "videoCount": 45
      },
      "authorStatsV2": {
        "diggCount": "372",
        "followerCount": "7747",
        "followingCount": "0",
        "friendCount": "0",
        "heart": "292700",
        "heartCount": "292700",
        "videoCount": "45"
      },
      "backendSourceEventTracking": "",
      "challenges": [
        {
          "coverLarger": "",
          "coverMedium": "",
          "coverThumb": "",
          "desc": "",
          "id": "1660434918591489",
          "profileLarger": "",
          "profileMedium": "",
          "profileThumb": ""
        }
      ],
      "collected": false,
      "contents": [
        {
          "desc": "The model deepseek V4 flash retained its small size yet they still managed to ma…",
          "textExtra": [
            {
              "awemeId": "",
              "end": 483,
              "hashtagId": "1660434918591489",
              "hashtagName": "deepseek",
              "isCommerce": false,
              "start": 474,
              "subType": 0,
              "type": 1
            }
          ]
        }
      ],
      "createTime": 1785660642,
      "creatorAIComment": {
        "eligibleVideo": false,
        "hasAITopic": false,
        "notEligibleReason": 101
      }
    }
  ],
  "log_pb": {
    "impr_id": "202611030744288C32E7C0DEB25902A31E"
  },
  "status_code": 0,
  "tt_chain_token": "e/Y90VJh…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `item_list[].id` | ID of the photo post. |
| `item_list[].desc` | Caption text of the post. Long captions may be shortened. |
| `item_list[].createTime` | Creation time of the post as a Unix timestamp in seconds. |
| `item_list[].stats.playCount / diggCount / commentCount / shareCount / collectCount` | Engagement counts for the post. `statsV2` holds the same numbers as strings. |
| `item_list[].author.id` | ID of the account that published the post. |
| `item_list[].authorStats.followerCount / heartCount / videoCount` | Follower, total like and video counts of the author. `authorStatsV2` repeats them as strings. |
| `item_list[].imagePost.images[].imageURL.urlList` | List of image URLs for each image in the post. `imageWidth` and `imageHeight` give the size of that image. |
| `item_list[].imagePost.title` | Title shown on the photo post. |
| `item_list[].textExtra[].hashtagName` | Hashtag names used in the caption. `start` and `end` give the position of each hashtag in the text. |
| `item_list[].music.id / authorName / duration` | ID, author name and duration of the sound used in the post. `original` shows whether it is an original sound. |

### Notes

- For the next page, send the `cursor` value from the response as `offset`. The first response returns `cursor` 20 and `has_more` 1.
- Send the `search_id` from the previous response in follow-up requests. Leave it empty on the first call.
- Image URLs in the response contain an `x-expires` value, so download the images soon after the call.
- To look up a single post in more detail, use [TikTok Video Detail](/apis/tiktok/web/post-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/search-photo.json`](../../../../catalog/models/tiktok/web/search-photo.json) · Store page: https://www.sandbase.ai/model/tiktok/web/search-photo
