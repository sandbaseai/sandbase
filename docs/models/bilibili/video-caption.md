# Bilibili Video Captions API: pricing, parameters and code examples

`bilibili/video-caption` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get caption data for a Bilibili video segment identified by BVID, AID, and CID. Use it to obtain subtitles for transcript extraction, accessibility review, or language-focused content analysis.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/video-caption", "bvid": "BV1GJ411x7h7", "aid": "80433022", "cid": "137649199"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/video-caption', {'bvid': 'BV1GJ411x7h7', 'aid': '80433022', 'cid': '137649199'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/video-caption", {
  "bvid": "BV1GJ411x7h7",
  "aid": "80433022",
  "cid": "137649199"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/video-caption", sandbase.Params{
	"bvid": "BV1GJ411x7h7",
	"aid": "80433022",
	"cid": "137649199",
})
```

Same call via the path form: `POST /v1/api/bilibili/video-caption` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aid` | string | yes | Bilibili AID.  |
| `cid` | string | yes | Bilibili CID.  |
| `bvid` | string | yes | Bilibili Video ID (BVID).  |

## Details

Returns the list of caption tracks available for one Bilibili video part. Each track has a language code, a language name, and a URL to the subtitle file. You send `bvid`, `aid`, and `cid` together.

### Use cases

- Download the subtitle file for each language to build a transcript of a Bilibili video.
- Check which caption languages a video offers before you plan translation or review work.
- Collect Simplified and Traditional Chinese tracks to compare wording for language analysis.
- Audit whether a video has captions for accessibility review.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/video-caption" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bvid": "BV1GJ411x7h7", "aid": "80433022", "cid": "137649199"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aid` | string | Yes | Bilibili AID. |
| `bvid` | string | Yes | Bilibili Video ID (BVID). |
| `cid` | string | Yes | Bilibili CID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "lan": "zh-CN",
      "lan_doc": "中文（中国）",
      "subtitle_url": "https://aisubtitle.hdslb.com/bfs/subtitle/662b660a420431045b483f9b560057c262539b…"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One caption track per item. The list has one entry for each language available for the video part. |
| `data[].lan` | Language code of the track, such as `zh-CN`, `zh-Hans`, or `zh-Hant`. |
| `data[].lan_doc` | Display name of the language, such as `中文（简体）` for Simplified Chinese. |
| `data[].subtitle_url` | URL of the subtitle file for this track. The file is JSON and the URL carries an `auth_key` query parameter. |

### Notes

- All three parameters are required: `bvid`, `aid`, and `cid`. They must describe the same video part.
- Use [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid) to get the `aid` from a `bvid`.
- Use [Bilibili Video Parts](/apis/bilibili/web/video-parts) to find the `cid` of each part of a video.
- The `subtitle_url` values include an `auth_key`, so fetch the subtitle file soon after you receive the response.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/bilibili/video-caption.json`](../../../catalog/models/bilibili/video-caption.json) · Store page: https://www.sandbase.ai/model/bilibili/video-caption
