# Bilibili Video Details API: pricing, parameters and code examples

`bilibili/web/one-video` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata and honor tags for a single Bilibili video based on its unique BV identifier, including recommendation status.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/one-video", "bv_id": "BV1dVbC6WE6p"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/one-video', {'bv_id': 'BV1dVbC6WE6p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/one-video", {
  "bv_id": "BV1dVbC6WE6p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/one-video", sandbase.Params{
	"bv_id": "BV1dVbC6WE6p",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/one-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bv_id` | string | yes | Video id  |

## Details

Returns metadata for one Bilibili video, including its stats, owner, pages, rights flags and honor tags such as `热门`. It needs one input: the video's BV id in `bv_id`.

### Use cases

- Pull the view, like, coin and favorite counts of a video to track how it performs.
- Check `honor_reply.honor` to see whether a video carries a popular or weekly recommendation tag.
- Read the owner `mid` and name of a video to credit or look up its creator.
- Get the title of each part, the duration and the frame size to catalog video files.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/one-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bv_id": "BV1M1421t7hT"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bv_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "aid": 1556386640,
    "argue_info": {
      "argue_link": "",
      "argue_msg": "",
      "argue_type": 0
    },
    "bvid": "BV1M1421t7hT",
    "cid": 1645628975,
    "copyright": 1,
    "ctime": 1723355942,
    "desc": "",
    "desc_v2": null,
    "dimension": {
      "height": 1080,
      "rotate": 0,
      "width": 1920
    },
    "disable_show_up_info": false,
    "duration": 353,
    "dynamic": ""
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.bvid / data.aid / data.cid` | The video's BV id, its numeric AID and the CID of its first part. |
| `data.owner.mid / data.owner.name / data.owner.face` | ID, display name and avatar URL of the user who posted the video. |
| `data.stat.view / data.stat.like / data.stat.coin / data.stat.favorite / data.stat.share` | View, like, coin, favorite and share counts for the video. |
| `data.stat.danmaku / data.stat.reply` | Count of danmaku (on-screen comments) and count of replies. |
| `data.honor_reply.honor[].desc` | Name of an honor tag on the video, for example `热门` or `热门收录`. |
| `data.honor_reply.honor[].type / data.honor_reply.honor[].weekly_recommend_num` | Numeric code of the honor tag, and the weekly recommendation number tied to it. |
| `data.pubdate / data.ctime` | Unix timestamps in seconds for the publish time and the creation time of the video. |
| `data.duration / data.dimension.width / data.dimension.height` | Video length and frame size. The `duration` of 353 matches the single page's `duration`. |
| `data.pages[].part / data.pages[].page / data.pages[].cid` | Title, page number and CID of each part of the video. |
| `data.pic` | URL of the video's cover image. |

### Notes

- The `bv_id` looks like `BV1M1421t7hT`. It is the id in a Bilibili video URL.
- To get the numeric AID from a BV id on its own, call [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid).
- For other versions of video details, see [Bilibili Video Details (V2)](/apis/bilibili/web/one-video-v2) or [Bilibili Web Video Details](/apis/bilibili/web/video-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/one-video.json`](../../../../catalog/models/bilibili/web/one-video.json) · Store page: https://www.sandbase.ai/model/bilibili/web/one-video
