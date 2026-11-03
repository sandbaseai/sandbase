# Douyin Hot Search API: pricing, parameters and code examples

`douyin/hot-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Search Douyin (TikTok China) content with optional keyword, category, video-type, ranking, pagination, engagement, and creator-follower filters. Use it to support trend discovery and campaign research.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/hot-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/hot-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/hot-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/hot-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/hot-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (starting from 1). Page size is fixed at 10. default `1` |
| `keyword` | string |  | Optional search keyword.  |
| `sortType` | string |  | Sorting criteria for hot content results. one of: `COMPREHENSIVE`, `HIGH_INTERACTION`, `HIGH_LIKE`, `HIGH_COMMENT`, `HIGH_SHARE`; default `"COMPREHENSIVE"` |
| `videoType` | string |  | Video type filter. one of: `ALL`, `XINGTU_VIDEO`, `NATURAL_VIDEO`; default `"ALL"` |
| `contentType` | string |  | Top-level content type. Only one content type can be selected. one of: `ALL`, `FASHION`, `TECHNOLOGY`, `SCIENCE`, `PHOTOGRAPHY`, `FOOD`, `MOTHER_BABY`, `PARENTING`, `DRAMA`, `GAME`, `AUTOMOTIVE`, `ANIMAL` …; default `"ALL"` |
| `likeCountMax` | integer |  | Maximum raw like count.  |
| `likeCountMin` | integer |  | Minimum raw like count.  |
| `shareCountMax` | integer |  | Maximum raw share count.  |
| `shareCountMin` | integer |  | Minimum raw share count.  |
| `commentCountMax` | integer |  | Maximum raw comment count.  |
| `commentCountMin` | integer |  | Minimum raw comment count.  |
| `followerCountMax` | integer |  | Maximum raw creator follower count.  |
| `followerCountMin` | integer |  | Minimum raw creator follower count.  |
| `interactionCountMax` | integer |  | Maximum raw interaction count.  |
| `interactionCountMin` | integer |  | Minimum raw interaction count.  |

## Details

This API returns a page of 10 Douyin videos with engagement stats and creator details. Every input is optional, so an empty request returns the default ranking across all content types. You can narrow results by `keyword`, `contentType`, `videoType`, engagement ranges and creator follower range.

### Use cases

- Find high-comment or high-share Douyin videos in a single category such as `FOOD` or `GAME` for trend research.
- Filter by `followerCountMin` and `followerCountMax` to find videos from mid-sized creators for campaign planning.
- Compare `interact_rate` and `finish_rate` across videos to see which ones hold viewers and drive engagement.
- Search a `keyword` and rank by `HIGH_LIKE` to collect top-performing examples for a topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/hot-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `commentCountMax` | integer | No | Maximum raw comment count. |
| `commentCountMin` | integer | No | Minimum raw comment count. |
| `contentType` | string | No | Top-level content type. Only one content type can be selected. |
| `followerCountMax` | integer | No | Maximum raw creator follower count. |
| `followerCountMin` | integer | No | Minimum raw creator follower count. |
| `interactionCountMax` | integer | No | Maximum raw interaction count. |
| `interactionCountMin` | integer | No | Minimum raw interaction count. |
| `keyword` | string | No | Optional search keyword. |
| `likeCountMax` | integer | No | Maximum raw like count. |
| `likeCountMin` | integer | No | Minimum raw like count. |
| `page` | integer | No | Page number (starting from 1). Page size is fixed at 10. |
| `shareCountMax` | integer | No | Maximum raw share count. |
| `shareCountMin` | integer | No | Minimum raw share count. |
| `sortType` | string | No | Sorting criteria for hot content results. |
| `videoType` | string | No | Video type filter. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "content_list": [
    {
      "attribute_datas": {
        "comment_cnt_all": "20665",
        "core_user_id": "57918142065",
        "cover_image_uri": "tos-cn-p-0015c000-ce/oImMIBo9uAwdfrDsE4wFSy67Ef37qOEBWCzlJA",
        "finish_rate": "0.140593",
        "interact_cnt": "249138",
        "interact_rate": "0.015762",
        "is_star_item": "1",
        "item_create_time": "1791614892"
      },
      "id": "7694927369400548849",
      "object_type": 2,
      "user_info": {
        "avatar_url": "https://p11.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_1bc5360e6…",
        "core_user_id": "57918142065",
        "follower": "6830884",
        "name": "My name is 伊森",
        "star_id": "6972769927115571236"
      }
    }
  ],
  "pagination": {
    "has_more": true,
    "limit": 10,
    "page": 1,
    "total_count": 2000
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `content_list[].id` | ID of the video, returned as a string. |
| `content_list[].attribute_datas.interact_cnt` | Total interaction count for the video. |
| `content_list[].attribute_datas.interact_rate` | Interaction rate for the video, returned as a decimal string such as `0.015762`. |
| `content_list[].attribute_datas.comment_cnt_all` | Total comment count for the video. |
| `content_list[].attribute_datas.finish_rate` | Finish rate for the video, returned as a decimal string. |
| `content_list[].attribute_datas.item_create_time` | Creation time of the video as a Unix timestamp in seconds, returned as a string. |
| `content_list[].attribute_datas.is_star_item` | Flag for the video. The sample values are `1`. |
| `content_list[].attribute_datas.cover_image_uri` | URI of the video cover image. |
| `content_list[].user_info.name / content_list[].user_info.follower` | Creator display name and follower count. |
| `content_list[].user_info.core_user_id / content_list[].user_info.star_id` | IDs of the creator. `core_user_id` also appears in `attribute_datas`. |

### Notes

- Page size is fixed at 10. Increase `page` to read more results, and check `pagination.has_more` to see if another page exists.
- `pagination.total_count` shows the total number of matching results, and `pagination.limit` shows the page size.
- Count fields and IDs come back as strings, so convert them to numbers before sorting or comparing.
- To get full detail for a video from `content_list[].id`, try [Douyin Video Detail](/apis/douyin/app-v3/one-video-v3) or [Douyin Video Statistics](/apis/douyin/app-v3/video-statistics).

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/hot-search.json`](../../../catalog/models/douyin/hot-search.json) · Store page: https://www.sandbase.ai/model/douyin/hot-search
