# Bilibili App Single Video Details API: pricing, parameters and code examples

`bilibili/app/one-video` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync, async

Returns detailed video metadata for a specific Bilibili video. Looks up video information using either an AV ID or a BV ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync, async (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/one-video", "bv_id": "BV1dVbC6WE6p"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/one-video', {'bv_id': 'BV1dVbC6WE6p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/one-video", {
  "bv_id": "BV1dVbC6WE6p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/one-video", sandbase.Params{
	"bv_id": "BV1dVbC6WE6p",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/bilibili/app/one-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `av_id` | string |  | AV ID (choose one of av_id or bv_id)  |
| `bv_id` | string |  | BV ID (choose one of av_id or bv_id)  |

## Details

Returns metadata for one Bilibili video, including title-level details, uploader info, cover images, page list, and charging (elec) data. It needs a video ID, passed as either `av_id` or `bv_id`.

### Use cases

- Pull the uploader name, `mid` and follower count for a video to build a creator profile.
- Read the video's `duration`, `dimension` and `pages[]` list to check length, resolution and number of parts.
- Collect the top charging supporters and total charge count for a video to track fan support.
- Fetch the cover image, description and tags of a video to fill a content catalog.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/one-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"av_id": "115568241811221", "bv_id": "BV18SCrBGE9E"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `av_id` | string | No | AV ID (choose one of av_id or bv_id) |
| `bv_id` | string | No | BV ID (choose one of av_id or bv_id) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "DagwUser": {
    "entry_room": {
      "list": {
        "203680252": {
          "area_id": 89,
          "area_name": "CS2",
          "cover": "https://i0.hdslb.com/bfs/live/new_room_cover/8dbb387f14b91e20ba184f71c3409390811…",
          "is_room_feed": 1,
          "jump_url": {
            "ugc_video_close": "https://live.bilibili.com/25255343?accept_quality=%5B10000%2C400%2C250%5D&all_sp…",
            "ugc_video_detail": "https://live.bilibili.com/25255343?accept_quality=%5B10000%2C400%2C250%5D&all_sp…"
          },
          "keyframe": "https://i0.hdslb.com/bfs/live-key-frame/keyframe11031525000025255343q2a1no.jpg",
          "live_id": 746048077177118127,
          "live_info": {
            "build": 10489,
            "live_model": 0,
            "live_platform": "pc_link",
            "remote_ip": "180.213.90.90",
            "voice_background": ""
          }
        }
      }
    }
  },
  "DataCenterInfo": "",
  "ElecReply": null,
  "InteractLabel": "",
  "LiveOrderText": "",
  "PlayToast": null,
  "QueryUpSet": null,
  "RejectPage": null,
  "TabModule": null,
  "aid": 115568241811221,
  "attribute_v3": 4,
  "bvid": "BV18SCrBGE9E"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aid / bvid / cid` | The video's numeric AV ID, its BV ID, and the ID of the first part (`cid`). Use `cid` to look up danmaku or subtitles for that part. |
| `desc` | The video description text written by the uploader. |
| `desc_tag[].tag_name` | Name of each tag attached to the video. `tag_id` gives the tag's ID. |
| `duration` | Video length. For this sample it is `1586`, and the single page has the same `duration`. |
| `ctime` | Publish time as a Unix timestamp in seconds. |
| `pic / cover43 / first_frame` | URLs of the cover image, a 4:3 cover, and the first video frame. |
| `dimension.width / dimension.height` | Video resolution in pixels. `rotate` shows the rotation flag. |
| `owner.mid / owner.name / owner.face` | Uploader's user ID, display name and avatar URL. |
| `owner_ext.fans / owner_ext.arc_count / owner_ext.official_verify.desc` | Uploader's follower count, video count as a text label, and verification description. |
| `pages[].page / pages[].part / pages[].cid / pages[].duration` | Each part of the video: part number, part title, part `cid` and part length. `dmlink` is the danmaku XML link for that part. |
| `elec.total / elec.count / elec.list[].uname` | Charging (elec) totals and the ranked supporters. Each supporter has `uname`, `avatar`, `rank` and `mid`. |
| `pid_name_v2 / pid_v2` | Name and ID of the video's category, here `游戏` and `1008`. |

### Notes

- Send either `av_id` or `bv_id`. The sample request sent both, and both pointed to the same video.
- `bvid` values look like `BV18SCrBGE9E`. `aid` is a long number.
- The response has no view, like or comment counts, so use [Bilibili Video Details](/apis/bilibili/video-detail) if you need engagement stats.
- Pass `owner.mid` to [Bilibili App User Info](/apis/bilibili/app/user-info) to get the uploader's profile.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili App Bangumi Tab](/apis/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/apis/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/apis/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.

---
Machine-readable: [`catalog/models/bilibili/app/one-video.json`](../../../../catalog/models/bilibili/app/one-video.json) · Store page: https://www.sandbase.ai/model/bilibili/app/one-video
