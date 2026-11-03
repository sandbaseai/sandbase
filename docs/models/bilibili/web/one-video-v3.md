# Bilibili Single Video Details API: pricing, parameters and code examples

`bilibili/web/one-video-v3` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata for a single Bilibili video, including season information, episode titles, duration, and post timestamps via its URL.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/one-video-v3", "url": "https://www.bilibili.com/video/BV1S5uKzzE4r"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/one-video-v3', {'url': 'https://www.bilibili.com/video/BV1S5uKzzE4r'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/one-video-v3", {
  "url": "https://www.bilibili.com/video/BV1S5uKzzE4r"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/one-video-v3", sandbase.Params{
	"url": "https://www.bilibili.com/video/BV1S5uKzzE4r",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/one-video-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Video URL  |

## Details

Returns metadata for one Bilibili video: IDs, title parts, description, duration, upload and publish timestamps, uploader info, and engagement counts. It needs the video page link in `url`.

### Use cases

- Pull view, like, coin, favorite and share counts for a Bilibili video to track how it performs.
- Read the uploader's `mid` and `name` to attribute a video to its channel.
- Get the `duration` and per-part titles of a video to build a catalog of its content.
- Convert a video link into `aid`, `bvid` and `cid` for other video lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/one-video-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.bilibili.com/video/BV1S5uKzzE4r"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Video URL |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aid": 114830681840711,
  "argue_info": {
    "argue_link": "",
    "argue_msg": "作者声明：个人观点，仅供参考",
    "argue_type": 0
  },
  "bvid": "BV1S5uKzzE4r",
  "cid": 30966218981,
  "copyright": 1,
  "ctime": 1752177842,
  "desc": "如果杀人不犯法，你是拿起武器加入狂欢，还是躲在家裡瑟瑟发抖？\n就有那么一个国家，他有个法定杀人日，越杀越美好，越杀越伟大！\n这是一部寓言奇作，常看常新，什么国会…",
  "desc_v2": [
    {
      "biz_id": 0,
      "raw_text": "如果杀人不犯法，你是拿起武器加入狂欢，还是躲在家裡瑟瑟发抖？\n就有那么一个国家，他有个法定杀人日，越杀越美好，越杀越伟大！\n这是一部寓言奇作，常看常新，什么国会…",
      "type": 1
    }
  ],
  "dimension": {
    "height": 1920,
    "rotate": 0,
    "width": 3840
  },
  "disable_show_up_info": false,
  "duration": 2177,
  "dynamic": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `bvid / aid / cid` | The video's BV ID, numeric AV ID and numeric part ID. Use them as keys in other Bilibili calls. |
| `desc` | The video description text written by the uploader. |
| `duration` | Video length. `pages[].duration` gives the length of each part. Both values are plain numbers. |
| `pubdate / ctime` | Unix timestamps in seconds. `pubdate` is the publish time and `ctime` is the creation time. |
| `owner.mid / owner.name / owner.face` | The uploader's numeric user ID, display name and avatar image URL. |
| `stat.view / stat.like / stat.coin / stat.favorite / stat.share` | Counts of views, likes, coins, favorites and shares for the video. |
| `stat.danmaku / stat.reply` | Count of danmaku (on-screen comments) and count of replies. |
| `pages[].part / pages[].page / pages[].cid` | Title, part number and ID of each part of the video. |
| `season_id` | ID of the season (collection) the video belongs to. |
| `pic` | URL of the video cover image. |

### Notes

- Copy the video link from the Bilibili page, for example `https://www.bilibili.com/video/BV1S5uKzzE4r`, and send it as `url`.
- The `bvid` value is the same BV ID that appears at the end of the video link.
- To get comments, call [Bilibili Video Comments (Web)](/apis/bilibili/web/video-comments). To get subtitles, call [Bilibili Video Subtitle Details](/apis/bilibili/web/video-subtitle).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/one-video-v3.json`](../../../../catalog/models/bilibili/web/one-video-v3.json) · Store page: https://www.sandbase.ai/model/bilibili/web/one-video-v3
