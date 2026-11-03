# Douyin Item Report Detail API: pricing, parameters and code examples

`douyin/xingtu-v2/item-report-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call · **Modes:** sync

Get Item Report Detail on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.002 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/item-report-detail", "item_id": "7372484719365098803"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/item-report-detail', {'item_id': '7372484719365098803'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/item-report-detail", {
  "item_id": "7372484719365098803"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/item-report-detail", sandbase.Params{
	"item_id": "7372484719365098803",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/item-report-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video (item) ID  |

## Details

Returns a report for one Douyin video on Xingtu. The report covers the video's counts, rates, music and author summary. It needs one input, the video `item_id`.

### Use cases

- Check the likes, comments, shares and collects of a creator's sponsored video after it goes live.
- Compare `finish_rate` and `interact_rate` across several videos to see which content holds viewers best.
- Pull the author summary of a video to screen the creator before a brand deal.
- Find the sound used in a video and track which music creators pick.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/item-report-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7372484719365098803"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video (item) ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "author_info": {
    "author_id": "6811013757230120974",
    "avatar_uri": "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_f96ccdf24e…",
    "city": "杭州市",
    "content_tags": {
      "随拍": [
        "随拍"
      ]
    },
    "core_user_id": "95823111667",
    "follower": "2606021",
    "gender": 2,
    "industry_tags": [],
    "ink_cnt": "237487",
    "is_star": 1,
    "link_cnt": "926519",
    "name": "萧萧不吃辣"
  },
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "video_info": {
    "collect_cnt": "19905",
    "comment_cnt": "4071",
    "create_time": "1716540374",
    "duration": 8.01,
    "finish_rate": 0.138603596,
    "head_image_uri": "tos-cn-i-0813c001/o4AAWPm4AU97EUKAFFAB8EIDQg9DUAcCfSfT9n",
    "interact_cnt": "397010",
    "interact_rate": 0.101,
    "item_id": "7372484719365098803",
    "like_cnt": "312973",
    "music_info": {
      "album": "",
      "author": "KD_B Music",
      "cover_uri": "100x100/aweme-avatar/tos-cn-i-0813_oMDhlc4OEhKACgeCH1nztAM9h0AfAArgAzpkId",
      "cover_url": [
        "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813_oMDhlc4OEhKACg…"
      ],
      "create_time": "1711050340",
      "duration": "29",
      "music_id": "7348905216869174025",
      "play_url": "https://sf11-cdn-tos.douyinstatic.com/obj/ies-music/7348905229246532379.mp3",
      "source_platform": 0,
      "title": "@KD_B Music创作的原声",
      "used_count": "0"
    },
    "share_cnt": "79966"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `video_info.title` | Video caption text, including hashtags. |
| `video_info.vv_cnt` | View count of the video, returned as a string. |
| `video_info.like_cnt / comment_cnt / share_cnt / collect_cnt` | Counts of likes, comments, shares and collects. Values are strings. |
| `video_info.interact_cnt / interact_rate` | Total interaction count and the interaction rate of the video. |
| `video_info.finish_rate` | Finish rate of the video as a decimal fraction, for example `0.1386`. |
| `video_info.duration` | Video length. The value `8.01` is a number. |
| `video_info.create_time` | Creation time as a Unix timestamp string, in seconds. |
| `video_info.music_info.title / author / music_id` | Name, author and ID of the sound used in the video. |
| `author_info.name / author_id / core_user_id` | Name of the creator and the creator's IDs. |
| `author_info.follower / city / gender` | Follower count (string), city and gender code of the creator. |

### Notes

- `item_id` is the numeric Douyin video ID, such as `7372484719365098803`. It also appears in the `video_info.url` share link.
- Counts are returned as strings. Convert them to numbers before you sort or sum them.
- To see how the video grows over time, call [Douyin Item Report Trend](/apis/douyin/xingtu-v2/item-report-trend). For the comments, call [Douyin Item Report Comments](/apis/douyin/xingtu-v2/item-report-comments).
- Use `author_info.author_id` with [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info) to get more on the creator.

### Pricing

$0.002 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/item-report-detail.json`](../../../../catalog/models/douyin/xingtu-v2/item-report-detail.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/item-report-detail
