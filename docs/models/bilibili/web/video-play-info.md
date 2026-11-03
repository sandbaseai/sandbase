# Bilibili Single Video Play Info API: pricing, parameters and code examples

`bilibili/web/video-play-info` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns playback stream information, including video stream URLs, MIME types, and frame rates, for a single Bilibili video URL.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/video-play-info", "url": "https://www.bilibili.com/video/BV1S5uKzzE4r"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/video-play-info', {'url': 'https://www.bilibili.com/video/BV1S5uKzzE4r'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/video-play-info", {
  "url": "https://www.bilibili.com/video/BV1S5uKzzE4r"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/video-play-info", sandbase.Params{
	"url": "https://www.bilibili.com/video/BV1S5uKzzE4r",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/video-play-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Video URL  |

## Details

Returns playback stream information for one Bilibili video. It includes DASH video and audio stream URLs, codecs, MIME types, frame rates, and the quality levels on offer. The input is a Bilibili video page `url`.

### Use cases

- Pull direct DASH video and audio stream URLs for a Bilibili video.
- Compare the codecs, resolutions and bandwidth of each available video stream.
- List the quality levels a video offers, such as 4K or 1080P.
- Check MIME types and frame rates before you hand a stream to an external player.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/video-play-info" \
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
  "accept_description": [
    "超清 4K"
  ],
  "accept_format": "hdflv2,hdflv2,flv,flv720,flv480,mp4",
  "accept_quality": [
    120
  ],
  "auto_qn_resp": {
    "dyeid": "32720d4a99eabdba00eb79966ae98d09"
  },
  "cur_language": "",
  "cur_production_type": 0,
  "dash": {
    "audio": [
      {
        "SegmentBase": {
          "Initialization": "0-825",
          "indexRange": "826-6089"
        },
        "backupUrl": [
          "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/81/89/30966218981/30966218981-1…"
        ],
        "backup_url": [
          "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/81/89/30966218981/30966218981-1…"
        ],
        "bandwidth": 75307,
        "baseUrl": "https://upos-sz-mirrorhwo1.bilivideo.com/upgcxcode/81/89/30966218981/30966218981…",
        "base_url": "https://upos-sz-mirrorhwo1.bilivideo.com/upgcxcode/81/89/30966218981/30966218981…",
        "codecid": 0,
        "codecs": "mp4a.40.2",
        "frameRate": "",
        "frame_rate": "",
        "height": 0,
        "id": 30216
      }
    ],
    "dolby": {
      "audio": null,
      "type": 0
    },
    "duration": 2177,
    "flac": null,
    "minBufferTime": 1.5,
    "min_buffer_time": 1.5,
    "video": [
      {
        "SegmentBase": {
          "Initialization": "0-929",
          "indexRange": "930-6193"
        },
        "backupUrl": [
          "https://upos-sz-estgoss.bilivideo.com/upgcxcode/81/89/30966218981/30966218981-1-…"
        ],
        "backup_url": [
          "https://upos-sz-estgoss.bilivideo.com/upgcxcode/81/89/30966218981/30966218981-1-…"
        ],
        "bandwidth": 261921,
        "baseUrl": "https://upos-sz-estgoss.bilivideo.com/upgcxcode/81/89/30966218981/30966218981-1-…",
        "base_url": "https://upos-sz-estgoss.bilivideo.com/upgcxcode/81/89/30966218981/30966218981-1-…",
        "codecid": 7,
        "codecs": "avc1.64001F",
        "frameRate": "30.000",
        "frame_rate": "30.000",
        "height": 426,
        "id": 32
      }
    ]
  },
  "format": "flv480",
  "from": "local",
  "high_format": null,
  "last_play_cid": 0,
  "last_play_time": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `dash.video[].baseUrl / base_url` | Main URL of a video stream. `backupUrl` and `backup_url` list alternate URLs for the same stream. |
| `dash.video[].codecs / mimeType / frameRate` | Codec string, MIME type and frame rate of a video stream. For example `avc1.64001F`, `video/mp4` and `30.000`. |
| `dash.video[].width / height / bandwidth` | Frame size and bandwidth value of a video stream. |
| `dash.audio[].baseUrl / codecs / mimeType` | Main URL, codec and MIME type of an audio stream. Audio streams are listed apart from video streams. |
| `dash.duration / timelength` | Length of the video. `dash.duration` is `2177` and `timelength` is `2176490` in this response. |
| `accept_quality / accept_description` | Quality codes (such as `120`, `112`, `80`) and their text labels (such as `超清 4K`). |
| `support_formats[].quality / display_desc / format / codecs[]` | Each quality level on offer. It has a short label, a format name and a list of codecs for that level. |
| `quality / format` | Quality code and format name of the streams in this response. Here they are `32` and `flv480`. |
| `dash.video[].SegmentBase / segment_base` | Byte ranges for the initialization data and the index (`initialization`, `index_range`) of a stream. |

### Notes

- Pass the full video page link in `url`, for example `https://www.bilibili.com/video/BV1S5uKzzE4r`.
- `dash.video[]` can hold several entries with the same `id` but different `codecid` and `codecs` values, so match on codec as well.
- The request takes only `url`, so it has no pagination.
- To get the title, author and stats of the same video, call [Bilibili Video Details](/apis/bilibili/web/one-video).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/video-play-info.json`](../../../../catalog/models/bilibili/web/video-play-info.json) · Store page: https://www.sandbase.ai/model/bilibili/web/video-play-info
