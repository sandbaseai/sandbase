# Douyin DOU+ Video Ranking API: pricing, parameters and code examples

`douyin/douplus/video-ranking` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves DOU+ video leaderboard metrics filterable by category, ranking dimension, and time range. Returns video titles, author details, and engagement statistics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/douplus/video-ranking"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/douplus/video-ranking', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/douplus/video-ranking", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/douplus/video-ranking", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/douplus/video-ranking` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `adv_id` |  |  | Advertiser id, optional  |
| `tag_id` |  |  | Category id, default 634 (Entertainment). Full map: 601 Plot, 602 Star, 606 Music, 607 ACGN,  |
| `dim_type` |  |  | Ranking dimension, default 5. 1=low-fan hits, 2=high completion, 3=high like-rate, 4=high follower-growth, 5=hotness index  |
| `time_range` |  |  | Time range, 1 / 2 / 3, default 2  |

## Details

Returns the DOU+ video leaderboard for Douyin. Each entry has the video title, author, cover, and engagement statistics. All inputs are optional, and the defaults return the Entertainment category ranked by hotness index.

### Use cases

- Find which videos in a category currently lead the DOU+ hotness ranking.
- Spot low-follower authors whose videos reach a large audience by ranking with `dim_type` 1.
- Compare `FinishPlayRate` and `LikeRate` across top videos to see which content holds viewers.
- Collect `itemId` values of top videos to pull their full details with another API.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/douplus/video-ranking" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `adv_id` | string | No | Advertiser id, optional |
| `dim_type` | string | No | Ranking dimension, default 5. 1=low-fan hits, 2=high completion, 3=high like-rate, 4=high follower-growth, 5=hotness index |
| `tag_id` | string | No | Category id, default 634 (Entertainment). Full map: 601 Plot, 602 Star, 606 Music, 607 ACGN, |
| `time_range` | string | No | Time range, 1 / 2 / 3, default 2 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": [
    {
      "author": {
        "followerCount": 638,
        "nickname": "日出夜游"
      },
      "cover": "https://p26-sign.douyinpic.com/eden-cn/lsfreh7ulphrvhps/douplus/private_cover.pn…",
      "createTime": "1792581711",
      "isPhoto": false,
      "itemId": "7699079819598533282",
      "photos": [],
      "statistics": {
        "CommentCnt": "0",
        "FinishPlayRate": 0.5975203935815757,
        "IndexCnt": "82170",
        "LikeCnt": "0",
        "LikeRate": 0.01576316934408921,
        "NewFansCnt": "406",
        "NewFansRate": 9.375828467601663e-05,
        "NewLikeCnt": "68259"
      },
      "title": "这变脸速度不挣钱不行啊"
    }
  ],
  "msg": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].title` | Caption of the video, including its hashtags. |
| `data[].itemId` | ID of the video, as a string. |
| `data[].author.nickname / data[].author.followerCount` | Display name of the author and the author's follower count. |
| `data[].createTime` | Publish time as a Unix timestamp in seconds, returned as a string. |
| `data[].statistics.IndexCnt` | Count behind the ranking index for this video, returned as a string. Higher values appear first in the sample under the default ranking. |
| `data[].statistics.FinishPlayRate / data[].statistics.LikeRate / data[].statistics.NewFansRate` | Ratios between 0 and 1 for completed plays, likes, and new followers gained. |
| `data[].statistics.NewFansCnt / data[].statistics.NewLikeCnt` | Counts of new followers and new likes, returned as strings. |
| `data[].cover` | Signed URL of the cover image. The URL carries an expiry in its query string. |
| `data[].playAddr` | Video play URL. Some entries do not include it. |
| `data[].isPhoto / data[].photos` | `isPhoto` shows whether the entry is a photo post. `photos` lists the images for photo posts. |

### Notes

- Send an empty body `{}` to get the defaults: `tag_id` 634 (Entertainment), `dim_type` 5 (hotness index), `time_range` 2.
- Set `dim_type` to 1 for low-fan hits, 2 for high completion, 3 for high like-rate, 4 for high follower-growth, or 5 for hotness index.
- Count fields such as `IndexCnt` and `NewFansCnt` are strings, so convert them to numbers before sorting.
- To read more about one video from the list, pass its `itemId` to [Douyin Douplus Video Detail](/apis/douyin/douplus/video-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin DOU+ Promotable Items](/apis/douyin/douplus/promotable-item-list): Returns the promotable video item list for a Douyin account on the DOU+ promotion page.
- [Douyin DOU+ User Search](/apis/douyin/douplus/search-user): Searches for Douyin users in the DOU+ delivery context using a Douyin ID or nickname.
- [Douyin DOU+ Talent Categories](/apis/douyin/douplus/talent-categories): Returns the Douyin DOU+ talent category directory.

---
Machine-readable: [`catalog/models/douyin/douplus/video-ranking.json`](../../../../catalog/models/douyin/douplus/video-ranking.json) · Store page: https://www.sandbase.ai/model/douyin/douplus/video-ranking
