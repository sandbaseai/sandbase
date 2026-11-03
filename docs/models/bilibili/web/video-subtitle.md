# Bilibili Video Subtitle Details API: pricing, parameters and code examples

`bilibili/web/video-subtitle` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns subtitle data for a specified Bilibili video based on its video ID and CID. Helps retrieve available caption tracks and related metadata.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/video-subtitle", "a_id": "114006081739452", "c_id": "28400484458"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/video-subtitle', {'a_id': '114006081739452', 'c_id': '28400484458'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/video-subtitle", {
  "a_id": "114006081739452",
  "c_id": "28400484458"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/video-subtitle", sandbase.Params{
	"a_id": "114006081739452",
	"c_id": "28400484458",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/video-subtitle` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `a_id` | string | yes | Video id  |
| `c_id` | string | yes | Video cid  |

## Details

List the subtitle tracks of a Bilibili video, including AI-generated Chinese subtitles, with a download URL for each track. Needs the video's `aid` and `cid`.

### Use cases

- Get a video's transcript for summaries or search.
- Translate or index Bilibili videos by their spoken content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/video-subtitle" \
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
  "allow_submit": false,
  "font_size_type": 0,
  "lan": "",
  "lan_doc": "",
  "subtitle_position": null,
  "subtitles": [
    {
      "ai_status": 2,
      "ai_type": 0,
      "id": 1689850260387946240,
      "id_str": "1689850260387946240",
      "is_lock": false,
      "lan": "ai-zh",
      "lan_doc": "中文",
      "subtitle_url": "//aisubtitle.hdslb.com/bfs/ai_subtitle/prod/1140060817394522840048445829058a24de…",
      "subtitle_url_v2": "//subtitle.bilibili.com/S%13%1BP.%1D%28%29X%2CR%5Ej%1F%25w%0E%02H%5EHO4%14%7B4%0…",
      "type": 1
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `subtitles[]` | Subtitle tracks. |
| `subtitles[].lan / lan_doc` | Language code (`ai-zh` for AI Chinese) and its label. |
| `subtitles[].subtitle_url` | Protocol-relative URL of the subtitle JSON; prefix it with `https:`. The file has `body[]` entries with `from`, `to` (seconds) and `content`. |
| `subtitles[].ai_type / ai_status` | Set for AI-generated tracks. |

### Notes

- Get `aid` and `cid` from a video detail API; one video has one `cid` per part.
- Videos without subtitles return an empty `subtitles` list.

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/video-subtitle.json`](../../../../catalog/models/bilibili/web/video-subtitle.json) · Store page: https://www.sandbase.ai/model/bilibili/web/video-subtitle
