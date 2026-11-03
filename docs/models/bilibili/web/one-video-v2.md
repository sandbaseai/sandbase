# Bilibili Video Details (V2) API: pricing, parameters and code examples

`bilibili/web/one-video-v2` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns detailed metadata and playback information for a specific Bilibili video using its unique video and CID identifiers.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/one-video-v2", "a_id": "114006081739452", "c_id": "28400484458"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/one-video-v2', {'a_id': '114006081739452', 'c_id': '28400484458'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/one-video-v2", {
  "a_id": "114006081739452",
  "c_id": "28400484458"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/one-video-v2", sandbase.Params{
	"a_id": "114006081739452",
	"c_id": "28400484458",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/one-video-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `a_id` | string | yes | Video id  |
| `c_id` | string | yes | Video cid  |

## Details

Returns player-side metadata for one Bilibili video, such as its `bvid`, `cid`, permission flags, paid-preview status and the current online viewer count. It needs the numeric video id as `a_id` and the part id as `c_id`.

### Use cases

- Convert a known `aid` and `cid` pair into the matching `bvid` for building a video link.
- Check whether a video is a paid or exclusive preview by reading `is_ugc_pay_preview`, `is_upower_exclusive` and `preview_toast`.
- Read the live `online_count` for a video at the moment of the call.
- Check subtitle login requirements and playback limits before building a player page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/one-video-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"a_id": "114006081739452", "c_id": "28400484458"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `a_id` | string | Yes | Video id |
| `c_id` | string | Yes | Video cid |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "aid": 114006081739452,
    "allow_bp": false,
    "answer_status": 2,
    "arc_aigc": null,
    "asr_language": "",
    "bgm_info": null,
    "block_time": 0,
    "bvid": "BV1GYAAefEjL",
    "cid": 28400484458,
    "disable_show_up_info": false,
    "elec_high_level": {
      "button_text": "",
      "intro": "",
      "jump_url": "",
      "new": false,
      "privilege_type": 0,
      "qa_title": "",
      "question_text": "",
      "show_button": false,
      "sub_title": "",
      "title": ""
    },
    "fawkes": {
      "config_version": 39232,
      "ff_version": 21289
    }
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.aid / data.bvid / data.cid` | The numeric video id, the BV-format video id and the part id (`cid`) of the video that was requested. |
| `data.online_count` | Number of viewers shown as online for the video when the call was made. |
| `data.is_ugc_pay_preview` | Whether the video is shown as a paid preview. When it is `true`, `data.preview_toast` holds the prompt text for buying the full video. |
| `data.preview_toast` | Text shown to viewers about purchasing the full video. It is returned in Chinese. |
| `data.is_upower_exclusive / data.is_upower_exclusive_with_qa / data.is_upower_play` | Flags for exclusive-content status on the video. |
| `data.need_login_subtitle` | Whether subtitles require a logged-in user. |
| `data.max_limit` | A numeric limit value returned for the video. The response does not state which item it limits. |
| `data.has_next` | Whether another item follows this one. |
| `data.page_no` | The page (part) number of the video that this response covers. |
| `data.now_time` | A Unix timestamp that marks when the response was generated. |

### Notes

- Both `a_id` and `c_id` are required and are sent as strings.
- If you only have a `bvid`, call [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid) to get the `a_id`.
- To list the parts and `cid` values of a video, call [Bilibili Video Parts](/apis/bilibili/web/video-parts).
- For stream addresses, use [Bilibili Video Playback URL](/apis/bilibili/web/video-playurl).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/one-video-v2.json`](../../../../catalog/models/bilibili/web/one-video-v2.json) · Store page: https://www.sandbase.ai/model/bilibili/web/one-video-v2
