# Douyin Xingtu Creator Homepage Videos API: pricing, parameters and code examples

`douyin/xingtu-v3/aggregator-author-homepage-videos` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.071429 per call · **Modes:** sync

List a Douyin Creator Marketplace (Xingtu) creator's homepage videos with keyword, video-type, assignment, date, and page filters. Use it to review relevant content before campaign selection.

## Pricing

- **$0.071429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/aggregator-author-homepage-videos", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/aggregator-author-homepage-videos', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/aggregator-author-homepage-videos", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/aggregator-author-homepage-videos", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/aggregator-author-homepage-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starting from 1. default `1` |
| `endDate` | string |  | End publish date in yyyyMMdd format. The filter ends at 23:59:59 in Asia/Shanghai.  |
| `keyword` | string |  | Keyword used to search creator homepage videos.  |
| `oAuthorId` | string | yes | Author's unique Xingtu ID.  |
| `startDate` | string |  | Start publish date in yyyyMMdd format. The filter starts at 00:00:00 in Asia/Shanghai.  |
| `videoType` | string |  | Homepage video type filter. one of: `ALL`, `PERSONAL`, `XINGTU`; default `"ALL"` |
| `onlyAssign` | boolean |  | Whether to include only assigned videos. Xingtu usually shows this option when `videoType` is `XINGTU`. default `false` |

## Details

This API returns a page of videos from a Douyin creator's homepage as listed in Xingtu. It needs the creator's Xingtu ID in `oAuthorId`. You can narrow the list by keyword, video type, assignment status and publish date.

### Use cases

- Review a creator's recent videos and their view and like counts before you shortlist them for a campaign.
- Search a creator's videos with `keyword` to check whether they have covered a brand or product topic.
- Filter to `XINGTU` videos to see the creator's past platform-assigned work.
- Pull videos from a date range to compare content performance across a campaign window.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/aggregator-author-homepage-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique Xingtu ID. |
| `endDate` | string | No | End publish date in yyyyMMdd format. The filter ends at 23:59:59 in Asia/Shanghai. |
| `keyword` | string | No | Keyword used to search creator homepage videos. |
| `onlyAssign` | boolean | No | Whether to include only assigned videos. Xingtu usually shows this option when `videoType` is `XINGTU`. |
| `page` | integer | No | Page number, starting from 1. |
| `startDate` | string | No | Start publish date in yyyyMMdd format. The filter starts at 00:00:00 in Asia/Shanghai. |
| `videoType` | string | No | Homepage video type filter. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "items": [
    {
      "comment_cnt": "91",
      "content_theme_labels": [],
      "cover_uri": "tos-cn-i-dy/643299bf28474b9e9adc28a863baeba6",
      "create_time": "1793113313",
      "duration": 12.538,
      "finish_rate": 0.135421,
      "interact_rate": 0.024438,
      "item_id": "7701362991266123034",
      "like_cnt": "665436",
      "title": "网友拍到高速两旁，挂满一块块不一样的“广告牌”……致敬国之栋梁！（来源：@有名 ）",
      "url": "https://www.iesdouyin.com/share/video/7701362991266123034/?region=CN&mid=7667641…",
      "video_id": "v0d00fg10000dbgbp67og65rp7vvjd00"
    }
  ],
  "pagination": {
    "has_more": true,
    "limit": 20,
    "page": 1,
    "total_count": 2518
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].item_id / items[].video_id` | Identifiers for the video. `item_id` is the numeric ID that also appears in the share `url`. |
| `items[].title` | Video caption text, including any hashtags and @mentions. |
| `items[].create_time` | Publish time as a Unix timestamp in seconds, returned as a string. |
| `items[].duration` | Video length. The values look like seconds with decimals. |
| `items[].watch_cnt / items[].like_cnt / items[].comment_cnt` | View, like and comment counts for the video. They come back as strings. |
| `items[].finish_rate / items[].interact_rate` | Completion rate and interaction rate for the video, as decimal fractions. |
| `items[].url` | Share link for the video on Douyin. |
| `items[].cover_uri` | Cover image path for the video. |
| `items[].content_theme_labels` | Content theme labels for the video. The list is empty in this sample. |
| `pagination.has_more / pagination.total_count` | `has_more` tells you whether another page exists. `total_count` is the total number of matching videos. |

### Notes

- Get the `oAuthorId` from [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- Use `page` to move through results, starting at 1. Each page returned `limit` 20 items in this sample.
- Send `startDate` and `endDate` as `yyyyMMdd` strings. Check `base_resp.status_code`, where `0` means success.
- For the creator's profile details, call [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info).

### Pricing

$0.071429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/aggregator-author-homepage-videos.json`](../../../../catalog/models/douyin/xingtu-v3/aggregator-author-homepage-videos.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/aggregator-author-homepage-videos
