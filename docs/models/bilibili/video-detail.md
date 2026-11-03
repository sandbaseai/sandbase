# Bilibili Video Details API: pricing, parameters and code examples

`bilibili/video-detail` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get details for a Bilibili video identified by its BVID. Use it to look up a known video for content review, cataloging, or subsequent engagement analysis.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/video-detail", "bvid": "BV1GJ411x7h7"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/video-detail', {'bvid': 'BV1GJ411x7h7'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/video-detail", {
  "bvid": "BV1GJ411x7h7"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/video-detail", sandbase.Params{
	"bvid": "BV1GJ411x7h7",
})
```

Same call via the path form: `POST /v1/api/bilibili/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bvid` | string | yes | Bilibili Video ID (BVID).  |

## Details

This API returns the details Bilibili's video page holds for one video. It needs the video's `bvid` and returns IDs, the part list, channel data, related videos, and playback stream info.

### Use cases

- Resolve a known `bvid` to its `aid` and `cid` before calling comment, danmaku, or caption APIs.
- List the parts of a multi-part video and read each part's `cid` and title.
- Read the duration and available stream qualities of a video for cataloging.
- Check which related videos Bilibili lists beside a video to map nearby content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bvid": "BV1GJ411x7h7"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bvid` | string | Yes | Bilibili Video ID (BVID). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "abtest": {},
  "adData": {
    "2624": null,
    "2625": null,
    "3038": [
      {
        "activity_type": 0,
        "ad_cb": "",
        "ad_desc": "",
        "adver_name": "",
        "agency": "",
        "archive": {
          "aid": 117546359521318,
          "attribute_v3": 4,
          "bvid": "BV19P4w6aEk3",
          "cid": 43282728004,
          "copyright": 3,
          "cover43": "http://i2.hdslb.com/bfs/archive/952648975fb24a15e3fbd108f242474fdf8b26ef.jpg",
          "ctime": 1793615553,
          "current_state": 0
        },
        "area": 1,
        "asg_id": 1733926,
        "business_mark": null,
        "card_type": 0,
        "click_urls": null,
        "cm_mark": 0
      }
    ],
    "4330": null
  },
  "adsControl": {
    "has_danmu": 0,
    "has_live_booking_ad": false,
    "under_player_scroller_seconds": 0
  },
  "aid": 80433022,
  "availableVideoList": [
    {
      "aid": 80433022,
      "bvid": "BV1GJ411x7h7",
      "cid": 137649199,
      "cover": "http://i1.hdslb.com/bfs/archive/5242750857121e05146d5d5b13a47a2a6dd36e98.jpg",
      "list": [
        {
          "aid": 80433022,
          "bvid": "BV1GJ411x7h7",
          "cid": 137649199,
          "p": 1,
          "title": "Never Gonna Give You Up - Rick Astley"
        }
      ],
      "redirect_url": "",
      "title": "【官方 MV】Never Gonna Give You Up - Rick Astley"
    }
  ],
  "bvid": "BV1GJ411x7h7",
  "channelKv": [
    {
      "channelId": 25,
      "config": {
        "enableSub": 0
      },
      "icon": "homeicon/ai/1",
      "name": "人工智能",
      "route": "ai",
      "sub": [
        {
          "name": "AI学习",
          "route": "tutorial",
          "subChannelId": 250001,
          "tid": 2096,
          "tkey": "CommonChannel:aiTutorial",
          "url": ""
        }
      ],
      "tid": 1011,
      "tkey": "CommonChannel:ai",
      "url": "//www.bilibili.com/c/ai/"
    }
  ],
  "cid": 137649199,
  "cidMap": {
    "80433022": {
      "aid": 80433022,
      "bvid": "BV1GJ411x7h7",
      "cids": {
        "1": 137649199
      }
    },
    "BV1GJ411x7h7": {
      "aid": 80433022,
      "bvid": "BV1GJ411x7h7",
      "cids": {
        "1": 137649199
      }
    }
  },
  "constants": {},
  "continuousPlay": true,
  "corePlayer": {
    "id": 0,
    "ref": "<link rel='preload' href='//s1.hdslb.com/bfs/static/player/main/core.9c6ca999.js…",
    "str": "<script type='text/javascript' src='//s1.hdslb.com/bfs/static/player/main/core.9…",
    "version": "4.10.8"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `bvid / aid / cid` | The video's BV ID, numeric AV ID, and the `cid` of its first part. Other Bilibili APIs use these IDs as input. |
| `cidMap` | Maps both the `aid` and the `bvid` to an object with the video's IDs. `cids` inside it maps part number to `cid`. |
| `availableVideoList[].bvid / availableVideoList[].aid / availableVideoList[].cid` | IDs of each video in the list. The first entry is the requested video. The later entries are other videos. |
| `availableVideoList[].title` | Title of the video in that list entry. Some entries show a placeholder title that means the video is no longer available. |
| `availableVideoList[].list[].p` | Part number of a video part. `list[].title` gives the part title. |
| `availableVideoList[].cover` | Cover image URL of the video. |
| `dash_info.dash.duration` | Length of the video. The value is 213 for this video. |
| `dash_info.accept_description / dash_info.accept_quality` | Names and numeric codes of the video qualities that can be played, such as `高清 1080P` with code `80`. |
| `dash_info.dash.video[].codecs / dash_info.dash.audio[].codecs` | Codec string of each video or audio stream. `bandwidth` and `base_url` sit beside it in each stream object. |
| `channelKv[].name` | Name of a Bilibili channel. `sub[]` lists its sub-channels with `name` and `tid`. |

### Notes

- Take the `bvid` from a Bilibili video URL. It looks like `BV1GJ411x7h7`.
- The response is large. It also holds page data such as `adData`, `corePlayer`, and `constants`, which you can ignore for most uses.
- Stream URLs in `dash_info` are long links that carry query parameters. Read them from the response when you need them.
- To convert a `bvid` to an `aid`, you can also call [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/bilibili/video-detail.json`](../../../catalog/models/bilibili/video-detail.json) · Store page: https://www.sandbase.ai/model/bilibili/video-detail
