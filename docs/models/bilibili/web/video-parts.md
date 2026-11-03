# Bilibili Video Parts API: pricing, parameters and code examples

`bilibili/web/video-parts` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns video part details for a specified Bilibili video using its video ID. The response includes the duration and creation timestamp for each segment.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/video-parts", "bv_id": "BV1dFad6aEz9"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/video-parts', {'bv_id': 'BV1dFad6aEz9'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/video-parts", {
  "bv_id": "BV1dFad6aEz9"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/video-parts", sandbase.Params{
	"bv_id": "BV1dFad6aEz9",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/video-parts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bv_id` | string | yes | Video id  |

## Details

Returns the list of parts (pages) of a Bilibili video. It needs the video's BV ID in `bv_id`. Each part comes with its `cid`, title, duration, resolution and first-frame image.

### Use cases

- List every part of a multi-part Bilibili video with its title and page number.
- Sum the `duration` values to get the total running time of a multi-part video.
- Collect each part's `cid` to use in other video calls that ask for a part-level ID.
- Check the resolution of each part before choosing which videos to process.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/video-parts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bv_id": "BV1dFad6aEz9"}'
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
  "data": [
    {
      "asr_language": "eng",
      "cid": 42329116378,
      "ctime": 1790748319,
      "dimension": {
        "height": 2160,
        "rotate": 0,
        "width": 3840
      },
      "duration": 1171,
      "first_frame": "http://i1.hdslb.com/bfs/storyff/_000029mksn8nfp3wi26eln302viuwxb_firsti.jpg",
      "from": "vupload",
      "page": 1,
      "part": "老Y蜜月之旅 | 马尔代夫菲诺芙",
      "vid": "",
      "weblink": ""
    }
  ],
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].page` | Position of the part in the video, starting at 1. |
| `data[].part` | Title of the part. |
| `data[].cid` | Numeric ID of the part. |
| `data[].duration` | Length of the part. The value 1171 for this video suggests seconds, but the response does not state the unit. |
| `data[].ctime` | Creation time of the part as a Unix timestamp. |
| `data[].dimension.width / data[].dimension.height` | Pixel size of the part's video. `data[].dimension.rotate` gives the rotation value. |
| `data[].first_frame` | URL of the first-frame image of the part. |
| `data[].asr_language` | Language code for automatic speech recognition on the part, such as `eng`. |
| `data[].from` | Source label for the part, such as `vupload`. |
| `code / message` | Status of the request. `code` is `0` and `message` is `OK` on success. |

### Notes

- Take `bv_id` from the Bilibili video link. It starts with `BV`, for example `BV1dFad6aEz9`.
- The `data` list has one item per part. A single-part video returns one item with `page` set to 1.
- Use [Bilibili Video Details](/apis/bilibili/web/one-video) for the video's general information.
- Use [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid) if you need the numeric AID of the video.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/video-parts.json`](../../../../catalog/models/bilibili/web/video-parts.json) · Store page: https://www.sandbase.ai/model/bilibili/web/video-parts
